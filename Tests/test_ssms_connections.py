from sqlalchemy import create_engine, text

server = "ASHISH-PC\\SQLEXPRESS"
database = "master"

def test_ssms_connetion():
    connection_string = (
        f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
    )

    engine = create_engine(connection_string)
    connection = engine.connect()
    query = text("select * from harry;")
    result = connection.execute(query)
    for row in result:
        print(row)


