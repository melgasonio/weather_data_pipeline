import psycopg

class DBServer():
    def __init__(self, uri):
        self.uri = uri
        
    def connect(self):
        try:
            self.conn = psycopg.connect(self.uri)
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