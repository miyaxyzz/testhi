# Base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot code
COPY bot.py .
COPY config.py .

# Run the bot
CMD ["python", "bot.py"]
