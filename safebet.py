import uvicorn
from fastapi import FastAPI
from models.User import Base as UserBase
from models.Prediction import Base as PredictionBase
from models.RateLimit import Base as RateBase
from services.database import engine
from api.auth import AuthRouter
from api.root import RootRouter
from starlette.middleware.sessions import SessionMiddleware
app = FastAPI()

UserBase.metadata.create_all(bind=engine)
PredictionBase.metadata.create_all(bind=engine)
RateBase.metadata.create_all(bind=engine)

app.add_middleware(SessionMiddleware, secret_key="SECRET_KEY")
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(AuthRouter)
app.include_router(RootRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)