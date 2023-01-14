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
    TG_USER_SESSION = "AQD3Fk4AqmRPuc_WDHMuNd-QGtpeaQQlksaqK9TC5yM5nJgfuvy8aXji9DfU6UaVZJtqgDPliVNZi_venQBcfFWxiSttm-58oboNtG-remFyB9O5lWPDqGjIN24uyM_xeGiBmi-8sImzdCKiB-KMc2j37hc5UM1CUHBm5-3I8yUaayt_ULTT8kXVR2uc0L9zN_ynIRntRXRifZwvDjrtNjHGAd5Ed1lUUDpOT3vvjfdODaVpeNjHlzcI2Fspz4QT7EtujeZWZDO2Kx2AeuH6ABSAiGDK5QTQl2etfZrWUpjM8LD0GWZ3Xg4XJ1of25I0hqUkZd7GGvKgjhCAqDjgWQKDO7ObjAAAAABqqqKMAA"
    DB_URI = "postgres://axqblmkb:XcuBrZsUKelKADBYwoV6EF-pwOH11-Xl@snuffleupagus.db.elephantsql.com/axqblmkb"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
