# 📚 SQLite 학습 프로젝트

백엔드 개발을 위한 SQLite 데이터베이스 기초 학습 저장소입니다.

## 🎯 학습 목표

- SQLite 기본 문법 익히기
- Python과 SQLite 연동 방법 학습
- 실전 프로젝트를 통한 데이터베이스 활용 경험

## 📋 학습 내용

### 1단계: SQLite 기초
- [x] 데이터베이스 연결 및 기본 설정
- [ ] 테이블 생성 (CREATE TABLE)
- [ ] 데이터 삽입 (INSERT)
- [ ] 데이터 조회 (SELECT)
- [ ] 데이터 수정/삭제 (UPDATE/DELETE)

### 2단계: 중급 기능
- [ ] JOIN을 활용한 테이블 연결
- [ ] 집계 함수 (COUNT, SUM, AVG)
- [ ] 인덱스 활용
- [ ] 트랜잭션 처리

### 3단계: 실전 프로젝트
- [ ] 개인 도서 관리 시스템
- [ ] 간단한 블로그 API
- [ ] 할일 관리 앱

## 🛠️ 기술 스택

- **언어**: Python 3.x
- **데이터베이스**: SQLite
- **라이브러리**: sqlite3 (내장 모듈)

## 🚀 시작하기

### 필요 조건
- Python 3.6 이상

### 설치 및 실행
```bash
# 저장소 클론
git clone https://github.com/[your-username]/sqlite-learning

# 디렉토리 이동
cd sqlite-learning

# Python 스크립트 실행
python basic_sqlite.py
```

## 📁 폴더 구조
```
sqlite-learning/
├── README.md
├── basic/
│   ├── 01_connection.py
│   ├── 02_create_table.py
│   └── 03_crud_operations.py
├── intermediate/
│   ├── joins.py
│   └── aggregations.py
└── projects/
    ├── book_manager/
    └── todo_app/
```

## 📝 학습 일지

| 날짜 | 학습 내용 | 비고 |
|------|-----------|------|
| 2025-07-27 | 프로젝트 시작, 기본 연결 | SQLite 첫 실습 |
| | | |

## 🔍 주요 학습 포인트

### 기본 패턴
```python
import sqlite3

# 1. 연결
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# 2. SQL 실행
cursor.execute("SQL 쿼리")

# 3. 저장 및 종료
conn.commit()
conn.close()
```

### 자주 사용하는 SQL 명령어
- `CREATE TABLE` - 테이블 생성
- `INSERT INTO` - 데이터 삽입
- `SELECT` - 데이터 조회
- `UPDATE` - 데이터 수정
- `DELETE` - 데이터 삭제

## 📚 참고 자료

- [SQLite 공식 문서](https://www.sqlite.org/docs.html)
- [Python sqlite3 문서](https://docs.python.org/3/library/sqlite3.html)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)

## 🤝 기여하기

학습 과정에서 발견한 좋은 예제나 개선사항이 있다면 언제든 PR을 보내주세요!

## 📧 연락처

궁금한 점이나 피드백이 있으시면 이슈를 등록해주세요.

edwardcu3476@gmail.com

---

⭐ 이 저장소가 도움이 되었다면 Star를 눌러주세요!