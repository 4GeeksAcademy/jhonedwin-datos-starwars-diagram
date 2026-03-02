from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional


db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Users(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    last_name: Mapped[str] = mapped_column( String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    suscription_day: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="users")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


# Tabla Planets:

class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    rotation_period: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    orbital_period: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    climate: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    population: Mapped[str] = mapped_column(nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="planets")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


# Tabla Characters:

class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    type: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    race: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    height: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="characters")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


# Tabla Favorites:

class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    # FK hacia Users (hijo de Users)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)

    # FK hacia Planets (hijo de Planets)
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planets.id"),nullable=False)
    chracters_id: Mapped[Optional[int]] = mapped_column(ForeignKey("characters.id"),nullable=False)

    # RELACIONES
    user: Mapped["Users"] = relationship(back_populates="favorites")

    planet: Mapped[Optional["Planets"]] = relationship(back_populates="favorites")

    characters: Mapped[Optional["Characters"]] = relationship(back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }    