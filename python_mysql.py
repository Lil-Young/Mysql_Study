import pymysql
import dotenv, os

dotenv_file = dotenv.find_dotenv()
print(dotenv)
pw = os.environ['pw']

def get_cursor():
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd=pw,
        db='ecommerce',
        charset='utf8'
    )
    cursor = db.cursor()
    return cursor