from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
wiki = Scraper()

@app.get("/")
async def read_item():
    return wiki.scrapdata()