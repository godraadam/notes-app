from fastapi import APIRouter

from app.api.routes import notes, tasks, users, auth

router = APIRouter()

router.include_router(notes.router, prefix="/notes")
router.include_router(tasks.router, prefix="/tasks")
router.include_router(users.router, prefix="/users")
router.include_router(auth.router, prefix="/auth")


