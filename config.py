# Copyright (c) 2022 Itz-fork

import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 1293082))
    API_HASH = os.environ.get("API_HASH", "0b113c40038ed82cea13be3eeaa2b0e6")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6145911399:AAGbx91MAd_paiRd7BW_7hkm9v97n9D6Bws")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "705793735").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT") in ["True", "true"]
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL")) if os.environ.get("LOGS_CHANNEL") else None
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD")
