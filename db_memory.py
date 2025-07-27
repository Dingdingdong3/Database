import sqlite3

memory_conn = sqlite3.connect(':memory:')
print("메모리 데이터베이스 연결")

memory_conn.close()
print("메모리 데이터베이스 종료!")