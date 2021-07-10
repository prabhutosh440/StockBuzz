import pandas as pd


class FactorClass:

    def __init__(self):
        pass

    def return_series(self, data, type='Close'):

        return_dict = {}
        equityIds = data.keys()
        for equityid in equityIds:
            equityData = data[equityid]
            equity_return = (equityData[type].iloc[-1]-equityData[type].iloc[-2])/equityData[type].iloc[-1]
            return_dict[equityid] = [equity_return]
        return_series = pd.DataFrame(return_dict).T.reset_index()
        return_series.columns = ['EquityId', 'Return']
        return return_series










