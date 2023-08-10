from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base
from flask_login import UserMixin

DB_URL = 'sqlite:///flask_study.sqlite3'

engine = create_engine(DB_URL)
base = declarative_base()

class User(UserMixin, base):
    __tablename__ = 'User'

    id = Column('id', String(64), primary_key=True)
    name = Column('name', String(128))

    def to_dict(self):
        user = {
            "email":self.id,
            "name":self.name
        }
        return user
    

def create_database():
    base.metadata.create_all(bind=engine)

def create_session():
    return sessionmaker(bind=engine)()


if __name__ == '__main__':
    create_database()