from sqlalchemy import Column, Integer, String, Date

from db import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    birthday = Column(Date)
    additional = Column(String(255), nullable=True)