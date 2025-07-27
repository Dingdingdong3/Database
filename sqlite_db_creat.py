import sqlite3

# 만들고 싶은 데이터베이스 파일 이름들
databases = ['books.db', 'news.db', 'foods.db']

for db_name in databases:
    conn = sqlite3.connect(db_name)
    print(f"{db_name} 생성완료")
    conn.close()

print("데이터베이스 파일 생성완료")