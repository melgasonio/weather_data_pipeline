import psycopg2

class DBServer():
    def __init__(self, keys):
        self.keys = keys
        self.conn = None
        self.cur = None
        
    def connect(self):
        keys = self.keys
        
        try:
            self.conn = psycopg2.connect(
                host=keys["host"],
                port=keys["port"],
                database=keys["db"],
                user=keys["user"],
                password=keys["password"]
            )
            self.cur = self.conn.cursor()
            print("Successfully connected to db")
        except Exception:
            raise
    
    def execute_sql(self, sql, fetch=False):
        if not self.cur:
            raise Exception("Call connect() first to establish a connection")
        self.cur.execute(sql)
        print("Successfull executed SQL statements")
        
        if fetch:
            return self.cur.fetchall()
        self.conn.commit()
    
    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()