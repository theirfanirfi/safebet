from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float

from services.database import Base


class RateLimit(Base):
    __tablename__ = "rate_limits"
    id = Column(Integer, primary_key=True)
    ip_address = Column(String, nullable=False, unique=True)
    request_count = Column(Integer, default=0)
    reset_time = Column(DateTime, nullable=False)