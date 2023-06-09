from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import datetime

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
async def index():
    return {"message": "Hello, world!"}

@app.get('/check_connection')
async def check_connection():
    return {"message": "API connection successful"}

@app.post('/index/obtener_numeros')
async def obtener_numeros(request: Request):
    data = await request.json()

    if 'numeros' in data:
        card_number = data['numeros']

        if len(card_number) >= 16 and len(card_number) <= 19:
            expiration_date = data['fecha']
            expiration_date_obj = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")  # Convertir a objeto de fecha

            if expiration_date_obj.date() >= datetime.date.today():
                cvv = data['cvv']

                is_amex = card_number.startswith("34") or card_number.startswith("37")

                if (is_amex and len(cvv) == 4) or (not is_amex and len(cvv) == 3):
                    return JSONResponse({'mensaje': 'correct  \u2705'}, status_code=status.HTTP_200_OK)

    return JSONResponse({'mensaje': 'incorrect'}, status_code=status.HTTP_400_BAD_REQUEST)

@app.options('/index/obtener_numeros')
async def obtener_numeros_options():
    allowed_methods = ["POST", "OPTIONS"]
    return JSONResponse({"allow": allowed_methods}, headers={"Access-Control-Allow-Methods": ",".join(allowed_methods)})
