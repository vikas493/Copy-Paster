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
    APP_ID = 16193102
    API_HASH = "75eadea6904c83b9be6f2114bd45f6ff"
    TG_USER_SESSION = "1AZWarzwBu5Z8TL3oL_UGr8K7JbbYsuhgU36J-RJDy9MQkz2v2Ikkh3GswmyUeCYPGMxO6BSetabisEBnr7Oy3pbwvKvBeK0-MZKC6zZcUKzSIL8D8yPhAvw9_UT0yNI-dTta6r_OA_0Pn_dhtQjsVLXv6K8yoUig1KXRHbQXvClkYt7prQVixLTHIOm42rEiPQTS2T2CciP0CLkolvEHU9nW-847_b6FikbwbyhtgqfKH3BB4CX1V1Vp2SGMwO5QeqkEK5ltWavyFd06nYheL5bjlcNJtprKD-lVxsz2FV802MmzgSiTJzn-QjxSRsJNm2PR-5-Qrj2RZz-2XXFDtm4iC6E8o10="
    DB_URI = "postgres://rkynohls:xHZVYqtUEaLfKqscSHd6ENpb84bHP24g@kashin.db.elephantsql.com/rkynohls"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
