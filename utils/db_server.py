import psycopg2

class DBServer():
    def __init__(self, uri):
        self.uri = uri
        
    def connect(self):
        try:
            self.conn = psycopg2.connect(self.uri)
            self.conn.autocommit = True
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
    
    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()