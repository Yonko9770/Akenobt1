# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/AsukaRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 14141732  # integer value, dont use ""
    API_HASH = "8fef4d9d2287f2e6ce63fdaaa7fbd0ba"
    ARQ_API_URL = "http://arq.hamker.dev"
    ARQ_API_KEY = "VVNCDW-NIBQUU-QKDTOM-JTRWBQ-ARQ"
    BOT_NAME = "𝓐𝓴𝓮𝓷𝓸"
    BOT_USERNAME = "akeno001bot"
    BOT_ID = "5597597776"
    TOKEN = "5597597776:AAGKXDhaXofFMNeK9qhXbs-lstp4U5SKCqw"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5700727404  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "YeahKakashi"
    SUPPORT_CHAT = "akeno001support"  # Your own group for support, do not add the @
    LOG_GROUP_ID = -1001791449328
    JOIN_LOGGER = (
        -1001791449328
    )  # Prints any new group the bot is added to, prints just the name and ID.
    ERROR_LOGS = (
        -1001791449328
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    EVENT_LOGS = -1001791449328
    LOG_GROUP_ID = ""
    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://npgdwozm:4Ced4mzwTADSPO8-2xQjx_d8DXD9d6g4@kashin.db.elephantsql.com/npgdwozm"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@akeno001support"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    OPENWEATHERMAP_ID = ""
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ERROR_LOGS = ""
    STRICT_GMUTE = True


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
