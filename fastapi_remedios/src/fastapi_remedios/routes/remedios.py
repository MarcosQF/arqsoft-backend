from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_remedios import models, schemas
from fastapi_remedios.database import SessionLocal

router = APIRouter(prefix="/remedios", tags=["Remedios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.RemedioOut)
def create_remedio(remedio: schemas.RemedioCreate, db: Session = Depends(get_db)):
    db_remedio = models.Remedio(**remedio.dict())
    db.add(db_remedio)
    db.commit()
    db.refresh(db_remedio)
    return db_remedio

@router.get("/", response_model=list[schemas.RemedioOut])
def read_remedios(db: Session = Depends(get_db)):
    return db.query(models.Remedio).all()

@router.get("/{remedio_id}", response_model=schemas.RemedioOut)
def read_remedio(remedio_id: int, db: Session = Depends(get_db)):
    remedio = db.query(models.Remedio).filter(models.Remedio.id == remedio_id).first()
    if not remedio:
        raise HTTPException(status_code=404, detail="Remédio não encontrado")
    return remedio

@router.put("/{remedio_id}", response_model=schemas.RemedioOut)
def update_remedio(remedio_id: int, update_data: schemas.RemedioUpdate, db: Session = Depends(get_db)):
    remedio = db.query(models.Remedio).filter(models.Remedio.id == remedio_id).first()
    if not remedio:
        raise HTTPException(status_code=404, detail="Remédio não encontrado")
    for key, value in update_data.dict().items():
        setattr(remedio, key, value)
    db.commit()
    db.refresh(remedio)
    return remedio

@router.delete("/{remedio_id}")
def delete_remedio(remedio_id: int, db: Session = Depends(get_db)):
    remedio = db.query(models.Remedio).filter(models.Remedio.id == remedio_id).first()
    if not remedio:
        raise HTTPException(status_code=404, detail="Remédio não encontrado")
    db.delete(remedio)
    db.commit()
    return {"ok": True, "message": "Remédio deletado"}
