import python_mysql
import pandas as pd

# create, alter, drop

# mysql 연결
cursor = python_mysql.get_cursor()

# 쿼리 정의
# CREATE
create_db_sql = "create database test"
create_table_sql = """create table test_table(
    col1    int not null auto_increment,
    col2    varchar(20),
    col3    varchar(30),
    col4    varchar(50),
    primary key(col1)
    )"""

# ALTER
# 테이블에 새로운 컬럼 추가
alter_table_sql = "alter table test add column col5 varchar(10) not null"
# 테이블 컬럼 타입 변경
alter_table_column_type_change_sql = "alter table test modify column col_5 varchar(20) not null"
# 테이블 컬럼 이름 변경
alter_table_column_name_change_sql = "alter table test change column col_5 col_6 varchar(20) not null"
# 테이블 컬럼 삭제
alter_table_column_drop_sql = "alter table test drop column col_6"
# 테이블 이름 변경
alter_table_renmae_sql = "alter table test rename new_test"

# DROP
drop_db_sql = "drop database test"
drop_table_sql = "drop table test"
drop_db_if_exists_sql = "drop database if exists test"
drop_table_if_exists_sql = "drop table if exists test"

# db, table 목록 보기
show_db_sql = "show databases"
show_table_sql = "show tables"

# db 사용하기
use_db_sql = "use test"

# table 구조 보기
desc_table_sql = "desc test"

# execute를 통해 쿼리를 실행함.
cursor.execute(use_db_sql)

# 실행된 쿼리의 결과를 가져옴
result = cursor.fetchall()
print(result)
a = pd.DataFrame(result) # 데이터프레임으로 변환함.
print(a)
