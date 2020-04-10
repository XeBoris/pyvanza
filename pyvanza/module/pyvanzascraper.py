import urllib.request
import json
import datetime

class AvanzaScraper(object):

    def __init__(self):
        self.url = None
        self.fond = None
        self.fond_id = None
        self.fond_name = None
        self.beg = None
        self.end = None
        self.purl = "https://www.avanza.se/_cqbe/fund/chart/{f_id}/{f_beg}/{f_end}"

    def SetFond(self, fond_url):
        """SetFond

        Requires a list of fonds
        """
        self.url = fond_url
        self.fond_name = fond_url.split("/")[-1]
        self.fond_id = fond_url.split("/")[5]

    def GetFond(self, fond_url=None, beg=None, end=None):
        """Function: GetFond:
        :param fond_url: A string with a valid URL from an Avanza fond or stock webpage
        :param beg: A day (string) in format of YYYY-MM-DD
        :param end: A day (string) in format of YYYY-MM-DD
        :return return_data: A dictionary with a time series and meta information
        """
        if fond_url != None:
            self.SetFond(fond_url)

        purl = self.purl.format(f_id=self.fond_id,
                                f_beg=beg,
                                f_end=end)
        with urllib.request.urlopen(purl) as url:
            data = json.loads(url.read().decode())

        # extract data:
        return_data = {}
        return_data['id'] = data['id']
        return_data['fromDate'] = data['fromDate']
        return_data['toDate'] = data['toDate']
        return_data['name'] = data['name']
        return_data['url'] = self.url
        return_data['time_series'] = []
        for i_data in data['dataSerie']:
            x_ = i_data['x']
            y_ = i_data['y']
            x_ = datetime.datetime.utcfromtimestamp(int(x_ / 1000))
            return_data['time_series'].append([x_, y_])

        #transpose time_series entry:
        return_data['time_series'] = list(map(list, zip(*return_data['time_series'])))

        return return_data

    def GetDetailFond(self, fond_url=None, beg=None, end=None):

        t_slices = self._create_time_slices(beg, end)

        x_ = []
        y_ = []
        last = 0
        for i_slice in t_slices:
            # stupid reverse transform:
            beg_ = i_slice[0].strftime("%Y-%m-%d")
            end_ = i_slice[1].strftime("%Y-%m-%d")

            # Get fond values
            fond_slice = self.GetFond(fond_url, beg_, end_)

            x_a = fond_slice['time_series'][0]
            y_a = fond_slice['time_series'][1]

            for i, i_element in enumerate(x_a):
                if x_a[i] in x_ or y_a[i] is None:
                    continue
                else:
                    x_.append(x_a[i])
                    y_.append(y_a[i]+last)
            print(y_a[0], y_a[-1], len(y_a))
            last = y_[-1]


        #manipulate time series entry before returning:
        fond_slice['time_series'] = [x_, y_]

        return fond_slice


    def _create_time_slices(self, time_beg, time_end):
        """create_time_slices

        Aims to create time slices from the beginning (time_beg) to the end date (time_date)
        Each time slices reflects the valid months. E.g. 1st of July to 31st of July

        :param time_beg: A string in format YYYY-MM-DD or a datetime object
        :param time_end: A string in format YYYY-MM-DD or a datetime object
        :return t_slices: A list of datetime objects where each list entry is [beg_, end_]
        """
        if isinstance(time_beg, str):
            beg = datetime.datetime.strptime(time_beg, '%Y-%m-%d')
        else:
            beg = time_beg
        if isinstance(time_end, str):
            end = datetime.datetime.strptime(time_end, '%Y-%m-%d')
        else:
            end = time_end
        day = 1
        t_slices = []
        d0 = beg
        d1 = (beg.replace(day=day) + datetime.timedelta(days=31)).replace(day=day)

        t_slices.append([d0, d1])

        while d1 <= end:
            d0 = (d0.replace(day=day) + datetime.timedelta(days=31)).replace(day=day)
            d1 = (d1.replace(day=day) + datetime.timedelta(days=31)).replace(day=day)
            t_slices.append([d0, d1])

        return t_slices

    def _get_first(self, time_series, reverse=False):

        if reverse == True:
            time_series.reverse()

        first_x = None
        first_y = None
        for i_day in time_series:
            x_ = i_day[0]
            y_ = i_day[1]
            if y_ != None:
                first_x = x_
                first_y = y_
                break
        return first_x, first_y

