from pydantic import BaseModel, ConfigDict

from pydantic import BaseModel, ConfigDict


class Prediction(BaseModel):
    id:int
    username: str
    match_date: str
    prediction_date : str
    player1: str
    player2: str
    tournament: str
    player1odds: float
    player2odds: float
    n_sets: int
    t_round: str
    predicted_winner: str
    stake: float