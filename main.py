import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.models import Base, db_helper
from api import router as api_router
from core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print(f"CONN === {conn} + ")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=api_router, prefix=settings.api_prefix)

@app.get('/')
def read_root(name: str = "Luna-Corn"):
    name = name.strip().title()
    return  f"Hello {name}"


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)