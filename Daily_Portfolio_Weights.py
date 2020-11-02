from datetime import date,timedelta
from nsepy import get_history
import pandas as pd
import time

start_date = date.today() 
end_date   = date.today()

syms = pd.read_csv("ind_nifty100list.csv")
symbols = list(syms.Symbol)
data = pd.DataFrame(columns=symbols)

for sym in symbols:
    col = get_history(symbol=sym,start=start_date,end=end_date)
    data[sym] = col.Close
    time.sleep(5)
    print(sym)
    
data.to_csv("100.csv",mode='a',header=False)

time.sleep(2)
    
nDays = 50

data = pd.read_csv("100.csv")

shorts = (data[-nDays:].skew()/(data[-nDays:].kurtosis() + 2)).sort_values(ascending=False)[:5]
shorts = shorts/(shorts.sum())

shorts.to_csv("/Users/vipultanwar/Desktop/DailyCalls/" + str(end_date) + ".csv")