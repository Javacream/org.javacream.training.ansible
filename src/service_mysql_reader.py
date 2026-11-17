import mysql.connector

with mysql.connector.connect(
    host="10.160.1.85",
    port=3306,
    user="user0",
    password="user0",
    database="javacream"
) as connection:
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT name, ipaddress, port FROM Services")

        services = {
            row["name"]: (row["ipaddress"], row["port"])
            for row in cursor
        }

print(services)

