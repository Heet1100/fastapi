from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    Subject_assign: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name:str
    email: str
    age:int


class UserCreate(UserBase):
    password: str


class User(UserBase):
    roll_no: int
    Teacher_id:int
    items: list[Item] = []

    class Config:
        orm_mode = True