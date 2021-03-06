import logging
from sklearn import model_selection

import uvicorn
from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware
from autocorrection.correct import AutoCorrection
from config.config import get_config

config_app = get_config()

logging.basicConfig(filename=config_app['log']['app'],
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

description = """
# Vietnamese Spelling Correction
"""

app = FastAPI(
    title="Spell Correction",
    description=description,
    version="0.0.1"
)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

autocorrection = AutoCorrection(threshold_correction=0.5)

@app.post("/correct")
async def correct_sentence(request: Request):
    data = await request.json()
    
    data = dict(data)
    print(data)
    sent = data["text"]
    mode = data["model"]
    p_ins = data["insertPenalty"]
    p_del = data["deletePenalty"]

    try:
        corrected, align = autocorrection.correct(sent, mode, p_ins, p_del)
    except Exception as e:
        corrected = sent
        align = []
        logging.warning(e)
        
    return {
        "result": {
            "text": corrected,
            "align": align
        }
    }


if __name__ == "__main__":  
    uvicorn.run(
        app, 
        host=config_app['server']['ip_address'], 
        port=config_app['server']['port']
    )
    # uvicorn.run(app, host="0.0.0.0", port=8000)