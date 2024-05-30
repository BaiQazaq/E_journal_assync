from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from typing import Annotated

from .base import Base

class Score(Base):
    __tablename__ = "scores"
    
    subject = Column(String, index=True)
    value = Column(Float)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="scores")


class Student(Base):
    __tablename__ = "students"
    
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    scores = relationship("Score", back_populates="student", cascade="all, delete-orphan", )