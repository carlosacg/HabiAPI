import MySQLdb
import os

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('MYSQL_USER')
DB_PASS = os.environ.get('MYSQL_PASSWORD')
DB_NAME = os.environ.get('MYSQL_DB')
DB_PORT = int(os.environ.get('DB_PORT'))


def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT]
    conn = MySQLdb.connect(*datos)
    cursor = conn.cursor()

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
