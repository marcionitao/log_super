from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


# poetry run fastapi dev src/app.py
