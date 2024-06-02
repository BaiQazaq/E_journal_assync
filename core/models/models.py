from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Score(Base):
    __tablename__ = "scores"
    
    subject: Mapped[str]
    value: Mapped[float]
    student_id:Mapped[int]  = mapped_column(ForeignKey("students.id"))
    student = relationship("Student", back_populates="scores")


class Student(Base):
    __tablename__ = "students"
    
    name: Mapped[str]
    email: Mapped[str]
    scores: Mapped[float] = relationship("Score", back_populates="student", cascade="all, delete-orphan", )