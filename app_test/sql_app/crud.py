from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

# ユーザー一覧


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# 会議室一覧


def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit).all()

# 予約一覧


def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User):
    # インスタンスを作成
    db_user = models.User(username=user.username)
    # 登録する
    db.add(db_user)
    db.commit()
    # もろもろリフレッシュ(セッション情報など)
    db.refresh(db_user)
    return db_user


def create_room(db: Session, room: schemas.Room):
    # インスタンスを作成
    db_room = models.Room(room_name=room.room_name, capacity=room.capacity)
    # 登録する
    db.add(db_room)
    db.commit()
    # もろもろリフレッシュ(セッション情報など)
    db.refresh(db_room)
    return db_room


def create_booking(db: Session, booking: schemas.Booking):
    # 重複チェック

    db_booked = db.query(models.Booking).\
    filter(models.Booking.booking_id == booking.booking_id ).\
    filter(models.Booking.end_datetime >  booking.start_datetime ).\
    filter(models.Booking.start_datetime == booking.end_datetime ).\
    all()

    if len(db_booked) == 0:
    # インスタンスを作成
        db_booking = models.Booking(
            user_id=booking.user_id,
            room_id=booking.room_id,
            booked_num=booking.booked_num,
            start_datetime=booking.start_datetime,
            end_datetime=booking.end_datetime
        )
        # 登録する
        db.add(db_booking)
        db.commit()
        # もろもろリフレッシュ(セッション情報など)
        db.refresh(db_booking)
        return db_booking
    else:
        raise HTTPException(status_code=404, detail="すでに予約されています")
