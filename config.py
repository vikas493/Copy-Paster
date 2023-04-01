import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "5603607413:AAF9jqPDuGeMBcdlhxhV6RLyJyGmFGrPaL8"
    APP_ID = 7664661
    API_HASH = "9917a213ffbf087c7d98955bef592e75"
    TG_USER_SESSION = "AQB09BUAgbbVoR1QdPFpnYWuakcX6u-FnT69sNF4FmcWAjxh5lefKLu0Bi9seYqAq145dgA8dL27zhVUNTwrhBfTymHXjA4s-PeP6QweoGVmgU6SXz3RMV1ppI_NJppyOohEk0zc2lWIL7fmRYlTY1Rka7GMMo2qqEp0M_UA6PI7Wa6hrNpZScKouOqKhJqwGa9AA3LVgMdqgyvNQNykvn_uLVHzEtrL80F5ovxi6W0uq0gQBNJLt-cRUSCVXToz0KuHhx3FfeJtYbtmuJH0tQQzSKt1pZ5qRtZyx5Ku-7N3LxM66qx-STHWng9KaF5NOzXIjkZViejtOJVRS2_uFYMdZGAQ9gAAAABrBYsvAA"
    DB_URI = "postgres://rkynohls:xHZVYqtUEaLfKqscSHd6ENpb84bHP24g@kashin.db.elephantsql.com/rkynohls"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
