-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH from Member_profile
Where month(Date_of_birth) = 3
AND gender = 'W'
AND TLNO is not null
order by Member_id asc;



