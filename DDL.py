import python_mysql
import pymysql
import pandas as pd

# create, alter, drop, rename

cursor = python_mysql.get_cursor() # mysql 연결
sql = "alter table product rename pro" # 쿼리를 정의함
cursor.execute(sql) # execute를 통해 쿼리를 실행함.
result = cursor.fetchall() # 실행된 쿼리의 결과를 가져옴
print(result)
a = pd.DataFrame(result) # 데이터프레임으로 변환함.
print(a)
