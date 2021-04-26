from typing import Optional
from fastapi import FastAPI, File, UploadFile
import json
from fastapi.responses import HTMLResponse
import uvicorn 

import pandas as pd
import numpy as np


app = FastAPI()

@app.get('/analisa')
def total_positif():
    df=pd.read_csv('data-rekap-kasus-covid19-per-kelurahan-di-provinsi-dki-jakarta-tanggal-25-maret-2020.csv')
    df['date']='25 Maret 2020'
    df_top10=df.groupby(['date','nama_provinsi','nama_kota','nama_kecamatan'])[['positif','sembuh','meninggal']].sum().reset_index()
    df_top10['Rank'] = df_top10['positif'].rank(method='dense', ascending=False)
    df_top10=df_top10.sort_values('Rank').head(11)
    df_dict=df_top10.to_dict(orient="records")
    result = df_dict
    return result




