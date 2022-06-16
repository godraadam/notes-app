from fastapi import APIRouter

from app.api.routes import notes, tasks

router = APIRouter()

router.include_router(notes.router, prefix="/notes")
router.include_router(tasks.router, prefix="/tasks")


