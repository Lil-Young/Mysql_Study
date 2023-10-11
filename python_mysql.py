import pymysql
import dotenv, os

# dotenv 라이브러리를 사용해서 .env 파일을 찾음. 이 파일에는 환경변수와 .env에 들어있는 내용이 저장됨
dotenv_file = dotenv.find_dotenv()
# dotenv 라이브러리를 사용해서 .env 파일에서 환경변수 및 파일에 있는 내용을 로드함. 그래서 .env 파일에 정의된 환경변수를 사용할 수 있음
dotenv.load_dotenv(dotenv_file)

# .env 파일에서 pw라는 이름의 환경변수 값을 가져옴
pw = os.environ['pw']

def get_cursor():
    # db 변수: mysql에 연결하기 위한 연결 객체
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd=pw,
        db='test',
        charset='utf8'
    )
    # cursor 변수: 연결 객체에서 커서를 가져옴. 커서는 sql 쿼리를 실행하고 데이터베이스와 상호작용함
    cursor = db.cursor()
    return cursor