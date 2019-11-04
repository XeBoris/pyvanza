import urllib.request
import json
import datetime

class AvanzaScrapper(object):

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
        return return_data

