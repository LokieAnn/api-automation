#-*- coding:utf-8 -*-
import requests
import time
import collections
import copy

from urllib import unquote
from lib.pro import Pro
from lib.user import User
from lib.sqlUtil import SqlUtil
from lib.config import TODAY,NOW_TIME

from lib.table import Table
from params.params import Params
from params.utrgParams import UtrgParams

SqlUtil.init()

class UtrRequest(requests.Session):
	def __init__(self,pro=None,pack=None):
		super(UtrRequest,self).__init__()
		self.pro = pro
		self.pack = pack
		self.params = Params()
		self.headers = {'Accept' :'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                	    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 
                	    'Accept-Encoding': 'gzip, deflate', 
                	    'Accept': 'application/json, text/javascript, */*; q=0.01', 
                	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0', 
                	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                	    'X-Requested-With': 'XMLHttpRequest',
                	    }


	#登录请求
	def login(self,address,param):
		self.post(address,param,headers = self.headers)
		#self.get("http://utr.utrm.com/utr-web/") #**地址不能写死

	#portal登录
	def portalLogin(self,address,param):
		#s = 'http://www.utrm.com/portal/doUsers/login?userAgent=m'
		s = 'http://portal.zjpse.com/portal/doUsers/login?userAgent=m'
		self.post(s,{'username':param['userEname'],'password':'96e79218965eb72c92a549dd5a330112'})
		#self.login(address,param) #需替换登录用户名
		self.get('http://jjdt.utrm.com/applyc.jsp')#**地址不能写死

	#新增单项目
	def newPro(self,param):
		# pro = self.pro
		# param['requestBody']['proName'] = pro.proName
		# param['proPrice'] = pro.rule.proPrice
		r = self.post(param['requestUrl'],param['requestBody'],headers = self.headers)
		if 'T' == eval(r.text)['flag']:
			return eval(r.text)['msg']
		else:
			raise Exception(eval(r.text)['msg'])

	#新增资产包
	def newPack(self,param):
		#pro = self.pro
		# param['requestBody']['proName'] = pro.proName
		# param['proPrice'] = pro.rule.proPrice
		r = self.post(param['requestUrl'],param['requestBody'],headers = self.headers)
		if 'T' == eval(r.text)['flag']:
			return eval(r.text)['msg']
		else:
			raise Exception(eval(r.text)['msg'])

	def utrRequest(self,param_,user = None):
		param = self.fixParam(param_,user)
		result = ''
		if 'post' == param['requestMethod']:
			result = self.postRequest(param)
		elif 'put' == param['requestMethod']:
			result = self.putRequest(param)
		elif 'get' == param['requestMethod']:
			result = self.getRequest(param)
		elif 'mix' == param['requestMethod']:
			result = self.mixRequest(param)

		if 'T' == eval(result.text)['flag']:
			return eval(result.text)['msg']
		else:
			raise Exception(eval(result.text)['msg'])

	def fixParam(self,param_,user = None):
		param = copy.deepcopy(param_)
		pro = self.pro
		pack = self.pack
		if pack:
			if 'seller' == param['requestAddress']:
				param['requestBody']['proId'] = pack.packId
				param['requestBody']['sellerId'] = SqlUtil.queryOne("select t.seller_id from UTR_SELLER t where t.pro_id ='" + pack.packId +"'")[0]
				param['extendUrl'] = param['requestBody']['sellerId']
			elif 'estimate' == param['requestAddress']:
				param['requestBody']['proId'] = pack.packId
				param['requestBody']['estimateId'] = SqlUtil.queryOne("select t.estimate_id from UTR_ESTIMATE t where t.pro_id = '" + pack.packId + "'")[0]
				param['extendUrl'] = param['requestBody']['estimateId']
			elif 'mgr' == param['requestAddress']:
				param['requestBody']['proId'] = pack.packId
				param['requestBody']['sellerId'] = SqlUtil.queryOne("select t.seller_id from UTR_SELLER t where t.pro_id ='" + pack.packId +"'")[0]
			elif 'contact' == param['requestAddress']:
				if 'post' == param['requestMethod']:
					param['requestBody']['proId'] = pack.packId
				elif 'put' == param['requestMethod']:
					param['requestBody']['proId'] = pack.packId
					param['requestBody']['proContactId'] = SqlUtil.queryOne("select t.pro_contact_id from UTR_PRO_CONTACT t where t.pro_id = '" + pack.packId + "'")[0]
			elif 'newSubPro' == param['requestAddress']:
				param['requestBody']['packId'] = pack.packId
			elif 'utrmPackSubmit' == param['requestAddress']:
				param['extendUrl'] = "packId=" + pack.packId + "&taskId="
			elif 'packFlow' == param['requestAddress']:
				self.packFlowParamfix(param)
			elif 'pubMethod' == param['requestAddress']:
				param['requestBody']['proId'] = pack.packId
				param['requestBody']['pubId'] = SqlUtil.queryOne("select t.pub_id from UTR_PUB t where t.pro_id = '" + pack.packId + "'")[0]
			elif 'pub' == param['requestAddress']:
				param['requestBody']['proId'] = pack.packId
				param['requestBody']['pubId'] = SqlUtil.queryOne("select t.pub_id from UTR_PUB t where t.pro_id = '" + pack.packId + "'")[0]
				param['extendUrl'] = param['requestBody']['pubId']
			elif 'rules' == param['requestAddress']:
				self.packFlowParamfix(param)


		elif pro:
			if 'newUTRG' == param['requestAddress']:
				param['requestBody']['proName'] = pro.proName
				param['proPrice'] = pro.rule.proPrice
			# elif 'newUtrmPro' == param['requestAddress']:
			# 	param['requestBody']['proName'] = pro.proName
			elif 'comp' == param['requestAddress']:
				param['requestBody']['proId'] = pro.proId
				param['requestBody']['compId'] =SqlUtil.queryOne("select t.comp_id from UTR_COMP t where t.pro_id= '" + pro.proId + "'")[0]
				param['extendUrl'] = param['requestBody']['compId']
			elif 'finance' == param['requestAddress']:
				param['requestBody']['financeId'] = SqlUtil.queryOne("select t.finance_id from UTR_FINANCE t where t.pro_id = '" + pro.proId + "'")[0]
				param['extendUrl'] = param['requestBody']['financeId']
			elif 'seller' == param['requestAddress']:
				param['requestBody']['proId'] = pro.proId
				param['requestBody']['sellerId'] = SqlUtil.queryOne("select t.seller_id from UTR_SELLER t where t.pro_id ='" + pro.proId +"'")[0]
				param['extendUrl'] = param['requestBody']['sellerId']
			elif 'estimate' == param['requestAddress']:
				param['requestBody']['estimateId'] = SqlUtil.queryOne("select t.estimate_id from UTR_ESTIMATE t where t.pro_id = '" + pro.proId + "'")[0]
				param['extendUrl'] = param['requestBody']['estimateId']
			elif 'mgr' == param['requestAddress']:
				param['requestBody']['proId'] = pro.proId
				param['requestBody']['sellerId'] = SqlUtil.queryOne("select t.seller_id from UTR_SELLER t where t.pro_id ='" + pro.proId +"'")[0]
			elif 'pub' == param['requestAddress']:
				param['requestBody']['proId'] = pro.proId
				param['requestBody']['pubId'] = SqlUtil.queryOne("select t.pub_id from UTR_PUB t where t.pro_id = '" + pro.proId + "'")[0]
				param['extendUrl'] = param['requestBody']['pubId']
			elif 'p3ProSubmit' == param['requestAddress'] or 'g3ProSubmit' == param['requestAddress']:
				param['extendUrl'] = "proId=" + pro.proId + "&taskId="
			elif 'holder' == param['requestAddress']:
				param['requestBody']['proId'] = pro.proId
			elif 'contact' == param['requestAddress']:
				if 'post' == param['requestMethod']:
					param['requestBody']['proId'] = pro.proId
				elif 'put' == param['requestMethod']:
					param['requestBody']['proId'] = pro.proId
					param['requestBody']['proContactId'] = SqlUtil.queryOne("select t.pro_contact_id from UTR_PRO_CONTACT t where t.pro_id = '" + pro.proId + "'")[0]
			elif 'utrmProSubmit' == param['requestAddress']:
				param['extendUrl'] = "proId=" + pro.proId + "&taskId="
			elif 'buyerFlow' == param['requestAddress']: #受让方审核流程
				param['requestBody']['buyerId'] = user.buyerId
				param['requestBody']['formId'] = user.buyerId
				result = SqlUtil.queryBuyerTask(user,pro)
				param['requestBody']['taskId'] = str(result['taskId'])
				param['requestBody']['processStatus'] = result['taskName'].decode('gb2312')
				param['requestBody']['taskName'] = result['taskName'].decode('gb2312')
				param['requestBody']['processInsId'] = result['processInsId']
				param['requestBody']['assignee'] = result['assignee']
				if u'部门负责人审核意向受让方' == result['taskName'].decode('gb2312'):
					param['requestBody']['pluginName'] = ''
					#del param['requestBody']['notAccept']
				elif u'经办人确认意向受让方' == result['taskName'].decode('gb2312'):
					param['requestBody']['pluginName'] = 'buyerAccept'
					param['requestBody']['proId'] = pro.proId
					param['requestBody']['auditResult'] = 'T'
				elif u'推送竞买人' == result['taskName'].decode('gb2312'):
					param['requestBody']['pluginName'] = ''
					param['requestUrl'] = self.params.utrInterFaceAddress['pushBuyer']
			elif 'proFlow' == param['requestAddress']:
				param = self.proFlowParamFix(param)
			elif 'g3Flow' == param['requestAddress']:
				param = self.g3FlowParamFix(param)
			elif 'unpub' == param['requestAddress']: #模拟摘牌
				param['extendUrl'] = SqlUtil.getProcessId(pro)
			elif 'manUnpub' == param['requestAddress']: #摘牌确认
				param['requestBody']['proId'] = pro.proId
				param['requestBody']['formId'] = pro.proId
				result = SqlUtil.queryTask(pro)
				param['requestBody']['taskId'] = str(result['taskId'])
				param['requestBody']['taskName'] = result['taskName'].decode('gb2312')
				param['requestBody']['processStatus'] = result['taskName'].decode('gb2312')
				param['requestBody']['processInsId'] = result['processInsId']
				param['requestBody']['assignee'] = result['assignee']
			elif 'confirmBill' == param['requestAddress']:
				param['requestBody']['proId'] = pro.proId
				param['requestBody']['billId'] = SqlUtil.getBillId(pro,'40')
				param['requestBody']['reachDate'] = TODAY +' '+ NOW_TIME
		return param				

	def proFlowParamFix(self,param):
		pro = self.pro
		nowTaskName = SqlUtil.getTaskName(pro)
		print u'当前节点： ' + nowTaskName
		param['requestBody']['proId'] = pro.proId
		param['requestBody']['formId'] = pro.proId
		result = SqlUtil.queryTask(pro)
		param['requestBody']['taskId'] = str(result['taskId'])
		param['requestBody']['taskName'] = result['taskName'].decode('gb2312')
		param['requestBody']['processStatus'] = result['taskName'].decode('gb2312')
		param['requestBody']['processInsId'] = result['processInsId']
		param['requestBody']['assignee'] = result['assignee']
		if nowTaskName in (u'确定挂牌时间',):
			param['requestBody']['pubStartTime'] = TODAY
			param['requestBody']['pluginName'] = 'confrimPubTime'
		elif nowTaskName in (u'推送到动态报价大厅',):
			param['requestAddress'] = 'pushPro'
			param['requestUrl'] = self.params.utrInterFaceAddress['pushPro']
		elif nowTaskName in (u'受让资格确认（受让通知）',):
			param['requestBody']['pluginName'] = 'confirmBuyers'
		elif nowTaskName in (u'经办人确定交易方式，拟定交易规则'):
			param['requestBody']['pluginName'] = 'setDealWay'
			param['requestBody']['mainStatus'] = '70'
			param['requestBody']['lastUser'] = ''
			param['requestBody']['buyerCount'] = ''
			param['requestBody']['preDealWay'] = pro.param['pub']['pubDealWay']
			param['requestBody']['bidmode'] = '1'
		elif nowTaskName in (u'组织线下交易',):
			param['requestBody']['pluginName'] = 'dealAndPro'
			param['requestBody']['doDealAddress'] = u'北京'
			param['requestBody']['doDealTime'] = TODAY
		elif nowTaskName in (u'[成交]成交价格录入',):
			param['requestBody']['keyId'] = pro.proId
			param['requestBody']['pluginName'] = 'dealAndPro'
			param['requestBody']['mainStatus'] = '79'
			param['requestBody']['dealId'] = SqlUtil.getDealId(pro)
			param['requestBody']['dealPrice'] = '%.2f' % (float(pro.param['newItem']['proPrice']) * 10000 *1.50)
			param['requestBody']['buyerId'] = pro.buyerGroup[0].buyerId
			param['requestBody']['buyerName'] = pro.buyerGroup[0].userEname
			param['requestBody']['dealWay'] = pro.param['pub']['pubDealWay']
			param['requestBody']['changeDesc'] = ''
			param['requestBody']['dealTime'] = TODAY
			param['requestBody']['doDealAddress'] = ''
			param['requestBody']['doDealTime'] = ''
			param['requestBody']['doDealBuyers'] = ''
			param['requestBody']['doDealTimes'] = ''
			param['requestBody']['beizhu'] = ''
			if 'A10001' == pro.param['pub']['pubDealWay']:
				param['requestBody']['doDealAddress'] = u'北京'
				param['requestBody']['doDealTime'] = TODAY
		elif nowTaskName in (u'填写合同/结算信息',):
			param['requestBody']['pluginName'] = 'proAndDeal'
			param['requestBody']['mainStatus'] = '79'
			param['requestBody']['dealId'] = SqlUtil.getDealId(pro)
			param['requestBody']['buyerName'] = pro.buyerGroup[0].userEname
			param['requestBody']['dealPrice'] = '%.2f' % (float(pro.param['newItem']['proPrice']) * 10000 *1.50)
			param['requestBody']['dealTime'] = TODAY
			param['requestBody']['contractNo'] = '123456'
			param['requestBody']['contractDate'] = TODAY
			param['requestBody']['hasContractDate'] = TODAY
			param['requestBody']['jiesuanType'] = 'balin'
			param['requestBody']['payMethod'] = 'A03001'
			param['requestBody']['firstPayPercent'] = ''
			param['requestBody']['firstPay'] = ''
			param['requestBody']['payDeadline'] = TODAY
			param['requestBody']['firstEndDate'] = ''
			param['requestBody']['jiesuanPrice'] = '%.2f' % (float(pro.param['newItem']['proPrice']) * 10000 *1.50)
			param['requestBody']['beizhu'] = ''
		elif nowTaskName in (u'确认成交并发布公告',u'确认成交（自动发布公告）',):
			param['requestUrl'] = self.params.utrInterFaceAddress['setDeal']
		elif nowTaskName in (u'生成交易凭证',):
			param['requestUrl'] = self.params.utrInterFaceAddress['certFlow']
			param['requestBody']['pluginName'] = 'createCert'
			param['requestBody']['sysEname'] = 'UTRM'
			param['requestBody']['proName'] = pro.param['newItem']['proName']
			param['requestBody']['proNo'] = SqlUtil.getProNo(pro)
		elif nowTaskName in (u'[交易凭证]一级审核',):
			param['requestUrl'] = self.params.utrInterFaceAddress['certFlow']
			param['requestBody']['pluginName'] = 'auditCert1'
		elif nowTaskName in (u'[交易凭证]二级审核',):
			param['requestUrl'] = self.params.utrInterFaceAddress['certFlow']
			param['requestBody']['pluginName'] = 'auditCert'
		elif nowTaskName in (u'生成价款划入凭单',):
			param['requestUrl'] = self.params.utrInterFaceAddress['createBill']
			param['requestBody']['dealId'] = SqlUtil.getDealId(pro)
			param['requestBody']['fee1'] = '%.2f' % (float(pro.param['newItem']['proPrice']) * 10000 *1.50*0.001)
			param['requestBody']['fee2'] = '%.2f' % (float(pro.param['newItem']['proPrice']) * 10000 *1.50*0.001)
		elif nowTaskName in (u'确认交易价款已结算',):
			param['requestUrl'] = self.params.utrInterFaceAddress['setBillIn']
		elif nowTaskName in (u'生成退保单据',):
			param['requestUrl'] = self.params.utrInterFaceAddress['returnBail']
		elif nowTaskName in (u'生成价款划出及服务费凭单',u'生成价款划出凭单',):
			param['requestUrl'] = self.params.utrInterFaceAddress['createBillOut']
			param['requestBody']['sellerFee1'] = '%.2f' % (float(pro.param['newItem']['proPrice']) * 10000 *1.50*0.001)
			param['requestBody']['sellerFee2'] = '%.2f' % (float(pro.param['newItem']['proPrice']) * 10000 *1.50*0.001)
			param['requestBody']['ruleId'] = SqlUtil.queryOne("select rule_id from UTR_FEE_RULE where pro_id ='" + pro.proId +"'")[0]
			param['requestBody']['bankNo'] = '6600123456789900'
			param['requestBody']['account'] = u'账户名称'
			param['requestBody']['openBankAddres'] = u'开户银行'
			param['requestBody']['spare1'] = ''
		return param		

	def packFlowParamfix(self,param):
		pack = self.pack
		nowTaskName = SqlUtil.getTaskName(pack = pack)
		print u'当前节点：' + nowTaskName
		param['requestBody']['packId'] = pack.packId
		param['requestBody']['formId'] = pack.packId
		result = SqlUtil.queryTask(pack=pack)
		param['requestBody']['taskId'] = str(result['taskId'])
		param['requestBody']['taskName'] = result['taskName'].decode('gb2312')
		param['requestBody']['processStatus'] = result['taskName'].decode('gb2312')
		param['requestBody']['processInsId'] = result['processInsId']
		param['requestBody']['assignee'] = result['assignee']
		if nowTaskName in (u'确定挂牌时间及纸媒发布时间'):
			param['requestBody']['pubStartTime'] = TODAY
			param['requestBody']['pluginName'] = 'proAndPub'
			param['requestBody']['pubId'] = SqlUtil.queryOne("select t.pub_id from UTR_PUB t where t.pro_id = '" + pack.packId + "'")[0]
			param['requestBody']['flowMap_ifMedia'] = 'F'
			param['requestBody']['sysEname'] = 'UTRM'
		elif nowTaskName in (u'[受理]部门经理审核',u'[受理]分管领导审核'):
			param['requestBody']['flowMap_fh'] = 'F'


		return param




	def g3FlowParamFix(self,param):
		pro = self.pro
		nowTaskName = SqlUtil.getTaskName(pro)
		print u'当前节点： ' + nowTaskName
		param['requestBody']['proId'] = pro.proId
		param['requestBody']['formId'] = pro.proId
		result = SqlUtil.queryTask(pro)
		param['requestBody']['taskId'] = str(result['taskId'])
		param['requestBody']['taskName'] = result['taskName'].decode('gb2312')
		param['requestBody']['processStatus'] = result['taskName'].decode('gb2312')
		param['requestBody']['processInsId'] = result['processInsId']
		param['requestBody']['assignee'] = result['assignee']
		if nowTaskName in (u'确定挂牌时间',):
			param['requestBody']['pubStartTime'] = TODAY
		return param

	def postRequest(self,param):
		r = self.get('http://utr.utrm.com/utr-web/sendPage/formToken?_='+str(time.time()*1000))
		#r = self.get('http://web.unibid.cn/utr/sendPage/formToken?_='+str(time.time()*1000))
		param['requestBody']['formToken'] = r.text.replace('"','')
		return self.post(param['requestUrl'],param['requestBody'],headers=self.headers)

	def putRequest(self,param):
		r = self.get('http://utr.utrm.com/utr-web/sendPage/formToken?_='+str(time.time()*1000))
		#r = self.get('http://web.unibid.cn/utr/sendPage/formToken?_='+str(time.time()*1000))
		param['requestBody']['formToken'] = r.text.replace('"','')
		return self.put(param['requestUrl'] + param['extendUrl'],param['requestBody'],headers = self.headers)

	def getRequest(self,param):
		return self.get(param['requestUrl'] + param['extendUrl'],headers = self.headers)

	def mixRequest(self,param):
		return self.post(param['requestUrl'] + param['extendUrl'],param['requestBody'],headers = self.headers)

	def holderPost(self,param):
	#	title = ('holderNo', 'holderName', 'holdingRatio')
	#	holderDict = map(lambda x:dict(zip(title,x)),zip(getall('holderNo'),getall('holderName'),getall('holdingRatio')))
		table = param['table']
		table.changeSheet('comp')
		h = int(table.getData('holderNum'))
		table.changeSheet('holder')
		param['requestBody']['proId'] = self.pro.proId
		for i in xrange(h):
			param['requestBody']['holderNo'] = str(i+1)
			param['requestBody']['holderName'] = table.getData('holderName-'+str(i+1))
			param['requestBody']['holdingRatio'] = table.getData('holdingRatio-'+str(i+1))
			param['requestBody']['originalShare'] = table.getData('originalShare-'+str(i+1))
			self.postRequest(param)

	def userSignUp(self,userGroup,param,pack=None):
		pro = self.pro
		pro.setBuyerGroup(userGroup)
		for user in pro.buyerGroup:
			print user.userEname + u'报名中,请稍候'
			user.userId = SqlUtil.getUserId(user)
			param.signUpParam['extendUrl'] = 'proId=' + pro.proId + '&packId=' +''+ '&customId=' + user.userId + '&v=0'
			self.utrRequest(param.signUpParam)
			while not SqlUtil.getBuyerId(user,pro):
				time.sleep(0.1)
			user.buyerId = SqlUtil.getBuyerId(user,pro)
			while not SqlUtil.queryBuyerTask(user,pro):
				time.sleep(0.1)
			while SqlUtil.getBuyerTaskName(user,pro) not in (u'推送竞买人',None):
				self.utrRequest(copy.deepcopy(param.buyerFlowParam),user)
		for user in pro.buyerGroup:
			while SqlUtil.getBuyerBailFinishFlag(user) != '2':
				print u'竞买人资格确认中,请稍候'
				time.sleep(5)
			print user.userEname + u'资格已确认'
			if 'T' == self.pro.param['pub']['ifBiddyn']:
				self.utrRequest(copy.deepcopy(param.buyerFlowParam),user)
				print user.userEname + u'推送竞价完成'

if __name__ == "__main__":
	pass
