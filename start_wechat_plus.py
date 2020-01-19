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

def main():  
    itchat.auto_login(hotReload=True) 
    friends = itchat.get_friends(update=True)[1:]    
    df = pd.DataFrame(friends)
    df.to_pickle("friends")
    print("ok")
    return df
if __name__ == "__main__":
    fs = main()
    print(111)
    