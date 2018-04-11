#-*- coding:utf-8 -*-
from params import Params
import hashlib

class UtrmProParams(Params):
	def __init__(self,table):
		super(UtrmProParams,self).__init__()
		self.table = table
		self.initParams()
		self.bid = self.getParam('proFlow','post','bid')

	def initParams(self):
		self.initLoginParam()
		self.initNewProParam()
		#self.initCompParam()
		self.initSellerParam()
		#self.initFinanceParam()
		self.initEstimateParam()
		self.initManagerParam()
		self.initPubParam()
		#self.initHolderParam()
		self.initContactParam()
		self.initSubmitParam()
		self.initProFlowParam()

	#初始化登录参数
	def initLoginParam(self):
		self.table.changeSheet('config')
		self.loginParam['userEname'] = self.table.getData('loginUserName')
		self.loginParam['userPass'] = hashlib.md5(self.table.getData('loginUserPW')).hexdigest()

	#初始化新增项目参数
	def initNewProParam(self):
		self.table.changeSheet('newItem')
		self.newPro = {'requestAddress' : 'newUtrmPro',
					   'requestMethod' : 'post',
					   'requestUrl' : self.utrInterFaceAddress['newUtrmPro'],
					   'extendUrl' : '',
					   'requestBody' : {'formToken' : '',
										'proId' : '',
										'createUserid' : '',
										'proName' : self.table.getData('proName'),
										'proPrice' : self.table.getData('proPrice'),
										'isGzw' : self.table.getData('isGzw'),
										'pauseTime' : self.table.getData('pauseTime'),
										'proType' : self.table.getData('proType'),
										'proTypeText' : self.table.getData('proTypeText'),
										'zoneName' : self.table.getData('zoneName'),
										'zone' : self.table.getData('zone'),
										'proSource' : self.table.getData('proSource'),
										'pauseText' : self.table.getData('pauseText'),
										'spare4' : self.table.getData('spare4'),
										'proDesc' : self.table.getData('proDesc'),
									   }
					}

	#初始化企业参数
	def initCompParam(self):
		self.table.changeSheet('comp')
		self.editComp = {'requestAddress' : 'comp',
				         'requestMethod' : 'put',
				         'requestUrl' : self.utrInterFaceAddress['comp'],
				         'extendUrl' : '',
				         'requestBody' : {'formToken' : '',
				       			          'compId' : '',
				       			          'proId' : '',
				       			          'compName' : self.table.getData('compName'),
				       			          'compZcode' : self.table.getData('compZcode'),
				       			          'compIndustry' : self.table.getData('compIndustry'),
				       			          'compTime' : self.table.getData('compTime'),
				       			          'compProvince' : self.table.getData('compProvince'),
				       			          'compCity' : self.table.getData('compCity'),
				       			          'compAddress' : self.table.getData('compAddress'),
				       			          'compUniGslx' : self.table.getData('compUniGslx'),
				       			          'compUniJjlx' : self.table.getData('compUniJjlx'),
				       			          'compScope' : self.table.getData('compScope'),
				       			          'compFunding' : self.table.getData('compFunding'),
				       			          'moneytype' : 'CNY',
				       			          'compBoss' : self.table.getData('compBoss'),
				       			          'compScale' : self.table.getData('compScale'),
				       			          'compZrs' : self.table.getData('compZrs'),
				       			          'innerAudit' : self.table.getData('innerAudit'),
				       			          'innerAuditDesc' : '',
				       			          'compTdhb' : self.table.getData('compTdhb'),
				       			          'holderNum' : self.table.getData('holderNum'),
				       			          'spare2' : self.table.getData('spare2'),
				       				     }
				   }

	#初始化转让方参数
	def initSellerParam(self):
		self.table.changeSheet('seller')
		sellerType = self.table.getData('sellerType')
		if 'A11001' == sellerType:
			self.table.changeSheet('sellerFR')
			self.editSeller = {	'requestAddress' : 'seller',
							    'requestMethod' : 'put',
							    'requestUrl' : self.utrInterFaceAddress['seller'],
							    'extendUrl' : '',
							    'requestBody' :	{'formToken' : '',
											     'proId' : '',
											     'sellerId' : '',
											     'mainFlag' : 'T',
											     'customerTypeCode' : 'SE',
											     'oldName' : '',
											     'changeFlag' : 'T',
											     'packFlag' : 'F',
											     'sellerType' : 'A11001',
											     'sellerName' : self.table.getData('sellerName'),
											     'customerNo' : '',
											     'unionFlag' : self.table.getData('unionFlag'),
											     'sellerProvince' : self.table.getData('sellerProvince'),
											     'sellerCity' : self.table.getData('sellerCity'),
											     'sellerIsGz' : 'T',
											     'sellerAddress' : self.table.getData('sellerAddress'),
											     'sellerFunding' : self.table.getData('sellerFunding'),
											     'moneyType' : 'CNY',
											     'sellerUniGslx' : self.table.getData('sellerUniGslx'),
											     'sellerUniJjlx' : self.table.getData('sellerUniJjlx'),
											     'sellerBoss' : self.table.getData('sellerBoss'),
											     'sellerIndustryOne' : self.table.getData('sellerIndustryOne'),
											     'sellerIndustry' : self.table.getData('sellerIndustry'),
											     'sellerScale' : self.table.getData('sellerScale'),
											     'sellerZcode' : self.table.getData('sellerZcode'),
											     'innerAudit' : self.table.getData('innerAudit'),
											     'innerAuditDesc' : '',
											     'assetApplyDesc' : '　',
											     }
						  	}
		else:
			pass

	#初始化财务参数
	def initFinanceParam(self):
		self.table.changeSheet('finance')
		self.editFinance = { 'requestAddress' : 'finance',
					         'requestMethod' : 'put',
					         'requestUrl' : self.utrInterFaceAddress['finance'],
					         'extendUrl' : '',
					         'requestBody' : { 'formToken' : '',
					       					   'financeId' : '',
					       					   'last2Year' : self.table.getData('last2Year'),
					       					   'last2Zzc' : self.table.getData('last2Zzc'),
					       					   'last2Zfz' : self.table.getData('last2Zfz'),
					       					   'last2Syzqy' : self.table.getData('last2Syzqy'),
					       					   'last2Yysl' : self.table.getData('last2Yysl'),
					       					   'last2Yylr' : self.table.getData('last2Yylr'),
					       					   'last2Jlr' : self.table.getData('last2Jlr'),
					       					   'last2Sjjgmc' : self.table.getData('last2Sjjgmc'),
					       					   'last2Desc' : self.table.getData('last2Desc'),
					       					   'thisType' : self.table.getData('thisType'),
					       					   'thisYear' : self.table.getData('thisYear'),
					       					   'thisZzc' : self.table.getData('thisZzc'),
					       					   'thisZfz' : self.table.getData('thisZfz'),
					       					   'thisSyzqy' : self.table.getData('thisSyzqy'),
					       					   'thisYysl' : self.table.getData('thisYysl'),
					       					   'thisYylr' : self.table.getData('thisYylr'),
					       					   'thisJlr' : self.table.getData('thisJlr'),
					       					   'thisDesc' : self.table.getData('thisDesc'),
					       					   }
						}

	#初始化评估参数
	def initEstimateParam(self):
		self.table.changeSheet('estimate')
		self.editEstimate = {'requestAddress' : 'estimate',
						     'requestMethod' : 'put',
						     'requestUrl' : self.utrInterFaceAddress['estimate'],
						     'extendUrl' : '',
						     'requestBody' : {'formToken' : '',
						   				      'estimateId' : '',
						   				      'hezhunFlag' : self.table.getData('hezhunFlag'),
						   				      'beianFlag' : self.table.getData('beianFlag'),
						   				      'pgjg' : self.table.getData('pgjg'),
						   				      'pgbajg' : self.table.getData('pgbajg'),
						   				      'hzbarq' : self.table.getData('hzbarq'),
						   				      'pgjzr' : self.table.getData('pgjzr'),
						   				      'estNoticeno' : self.table.getData('estNoticeno'),
						   				      'pgjzrsjjg' : self.table.getData('pgjzrsjjg'),
						   				      'lssws' : self.table.getData('lssws'),
						   				      'estimatePrice' : self.table.getData('estimatePrice'),
						   				      'originalPrice' : self.table.getData('originalPrice'),
						   				      'zmJzc' : self.table.getData('zmJzc'),
						   				      }
						 	}

	#初始化监管参数
	def initManagerParam(self):
		self.table.changeSheet('mgr')
		self.saveManager = {'requestAddress' : 'mgr',
				            'requestMethod' : 'post',
				            'requestUrl' : self.utrInterFaceAddress['mgr'],
				            'extendUrl' : '',
				            'requestBody' : {'sellerId' : '',
					         				 'proId' : '',
					         				 'inputStatus' : '',
					         				 'formToken' : '',
					         				 'mgrArea' : '0',
					         				 'sellerIsYq' : self.table.getData('sellerIsYq'),
					         				 'mgrType' : self.table.getData('mgrType'),
					         				 'mgrProvince' : '440000',
					         				 'mgrCity' : '',
					         				 'mgrDistrict' : '',
					         				 'Mgrlist' : self.table.getData('Mgrlist'),
					         				 'mgrName' : self.table.getData('mgrName'),
					         				 'mgrCode' : self.table.getData('mgrCode'),
					         				 'permitCompType' : self.table.getData('permitCompType'),
					         				 'permitCompName' : self.table.getData('permitCompName'),
					         				 'permitFileType' : self.table.getData('permitFileType'),
					         				 'permitFileName' : self.table.getData('permitFileName'),
					         				 'permitFileNo' : self.table.getData('permitFileNo'),
					         				 'permitDate' : self.table.getData('permitDate'),
					         				 }
				   		}
	#初始化披露参数
	def initPubParam(self):
		self.table.changeSheet('pub')
		self.editPub = {'requestAddress' : 'pub',
					    'requestMethod' : 'put',
					    'requestUrl' : self.utrInterFaceAddress['pub'],
					    'extendUrl' : '',
					    'requestBody' : {'formToken' : '',
									     'pubId' : '',
									     'inputStatus' : '0',
									     'proId' : '',
									     'packFlag' : 'F',
									     'buyerAuditLevel' : self.table.getData('buyerAuditLevel'),
									     'buyerPaperFlag' : 'T',
									     'ifPublicity' : 'F',
									     'transWay' : '2',
									     'bidmethod' : 'T',
									     'buyerEpaperFlag' : 'T',
									     'pluginName' : 'pubAndProExt',
									     'duration' : self.table.getData('pubDays'),
									     'pubBailDesc' : self.table.getData('pubBailDesc'),
									     'announceWay' : self.table.getData('announceWay'),
									     'pubDays' : self.table.getData('pubDays'),
									     'pubDelayFlag' : self.table.getData('pubDelayFlag'),
									     'delayBuyerSize' : self.table.getData('delayBuyerSize'),
									     'delayMax' : self.table.getData('delayMax'),
									     'delayPeroid' : self.table.getData('delayPeroid'),
									     'ifBiddyn' : self.table.getData('ifBiddyn'),
									     'pubDealWay' : self.table.getData('pubDealWay'),
									     'pubDesc' : self.table.getData('pubDesc'),
									     'holderIn' : self.table.getData('holderIn'),
									     'allowEndPrio' : self.table.getData('allowEndPrio'),
									     'announceWay1' : self.table.getData('announceWay1'),
									     'announceMedia' : self.table.getData('announceMedia'),
									     'unitTransferee' : self.table.getData('unitTransferee'),
									     'pubBail' : self.table.getData('pubBail'),
									     'bailStartFlag' : self.table.getData('bailStartFlag'),
									     'pubBailType' : self.table.getData('pubBailType'),
									     'pubBailDays' : self.table.getData('pubBailDays'),
									     'bailDeadTime' : self.table.getData('bailDeadTime'),
									     'pubBailMethod' : self.table.getData('pubBailMethod'),
									     'buyConditions' : self.table.getData('buyConditions'),
									     'payPeriodInfo' : self.table.getData('payPeriodInfo'),
									     'important' : self.table.getData('important'),
									     'sellConditions' : self.table.getData('sellConditions'),
									     }
					    }


	#初始化股东参数
	def initHolderParam(self):
		self.saveHolder = {'requestAddress' : 'holder',
						   'requestMethod' : 'post',
						   'requestUrl' : self.utrInterFaceAddress['holder'],
						   'table' : self.table,
					   	   'requestBody': {
									     'formToken' : 'acf0ecc7-dbfe-4f71-85e2-2348decd1a1e',
									     'proId' : '5b0604e3ddb24148a2d5d1da8f832ac7',
									     'newFlag' : 'F',
									     'holderNo' : '1',
									     'holderName' : 'holdername',
									     'holdingRatio' : 'holdingRatio',
									     'originalShare' : 'originalShare' ,
									     }
						}

	#初始化联系人
	def initContactParam(self):
		self.saveContact = {'requestAddress' : 'contact',
				            'requestMethod' : 'post',
				            'requestUrl' : self.utrInterFaceAddress['contact'],
				            'extendUrl' : '',
				            'requestBody' : {
								            'formToken' : '8e74687e-3360-4079-9b4c-a5fb70f75577',
								            'proContactId' : '',
								            'proId' : '390e0891c929490c977fa6527857fb38',
								            'sellerContactName' : '　',
								            'sellerContactPhone' : '　',
								            'sellerContactFax' : '',
								            'sellerContactEmail' : '',
								            'sellerAddress' : '　',
								            'sellerUrl' : '　',
								            'contactName' : u'超级用户',
								            'contactPhone' : '13241232366',
								            'contactFax' : 'super',
								            'contactEmail' : 'super@gemas.com',
								            'contactAddress' : '　',
								            'contactUrl' : '　',
								            }
				}	
		
	# #股东结构
	# self.saveHolder = {'requestAddress' : 'holder',
	# 			'requestMethod' : 'post',
	# 			'requestUrl' : self.utrInterFaceAddress['holder'],
	# 			'extendUrl' : '',
	# 			'holderDict' : self.getHolder(),
	# 			'requestBody': {
	# 							'formToken' : 'acf0ecc7-dbfe-4f71-85e2-2348decd1a1e',
	# 							'proId' : '5b0604e3ddb24148a2d5d1da8f832ac7',
	# 							'newFlag' : 'F',
	# 							'holderNo' : '1',
	# 							'holderName' : self.table.getall('holderName')[0],
	# 							'holdingRatio' : self.table.getall('holdingRatio')[0],
	# 							'originalShare' : '' ,
	# 							}
	# 			}

	#P3提交审核
	def initSubmitParam(self):
		self.utrmProSubmit = {'requestAddress' : 'utrmProSubmit',
				              'requestMethod' : 'mix',
				              'requestUrl' : self.utrInterFaceAddress['utrmProSubmit'],
				              'extendUrl' : '',
				              'requestBody' : {'taskName' : u'项目提交审核',
					           				  'logResult' : 'TJ',}
					         }



	#工作流参数
	def initProFlowParam(self):
		self.proFlowParam = {'requestAddress' : 'proFlow',
				            'requestMethod' : 'post',
				            'requestUrl' : self.utrInterFaceAddress['proFlow'],
				            'requestBody' : {'formToken' : '2fd230a8-0172-4572-ac1c-8c7cb6a89ba0',
								             'taskId' : '382398',
								             'taskName' : u'齐全性登记',
								             'processStatus' : u'齐全性登记',
								             'formId' : '11489fd9500e4368af5625a2dce56266',
								             'processInsId' : 'proFlow3.382385',
								             'logResult' : 'T',
								             'assignee' : 'super',
								             'pluginName' : '',
								             'mainStatus' : '',
								             'proId' : '11489fd9500e4368af5625a2dce56266',
								             'logText' : '1',}
							}

	#股东情况
	def getHolder(self):
		title = ('holderNo', 'holderName', 'holdingRatio')
		return map(lambda x:dict(zip(title,x)),zip(self.table.getall('holderNo'),self.table.getall('holderName'),self.table.getall('holdingRatio')))
	

class UtrmPackParams(Params):
	def __init__(self,table):
		super(UtrmPackParams,self).__init__()
		self.table = table
		self.proName = self.table.getData('subProName')
		self.initParams()
		

	def initParams(self):
		self.initNewPackParam()
		self.initSellerParam()
		self.initEstimateParam()
		self.initManagerParam()
		self.initContactParam()
		self.initSubProParam()
		self.editSubProInfoParam()
		self.editSubProEstimateParam()
		self.initSubmitPackParam()
		self.initPackFlowParam()
		self.initPubMethodParam()
		self.initPackPubParam()
		self.initSetProRulesParam()

	def initNewPackParam(self):
		self.table.changeSheet('newUtrmPack')
		self.newPack = {'requestAddress' : 'newUtrmPack',
					    'requestMethod' : 'post',
					    'requestUrl' : self.utrInterFaceAddress['newUtrmPack'],
					    'extendUrl' : '',
					    'requestBody' : {'proType' : 'sw',
										 'formToken' : '',
										 'packId' : '',
										 'packTypeTxt' : self.table.getData('packTypeTxt'),
										 'pubDesc' : '',
										 'packName' : self.table.getData('packName'),
										 'isGzw' : self.table.getData('isGzw'),
										 'spare3' : self.table.getData('spare3'),
										 'packType' : self.table.getData('packType'),
										 'zoneName' : self.table.getData('zoneName'),
										 'zone' : self.table.getData('zone'),
										 'proSource' : self.table.getData('proSource'),
										 'contactName' : self.table.getData('contactName'),
										}
						}

	#初始化转让方参数
	def initSellerParam(self):
		self.table.changeSheet('seller')
		sellerType = self.table.getData('sellerType')
		if 'A11001' == sellerType:
			self.table.changeSheet('sellerFR')
			self.editSeller = {	'requestAddress' : 'seller',
							    'requestMethod' : 'put',
							    'requestUrl' : self.utrInterFaceAddress['seller'],
							    'extendUrl' : '',
							    'requestBody' :	{'formToken' : '',
											     'proId' : '',
											     'sellerId' : '',
											     'mainFlag' : 'T',
											     'customerTypeCode' : 'SE',
											     'oldName' : '',
											     'changeFlag' : 'T',
											     'packFlag' : 'F',
											     'sellerType' : 'A11001',
											     'sellerName' : self.table.getData('sellerName'),
											     'customerNo' : '',
											     'unionFlag' : self.table.getData('unionFlag'),
											     'sellerProvince' : self.table.getData('sellerProvince'),
											     'sellerCity' : self.table.getData('sellerCity'),
											     'sellerIsGz' : 'T',
											     'sellerAddress' : self.table.getData('sellerAddress'),
											     'sellerFunding' : self.table.getData('sellerFunding'),
											     'moneyType' : 'CNY',
											     'sellerUniGslx' : self.table.getData('sellerUniGslx'),
											     'sellerUniJjlx' : self.table.getData('sellerUniJjlx'),
											     'sellerBoss' : self.table.getData('sellerBoss'),
											     'sellerIndustryOne' : self.table.getData('sellerIndustryOne'),
											     'sellerIndustry' : self.table.getData('sellerIndustry'),
											     'sellerScale' : self.table.getData('sellerScale'),
											     'sellerZcode' : self.table.getData('sellerZcode'),
											     'innerAudit' : self.table.getData('innerAudit'),
											     'innerAuditDesc' : '',
											     'assetApplyDesc' : '　',
											     }
						  	}
		else:
			pass

	#初始化评估参数
	def initEstimateParam(self):
		self.table.changeSheet('estimate')
		self.editEstimate = {'requestAddress' : 'estimate',
						     'requestMethod' : 'put',
						     'requestUrl' : self.utrInterFaceAddress['estimate'],
						     'extendUrl' : '',
						     'requestBody' : {'formToken' : '',
						   				      'estimateId' : '',
						   				      'hezhunFlag' : self.table.getData('hezhunFlag'),
						   				      'beianFlag' : self.table.getData('beianFlag'),
						   				      'pgjg' : self.table.getData('pgjg'),
						   				      'pgbajg' : self.table.getData('pgbajg'),
						   				      'hzbarq' : self.table.getData('hzbarq'),
						   				      'pgjzr' : self.table.getData('pgjzr'),
						   				      'estNoticeno' : self.table.getData('estNoticeno'),
						   				      'pgjzrsjjg' : self.table.getData('pgjzrsjjg'),
						   				      'lssws' : self.table.getData('lssws'),
						   				      'estimatePrice' : self.table.getData('estimatePrice'),
						   				      'originalPrice' : self.table.getData('originalPrice'),
						   				      'zmJzc' : self.table.getData('zmJzc'),
						   				      }
						 	}

	#初始化监管参数
	def initManagerParam(self):
		self.table.changeSheet('mgr')
		self.saveManager = {'requestAddress' : 'mgr',
				            'requestMethod' : 'post',
				            'requestUrl' : self.utrInterFaceAddress['mgr'],
				            'extendUrl' : '',
				            'requestBody' : {'sellerId' : '',
					         				 'proId' : '',
					         				 'inputStatus' : '',
					         				 'formToken' : '',
					         				 'mgrArea' : '0',
					         				 'sellerIsYq' : self.table.getData('sellerIsYq'),
					         				 'mgrType' : self.table.getData('mgrType'),
					         				 'mgrProvince' : '440000',
					         				 'mgrCity' : '',
					         				 'mgrDistrict' : '',
					         				 'Mgrlist' : self.table.getData('Mgrlist'),
					         				 'mgrName' : self.table.getData('mgrName'),
					         				 'mgrCode' : self.table.getData('mgrCode'),
					         				 'permitCompType' : self.table.getData('permitCompType'),
					         				 'permitCompName' : self.table.getData('permitCompName'),
					         				 'permitFileType' : self.table.getData('permitFileType'),
					         				 'permitFileName' : self.table.getData('permitFileName'),
					         				 'permitFileNo' : self.table.getData('permitFileNo'),
					         				 'permitDate' : self.table.getData('permitDate'),
					         				 }
				   		}

	#初始化联系人
	def initContactParam(self):
		self.saveContact = {'requestAddress' : 'contact',
				            'requestMethod' : 'post',
				            'requestUrl' : self.utrInterFaceAddress['contact'],
				            'extendUrl' : '',
				            'requestBody' : {
								            'formToken' : '8e74687e-3360-4079-9b4c-a5fb70f75577',
								            'proContactId' : '',
								            'proId' : '390e0891c929490c977fa6527857fb38',
								            'sellerContactName' : '　',
								            'sellerContactPhone' : '　',
								            'sellerContactFax' : '',
								            'sellerContactEmail' : '',
								            'sellerAddress' : '　',
								            'sellerUrl' : '　',
								            'contactName' : u'超级用户',
								            'contactPhone' : '13241232366',
								            'contactFax' : 'super',
								            'contactEmail' : 'super@gemas.com',
								            'contactAddress' : '　',
								            'contactUrl' : '　',
								            }
				}

	#初始化子项目
	def initSubProParam(self):
		self.table.changeSheet('subPro')
		self.saveSubPro = {'requestAddress' : 'newSubPro',
				            'requestMethod' : 'post',
				            'requestUrl' : self.utrInterFaceAddress['newSubPro'],
				            'extendUrl' : '',
				            'requestBody' : {'proName' : self.table.getData('proName'),
											 'proDesc' : self.table.getData('proDesc'),
											 'proPrice' : self.table.getData('proPrice'),
											 'estimatePrice' : self.table.getData('estimatePrice'),
											 'bookValue' : self.table.getData('bookValue'),
											 'packId' : '',
											 'currency' : 'CNY',
											 'proType' : self.table.getData('proType'),
											 'proTypeText' : self.table.getData('proTypeText'),
								            }
					   	}

	def editSubProInfoParam(self):
		self.table.changeSheet('proInfo')
		self.editSubProInfo = {'requestAddress' : 'info',
							   'requestMethod' : 'post',
							   'requestUrl': self.utrInterFaceAddress['info'],
							   'extendUrl' : '',
							   'requestBody' : {'infoId' : '',
												'formToken' : 'e2e20490-da7c-40a4-8ea2-12b7ffd4325f',
												'proId' : '8acf80513f6f4d76ac856acbe8fa38ea',
												'sortCode' : self.table.getData('sortCode'),
												'synchroType' : 'pro',
												'status' : self.table.getData('status'),
												'specificationModel' : self.table.getData('specificationModel'),
												'manufacturer' : self.table.getData('manufacturer'),
												'unitOfMeasurement' : self.table.getData('unitOfMeasurement'),
												'num' : self.table.getData('num'),
												'purchaseDate' : self.table.getData('purchaseDate'),
												'newRate' : self.table.getData('newRate'),}
							   }

	def editSubProEstimateParam(self):
		self.table.changeSheet('subProEstimate')
		self.subProEstimate = {'requestAddress' : 'subestimate',
							   'requestMethod' : 'post',
							   'requestUrl' : self.utrInterFaceAddress['estimate'],
							   'extendUrl' : '',
							   'requestBody' : {'formToken' : '7fc05122-1ca1-45ab-8b6e-3712f40316dc',
												'estimateId' : '',
												'proId' : '8acf80513f6f4d76ac856acbe8fa38ea',
												'hezhunFlag' : self.table.getData('hezhunFlag'),
												'beianFlag' : self.table.getData('beianFlag'),
												'pgjg' : self.table.getData('pgjg'),
												'pgbajg' : self.table.getData('pgbajg'),
												'hzbarq' : self.table.getData('hzbarq'),
												'pgjzr' : self.table.getData('pgjzr'),
												'estNoticeno' : self.table.getData('estNoticeno'),
												'pgjzrsjjg' : self.table.getData('pgjzrsjjg'),
												'lssws' : self.table.getData('lssws'),
												'estimatePrice' : self.table.getData('estimatePrice'),
												'originalPrice' : self.table.getData('originalPrice'),
												'zmJzc' : self.table.getData('zmJzc'),}
								}

	def initSubmitPackParam(self):
		self.submitPack = {'requestAddress' : 'utrmPackSubmit',
						   'requestMethod' : 'mix',
						   'requestUrl' : self.utrInterFaceAddress['utrmPackSubmit'],
						   'extendUrl' : '',
						   'requestBody' : {'taskName' : '资产包提交审核',
											'logResult' : 'TJ',}
						   }

	def initPackFlowParam(self):
		self.packFlowParam = {'requestAddress' : 'packFlow',
							  'requestMethod' : 'post',
							  'requestUrl' : self.utrInterFaceAddress['packFlow'],
							  'extendUrl' : '',
							  'requestBody' : {'formToken' : 'aed34803-9295-4634-a3ee-edb1659d4daa',
											   'taskId' : '1212691',
											   'processStatus' : u'[受理]部门经理审核',
											   'formId' : '05c10f0f90824952902aa4bf1723d049',
											   'taskName' : u'[受理]部门经理审核',
											   'processInsId' : 'packFlow2.1212676',
											   'logResult' : 'T',
											   'assignee' : 'super',
											   'pluginName' : '',
											   'mainStatus' : '',
											   'packId' : '05c10f0f90824952902aa4bf1723d049',
											   'logText' : '',}
							  }

	def initPubMethodParam(self):
		self.table.changeSheet('pubMethod')
		self.pubMethodParam = {'requestAddress' : 'pubMethod',
							   'requestMethod' : 'post',
							   'requestUrl' : self.utrInterFaceAddress['pubMethod'],
							   'extendUrl' : '',
							   'requestBody' : {'proId' : '66cdc9f72f7242e8bfca08ab74fa1322',
												'packFlag' : 'T',
												'formToken' : '',
												'pubId' : '9b9a750573ff4964b254bda85f061406',
												'bidmethod' : self.table.getData('bidmethod'),
												'pubBailCtrl' : self.table.getData('pubBailCtrl'),
												'pubBail' : self.table.getData('pubBail'),
												'pubBailMax' : self.table.getData('pubBailMax'),
												'seId' : self.table.getData('seId'),
												'transWay' : self.table.getData('transWay'),
												'pubBailMark' : self.table.getData('pubBailMark'),
												'isBind' : self.table.getData('isBind'),
												'ifBiddyn' : self.table.getData('ifBiddyn'),
												'pubDealWay' : self.table.getData('pubDealWay'),
												'bidmode' : self.table.getData('bidmode'),
												'seIdSelect' : self.table.getData('seIdSelect'),
												'transWaySe' : self.table.getData('transWaySe'),
												'pubBailMarkSe' : self.table.getData('pubBailMarkSe'),
												'pubBailCtrlSelect' : self.table.getData('pubBailCtrlSelect'),
												'allowEndPrio' : 'F',}
							   }

	def initPackPubParam(self):
		self.table.changeSheet('pub')
		self.packPubParam = {'requestAddress' : 'pub',
							 'requestMethod' : 'put',
							 'requestUrl' : self.utrInterFaceAddress['pub'],
							 'extendUrl' : '',
							 'requestBody' : {'formToken' : 'e2f6a25f-07c5-4a1f-9086-513abde7a0c4',
											  'pubId' : 'c997f777dfef4726b59840ffe298d2d8',
											  'inputStatus' : '0',
											  'proId' : '917ca4ba7f314404a646da93a293594e',
											  'packFlag' : 'T',
											  'buyerPaperFlag' : 'T',
											  'ifPublicity' : 'F',
											  'bidmethod' : 'A10001002',
											  'buyerEpaperFlag' : 'T',
											  'pluginName' : '',
											  'duration' : '20',
											  'pubBailDesc' : self.table.getData('pubBailDesc'),
											  'ifBiddyn' : self.table.getData('ifBiddyn'),
											  'pubStartTime' : self.table.getData('pubStartTime'),
											  'pubDays' : self.table.getData('pubDays'),
											  'pubDelayFlag' : self.table.getData('pubDelayFlag'),
											  'delayBuyerSize' : '',
											  'delayMax' : '',
											  'delayPeroid' : '',
											  'ifMedia' : self.table.getData('ifMedia'),
											  'buyerPaper' : self.table.getData('buyerPaper'),
											  'unitTransferee' : self.table.getData('unitTransferee'),
											  'buyerAuditLevel' : self.table.getData('buyerAuditLevel'),
											  'bailStartFlag' : self.table.getData('bailStartFlag'),
											  'pubBailType' : self.table.getData('pubBailType'),
											  'pubBailDays' : '',
											  'bailDeadTime' : '',
											  'pubBailMethod' : self.table.getData('pubBailMethod'),
											  'buyConditions' : self.table.getData('buyConditions'),
											  'pubPayMode' : self.table.getData('pubPayMode'),
											  'payPeriodInfo' : self.table.getData('payPeriodInfo'),
											  'important' : self.table.getData('important'),
											  'sellConditions' : self.table.getData('sellConditions'),}
							 }
		if 'T' == self.packPubParam['requestBody']['pubDelayFlag']:
			self.packPubParam['requestBody']['delayBuyerSize'] = self.table.getData('delayBuyerSize')
			self.packPubParam['requestBody']['delayMax'] = self.table.getData('delayMax')
			self.packPubParam['requestBody']['delayPeroid'] = self.table.getData('delayPeroid')
		if '1' == self.packPubParam['requestBody']['pubBailType']:
			self.packPubParam['requestBody']['pubBailDays'] = self.table.getData('pubBailDays')
		elif '2' == self.packPubParam['requestBody']['pubBailType']:
			self.packPubParam['requestBody']['bailDeadTime'] = self.table.getData('bailDeadTime')


	def initSetProRulesParam(self):
		self.setProRulesParam = {'requestAddress' : 'rules',
								 'requestMethod' : 'post',
								 'requestUrl' : self.utrInterFaceAddress['rules'],
								 'extendUrl' : '',
								 'requestBody' : {'formToken' : '3648e6f4-3968-42e7-a59d-3c8f984dbd9f',
												  'taskId' : '1238865',
												  'processStatus' : '设置挂牌条件交易方式',
												  'formId' : 'b878274f2b6e4fcb9f4128da595b87d9',
												  'taskName' : '设置挂牌条件交易方式',
												  'processInsId' : 'packFlow2.1238613',
												  'logResult' : 'F',
												  'assignee' : 'super',
												  'pluginName' : '',
												  'mainStatus' : '',
												  'packId' : 'b878274f2b6e4fcb9f4128da595b87d9',
												  'nextUsers' : '',}
								}