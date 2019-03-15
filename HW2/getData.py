import wbdata
import datetime
import pandas as pd

# SP.URB.TOTL.IN.ZS	            Urban population as percentage of total population
# NY.GDP.PCAP.CD                GDP per capita in USD

def getData():
    data_date = datetime.datetime(2010, 1, 1)
    x = wbdata.get_data("NY.GDP.PCAP.CD", data_date = data_date, pandas = True)
    y = wbdata.get_data("SP.URB.TOTL.IN.ZS", data_date = data_date, pandas = True)
    data = pd.concat([x, y], axis = 1)
    data = data.dropna(axis=0, how='any')
    data.columns = ["gdp", "urbanPop"]
    x = data["gdp"].tolist()
    y = data["urbanPop"].tolist()
    return (x, y)
