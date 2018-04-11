import cx_Oracle
import urllib

def errorReturnNone(func):
	def deco(*args, **kwargs):
		try:
			func(*args, **kwargs)
		except:
			print 'query error'
			return -1
	return deco

class SqlUtil(object):
	@classmethod
	def init(cls):
		#cls.conn = cx_Oracle.connect('qyy/qyy@192.168.9.46/orcl')
		cls.conn = cx_Oracle.connect('utrm_db/utrm_db@192.168.9.46/orcl')
		#cls.conn = cx_Oracle.connect('utr_db/utr_db@192.168.9.28/orcl')
		cls.cursor =cls.conn.cursor()

	@classmethod
	def update(cls,sql):
		cls.cursor.execute(sql)
		cls.conn.commit()

	@classmethod
	def query(cls,sql):
		cls.cursor.execute(sql)
		return cls.cursor.fetchall()

	@classmethod
	def queryOne(cls,sql):
		cls.cursor.execute(sql)
		return cls.cursor.fetchone()

	@classmethod
	#@errorReturnNone
	def queryTask(cls,pro = None,pack = None):
		title = ('taskId','processInsId','taskName','proId','form','assignee')
		try:
			if not pro and not pack:
				return 
			elif pro:
				sql = "select q.dbid_,t.process_ins_id,q.activity_name_,t.pro_id,q.form_,q.assignee_ from UTR_PRO t,JBPM4_TASK q where t.process_ins_id = q.execution_id_ and t.pro_id ='" + pro.proId + "'and q.assignee_ = '" + pro.manager +"'"
				#sql = "select q.dbid_,t.process_ins_id,q.activity_name_,t.pro_id,q.form_,q.assignee_ from UTR_PRO t,JBPM4_TASK q where t.process_ins_id = q.execution_id_ and t.pro_id ='" + pro.proId + "'and q.assignee_ = 'super'"
				return dict(zip(title,cls.query(sql)[0]))
			else:
				sql = "select q.dbid_,t.process_ins_id,q.activity_name_,t.pack_id,q.form_,q.assignee_ from UTR_PACK t,JBPM4_TASK q where t.process_ins_id = q.execution_id_ and t.pack_id ='"+ pack.packId +"'and q.assignee_ = '" + pack.manager +"'"
				#sql = "select q.dbid_,t.process_ins_id,q.activity_name_,t.pack_id,q.form_,q.assignee_ from UTR_PACK t,JBPM4_TASK q where t.process_ins_id = q.execution_id_ and t.pack_id ='"+ pack.packId +"'and q.assignee_ = 'super'"
				return dict(zip(title,cls.query(sql)[0]))
		except Exception,e:
			print e

	@classmethod
	def queryBuyerTask(cls,user,pro):
		title = ('taskId','processInsId','taskName','buyerId','form','assignee')
		sql = "select q.dbid_,t.process_ins_id,q.activity_name_,t.pro_id,q.form_,q.assignee_ from UTR_BUYER t,JBPM4_TASK q where t.process_ins_id = q.execution_id_ and t.buyer_id ='" + user.buyerId + "'and q.assignee_ = '" + pro.manager +"'"		
		return dict(zip(title,cls.query(sql)[0])) if cls.query(sql) else None

	@classmethod
	def queryMainStatus(cls,pro):
		sql = "select t.main_status from UTR_PRO t where t.pro_id = '" + pro.proId + "'"
		return cls.query(sql)

	@classmethod
	def getTaskUrl(cls,pro):
		result = cls.queryTask(pro)
		q = urllib.quote
		if [] != result:
			return result[0][0] + '?processInsId=' + result[0][1] + '&taskId=' + str(result[0][2]) + '&taskName=' + q(q(result[0][3].decode('gb2312').encode('utf-8')))

	@classmethod
	def getTaskJS(cls,pro):
		result = cls.queryTask(pro)
		q = urllib.quote
		if [] != result:
			return "banli('" + str(result['taskId']) + "','" + result['processInsId'] + "','" + result['taskName'].decode('gb2312') + "','" + result['proId'] + "','" + (result['form'] or "") + "','" + result['assignee'] + "');"

	@classmethod
	def getTaskName(cls,pro = None,pack=None):
		if pro:
			result = cls.queryTask(pro=pro)
		elif pack:
			result = cls.queryTask(pack = pack)
		if result:
			return result['taskName'].decode('gb2312')
		else:
			return -1

	@classmethod
	def getBuyerTaskName(cls,user,pro):
		result = cls.queryBuyerTask(user,pro)
		if result:
			return result['taskName'].decode('gb2312')
		else:
			return None

	@classmethod
	def getMainStatus(cls,pro):
		result = cls.queryMainStatus(pro)
		if [] != result:
			return result[0][0]

	@classmethod
	def getBuyerMainStatus(cls,buyer):
		sql = "select t.main_status from UTR_BUYER t where t.buyer_Id = '" + buyer.buyerId + "'"
		result = cls.queryOne(sql)
		if [] != result:
			return result[0]

	@classmethod
	def getBuyerBailFinishFlag(cls,buyer):
		sql = "select bail_finish_flag from UTR_BUYER where buyer_Id = '" + buyer.buyerId + "'"
		result = cls.queryOne(sql)
		if [] != result:
			return result[0]

	@classmethod
	def getUserId(cls,user):
		sql = "select * from UCT_CUSTOMER t where t.create_realname = '" + user.userEname + "'"
		result = cls.queryOne(sql)
		if [] != result:
			return result[0]

	@classmethod
	def getBuyerId(cls,user,pro):
		sql = "select t.buyer_Id from UTR_BUYER t where t.buyer_userename = '" +user.userEname+"' and t.pro_id = '" + pro.proId + "'"
		result = cls.queryOne(sql)
		if [] != result:
			return result[0]

	@classmethod
	def getProcessId(cls,pro):
		sql = "select t.process_ins_id from UTR_PRO t where t.pro_id = '" + pro.proId + "'"
		result = cls.queryOne(sql)
		if [] != result:
			return result[0]

	@classmethod
	def getDealId(cls,pro):
		sql = "select t.deal_id from UTR_DEAL t where t.pro_id = '" + pro.proId + "'"
		result = cls.queryOne(sql)
		if result:
			return result[0]
		else:
			return ''

	@classmethod
	def getProNo(cls,pro):
		sql = "select pro_no from UTR_PRO where pro_id = '" + pro.proId + "'"
		result = cls.queryOne(sql)
		if result:
			return result[0]
		else:
			return ''

	@classmethod
	def getBillId(cls,pro,billStatus):
		sql = "select bill_id from UTR_BILL where pro_id = '" + pro.proId + "' and bill_status = '" + billStatus + "'"
		result = cls.queryOne(sql)
		if result:
			return result[0]
		else:
			return ''

	@classmethod
	def getBillStatus(cls,user,pro):
		sql = "select t. from UTR_BILL t join UTR_BUYER u \
       					on u.pro_id = '"+ pro.proId +"'\
      				   and t.pro_id = u.pro_id\
      				   and t.customer_no = u.customer_no\
      				   and u.buyer_userename = '" + user.buyerId +"'"
		result = cls.queryOne(sql)
		if [] != result:
			return result[0]

	# @classmethod
	# def setPro(cls,pro):
	# 	cls.setTaskUrl(pro)
	# 	cls.setTaskName(pro)
	# 	cls.setMainStatus(pro)

#title = ['pro_id','process_ins_id','dbid_','execution_id_']
#dict(zip(title,result[0]))
