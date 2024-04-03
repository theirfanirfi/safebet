from sqlalchemy import Column, Integer, String, Boolean, DateTime

from services.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username= Column(String, index=True, unique=True)
    email = Column(String, index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email_confirmed = Column(Boolean, default=False)

    hashed_password = Column(String)

    # admin priviledges
    is_user_admin = Column(Boolean, default=False) # Can modify user settings
    is_supervisor_admin = Column(Boolean, default=False) # Can modify user settings and user admin settings

    is_owner_admin = Column(Boolean, default=False) # Highest Access Level


    # safeBet pro
    is_pro_member = Column(Boolean, default=False)
    #pro_member_since = Column(DateTime)
    #pro_member_until = Column(DateTime)

    # stripe details
    stripe_customer_id = Column(String)
    stripe_customer_name = Column(String)
    stripe_customer_email = Column(String)
    stripe_customer_start = Column(DateTime)
    stripe_customer_expiry = Column(DateTime)