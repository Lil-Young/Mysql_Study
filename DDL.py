import python_mysql
import pymysql
import pandas as pd

cursor = python_mysql.get_cursor()

sql = "SHOW tables"
cursor.execute(sql)
result = cursor.fetchall()
a = pd.DataFrame(result)
print(a)
