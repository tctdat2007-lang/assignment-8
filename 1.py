import pymysql

conn = pymysql.connect(
    host='localhost',
    user='tctd',
    password='280807',
    database='flight_game',
    charset='utf8mb4'
)

cur = conn.cursor()

icao = input("Enter ICAO code: ").upper()
cur.execute("SELECT name, municipality FROM airport WHERE ident=%s", (icao,))
row = cur.fetchone()

if row:
    print("Airport name:", row[0])
    print("Location:", row[1])
else:
    print("Airport not found")



