import psycopg2

DATABASE_URL = 'postgresql://postgres:7crQ9MrrBC216QmgSB^S@darcydb.crgk48smefvn.ap-southeast-2.rds.amazonaws.com:5432/postgres'

def connect():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def run_sql_file(file_path):
    with open(file_path, 'r') as file:
        sql = file.read()
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()

def view_table(table_name):
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table_name}")
            return cursor.fetchall()

if __name__ == "__main__":
    run_sql_file('DDL/create.sql')
    run_sql_file('DML/insert.sql')
    rows = view_table('project_two.trinity')  # replace with your table name
    for row in rows:
        print(row)