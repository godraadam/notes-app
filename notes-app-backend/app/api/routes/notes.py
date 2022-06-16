from fastapi import APIRouter


router = APIRouter()


@router.get("/{username}")
def get_notes_of_user(username: str):
    return ["My first note", "My second note"]