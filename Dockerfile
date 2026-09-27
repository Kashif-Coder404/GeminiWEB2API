FROM python:3.12-slim

WORKDIR /app

# 1. Force real-time logs in 'docker logs' (no 4KB buffer delay)
ENV PYTHONUNBUFFERED=1
ENV PORT=8081

# 2. Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy application files
COPY gemini_web2api.py ./
COPY gemini_web2api/ ./gemini_web2api/
COPY config.example.json ./config.example.json

EXPOSE 8081

# 4. Start with the updated runner supporting .env, env vars, and config files
CMD ["python", "gemini_web2api.py"]
