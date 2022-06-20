from fastapi import APIRouter

from app.api.routes import notes, tasks, users, auth

router = APIRouter()

router.include_router(notes.router, prefix="/note")
router.include_router(tasks.router, prefix="/task")
router.include_router(users.router, prefix="/user")
router.include_router(auth.router, prefix="/auth")


