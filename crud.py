from sqlalchemy.orm import Session

import model
import schema


def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.roll_no == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.email == email).first()


def get_user_by_name(db: Session, name: str):
    return db.query(model.User).filter(model.User.name == name).first()


def get_user_by_age(db: Session, age: int):
    return db.query(model.User).filter(model.User.age == age).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = model.User(email=user.email, name=user.name, age=user.age, hashed_password=fake_hashed_password,
                         id=user.Teacher_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schema.ItemCreate, user_id: int):
    db_item = model.Item(**item.dict(), id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
