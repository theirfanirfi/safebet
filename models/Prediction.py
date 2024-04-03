from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float

from services.database import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    match_date = Column(String)
    prediction_date = Column(String)
    player1 = Column(String)
    player2 = Column(String)
    tournament = Column(String)
    player1odds = Column(Float)
    player2odds = Column(Float)
    n_sets = Column(Integer)
    t_round = Column(String)
    predicted_winner = Column(String)
    stake = Column(Float)