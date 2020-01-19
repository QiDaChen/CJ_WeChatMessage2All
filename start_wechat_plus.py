# -*- encoding: utf-8 -*-
'''
@File        :start_wechat_plus.py
@Desc        :
@Time        :2020/01/16 15:18:03
@Author      :chen.qi
@Mail        :chenphoun@outlook.com
'''

import itchat
import pandas as pd
import random
import time
import pickle
from Friends import OneMerber as OneMerber
dictAlready = dict()

def MakeExcel2List(SexId):
    df = pd.read_excel('WeiZhi.xlsx')
    dictSex2Words = df.to_dict()
    return random.choice(dictSex2Words[SexId])

def main():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)[1:13]
    df = pd.DataFrame(friends)
    df.to_pickle("friends")
    SendMsg()

def SendMsg():
    isok = False
    df = pd.read_pickle("friends").T
    for i in df:
        with open('svm_model_ard.pkl', 'rb') as f:
            dictAlready = pickle.load(f)
        dfOne = df[i]
        dictOne = dfOne.to_dict()
        Friend = OneMerber(dictOne)
        if dictAlready.get(Friend.UserName,False):
            continue
        msg = Friend.Name + " \n新年好鸭~~~~\n" + str(MakeExcel2List(Friend.Sex)) + "\n\n"
        print(msg)
        dictMsgBack = itchat.send_msg(msg=msg,toUserName=Friend.UserName).get("BaseResponse",'')
        if isinstance(dictMsgBack,dict):
            isok = dictMsgBack.get('RawMsg',False)
        dictAlready[Friend.UserName] = isok
        time.sleep(0.5)
        with open('svm_model_ard.pkl', 'wb') as f:
            pickle.dump(dictAlready, f)

if __name__ == "__main__":
    main()





    