from pydantic import BaseModel, EmailStr
from typing import List
from typing import Annotated
from annotated_types import MinLen, MaxLen

from api.scores.schemas import Score



class StudentBase(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(50)]
    email: EmailStr

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class StudentUpdateePartial(StudentCreate):
    name: Annotated[str, MinLen(2), MaxLen(50)] | None = None
    email: EmailStr | None = None
    

class Student(StudentBase):
    id: int
    scores: List[Score] = []

    class Config:
        orm_mode = True
