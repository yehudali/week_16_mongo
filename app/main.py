from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from routes import router


app = FastAPI()
app.include_router(router=router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8888, host="127.0.0.1", reload=True)