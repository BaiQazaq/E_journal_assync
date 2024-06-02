from typing import Annotated
from fastapi import Path
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status, Depends
from core.models import db_helper, Score
from . import score_crud


async def score_by_id(
    score_id: Annotated[int, Path], 
    session: AsyncSession = Depends(db_helper.session_dependency),
)-> Score:
    score =  await score_crud.get_score(session=session, score_id=score_id)
    if score is not None:
        return score
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Score by id -> {score_id} not found",
    )