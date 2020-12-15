SELECT
	A.NAME AS name,
	A.idcard_number AS idcardNumber,
	A.phone AS phone,
	B.record_status AS recordStatus 
FROM
	public_health_db.user_base_info A
	INNER JOIN public_health_db.ph_high_risk_group_info B ON A.residenter_id = B.residenter_id 
WHERE
	if('{name}'!='',A.NAME = '{name}',1=1)
	and if('{idcard_numbe}'!='',A.idcard_number= '{idcard_numbe}',1=1);