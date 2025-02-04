from fastapi import FastAPI
from app.routes import router  # Importing routes

# Initialize FastAPI app
app = FastAPI(title="DeepMind API", description="AI service to answer Religion related question with the science aspect")

# Include routes
app.include_router(router)
