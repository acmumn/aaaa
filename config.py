import os
import sys

token = os.getenv("BOT_TOKEN")
log_channels = eval(os.getenv("BOT_CHANNELS", "{}"))

if not token:
    sys.stderr.write("No token specified. Please set the BOT_TOKEN environment variable.")
    sys.exit(1)
