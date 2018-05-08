import os
import sys

token = os.getenv("BOT_TOKEN")
reporting_channel = os.getenv("BOT_CHANNEL")

if not token:
    sys.stderr.write("No token specified. Please set the BOT_TOKEN environment variable.")
    sys.exit(1)
