from fastapi import FastAPI
import util
# from app.routers import  playersname, predictruns, predictwickets

app = FastAPI()

# @app.get('/players')
# def getPlayers():``
#     return util.player_names


@app.get('/predict_runs')
def predict(Player:str, Avg: float, Bf: int, Str:float, Fours:int, Six:int):
    util.load_saved_artifacts()
    return util.estimated_run(Player,Avg,Bf,Str,Fours,Six)

