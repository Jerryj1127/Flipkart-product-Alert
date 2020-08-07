import os

class Config(object):
    # get a token from @BotFather
    token = os.environ.get("Bot Token", "")
    # the page link for the specific FLIPKART product
    url = os.environ.get("Flipkart Product URL", "")
    # get the telegram user_ID from @ShowJsonBot
    tgm_userid = int(os.environ.get("User Id", 12345))
    # The time for which the bot slepps after sending a message
    sleep_time = int(os.environ.get("Sleep Time (sec)", 600))
    # The interval for checking flipkart
    refresh_rate = int(os.environ.get("Refresh Rate (sec)", 30))

