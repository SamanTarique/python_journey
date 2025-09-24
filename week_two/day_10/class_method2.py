class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    @classmethod
    def connect(cls, connection_string):
        """Factory method — will create the right DB class instance"""
        return cls(connection_string)

    def __str__(self):
        return f"Generic database at {self.connection_string}"


class PostgresDatabase(Database):
    def __init__(self, connection_string, version="15"):
        super().__init__(connection_string)
        self.version = version

    def __str__(self):
        return f"Postgres v{self.version} at {self.connection_string}"


class MySQLDatabase(Database):
    def __init__(self, connection_string, charset="utf8mb4"):
        super().__init__(connection_string)
        self.charset = charset

    def __str__(self):
        return f"MySQL with charset={self.charset} at {self.connection_string}"


db1 = PostgresDatabase.connect("postgres://localhost:5432/mydb")
db2 = MySQLDatabase.connect("mysql://localhost:3306/mydb")

print(db1)
print(db2)
