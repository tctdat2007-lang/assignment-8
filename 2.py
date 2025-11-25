import pymysql

conn = pymysql.connect(
    host='localhost',
    user='tctd',
    password='280807',
    database='flight_game',
    charset='utf8mb4'
)

cur = conn.cursor()

code = input("Enter area code (e.g. FI): ").upper()

cur.execute("""
    SELECT type, COUNT(*) 
    FROM airport 
    WHERE iso_country=%s 
    GROUP BY type
    ORDER BY type;
""", (code,))

rows = cur.fetchall()

if rows:
    print(f"Airports in {code}:")
    for t, c in rows:
        print(f"{t}: {c}")
else:
    print("No airports found.")

