import json
from typing import Union
from fastapi import FastAPI
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
from ProdidgyPython import getClient

app = FastAPI()


# print(getClient())
# data = pd.read_csv('CentralFile.csv')
# sns.displot(data=data, x=)

@app.get("/")
def read_root():
    return getClient()
