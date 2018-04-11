#-*- coding:utf-8 -*-
from pro import Pro
#资产包属性
class Pack(object):
	def __init__(self):
		self.packId = ''
		self.packName = ''
		self.taskName = ''
		self.packManager = ''
		self.proList = []
		self.proListLength = 1
		self.manager = ''
		
	@classmethod
	def getProList(cls):
		proList = []
		for i in xrange(cls.proListLength):
			proList.append(cls.packName + str(i+1))
		return proList

	def initProList(self,subProNum):
		for i in range(subProNum):
			self.proList.append(Pro())