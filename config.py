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
    TG_USER_SESSION = "AQD3Fk4AgomkDAAyjsMf4GoN6LqeMqit9hvWvsag8Yr2Hynp2f4yj7HeIaRiuBZR2-xfwMOQAeJXvkkJw_WV_49m9J2w1m5papVjSWgt8KEMVtycyeBwVqxQDa-C-A9m4Ugx53cJavIv5LuBa3pavHvJ5ep6nLRqYP_yn-WVSz_-fZJc0hl9E3ID-fRcuZG_JCSpJlX0kMVRg3nT1wOHF1OwdIkDaF8iTyTmHJANSrpIFabk1FRGKIJ36VxRu-cPM3WFXVl9vPrxqWmp8WSe5_XV9ag4-FKCYeFwfH4RV6QQxrDB8mog9Lx4u_r_fnUDSybpU2cPcztygC9xhUUhRpqSbota6QAAAABqqqKMAA"
    DB_URI = "postgres://rkynohls:xHZVYqtUEaLfKqscSHd6ENpb84bHP24g@kashin.db.elephantsql.com/rkynohls"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
