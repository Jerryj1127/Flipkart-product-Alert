import os

class Config(object):
    # get a token from @BotFather
    token = os.environ.get("token", "")
    # the page link for the specific FLIPKART product
    url = os.environ.get("url", "")
    # get the telegram user_ID from @ShowJsonBot
    tgm_userid = int(os.environ.get("tgm_userid", 12345))
    # The time for which the bot slepps after sending a message
    sleep_time = int(os.environ.get("sleep_time", 600))
    # The interval for checking flipkart
    refresh_rate = int(os.environ.get("refresh_rate", 30))

