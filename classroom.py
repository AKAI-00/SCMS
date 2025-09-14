from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import models, database
from schemas import AttendanceBase, AttendanceResponse
from typing import List

router = APIRouter()

@router.post("/attendance", response_model=AttendanceResponse)
def mark_attendance(record: AttendanceBase, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == record.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_record = models.Attendance(user_id=record.user_id, present=record.present)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get("/attendance", response_model=List[AttendanceResponse])
def get_attendance(db: Session = Depends(database.get_db)):
    return db.query(models.Attendance).all()