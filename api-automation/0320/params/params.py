#-*- coding:utf-8 -*-
import collections
from urllib import unquote

class Params(object):
	def __init__(self):
		#接口地址
		#**地址头不要写死
		#修改实物项目字典
		self.IFAddressHead = {
			#'utr' : "http://web.unibid.cn/utr",
			'utr' : "http://utr.utrm.com/utr-web",
			#'sso' : 'http://web.unibid.cn/sso',
			'sso' : "http://sso.utrm.com",
			#'sso' : "http://wwwtest.unibid.cn/sso",
		}
		self.utrInterFaceAddress = {\
			#登录
		    #'login' : 'http://sso.utrm.com/passport/login/login.action',
		    'login' : self.IFAddressHead['sso'] + "/passport/login/login.action",
			#新增
			'newUtrmPro' : self.IFAddressHead['utr'] + "/utr/pro/save.action",
			'newUtrmPack' : self.IFAddressHead['utr'] + "/utr/pack/save.action",
			#'newUTRG' : "http://utr.utrm.com/utr-web/utrg/pro/save.action",
			'newUTRG' : self.IFAddressHead['utr'] + "/utrg/pro/save.action",
			'newSubPro' : self.IFAddressHead['utr'] + "/utr/pro/singleSave.action",

			#录入
			#'comp' : "http://utr.utrm.com/utr-web/utr/comp/rf/",
			#'finance' : "http://utr.utrm.com/utr-web/utr/finance/rf/",
			#'info' : "http://utr.utrm.com/utr-web/utr/info/rf/",
			#'seller' : "http://utr.utrm.com/utr-web/utr/seller/rf/",
			#'buyer'	: "http://utr.utrm.com/utr-web/utr/buyer/rf/",
			#'estimate' : "http://utr.utrm.com/utr-web/utr/estimate/rf/",
			#'mgr' : "http://utr.utrm.com/utr-web/utr/seller/mgrSave.action",
			#'pub' : "http://utr.utrm.com/utr-web/utr/pub/rf/",
			#'holder' : "http://utr.utrm.com/utr-web/utr/holder/rf",
			'comp' : self.IFAddressHead['utr'] + "/utr/comp/rf/",
			'finance' : self.IFAddressHead['utr'] + "/utr/finance/rf/",
			'info' : self.IFAddressHead['utr'] + "/utr/info/rf/",
			'seller' : self.IFAddressHead['utr'] + "/utr/seller/rf/",
			'buyer'	: self.IFAddressHead['utr'] + "/utr/buyer/rf/",
			'estimate' : self.IFAddressHead['utr'] + "/utr/estimate/rf/",
			'mgr' : self.IFAddressHead['utr'] + "/utr/seller/mgrSave.action",
			'pub' : self.IFAddressHead['utr'] + "/utr/pub/rf/",
			'pubMethod' : self.IFAddressHead['utr'] + "/utr/pub/pubEdit.action",
			'rules' : self.IFAddressHead['utr'] + "/utr/packFlow/pack!setProRulesDo.action",
			'holder' : self.IFAddressHead['utr'] + "/utr/holder/rf",
			'contact' : self.IFAddressHead['utr'] + "/utr/proContact/rf/",
			'utrmProSubmit' : self.IFAddressHead['utr'] + "/utr/proFlow/pro!submit.action?",
			'utrmPackSubmit' : self.IFAddressHead['utr'] + "/utr/packFlow/pack!submit.action?",
			'p3ProSubmit' : self.IFAddressHead['utr'] + "/utrg/g3Flow/pro!p3submit.action?",
			'g3ProSubmit' : self.IFAddressHead['utr'] + "/utrg/g3Flow/pro!submit.action?",
			#工作流
			'g3Flow' : self.IFAddressHead['utr'] + "/utrg/g3Flow/flowDo",
			'proFlow' : self.IFAddressHead['utr'] + "/utr/proFlow/flowDo",
			'packFlow' : self.IFAddressHead['utr'] + "/utr/packFlow/flowDo",
			'buyerFlow' : self.IFAddressHead['utr'] + "/utr/buyerFlow/flowDo",
			#报名
			'backEndSignUp' : self.IFAddressHead['utr'] + "/utr/buyer/customTobuyer?",
			#模拟摘牌
			'unpub' : self.IFAddressHead['utr'] + "/utr/auto/pro!manUnpub.action?processInsId=",
			#摘牌确认(人)
			'manUnpub' : self.IFAddressHead['utr'] + "/utr/proFlow/pro!unpubConfirmDo.action",
			#推送竞价大厅
			'pushToBid' : self.IFAddressHead['utr'] + "/utr/auto/pro!pushProRuleAndBuyers.action",
			'pushPro' : self.IFAddressHead['utr'] + "/utr/auto/pro!pushPro.action",
			#推送受让方
			'pushBuyer' : self.IFAddressHead['utr'] + "/utr/auto/buyer!push.action",
			#确认成交发布公告
			'setDeal' : self.IFAddressHead['utr'] + "/utr/auto/pro!setDeal.action",
			#生成交易凭证
			'certFlow' : self.IFAddressHead['utr'] + "/utr/certFlow/flowDo.action",
			#生成价款划入凭单
			'createBill' : self.IFAddressHead['utr'] + "/utr/auto/pro!createBill.action",
			#状态更新
			'updateStatus' : self.IFAddressHead['utr'] + "/utr/bill/updateStatus.action",
			#确认价款结算
			'setBillIn' : self.IFAddressHead['utr'] + "/utr/auto/pro!setBillIn.action",
			#退保证金
			'returnBail' : self.IFAddressHead['utr'] + "/utr/auto/pro!returnBail.action",
			#生成价款划出凭单
			'createBillOut' : self.IFAddressHead['utr'] + "/utr/auto/createBillOut",
		} 
		# self.utrInterFaceAddress = {\
		# 	#登录
		#     'login' : 'http://sso.utrm.com/passport/login/login.action',
		# 	#新增
		# 	'newPro' : "http://utr.utrm.com/utr-web/utr/pro/save.action",
		# 	'newUTRG' : "http://utr.utrm.com/utr-web/utrg/pro/save.action",
		# 	#录入
		# 	'comp' : "http://utr.utrm.com/utr-web/utr/comp/rf/", 
		# 	'finance' : "http://utr.utrm.com/utr-web/utr/finance/rf/",
		# 	'info' : "http://utr.utrm.com/utr-web/utr/info/rf/",
		# 	'seller' : "http://utr.utrm.com/utr-web/utr/seller/rf/",
		# 	'buyer'	: "http://utr.utrm.com/utr-web/utr/buyer/rf/",
		# 	'estimate' : "http://utr.utrm.com/utr-web/utr/estimate/rf/",
		# 	'mgr' : "http://utr.utrm.com/utr-web/utr/seller/mgrSave.action",
		# 	'pub' : "http://utr.utrm.com/utr-web/utr/pub/rf/",
		# 	'holder' : "http://utr.utrm.com/utr-web/utr/holder/rf",
		# 	'contact' : "http://utr.utrm.com/utr-web/utr/proContact/rf/",
		# 	'p3ProSubmit' : "http://utr.utrm.com/utr-web/utrg/g3Flow/pro!p3submit.action?",
		# 	'g3ProSubmit' : "http://utr.utrm.com/utr-web/utrg/g3Flow/pro!submit.action?",
		# 	#工作流
		# 	'g3Flow' : 'http://utr.utrm.com/utr-web/utrg/g3Flow/flowDo',
		# 	'proFlow' : 'http://utr.utrm.com/utr-web/utr/proFlow/flowDo/',
		# 	'buyerFlow' : 'http://utr.utrm.com/utr-web/utr/buyerFlow/flowDo',
		# 	#报名
		# 	'backEndSignUp' : 'http://utr.utrm.com/utr-web/utr/buyer/customTobuyer?',
		# 	#模拟摘牌
		# 	'unpub' : "http://utr.utrm.com/utr-web/utr/auto/pro!manUnpub.action?processInsId=",
		# 	#摘牌确认(人)
		# 	'manUnpub' : "http://utr.utrm.com/utr-web/utr/proFlow/pro!unpubConfirmDo.action",
		# 	#推送竞价大厅
		# 	'pushToBid' : "http://utr.utrm.com/utr-web/utr/auto/pro!pushProRuleAndBuyers.action"
		# }
		#登录参数
		#self.loginParam = {'userEname': 'CS_super', 
        #                   'sys': 'e0cea4bb45e36c115356e46910c354af', 
        #                   'cset': 'http://wwwtest.unibid.cn:80/utr/cset', 
        #                   '_client': 'e9e417406b7bd6ee9915cac7d97e2520f106e986', 
        #                   'go': 'http://wwwtest.unibid.cn:80/utr/', 
        #                   'userPass': '96e79218965eb72c92a549dd5a330112', 
        #                   #'password': '918082'
        #                   }
		self.loginParam = {'userEname': 'super', 
                           'sys': 'e0cea4bb45e36c115356e46910c354af', 
                           'cset': 'http://utr.utrm.com:80/utr-web/cset', 
                           '_client': '1219518aa57a52bbfd8d12dc532e40571e03b424', 
                           'go': 'http://utr.utrm.com:80/utr-web/', 
                           'userPass': '96e79218965eb72c92a549dd5a330112', 
                           'password': '918082'}
		# self.loginParam = {'go' : 'http://web.unibid.cn:80/utr/',
		# 				   'cset' : 'http://web.unibid.cn:80/utr/cset',
		# 				   'sys' : 'e0cea4bb45e36c115356e46910c354af',
		# 				   '_client' : '24f3cb6b25138313c13755f37581ecd1b7faa879',
		# 				   'userPass' : '96e79218965eb72c92a549dd5a330112',
		# 				   'userEname' : 'TJ_super',}

		self.signUpParam = {'requestAddress' : 'backEndSignUp',
		  		  	       'requestMethod' : 'get',
		  		  	       'requestUrl' : self.utrInterFaceAddress['backEndSignUp'],
		  		  	       'extendUrl' : '',
				   	       'getParamExt' : '',
					       }

		self.buyerFlowParam = {'requestAddress' : 'buyerFlow',
						       'requestMethod' : 'post',
						       'requestUrl' : self.utrInterFaceAddress['buyerFlow'],
						       'extendUrl' : '',
						       'requestBody' :{'formToken' : '1174c3e3-b574-45b6-aaa8-8b56fd9b8a39',
										       'taskId' : '381877',
										       'processStatus' : u'经办人审核受让方',
										       'formId' : '85878eb3fdd1461985ac1d3b14a94003',
										       'taskName' : u'经办人审核受让方',
										       'processInsId' : 'buyerMain.381258',
										       'logResult' : 'T',
										       'assignee' : 'super',
										       'pluginName' : 'buyerReg',
										       'mainStatus' : '',
										       'buyerId' : '85878eb3fdd1461985ac1d3b14a94003',
										       'notAccept' : '',
										       'logText' : '1',}
						       }

		self.unpubParam = {'requestAddress' : 'unpub',
			               'requestMethod' : 'mix',
			               'requestUrl' : self.utrInterFaceAddress['unpub'],
			               'extendUrl' : '',
			               'requestBody' : {},
			              }

		self.manUnpubParam = {'requestAddress' : 'manUnpub',
						      'requestMethod' : 'post',
						      'requestUrl' : self.utrInterFaceAddress['manUnpub'],
						      'extendUrl' : '',
						      'requestBody' : {'formToken' : '0b815aed-3d03-4b60-9343-09fe2264af35',
						     				   'taskId' : '640595',
						     				   'processStatus' : u'摘牌确认(人)',
						     				   'formId' : 'aca906c9116445dc9652d7d1c7d019cd',
						     				   'taskName' : u'摘牌确认(人)',
						     				   'processInsId' : 'proFlow3.640433',
						     				   'logResult' : 'GOON',
						     				   'assignee' : 'super',
						     				   'pluginName' : '',
						     				   'mainStatus' : '',
						     				   'flowMap-menend' : '',
						     				   'flowMap_mendelay' : '',
						     				   'proId' : 'aca906c9116445dc9652d7d1c7d019cd',
						     				   'packId' : '',
						     				   'delayPeroid' : '',
						     				   'mendelayReason' : '',
						     				   'mendelayAudit' : 'T',
						 				 	  }
							}

		self.confirmBillParam = {'requestAddress' : 'confirmBill',
						         'requestMethod' : 'post',
						         'requestUrl' : self.utrInterFaceAddress['updateStatus'],
						         'extendUrl' : '',
						         'requestBody' : {'formToken' : '',
                                                  'billId' : '64d71cf21ea74a20acf1cf6e30293cd7',
                                                  'billStatus' : '40',
                                                  'proId' : 'b28b04d569c244f8af8a53bceb0d60fe',
                                                  'packId' : '',
                                                  'bankFlowNo' : '',
                                                  'bankNo' : '银行账号',
                                                  'account' : '账户名称',
                                                  'openBankAddres' : '开户银行',
                                                  'reachDate' : '2017-03-06+16:47:22',
                                                  'spare1' : '',
						 				 	     }
		}

	def getParam(self,requestAddress,requestMethod,sheetName):
		d = {}
		d['requestAddress'] = requestAddress
		d['requestMethod'] = requestMethod
		d['requestUrl'] = self.utrInterFaceAddress[requestAddress]
		d['requestBody'] = self.table.param[sheetName]
		return d

	def intNumber(self,string):
		for i in string.split('.')[-1]:
			if i in map(str,range(1,10)):
				return string
		return string.split('.')[0]

	def getProvince(self,zone):
		return int(zone)/1000*1000 if zone else ''

	def convertPostParam(self,s):
		d = collections.OrderedDict()
		s = s.split("&")
		for i in s:
		    i = i.split("=")
		    d[i[0]] = i[1]
		for k,l in d.items():
			if '%' in l:
				l = unquote(l).decode('utf-8')
			print '\'' + k + '\'' + ' : ' + '\'' + l + '\'' + ','
		return d