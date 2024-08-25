from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    year: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookInDB(BookBase):
    id: int

    class Config:
        orm_mode = True
