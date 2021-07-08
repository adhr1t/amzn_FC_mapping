import pandas as pd
import numpy as np

injurydf = pd.read_csv("Injuries_2018-2021.csv")
ratesdf = pd.read_csv("InjuryRates_2018-2021S.csv")
amnestydf = pd.read_csv("Amnesty_June2021.csv")


#drop unnecessary columns
injurydf.drop(["Organization","Sub-Organization", "Site", "World Region"], axis=1, inplace=True)
ratesdf.drop(["Organization","Sub-Organization", "Site"], axis=1, inplace=True)


# in injurydf maybe we can look at how "Place of Accident", "Shift Start", "Supervisor"?, "Time In Job", "Time In Company"
# and "Primary Cause" all relate to Injury Rates in ratesdf

# can also look at how amnestydf "Units" or ratesdf "Hours Worked"? relate to Injury Rates in ratesdf 
# "Cumulative Recordable Rate" or "Cumulative DAFW Rate"


#remove period in injurydf "Place of Accident"
placeAccident = injurydf['Place of Accident'].apply(lambda x: str(x).lower().split('.')[0])
