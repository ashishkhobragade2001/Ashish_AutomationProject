from sqlalchemy import create_engine, text


username = "root"
password = 654321
server = "localhost"
database = "automation_test_db"

def test_create_mysql_connections():
    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{server}/{database}"
    )

    connection = engine.connect()

    query = text("SELECT * FROM users")

    result = connection.execute(query)

    for row in result:
        print(row)