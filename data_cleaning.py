import pandas as pd
import numpy as np

injurydf = pd.read_csv("Injuries_2018-2021.csv")
ratesdf = pd.read_csv("InjuryRates_2018-2021S.csv")
amnestydf = pd.read_csv("Amnesty_June2021.csv")


#drop unnecessary columns
injurydf.drop(["Organization","Sub-Organization", "Site", "World Region", "Location", "Workstation", "Employee Badge",
               "Follow-up Investigation Team", "Case Closure Verifier", "Component", "In Home Country?"], axis=1, inplace=True)
ratesdf.drop(["Organization","Sub-Organization", "Site"], axis=1, inplace=True)
amnestydf.drop(["Employee Id","GL_CODE"], axis=1, inplace=True)


# in injurydf maybe we can look at how "Place of Accident", "Case Date"(see if injuries are higher in certain months), difference
# of "Shift Start" and "Case Time", "Supervisor"?, "Case Level", "Time In Company" and "Primary Cause" all relate to Injury Rates in ratesdf

# can also look at how amnestydf "Units" or ratesdf "Hours Worked"? relate to Injury Rates in ratesdf 
# "Cumulative Recordable Rate" or "Cumulative DAFW Rate"


# remove period in injurydf "Place of Accident"
placeAccident = injurydf['Place of Accident'].apply(lambda x: str(x).lower().split('.')[0])
injurydf['Place_of_Accident'] = placeAccident

# extract the month from the date of injury
monthInjury = injurydf['Case Date'].apply(lambda x: str(x).lower().split('-')[1])
injurydf['Month_of_Injury'] = monthInjury

# calc difference between "Shift Start" and "Case Time"

# add 0 to the beginning 
adjCaseTime = injurydf['Case Time'].apply(lambda x: '0' + str(x) if ':' in str(x)[:2] else x)

# convert times to 24hr clock
def convert24(str1):
      
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
          
    # remove the AM    
    elif str1[-2:] == "AM":
        return str1[:-2]
      
    # Checking if last two elements of time
    # is PM and first two elements are 12   
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
          
    else:
          
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]
    
    
print(adjCaseTime[5])
print(convert24(adjCaseTime[64]))
