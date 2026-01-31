from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
      <head><title>KDE Cash</title></head>
      <body>
        <h1>App carregado com sucesso 🚀</h1>
      </body>
    </html>
    """

