import pandas as pd

def readRollNumber():
    df=pd.DataFrame({"SNO":[42,43],
                     "TimeStamp":["09-02-2023 12:30","09-02-2023 12:31"],
                     "Rollnumber":["21881A12G6","21881A12K0"]
                    })
    return df

def readRollNumber():
    df=pd.DataFrame({"SNO":[40,41,42],
                     "TimeStamp":["equipment2","equipment1","equipment3"],
                     "Rollnumber":["21881A12G6","21881A12K0","21881A12K0"]
                    })
    return df