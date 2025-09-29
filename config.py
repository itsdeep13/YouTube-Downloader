import os

class Config:
    API_ID = int(os.getenv("API_ID","27473563" ))
    API_HASH = os.getenv("API_HASH", 'bc2ea0765ac96bb474891b0243f44390')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '7808765281:AAFXwNdJ1MySSFb3k9FJh6igON1twEQXhFo')
