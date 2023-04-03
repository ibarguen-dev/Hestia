import sqlite3

class Database():

    conn = sqlite3.connect("database.db")

    def __init__ (self):
        
        self.conn

        self.Create()

    def Create (self):

        self.conn.execute("CREATE TABLE IF NOT EXISTS settings (python integer, data integer)")

        self.conn.execute("CREATE TABLE IF NOT EXISTS address (addres text)")

        self.conn.execute("CREATE TABLE IF NOT EXISTS user (username text)")

    def InsertSettings (self,python,data):

        try: 
            py = str(python)

            datas = str(data)

            self.conn.execute("INSERT INTO settings  VALUES ('"+py+"','"+datas+"')")

            self.conn.commit()

            return True
        
        except Exception as e:

            return "Error: "+ e
    
    def ReadSetting (self):

        try:
            lista = self.conn.execute("SELECT * FROM settings")

            return lista.fetchone()
        
        except Exception as e:

            return "Error: "+ e
    
    def InsertAddres (self,adrees):

        try:
            self.conn.execute("INSERT INTO  address VALUES ('"+adrees+"')")

            self.conn.commit()

            return True
        
        except Exception as e:

            return "Error: "+ e

    def UpdateAdress (self,address):

        try:
            self.conn.execute("UPDATE address SET addres = '"+address+"'")

            self.conn.commit()

        except Exception as e:

            return "Error: "+ e

    def ReadAdress (self):

        try:
            lista = self.conn.execute("SELECT * FROM address")

            return lista.fetchone()
        
        except  Exception as e:

            return "Error: "+ e
    
    def InsertUser(self,user):

        try:

            self.conn.execute("INSERT INTO user VALUES ('"+user+"')")

            self.conn.commit()

            return True
        
        except Exception as e:

            return "Error: "+ e 
        
    def ReadUser(self):

        try:
            user = self.conn.execute("SELECT * FROM user")

            return user.fetchone()
        
        except Exception as e:

            return "Error: "+ e

