from os import environ

API_ID = int(environ.get("API_ID", "28814392"))
API_HASH = environ.get("API_HASH", "38d09c28822aa20a56c43c4b492efba6")
BOT_TOKEN = environ.get("BOT_TOKEN", "8039713186:AAGM11MHwlc1KqykmPIYHqjyVaMo68ZwqDw")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002419214262"))
ADMINS = int(environ.get("ADMINS", "7228509851"))
DB_URI = environ.get("DB_URI", "mongodb+srv://ramsaranhero1:EMVwKybGR1lBF5DZ@cluster0.tst47tx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "ramsaranhero1")
