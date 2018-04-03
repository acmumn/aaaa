FROM python:3

# Create bot directory
RUN mkdir /bot
WORKDIR /bot

# Install requirements
ADD requirements.txt /bot
RUN pip3 install -r /bot/requirements.txt

# Add required files
ADD config.py /bot
ADD script.py /bot

# Start the bot
CMD ["python3", "/bot/script.py"]
