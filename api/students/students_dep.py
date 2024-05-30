from typing import Annotated
from fastapi import Path
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status, Depends
from core.models import db_helper, Student
from . import crud


async def student_by_id(
    student_id: Annotated[int, Path], 
    session: AsyncSession = Depends(db_helper.session_dependency),
)-> Student:
    student =  await crud.get_student(session=session, student_id=student_id)
    if student is not None:
        return student
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Stydent by id -> {student_id} not found",
    )