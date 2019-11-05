# -*- coding: utf-8 -*-
import urllib.request
import json
import datetime
from pyvanza import AvanzaScrapper
import pickle
import pandas as pd
import argparse

"""Main module."""

class pyvanza():

    def __init__(self):
        #constructor
        print("Init")

    def SetStorageManager(self, storagem):
        self.storagem = storagem




def pyvanza_standalone():
    parser = argparse.ArgumentParser(description="Run your favourite aDMIX")

    parser.add_argument('--fond', dest="fond", type=str,
                        help="An Avanza URL you are interested in")
    parser.add_argument('--from', dest="beg", type=str,
                        help="A start date (form: <year><month><day>, e.g. 2019-11-01")
    parser.add_argument('--to', dest="end", type=str,
                        help="A end date (form: <year><month><day>, e.g. 2019-11-01")
    parser.add_argument('--output', dest="output", type=str, default="output",
                        help="Output file name (pandas dataframe)")

    args = parser.parse_args()

    #Init the scrapper
    avs = AvanzaScrapper()

    #Try/except to get a dataframe with the values:
    try:
        values = avs.GetFond(args.fond, args.beg, args.end)
        with open(f'{args.output}.pkl', 'wb') as handle:
            pickle.dump(values, handle, protocol=pickle.HIGHEST_PROTOCOL)

        nb = len(values['time_series'])
        print()
        print(f"A dataset with {nb} data points is extracted from {args.fond} and stored in {args.output}.pkl")
        print()
    except:
        print("... Something went wrong!")
        print("Check for:")
        print("  <> Your fond URL")
        print("  <> The format of the first and last day  to receive fond values")
    exit()
