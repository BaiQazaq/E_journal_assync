from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from . import score_crud
from .score_schemas import Score as ScoreSchema, ScoreCreate, ScoreUpdate
from core.models import db_helper, Student as Student_model

from .score_dep import score_by_id

router = APIRouter(tags=["Scores"])

#ALL scores
@router.get("/", response_model=list[ScoreSchema])
async def get_scores(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await score_crud.get_scores(session=session)

#One score
@router.get("/{score_id}/", response_model=ScoreSchema)
async def get_score(score: ScoreSchema = Depends(score_by_id)):
    return score

#Create score
@router.post(
        "/", 
        response_model=ScoreSchema, 
        status_code=status.HTTP_201_CREATED,
        )
async def create_student(
    score_in: ScoreCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await score_crud.create_score(session=session, score_in=score_in)

#Delete
@router.delete(
    "/{score_id}/", 
    status_code=status.HTTP_204_NO_CONTENT,
    )
async def delete_score(
    score: ScoreSchema = Depends(score_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
)-> None:
    await score_crud.delete_score(session=session, score=score)


#Update put
@router.put("/{score_id}/")
async def update_score(
    score_update: ScoreUpdate,
    score: ScoreSchema = Depends(score_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await score_crud.update_score(
        session=session,
        score=score,
        score_update=score_update,
    )
