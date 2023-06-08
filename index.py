from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import datetime

app = FastAPI()

@app.get('/')
async def index():
    return {"message": "Hello, world!"}

@app.post('/index/obtener_numeros')
async def obtener_numeros(request: Request):
    data = await request.json()

    if 'numeros' in data:
        card_number = data['numeros']

        if len(card_number) >= 16 and len(card_number) <= 19:
            expiration_date = data['fecha']

            if expiration_date >= datetime.date.today().isoformat():
                cvv = data['cvv']

                is_amex = card_number.startswith("34") or card_number.startswith("37")

                if (is_amex and len(cvv) == 4) or (not is_amex and len(cvv) == 3):
                    return JSONResponse({'mensaje': 'correcto'})

    return JSONResponse({'mensaje': 'incorrecto'})

