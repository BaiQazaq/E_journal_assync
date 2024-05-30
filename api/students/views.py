from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from .schemas import Student
from core.models import db_helper

from .students_dep import student_by_id

router = APIRouter(tags=["Students"])


@router.get("/", response_model=list[Student])
async def get_students(
    session: AsyncSession = Depends(db_helper.get_scoped_session),
):
    return await crud.get_students(session=session)

@router.get("/{student_id}/", response_model=Student)
async def get_student(product: Student = Depends(student_by_id)):
    return product
