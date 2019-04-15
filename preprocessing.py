import pandas as pd

# fetch the survey results of 2018 for Public Service and CFIA

data_2018 = data[(data["SURVEYR"] == 2018) & (data["BYCOND"].isnull())]
data_2018_ps = data_2018[data_2018["LEVEL1ID"] == 0]
data_2018_cfia = data_2018[data_2018["LEVEL1ID"] == 86]