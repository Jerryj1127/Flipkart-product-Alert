#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import os

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from flipkart.sample_config import Config
else:
    from flipkart.config import Config


# TODO: is there a better way?
token = Config.token
url = Config.url
tgm_userid = Config.tgm_userid
sleep_time = Config.sleep_time
refresh_rate = Config.refresh_rate
