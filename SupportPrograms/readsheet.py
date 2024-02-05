import csv
from datetime import datetime

# Class to help create objects for LabMonitor table 
class LabMonitor:  
    def __init__(self,dateTime,rollNumber):
        self.dateTime=dateTime
        self.rollNumber=rollNumber
        
# Class to help create objects for Equipment table 
class Equipment:
    def __init__(self,rollNumber,equipment):
        self.rollNumber=rollNumber
        self.equipment=equipment
   
# Finding total number of coloumns   
with open("E:\Padhai\Programs\RFID\Data\Chem28_01_23.csv","r") as rfid:
    first_line = rfid.readline()
    your_data = rfid.readlines()
ncol = first_line.count(',') + 1

# List of objects of LabMonitor and Equipment class
labMonitorList=[]
equipmentList=[]

with open("E:\Padhai\Programs\RFID\Data\Chem28_01_23.csv","r") as rfid:
    csvReader=csv.reader(rfid);
    
    for line in csvReader:
        for i in range (0,ncol):
            if(line[i].startswith("2")==True):
                labMonitorList.append(LabMonitor(datetime.now().strftime("%Y-/%m/%d %H:%M:%S"),line[i]));
                j=i+1
                equip=[]
                while (j<ncol and line[j].startswith("2")!=True):
                    equip.append(line[j])
                    j+=1
                equipmentList.append(Equipment(line[i],equip))

    