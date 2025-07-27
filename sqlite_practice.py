import sqlite3

# DB 연결 테스트
conn = sqlite3.connect('my_first_db.db')
print("DB 연결 완료")