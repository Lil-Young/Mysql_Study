import pymysql, os

pw = pw

def get_cursor():
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1111',
        db='ecommerce',
        charset='utf8'
    )
    cursor = db.cursor()
    return cursor