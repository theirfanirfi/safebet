from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from api.auth import get_current_user
from schemas.predictionchema import Prediction as PredictionSchema
from schemas.userschema import ForgotPassword, ResetPassword, User as UserSchema, UserLogin
from sqlalchemy.orm import Session
from services.database import get_db
from models.User import User
from models.Prediction import Prediction
from sqlalchemy import or_
import joblib 
from machinelearningmodel.machinelearning import predict

RootRouter = APIRouter(
    prefix="/api",
    tags=[""],
    responses={404: {"description": "Not found"}},
)

db_dependency = Annotated[Session, Depends(get_db)]

@RootRouter.get('/')
def about(request: Request, db: db_dependency, current_user: Annotated[str, Depends(get_current_user)]):
    print(current_user)
    # request.session['username']= "theirfanirfi"
    # username = request.session['username']
    user = db.query(User).filter_by(username="theirfanirfi").first()
    token = "YES"
    return {"status": True, "token": token}

@RootRouter.post('/add_prediction')
def add_prediction(prediction: PredictionSchema, db: db_dependency, current_user: Annotated[str, Depends(get_current_user)]):
    print(current_user['username'])
        # Create the new user
    try:
        new_prediction = Prediction(username=current_user['username'],
                              match_date=prediction.match_date,prediction_date=prediction.prediction_date,
                              player1=prediction.player1, player2=prediction.player2, 
                              tournament=prediction.tournament,player1odds=prediction.player1odds,
                              player2odds=prediction.player2odds,n_sets=prediction.n_sets,
                              t_round=prediction.t_round,predicted_winner=prediction.predicted_winner,
                              stake=prediction.stake)
        db.add(new_prediction)
        db.commit()
        db.refresh(new_prediction)
        return {'status': True, 'prediction':new_prediction, 'message': 'Prediction added successfully'}
    except Exception as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="error while adding prediction"
        )


@RootRouter.post('/prediction')
def prediction(prediction: PredictionSchema, db: db_dependency, current_user: Annotated[str, Depends(get_current_user)]):
    print(current_user['username'])
    # ml_model = joblib.load('./machinelearningmodel/ml.pkl')
    # output = ml_model.predict([[128, 536, 40, 7]])[0]
    output = predict(prediction.player1, prediction.player2, prediction.tournament, prediction.t_round)
    print(output)
    if output == 0:
        player_win = "Player 1"
    else:
        player_win = "Player 2"
        
    return {"status": True, "message": str(output),
            "prediction": str(output),
            "player_win_prediction": player_win }
    