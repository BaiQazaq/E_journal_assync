from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Student
from .schemas import StudentCreate



#Read all
async def get_students(session: AsyncSession) -> list[Student]:
    lst_res = select(Student).order_by(Student.id)
    result: Result = await session.execute(lst_res)
    students = result.scalars().all()

    return list(students)

#Read one
async def get_student(session: AsyncSession, student_id: int) -> Student | None:
    return await session.get(Student, student_id)

#Create
async def create_student(session: AsyncSession, student_in: StudentCreate) -> Student:
    #student = Student(**student_in.model_dump())
    student = Student(name=student_in.name, email=student_in.email)
    session.add(student)
    await session.commit()
    return student