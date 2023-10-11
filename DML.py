import python_mysql

# mysql 연결
cursor = python_mysql.get_cursor()

# CRUD(INSERT, SELECT, UPDATE, DELETE)

# INSERT
# table의 모든 속성에 값 넣기
insert_sql = "insert into test values(1, '값1', '값2', '값3')"
# 정해준 속성에 값 넣기(단, not null일 경우 값이 무조건 들어감)
insert_sql2 = "insert into test(col2, col3) values('값1', '값2')"

# SELECT
# 테이블 전체 컬럼의 데이터 모두 읽기
select_all_column_read_sql = "select * from test"
# 특정 데이터 모두 읽기
select_chose_column_read_sql = "select col2, col3 from test"
# 특정 컬럼의 데이터를 검색하되, 표시할 컬럼명도 다르게 하기
select_as_sql = "select col1 as pri_col, col2 as column from test"
# 데이터 정렬해서 읽기(desc: 오름차순, asc: 내림차순)
select_sort_read_sql = "select * from test order by col2 desc"
# 조건에 맞는 데이터만 검색하기(비교: >, <, = / 논리: and, or)
select_where_sql = "select * from test where col1 < 3"
select_where_sql2 = "select * from test where (col=3) or (col1=2)"
# 조건에 맞는 데이터만 검색하기(like)
select_like_sql = "select * from test where col2 like '김%'"
select_like_sql2 = "select * from test where col2 like '%김%'"
select_like_sql3 = "select * from test where col2 like '김__'" # 김으로 시작하고 뒤에 2글자가 붙을 경우
# 결과중 일부만 데이터 가져오기(limit)
select_limit_sql = "select * from test limit 10"
select_limit_sql2 = "select * from test limit 100, 10" # 100번째부터, 10개만 가져오기

# UPDATE
update_sql = "update test set 컬럼명 = '수정하고싶은 값' where 특정_컬럼 = '값'"

# DELETE
delete_all_sql = "delete from test"
delete_sql = "delete from test where col5='값'"

# execute를 통해 쿼리를 실행함
sql = ''
cursor.execute(sql)
