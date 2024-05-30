from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Student


#Read all
async def get_students(session: AsyncSession) -> list[Student]:
    stmt = select(Student).order_by(Student.id)
    result: Result = await session.execute(stmt)
    students = result.scalars().all()

    return list(students)

#Read one
async def get_student(session: AsyncSession, student_id: int) -> Student | None:
    return await session.get(Student, student_id)