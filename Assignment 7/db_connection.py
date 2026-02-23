import psycopg2

connection = psycopg2.connect(database="pythonproject",user="postgres",password="sa",host="127.0.0.1",port="5432")
print ("DB Connected Successfully")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    subject VARCHAR(50)
    )
""")

connection.commit()

print("Table create successfully")

cursor.execute(
    "SELECT * FROM teachers"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()