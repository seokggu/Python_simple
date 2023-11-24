from db.common.connection import connection


#리뷰 저장
def add_review(data):
    # 1. Connection
    conn = connection()

    try:
        # 2. 일꾼생성
        curs = conn.cursor()
        # 3. job 생성(sql) -> INSERT, DELETE, UPDATE, SELECT
        sql = """
                INSERT INTO tbl_review(title, review, score, writer, reg_data)
                VALUES(%(title)s, %(review)s, %(score)s, %(writer)s, %(reg_date)s)
                """
    except Exception as e:
        print(e)
    finally:
        # 5.자원 해제
        conn.close()