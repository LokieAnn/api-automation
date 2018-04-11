#-*- coding:utf-8 -*-
from params.utrgParams import UtrgParams
from params.utrmParams import UtrmProParams
from params.utrmParams import UtrmPackParams
from lib.sqlUtil import SqlUtil
from lib.pro import Pro
from lib.pack import Pack
from lib.table import Table
from lib.utrRequest import UtrRequest
from time import sleep

SqlUtil.init()
tablePro = Table('test-utrm.xlsx')
tableProG = Table('test-utrg.xlsx')
pro = Pro()
pro.param = tablePro.param

utrmProParams = UtrmProParams(tablePro)
utrgParams = UtrgParams(tableProG)

tablePack = Table('test-utrms.xlsx')
pack = Pack()
utrmPackParams = UtrmPackParams(tablePack)

utrR = UtrRequest(pro=pro)
utrRpack = UtrRequest(pack=pack)
userGroup = 'test01,test02' #报名帐号，多人中间用英文逗号隔开

def test():
	utrR.login(utrgParams.utrInterFaceAddress['login'],utrgParams.loginParam)
	utrR.pro.proId = utrR.utrRequest(utrgParams.newPro)
	utrR.utrRequest(utrgParams.editComp)
	utrR.utrRequest(utrgParams.editFinance)
	utrR.utrRequest(utrgParams.editEstimate)
	utrR.utrRequest(utrgParams.editSeller)
	utrR.utrRequest(utrgParams.saveManager)
	utrR.utrRequest(utrgParams.editPub)
	utrR.holderPost(utrgParams.saveHolder)
	utrR.utrRequest(utrgParams.saveContact)
	#utrR.utrRequest(utrmProParams.G3Submit)
	#utrR.utrRequest(utrmProParams.G3FlowParam)
	return utrR

def test2():
	utrR.pro.manager = utrmProParams.loginParam['userEname']
	utrR.login(utrmProParams.utrInterFaceAddress['login'],utrmProParams.loginParam)
	utrR.pro.proId = utrR.utrRequest(utrmProParams.newPro)
	utrR.utrRequest(utrmProParams.editEstimate)
	utrR.utrRequest(utrmProParams.editSeller)
	utrR.utrRequest(utrmProParams.saveManager)
	utrR.utrRequest(utrmProParams.editPub)
	utrR.utrRequest(utrmProParams.saveContact)
	utrR.utrRequest(utrmProParams.utrmProSubmit) #提交完成
	utrR.utrRequest(utrmProParams.proFlowParam) #一审
	utrR.utrRequest(utrmProParams.proFlowParam) #二审
	utrR.utrRequest(utrmProParams.proFlowParam) #确定挂牌时间
	# if 'T' == pro.param['pub']['ifBiddyn']:
	# 	gotonext = False
	# 	while not gotonext:
	# 		try:
	# 			utrR.utrRequest(utrmProParams.bid) #确认竞价参数
	# 			gotonext = True
	# 		except:
	# 			print u'等待自处理完成请稍候'
	# 			sleep(5)
	# 	utrR.utrRequest(utrmProParams.proFlowParam) #一审
	# 	utrR.utrRequest(utrmProParams.proFlowParam) #二审
	# 	utrR.utrRequest(utrmProParams.proFlowParam)
	# while SqlUtil.getMainStatus(utrR.pro) != 30:
	# 	print u'等待挂牌中请稍候'
	# 	sleep(5)
	# utrR.userSignUp(userGroup,utrmProParams) #受让方报名
	# utrR.utrRequest(utrmProParams.unpubParam) #模拟摘牌
	# utrR.utrRequest(utrmProParams.manUnpubParam) #手工摘牌
	# utrR.utrRequest(utrmProParams.proFlowParam) #受让资格确认
	# utrR.utrRequest(utrmProParams.proFlowParam) #经办人确认交易方式
	# utrR.utrRequest(utrmProParams.proFlowParam) #交易一审
	# utrR.utrRequest(utrmProParams.proFlowParam) #交易二审
	# utrR.utrRequest(utrmProParams.proFlowParam) #组织线下交易
	# utrR.utrRequest(utrmProParams.proFlowParam) #确认线下交易
	# utrR.utrRequest(utrmProParams.proFlowParam) #成交价格录入
	# utrR.utrRequest(utrmProParams.proFlowParam) #成交价格确认
	# utrR.utrRequest(utrmProParams.proFlowParam) #填写合同
	# utrR.utrRequest(utrmProParams.proFlowParam) #合同一审
	# utrR.utrRequest(utrmProParams.proFlowParam) #合同二审
	# utrR.utrRequest(utrmProParams.proFlowParam) #确认成交并发布公告
	# utrR.utrRequest(utrmProParams.proFlowParam) #生成交易凭证
	# utrR.utrRequest(utrmProParams.proFlowParam) #[交易凭证]一级审核
	# utrR.utrRequest(utrmProParams.proFlowParam) #[交易凭证]二级审核
	# utrR.utrRequest(utrmProParams.proFlowParam) #生成价款划入凭单
	# utrR.utrRequest(utrmProParams.confirmBillParam) #划入价款结算确认
	# utrR.utrRequest(utrmProParams.proFlowParam) #结算人员确认划入价款到账
	# utrR.utrRequest(utrmProParams.proFlowParam) #结算部领导确认划入价款到账
	# utrR.utrRequest(utrmProParams.proFlowParam) #确认交易价款已结算
	# utrR.utrRequest(utrmProParams.proFlowParam) #生成退保单据
	# while reduce(lambda x,y:x or y,map(lambda x:x[0]!='50',SqlUtil.query("select bill_status from UTR_BILL where pro_id = '" + pro.proId +"' and bill_type ='bailout'"))): #保证金结算不为50则等待
	# 	print u'退保自动结算中,请稍后'
	# 	sleep(5)
	# utrR.utrRequest(utrmProParams.proFlowParam) #经办人退保单据确认
	# utrR.utrRequest(utrmProParams.proFlowParam) #结算人员退保单据确认
	# utrR.utrRequest(utrmProParams.proFlowParam) #结算部领导退保单据确认
	# utrR.utrRequest(utrmProParams.proFlowParam) #生成价款划出及服务费凭单
	# utrR.utrRequest(utrmProParams.proFlowParam) #[凭单]一级审核
	# utrR.utrRequest(utrmProParams.proFlowParam) #[凭单]二级审核
	# utrR.utrRequest(utrmProParams.confirmBillParam) #划出价款结算确认
	# utrR.utrRequest(utrmProParams.proFlowParam) #结算人员确认价款划出
	# utrR.utrRequest(utrmProParams.proFlowParam) #结算领导确认价款划出


def test3(x):
	utrRpack.pack.manager = utrmPackParams.loginParam['userEname']
	utrRpack.login(utrmPackParams.utrInterFaceAddress['login'],utrmPackParams.loginParam)
	utrRpack.pack.packId = utrRpack.utrRequest(utrmPackParams.newPack)
	utrRpack.utrRequest(utrmPackParams.editSeller)
	utrRpack.utrRequest(utrmPackParams.editEstimate)
	utrRpack.utrRequest(utrmPackParams.saveManager)
	utrRpack.utrRequest(utrmPackParams.saveContact)
	pack.initProList(x)
	for i in range(x):
		utrmPackParams.saveSubPro['requestBody']['proName'] = utrmPackParams.proName+str(i+1)
		utrRpack.pack.proList[i].proId = utrRpack.utrRequest(utrmPackParams.saveSubPro)
	for i in range(x):
		utrmPackParams.editSubProInfo['requestBody']['proId'] = utrRpack.pack.proList[i].proId
		utrmPackParams.subProEstimate['requestBody']['proId'] = utrRpack.pack.proList[i].proId
		utrRpack.utrRequest(utrmPackParams.editSubProInfo)
		utrRpack.utrRequest(utrmPackParams.subProEstimate)
	utrRpack.utrRequest(utrmPackParams.submitPack)
	utrRpack.utrRequest(utrmPackParams.packFlowParam)
	utrRpack.utrRequest(utrmPackParams.packFlowParam)
	utrRpack.utrRequest(utrmPackParams.pubMethodParam)
	utrRpack.utrRequest(utrmPackParams.packPubParam)
	utrRpack.utrRequest(utrmPackParams.setProRulesParam)
	utrRpack.utrRequest(utrmPackParams.packFlowParam)
	utrRpack.utrRequest(utrmPackParams.packFlowParam)
	utrRpack.utrRequest(utrmPackParams.packFlowParam)
	utrRpack.utrRequest(utrmPackParams.packFlowParam)
	utrRpack.utrRequest(utrmPackParams.packFlowParam)
	utrRpack.utrRequest(utrmPackParams.packFlowParam)

		