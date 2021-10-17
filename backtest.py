import datetime
import os.path
import sys
import backtrader as bt

cerebro = bt.Cerebro()

modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
datapath = os.path.join(modpath, 'datas/orcl-1995-2014.txt')

data = bt.feeds.YahooFinanceData(
    dataname=datapath,
    fromdate=datetime.datetime(2000, 1, 1),
    todate=datetime.datetime(2000, 12, 31),
    reverse=False)

cerebro.adddata(data)

cerebro.broker.setcash(100000.0)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
