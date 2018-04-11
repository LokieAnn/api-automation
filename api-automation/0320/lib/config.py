#-*- coding:utf-8 -*-
import time
import sys,os

#每个操作间隔时间
WAIT_TIME = 10
SKIP_TIME = 1.5
DT_WAIT_TIME = 30

#-----------------------------------------------------
#当日时间
# nowtime = time.strftime("%Y-%m-%d", time.localtime())
# print nowtime

TODAY = time.strftime("%Y-%m-%d", time.localtime())

NOW_TIME = time.strftime("%H:%M:%S",time.localtime())
# if TODAY[5] == '0':
#     TODAY = TODAY[:5]+TODAY[6:]
# if TODAY[-2] == '0':
# 	TODAY = TODAY[:-2]+TODAY[-1]

date = time.strftime("%m%d", time.localtime())

ABSPATH = os.path.dirname(os.path.abspath(sys.argv[0]))

#-----------------------------------------------------
#常用URL
UTRM_LOGIN_URL = "http://utr.utrm.com/utr-web/"
PORTAL_LOGIN_URL = "http://www.utrm.com/portal/login.jsp"
PORTAL_MAIN_URL = "http://www.utrm.com"
SSO_LOGIN_URL = "http://sso.utrm.com"

#--------------------------------------------------------
#项目名称
PRO_CREATE_NAME = u'926单项目-test1'
PACK_CREATE_NAME = u'资产包-待改名'

