# -*- coding: utf-8 -*-
from pyvanza.module.pyvanzascraper import AvanzaScraper
import pickle
import argparse

"""Main module."""
def pyvanza_standalone():
    parser = argparse.ArgumentParser(description="Run the pyvanza scraper")

    parser.add_argument('--fond', dest="fond", type=str,
                        help="An Avanza URL you are interested in")
    parser.add_argument('--from', dest="beg", type=str,
                        help="A start date (form: <year><month><day>, e.g. 2019-11-01")
    parser.add_argument('--to', dest="end", type=str,
                        help="A end date (form: <year><month><day>, e.g. 2019-11-01")
    parser.add_argument('--output', dest="output", type=str, default="output",
                        help="Output file name (pandas dataframe)")

    args = parser.parse_args()

    #Init the scraper
    avs = AvanzaScraper()

    #Try/except to get a dataframe with the values:
    try:
        values = avs.GetFond(args.fond, args.beg, args.end)
        print(values)
        with open(f'{args.output}.pkl', 'wb') as handle:
            pickle.dump(values, handle, protocol=pickle.HIGHEST_PROTOCOL)

        nb = len(values['time_series'][0])
        print()
        print(f"A dataset with {nb} data points is extracted from {args.fond} and stored in {args.output}.pkl")
        print()
    except:
        print("... Something went wrong!")
        print("Check for:")
        print("  <> Your fond URL")
        print("  <> The format of the first and last day  to receive fond values")
    exit()
