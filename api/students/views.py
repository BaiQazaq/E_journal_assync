from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from . import crud
from .schemas import Student as StudentSchema, StudentCreate, StudentUpdate, StudentUpdateePartial
from core.models import db_helper, Student as Student_model

from .students_dep import student_by_id

router = APIRouter(tags=["Students"])

#ALL students
@router.get("/", response_model=list[StudentSchema])
async def get_students(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_students(session=session)

#One student
@router.get("/{student_id}/", response_model=StudentSchema)
async def get_student(student: StudentSchema = Depends(student_by_id)):
    return student

#Create student
@router.post(
        "/", 
        response_model=StudentSchema, 
        status_code=status.HTTP_201_CREATED,
        )
async def create_student(
    student_in: StudentCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_student(session=session, student_in=student_in)

#Delete
@router.delete(
    "/{student_id}/", 
    status_code=status.HTTP_204_NO_CONTENT,
    )
async def delete_product(
    student: StudentSchema = Depends(student_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
)-> None:
    await crud.delete_student(session=session, student=student)


#Update put
@router.put("/{student_id}/")
async def update_product(
    student_update: StudentUpdate,
    student: StudentSchema = Depends(student_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_student(
        session=session,
        student=student,
        student_update=student_update,
    )

#Update patch
@router.patch("/{student_id}/")
async def update_product(
    student_update: StudentUpdateePartial,
    student: StudentSchema = Depends(student_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_student(
        session=session,
        student=student,
        student_update=student_update,
        partial=True,
    )