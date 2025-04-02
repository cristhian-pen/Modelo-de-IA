import mysql.connector


def connectDataBase():
    conn = mysql.connector.connect(
        database="igrisdatalake",
        user="DBADM",
        password="@Aigris@",
        host="localhost"
    )
    return conn