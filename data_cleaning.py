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
# add 0 to the beginning of all the time recordings
injurydf['Shift_Start_Time'] = injurydf['Shift Start Time'].apply(lambda x: '0' + str(x) if ':' in str(x)[:2] else x)
injurydf['Time_Recorded'] = injurydf['Time Recorded'].apply(lambda x: '0' + str(x) if ':' in str(x)[:2] else x)
injurydf['Case_Time'] = injurydf['Case Time'].apply(lambda x: '0' + str(x) if ':' in str(x)[:2] else x)


# method to convert times to 24hr clock
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
    
    # add 12 to hours and remove PM    
    else:
        return str(int(str1[:2]) + 12) + str1[2:5]

# make list with all the times converted to the 24hr scale
caseTime24hr=[]
for i in range(len(injurydf['Case_Time'])):
    #if the time recorded is nan then insert the time listed from injurydf['Time_Recorded']
    if pd.isnull(injurydf['Case_Time'][i]):
        caseTime24hr.append(convert24(injurydf['Time_Recorded'][i]))
    else:
        caseTime24hr.append(convert24(injurydf['Case_Time'][i]))
injurydf['Case_Time_24hr'] = caseTime24hr



        

