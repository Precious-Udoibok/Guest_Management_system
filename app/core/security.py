import bcrypt
from typing import Any
from datetime import timedelta, datetime, timezone
from jose import jwt
import string
import secrets

ALGORITHM = "HS256"


def get_password_hash(password: str) -> str:
    """
    Hash a plaintext password using bcrypt.
    Returns:
        str: The securely hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify that a plain_password matches its hashed one.
    Returns: True if it does, else Return Flase
    """
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())


def create_access_token(
    subject: str | Any, secret_key: str, expiry_minutes: timedelta | int | None = 11520
):
    """
    Generate a signed JSON Web Token (JWT) for authentication.
    Returns: The JWT as a string
    """

    to_encode = {"sub": str(subject)}
    if expiry_minutes:
        if isinstance(expiry_minutes, int):
            expiry_minutes = timedelta(minutes=expiry_minutes)
        expire = datetime.now(timezone.utc) + expiry_minutes
        to_encode.update({"exp": expire})

    return jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)


def generate_random_password(length: int = 12) -> str:
    characters = string.ascii_letters + string.digits

    return "".join(secrets.choice(characters) for _ in range(length))
