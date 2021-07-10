import pandas as pd
import logging
from datetime import datetime
from kiteconnect import KiteConnect
from pandas._libs.tslibs.offsets import BDay

from EquityDataAccess import EquityDataAccess
from FactorClass import FactorClass
from Constants import equity_index_mapping
from WriteToGSheet import WriteToGSheets

print('''Connection Started''')
api_key = 'kite_connect will provide'
access_token = 'keep_on_changing_everytime' #https://kite.trade/connect/login?api_key=xyz
secret_key = 'kite_connect will provide'
kite = KiteConnect(api_key=api_key)
data = kite.generate_session(access_token, secret_key)
kite.set_access_token(data["access_token"])
print('''Connection Done''')


'''Fetching Data'''
todays_date = datetime.now()
equityIdList = ['SBIN', 'HDFC', 'ICICIBANK', 'AXISBANK', 'KOTAKBANK']
startDate = datetime(todays_date.year, todays_date.month, todays_date.day)-2*BDay()
endDate = startDate+BDay()
equity_data = EquityDataAccess(equityIdList, startDate, endDate).fill_data()
'''Fetching Data Done'''

'''Calling some signal from factor class'''
return_signal = FactorClass().return_series(equity_data)
'''Calling some signal from factor class done'''

'''Creating buy and sell trade using signal'''
buy_symbol = return_signal.sort_values('Return')['EquityId'].iloc[0]
sell_symbol = return_signal.sort_values('Return')['EquityId'].iloc[-1]

all_trades = {'BUY':[buy_symbol], 'SELL':[sell_symbol]}

for side in ['BUY','SELL']:
    for equityId in all_trades[side]:
        try:
            order_id = kite.place_order(tradingsymbol=equity_index_mapping[equityId],
                                        exchange=kite.EXCHANGE_NSE,
                                        transaction_type=side,
                                        quantity=1,
                                        variety=kite.VARIETY_REGULAR,
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        product=kite.PRODUCT_CNC)

            logging.info("Order placed. ID is: {}".format(order_id))
        except Exception as e:
            logging.info("Order placement failed: {}".format(e.message))















