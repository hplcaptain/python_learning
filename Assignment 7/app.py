import psycopg2

# This function will check the database connection
def get_connection():
    try:
        connection = psycopg2.connect(
            database="pythonproject",
            user="postgres",
            password="sa",
            host="127.0.0.1",
            port="5432"
        )
        print("DB Connected Successfully")
        return connection
    except Exception as e:
        print("Database Connection failed.", e)


# This function will check if the table exists or not, if not it will create a new one
def create_table():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            age INTEGER
        )
        """)
        conn.commit()
        print("Table created successfully")
        conn.close()
    except Exception as e:
        print("Error creating table", e)


# This function will insert data into the table
def insert(name, age):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students(name, age) VALUES (%s, %s)",
            (name, age)
        )
        conn.commit()
        conn.close()
        print("Record inserted successfully.")

    except Exception as e:
        print("Data insert error", e)


# This function will fetch records from the table
def get_all():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        print("\nAll student records:")
        for row in rows:
            print(row)

        conn.close()

    except Exception as e:
        print("Error in fetching the details", e)


# Program starts here
if __name__ == "__main__":
    create_table()

    name = input("Enter student name: ")
    age = int(input("Enter age of the student: "))

    insert(name, age)
    get_all()