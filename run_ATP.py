# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 15:04:04 2018

@author: JiaJun
"""
import os
import multiprocessing
#import atp
'''import win32api
import win32event
import win32process
import subprocess
import time
import win32gui
import win32con
'''
def execCmd(cmd):  
    r = os.popen(cmd)
#    print('key1') 
    text = r.read()
#    print('key2')
    r.close()  
    #print('key2.5')
    return text 


def run_ATP(ATPfile):
#    if os.path.exists(ATPfile+ '.pl4'):
#        os.remove(ATPfile+ '.pl4')
    ATPpath='cd C:\\ATP\\atpmingw && tpbig.exe both ';
    #ATPfile='D:\\ATPauto\\test';
    trytimes=1;
    while (not os.path.exists(ATPfile+ '.pl4')) and trytimes<3:
        text=execCmd(ATPpath+ ' ' + ATPfile + '.atp s -r');
        trytimes += 1
        
    #if os.path.exists(ATPfile+ '.pl4'):
    #    os.popen('D:\\ATPauto\\Pl42mat.exe ' +ATPfile+ '.pl4')
    #print('key3')
    #print(text)
    #handle=subprocess.popen(ATPpath+ ' ' + ATPfile + '.atp s -r')
    #result=os.system(ATPpath+ ' ' + ATPfile + '.atp s -r')#+ '&'
    #r=win32api.ShellExecute(0, 'open', ATPpath, ATPfile + '.atp','',0)
    '''handle = win32process.CreateProcess(ATPpath,
                                        ATPfile + '.atp s -r',
                                        None,
                                        None,
                                        0,
                                        win32process.CREATE_NO_WINDOW,
                                        None,
                                        None,
                                        win32process.STARTUPINFO());
    print(handle)'''
'''
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=1)
    pool.map(run_ATP, ['D:\\ATPauto\\test1','D:\\ATPauto\\test2','D:\\ATPauto\\test3','D:\\ATPauto\\test4','D:\\ATPauto\\test5','D:\\ATPauto\\test6'])
    pool.close()
    pool.join()   
    print('done')
'''