from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "Student"

    roll_no = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)
    age=Column(Integer)
    Teacher_id=Column(Integer, ForeignKey("Teacher.id"))

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "Teacher"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    Subject_assign = Column(String, index=True)

    owner = relationship("User", back_populates="items")