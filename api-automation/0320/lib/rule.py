#-*- coding:utf-8 -*-
from lib.config import TODAY

#规则类
class Rule(object):
	def __init__(self):
		self.projectType = "utrm"
		self.projectSubType = "utrmPro"
		self.proType = ""
		self.proPrice = "100"
		self.pubDays = "20"
		self.pubDealWay = "A10004"
		self.buyerAuditLevel = "1"
		self.pubBail = "1000"
		self.bailStartFlag = "0"
		self.pubBailType = "0"
		self.pubBailDays = "5"
		self.bailDeadTime = TODAY
		self.pubBailMethod = ["0","2"]
		self.pubPayMode = "A03001"
		self.pubDelayFlag = "F"
		self.delayBuyerSize = "2"
		self.delayMax = "5"
		self.delayPeroid = "2"
		self.allowEndPrio = "F"
		self.announceWay = ["A16001","A16002"]
		self.unitTransferee = "T"

		self.pubDealWayList = ["A10004","A10002","A10001","A10006"]
		self.pubBailMethodList = ["0","2","4"]
		self.announceWayList = ["A16001","A16002","A16003","A16004"]