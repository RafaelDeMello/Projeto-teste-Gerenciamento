import sqlite3

class DataBase():
    def __init__(self, name = "system.db") -> None:
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS users(
                           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           user TEXT UNIQUE NOT NULL,
                           passoword TEXT NOT NULL,
                           access TEXT NOT NULL
                   
                    );
            """)
        except AttributeError:
            print("faca a conexao")
            
    def insert_user(self, name, user, password, access):
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           
                INSERT INTO users(name , user, password, access) VALUES(?,?,?,?)  
                 
                           
            """,(name, user, password, access))
            self.connection.commit()
        except:
            pass

    def  check_user(self, user, password):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                                       
                 SELECT * FROM users;          
                                       
            """)  

            for linha in cursor.fetchall(): 
                if linha[2].upper() == user.upper() and linha[3] == password and linha[4] =="Administrador":
                     return "Administrador"
                     break
                elif linha[2].upper() == user.upper() and linha[3] == password and linha[4] =="Usuario":
                     return "user"
                else:
                    continue 
            return "Sem acesso"
        except:
            pass

if __name__== "__main__":

    db = DataBase()
    db.conecta()
    db.create_table_users()
    db.close_connection()

                           
    