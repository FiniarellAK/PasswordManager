from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from db.objects import BaseModel


class UsersModel(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(40))
    hashed_password: Mapped[str] = mapped_column(String(50))
    hashed_master_password: Mapped[str] = mapped_column(String(50))
    user_password = relationship("user_password")


class PasswordEntryModel(BaseModel):
    __tablename__ = "password_entry"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(50))
    service_name: Mapped[str] = mapped_column(String(50))
    user_password = relationship("user_password")


class UserPasswordModel(BaseModel):
    __tablename__ = "user_password"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    password_entry_id: Mapped[int] = mapped_column(ForeignKey("password_entry.id"))
    is_owner: Mapped[bool]
