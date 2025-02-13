import mysql.connector


class MySQLConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mukil_5241",
                database="new_schema",
            )
            print("Connected to MySQL database")

            return self.connection
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(f"Something went wrong: {err}")
            return None

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Disconnected from MySQL database")

    def execute_query(self, query, params=None):
        try:
            if self.connection and self.connection.is_connected():
                cursor = self.connection.cursor(dictionary=True)

                cursor.execute(query, params)
                response = cursor.fetchall()
                cursor.close()
                return response

            print("Not connected. Call connect() first.")
            return None
        except mysql.connector.Error as err:
            print(f"Query execution failed: {err}")
            return None

    def insert_data(self, table, data):  # Example insert
        try:
            if self.connection and self.connection.is_connected():
                cursor = self.connection.cursor()
                columns = ", ".join(data.keys())
                values = ", ".join(["%s"] * len(data))  # Placeholders for security

                query_statement = f"INSERT INTO {table} ({columns}) VALUES ({values})"
                cursor.execute(query_statement, list(data.values()))

                self.connection.commit()  # Important: Commit the changes
                cursor.close()
                return True

            print("Not connected. Call connect() first.")
            return False

        except mysql.connector.Error as err:
            self.connection.rollback()  # Rollback on error
            print(f"Insert failed: {err}")
            return False


mysql_conn = MySQLConnection()


if mysql_conn.connect():
    try:
        mysql_conn.insert_data(
            "courses",
            {"name": "Introduction to Python", "duration": 10, "fees": 500.00},
        )
        users = mysql_conn.execute_query("SELECT * FROM courses")
        print(users)

    finally:
        mysql_conn.disconnect()

else:
    print("Connection failed.")
