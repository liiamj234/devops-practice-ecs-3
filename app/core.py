from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "DevOps Practice App running"}

@router.get("/health")
def health():
    return {"status": "ok"}