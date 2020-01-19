import pandas as pd
import random 
def MakeExcel2List(SexId):
    df = pd.read_excel('WeiZhi.xlsx')
    dictSex2Words = df.to_dict()
    return random.choice(dictSex2Words[SexId])