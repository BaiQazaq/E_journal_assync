from fastapi import APIRouter

from .students.views import router as students_router
from .scores.score_views import router as scores_router

student_router = APIRouter()
student_router.include_router(router=students_router, prefix="/students")

score_router = APIRouter()
score_router.include_router(router=scores_router, prefix="/scores")

