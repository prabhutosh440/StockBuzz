from nsepy import get_history
import yfinance as yf
import pandas as pd
import logging


class EquityDataAccess:

    def __init__(self, eqIdList, startDate, endDate):
        self.eqIdList = eqIdList
        self.startDate = startDate
        self.endDate = endDate

    def fill_data(self):
        datas = {}
        try:
            for equityId in self.eqIdList:
                temp = get_history(equityId, start=self.startDate, end=self.endDate)
                temp.index = pd.to_datetime(temp.index)
                datas[equityId] = temp
        except Exception as e:
            logging.info("Issue with NSEPY data fetching: {}".format(e.message))
        return datas

