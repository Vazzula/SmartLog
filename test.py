from SupportPrograms import Server_PC
import mysql.connector
import pandas as pd

try:
    conn=mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="",
                                 database="smartlog")
    
    cursor=conn.cursor()
    
    while True:
        print("Connected")
        roll=Server_PC.read()
        i=0
        
        if roll[i].startswith('2')==True:
            equip=Server_PC.read()
            while equip[i].startswith('2')!=True:
                 cursor.execute("insert into entries(Timestamp,Rollnumber) values(current_timestamp(),%s)",(roll,))
                 cursor.execute("delete t1 from entries t1 inner join entries t2 where t1.SNO < t2.SNO and t1.Rollnumber=t2.Rollnumber")
                 conn.commit()
                 
                 cursor.execute("insert into pending(Rollnumber,EquipmentId) values(%s,%s)",(roll,equip))
                 cursor.execute("delete from pending where EquipmentId IN(SELECT EquipmentId FROM pending GROUP by EquipmentId HAVING COUNT(EquipmentId)=2)")
                 conn.commit()
                 
                 print('Data inserted')
                 equip=Server_PC.read()
                 
        else:
            print('Please tap your card first')
            
except :
    print('Failed to connect')

finally:
    if cursor:
        cursor.close()
        
    if conn:
        conn.close()