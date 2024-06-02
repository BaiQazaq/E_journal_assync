from pydantic import BaseModel


class ScoreBase(BaseModel):
    subject: str
    value: float
    

class ScoreCreate(ScoreBase):
    student_id: int | None = 0

class ScoreUpdate(ScoreBase):
    pass

class Score(ScoreBase):
    id: int

    class Config:
        orm_mode = True


