from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from schemas.userschema import ForgotPassword, ResetPassword, User as UserSchema, UserLogin
from sqlalchemy.orm import Session
from services.database import get_db
from models.User import User
from sqlalchemy import or_
from jose import JWTError, jwt
from passlib.context import CryptContext
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import bcrypt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


OUTLOOK_SMTP_SERVER = "smtp.gmail.com"
OUTLOOK_SMTP_PORT = 587  # or 25 if TLS is not used
OUTLOOK_EMAIL = "theirfi@gmail.com"
OUTLOOK_PASSWORD = "Irfan0001"

CONFIRMATION_URL = "https://127.0.0.1:8000/api/auth/confirmation"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# # Hash a password using bcrypt
# def get_password_hash(password):
#     pwd_bytes = password.encode('utf-8')
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
#     return hashed_password

# # Check if the provided password matches the stored password (hashed)
# def verify_password(plain_password, hashed_password):
#     password_byte_enc = plain_password.encode('utf-8')
#     return bcrypt.checkpw(password = password_byte_enc , hashed_password = hashed_password)

AuthRouter = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

db_dependency = Annotated[Session, Depends(get_db)]
@AuthRouter.post("/sign-up")
def signup(user: UserSchema, db: db_dependency):
    if db.query(User).filter(or_(User.username == user.username, User.email == user.email)).first():
            return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )
    # Create the new user
    try:
        new_user = User(username=user.username, email=user.email, hashed_password=get_password_hash(user.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        if send_email(new_user):
            return {'status': True, 'token': create_token(new_user)}
        return {'status': True, 'token': create_token(new_user), 'message': 'email could not be sent'}
    except Exception as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Username or email already registered"
        )


def get_user(db, user: UserLogin):
    return db.query(User).filter(or_(User.username == user.email, User.email == user.email)).first()

def create_token(dbuser):
    return jwt.encode({'id': dbuser.id, 'username': dbuser.username}, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload

def generate_confirmation_token(cuser):
    return jwt.encode({'id': cuser.id, 'username': cuser.username, 'email': cuser.email }, SECRET_KEY, algorithm=ALGORITHM)

def decode_confirmation_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

@AuthRouter.post("/login")
def login(user: UserLogin, db: db_dependency):
    dbuser = get_user(db, user)
    
    if dbuser:
        if not verify_password(user.password, dbuser.hashed_password):
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        if not dbuser.email_confirmed:
            send_email(dbuser)
        
        encoded_jwt = create_token(dbuser)
        return {'status': True, 'token': encoded_jwt}
    
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

@AuthRouter.get("/me")
def read_users_me(
    current_user: Annotated[str, Depends(get_current_user)],
):
    return current_user

def send_email(user, body="Please click the following link to confirm your email:", confirmation_link="confirmation"):
    # Get the user from the database by email
    # Generate confirmation token (You need to implement this part)
    # token = generate_confirmation_token(user.email)

    # Create confirmation link
    confirmation_link_formated = "https://127.0.0.1:8000/api/auth/"+confirmation_link+"?token="+generate_confirmation_token(user)

    # Email content
    subject = "Confirm your email"
    body = body+" "+confirmation_link_formated

    # Create MIME object
    msg = MIMEMultipart()
    msg['From'] = OUTLOOK_EMAIL
    msg['To'] = user.email
    msg['Subject'] = subject

    # Attach body to the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Outlook's SMTP server
        server = smtplib.SMTP(OUTLOOK_SMTP_SERVER, OUTLOOK_SMTP_PORT)
        server.starttls()  # Enable TLS
        server.login(OUTLOOK_EMAIL, OUTLOOK_PASSWORD)

        # Send email
        server.sendmail(OUTLOOK_EMAIL, user.email, msg.as_string())
        server.quit()

        return True
    except Exception as e:
        print(str(e))
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send email"
        )

@AuthRouter.get("/confirm_email")
def confirm_email(token: str, db:db_dependency):
    decoded_user = decode_confirmation_token(token)
    if not decoded_user:
        return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token provided",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    dbuser = db.query(User).filter(or_(User.username == decoded_user['username'], User.email == decoded_user['username'])).first()
    if not dbuser:
        return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token provided",
                headers={"WWW-Authenticate": "Bearer"},
            )
    print(dbuser.username)
    dbuser.email_confirmed = True
    db.commit()
    db.refresh(dbuser)
    return {"status": True, "user": dbuser}


@AuthRouter.get("/forgot_password")
def forgot_password(fp: ForgotPassword, db:db_dependency):
    dbuser = db.query(User).filter(or_(User.username == fp.email, User.email == fp.email)).first()
    if not dbuser:
        return {"status": True, "message": "A password reset link is sent to the email"}
    
    send_email(dbuser,body="Click on the link to reset your password ", confirmation_link="reset_password")
    return {"status": True, "message": "A password reset link is sent to the email"}


@AuthRouter.post("/reset_password")
def confirm_email(token: str, rp: ResetPassword, db:db_dependency):
    decoded_user = decode_confirmation_token(token)
    if not decoded_user:
        return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token provided",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    dbuser = db.query(User).filter(or_(User.username == decoded_user['username'], User.email == decoded_user['username'])).first()
    if not dbuser:
        return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token provided",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
    if not rp.new_password == rp.confirm_password:
        return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Password mismatch",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    print(dbuser.username)
    dbuser.hashed_password = get_password_hash(rp.new_password)
    db.commit()
    db.refresh(dbuser)
    return {"status": True, "user": dbuser}