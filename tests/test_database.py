import mysql.connector
import pytest

@pytest.fixture
def db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="test_db"
    )
    yield connection
    connection.close()

def test_select_books(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    result = cursor.fetchone()[0]
    assert result > 0
    cursor.close()