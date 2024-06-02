from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Student, Score as ScoreModel
from .score_schemas import ScoreCreate, ScoreUpdate, Score as ScoreSchem



#Read all
async def get_scores(session: AsyncSession) -> list[ScoreModel]:
    lst_res = select(ScoreModel).order_by(ScoreModel.id)
    result: Result = await session.execute(lst_res)
    scores = result.scalars().all()

    return list(scores)

#Read one
async def get_score(session: AsyncSession, score_id: int) -> ScoreModel | None:
    return await session.get(ScoreModel, score_id)

#Create
async def create_score(session: AsyncSession, score_in: ScoreCreate) -> ScoreModel:
    #student = Student(**student_in.model_dump())
    score = ScoreModel(subject=score_in.subject, value=score_in.value, student_id=score_in.student_id)
    session.add(score)
    await session.commit()
    return score

#Delete
async def delete_score(
        session: AsyncSession,
        score: ScoreModel,
)-> None:
    await session.delete(score)
    await session.commit()

#Update put
async def update_score(
        session: AsyncSession, 
        score: ScoreModel, 
        score_update: ScoreUpdate,
        partial: bool = False
) -> ScoreModel:
    for subject, value in score_update.model_dump(exclude_unset=partial).items():
        setattr(score, subject, value)
    await session.commit()
    return score