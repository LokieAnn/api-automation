#-*- coding:utf-8 -*-
from params import Params

class UtrgParams(Params):
	def __init__(self,table):
		super(UtrgParams,self).__init__()
		self.table = table
		self.initParams()

	def initParams(self):
		self.initNewProParam()
		self.initCompParam()
		self.initSellerParam()
		self.initFinanceParam()
		self.initEstimateParam()
		self.initManagerParam()
		self.initPubParam()
		self.initHolderParam()
		self.initContactParam()
		self.initSubmitParam()
		self.initG3FlowParam()

	#初始化新增项目参数
	def initNewProParam(self):
		self.table.changeSheet('newUTRG')
		self.newPro = {'requestAddress' : 'newUTRG',
					   'requestMethod' : 'post',
					   'requestUrl' : self.utrInterFaceAddress['newUTRG'],
					   'extendUrl' : '',
					   'requestBody' : {'formToken' : '',
					  				   'proId' : '',
					  				   'sellerName' : '',
					  				   'proType' : 'guquan',
					  				   'proMonths' : 'sell',
					  				   'priceUnit' : '万元',
					  				   'isGzw' : 'T',
					  				   'typeGz' : self.table.getData('typeGz'),
					  				   'proName' : self.table.getData('proName'),
					  				   'pauseTime' : self.table.getData('pauseTime'),
					  				   'proPrice' : self.table.getData('proPrice'),
					  				   'bidPrice' : self.table.getData('bidPrice'),
					  				   'sellPercent' : self.table.getData('sellPercent'),
					  				   'afterAddShares' : self.table.getData('afterAddShares'),
					  				   'ifControlTrans' : self.table.getData('ifControlTrans'),
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
										     'holdPercent' : self.table.getData('holdPercent'),
										     'sharesHave' : self.table.getData('sharesHave'),
										     'sellPercent' : self.table.getData('sellPercent'),
										     'sharesWant' : self.table.getData('sharesWant'),
										     }
					  	}

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
						   				      'zmLdzc' : self.table.getData('zmLdzc'),
						   				      'pgLdzc' : self.table.getData('pgLdzc'),
						   				      'zmQtzc' : self.table.getData('zmQtzc'),
						   				      'pgQtzc' : self.table.getData('pgQtzc'),
						   				      'zmZzc' : self.table.getData('zmZzc'),
						   				      'pgZzc' : self.table.getData('pgZzc'),
						   				      'zmLdfz' : self.table.getData('zmLdfz'),
						   				      'pgLdfz' : self.table.getData('pgLdfz'),
						   				      'zmCqfz' : self.table.getData('zmCqfz'),
						   				      'pgCqfz' : self.table.getData('pgCqfz'),
						   				      'zmZfz' : self.table.getData('zmZfz'),
						   				      'pgZfz' : self.table.getData('pgZfz'),
						   				      'zmJzc' : self.table.getData('zmJzc'),
						   				      'pgJzc' : self.table.getData('pgJzc'),
						   				      'remark' : self.table.getData('remark'),
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
									     'buyerAuditLevel' : '2',
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
		self.P3Submit = {'requestAddress' : 'p3ProSubmit',
				         'requestMethod' : 'mix',
				         'requestUrl' : self.utrInterFaceAddress['p3ProSubmit'],
				         'extendUrl' : '',
				         'requestBody' : {'taskName' : u'项目提交审核',
					      				  'logResult' : 'TJ',}
					    }

		self.G3Submit = {'requestAddress' : 'g3ProSubmit',
				         'requestMethod' : 'mix',
				         'requestUrl' : self.utrInterFaceAddress['g3ProSubmit'],
				         'extendUrl' : '',
				         'requestBody' : {'taskName' : u'项目提交审核',
					      				  'logResult' : 'TJ',}
					    }	

	#工作流参数
	def initG3FlowParam(self):
		self.G3FlowParam = {'requestAddress' : 'g3Flow',
				            'requestMethod' : 'post',
				            'requestUrl' : self.utrInterFaceAddress['g3Flow'],
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
	

