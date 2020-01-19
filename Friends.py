import pandas as pd
import re
import random

listAllMenu = ['MemberList', 'Uin', 'UserName', 'NickName', 
               'HeadImgUrl', 'ContactFlag', 'MemberCount', 
               'RemarkName', 'HideInputBarFlag', 'Sex',
               'Signature', 'VerifyFlag', 'OwnerUin', 
               'PYInitial', 'PYQuanPin', 'RemarkPYInitial', 
               'RemarkPYQuanPin', 'StarFriend', 'AppAccountFlag',
               'Statues', 'AttrStatus', 'Province', 'City', 
               'Alias', 'SnsFlag', 'UniFriend', 'DisplayName', 
               'ChatRoomId', 'KeyWord', 'EncryChatRoomId', 
               'IsOwner', 'HeadImgUpdateFlag', 'ContactType', 'ChatRoomOwner']

class OneMerber():
    def __init__(self,dictOne):
        self.UserName = dictOne.get("UserName",None)
        self.Sex = dictOne.get("Sex",2)
        self.Signature = dictOne.get("Signature",'')
        self.RemarkName = dictOne.get("RemarkName",'')
        self.City = dictOne.get("City",'')
        self.Province = dictOne.get("Province",'')
        self.NickName = dictOne.get("NickName",'')
        self.DealAllAttr()
    def DealAllAttr(self):
        listNeedRemoveFH = [self.RemarkName,self.NickName,self.NickName,]
        self.RemarkName1= re.sub(re.compile("[^\u4e00-\u9fa5]"),'',self.RemarkName)
        self.NickName1= re.sub(re.compile("[^\u4e00-\u9fa5]"),'',self.NickName)
        self.Signature1= re.sub(re.compile("[^\u4e00-\u9fa5]"),'',self.Signature)
        
        self.Name = self.RemarkName1 if self.RemarkName1 else self.NickName1
        teacher = re.findall(".老师",self.Name)
        self.Name = self.Name if teacher == [] else teacher[0]
        FriendsMom = re.findall("妈",self.Name)
        self.Name = self.Name if FriendsMom == [] else "阿姨"
        self.Name = self.Name[-3:]
        self.Name = self.NickName if self.Name == '' else self.Name
        

def MakeExcel2List(SexId):
    df = pd.read_excel('WeiZhi.xlsx')
    dictSex2Words = df.to_dict()
    return random.choice(dictSex2Words[SexId])   
df = pd.read_pickle("friends").T

for i in df:
    dfOne = df[i]
    dictOne = dfOne.to_dict()
    Friend = OneMerber(dictOne)
    print(Friend.Name+" \n新年好啊\n"+str(MakeExcel2List(Friend.Sex))+"\n\n")

    
    
    