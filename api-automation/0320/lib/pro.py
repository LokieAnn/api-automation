#-*- coding:utf-8 -*-
from rule import Rule
from user import User

#项目属性
class Pro(object):
	def __init__(self):
		self.proId = ''
		self.proName = u'单项目-挂牌-场外结算1'
		self.taskUrl = ''
		self.taskName = ''
		self.mainStatus = ''
		self.rule = Rule()
		self.buyerGroup = []
		self.info = {}
		self.manager = ''

	def setBuyerGroup(self,userGroup):
		self.buyerGroup = []
		if ',' not in userGroup:
			self.buyerGroup.append(User(userGroup))
		else:
			for i in userGroup.split(','):
				self.buyerGroup.append(User(i))



 