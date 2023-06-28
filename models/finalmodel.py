import pickle
import numpy as np
import joblib
from pathlib import Path


def model(contract_start, age, min, pts, fgm, fga, threePM, threePA, ftm, fta, reb, ast, tov, stl, blk, pf):
    HERE = Path(__file__).parent
    scaler = pickle.load(open(HERE / "scaler.pkl", "rb"))  # load scaler

    contract_start -= 2011
    feature_array = np.array([contract_start, age, min, pts, fgm, fga, threePM,
                             threePA, ftm, fta, reb, ast, tov, stl, blk, pf]).reshape(1, -1)
    feature_array = scaler.transform(feature_array)
    return feature_array.tolist()
