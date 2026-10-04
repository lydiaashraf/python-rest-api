from fastapi import FastAPI
#bn3ml import l fastapi mn fastapi library

from app.routes import router
#bn3ml import ll router eli fih api endpoints bat3tna mn app.routes
#faslna el routes fi file lw7do 3lshan nnazm el application

app = FastAPI()
#Fastapi by3ml object gdid mn Fastapi class w bn5zno fi variable gdid esmo app
#w b3din uvicorn y2ol ah el application bta3k mawgod fi app 5las ha apply 3lih 3lshan keda bnktb main:app
#main asdo b main.py w app el fastapi application el magod fi el file

app.include_router(router)
#bndif el routes eli mawgoda fi el router ll fastapi application
#Men gheir el satr da, el endpoints el mawgooda fe routes.py mesh hatkoon mota7a.