import peewee
from datetime import datetime as dt

class Database():
    def __init__(self, dbname: str) -> None:
        self.dbname = dbname
        self.database = peewee.SqliteDatabase(self.dbname)
        self.create_tables()

    def connect_db(self) -> int:
        try:
            self.database.connect()
            return 0
        except:
            return -1

    def create_tables(self) -> int:
        try:
            tables = [_Passwords()]
            self.database.create_tables(tables)
            return 0
        except:
            return -1

    def insert_password(self, title: str, password: str) -> int:
        try:
            pswd = _Passwords(id=(_Passwords.select(_Passwords.id).max()+1), title=title, password=password, last_modify=dt.now())
            pswd.save()
            return 0
        except:
            return -1
        
    def select_all_passwords(self) -> dict:
        try:
            pswds = _Passwords.select()
            return pswds
        except:
            return -1
    
    def select_password(self, title: str) -> dict:
        try:
            pswd = _Passwords.select().where(_Passwords.title == title)
            return pswd
        except:
            return -1

    def update_password(self, title: str, password: str) -> int:
        try:
            pwsd = _Passwords.update(title=title, password=password, last_modify=dt.now())
            pwsd.save()
            return 0
        except:
            return -1


# region [Tables]

# region [BASE_CLASS]

class BaseModel(peewee.Model):
    class Meta():
        db = Database("Database.db")
        database = db.database

# endregion [BASE_CLASS]

class _Passwords(BaseModel):
    id = peewee.IntegerField()
    title = peewee.TextField()
    password = peewee.TextField()
    last_modify = peewee.DateField()


# endregion [Tables]