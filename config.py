import os
import sys
import json

token = os.getenv("BOT_TOKEN")
log_channels = json.loads(os.getenv("BOT_CHANNELS", "{}"))

if not token:
    sys.stderr.write("No token specified. Please set the BOT_TOKEN environment variable.")
    sys.exit(1)
