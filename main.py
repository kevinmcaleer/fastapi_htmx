from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/index/", response_class=HTMLResponse)
def index(request: Request, hx_request: Optional[str]= Header(None)):
    films = [
        {"name": "The Shawshank Redemption", "imdb": 9.2, "director": "Frank Darabont"},
        {"name": "The Godfather", "imdb": 9.1, "director": "Francis Ford Coppola"},
        {"name": "The Godfather: Part II", "imdb": 9.0, "director": "Francis Ford Coppola"},
        {"name": "The Dark Knight", "imdb": 9.0, "director": "Christopher Nolan"},
    ]
    context = {'request': request,
               'films': films}
    if hx_request:
        return templates.TemplateResponse("table.html", context)
    return templates.TemplateResponse("index.html", context)

                                      