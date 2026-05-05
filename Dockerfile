FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appgroup . .

USER appuser

EXPOSE 5000

CMD ["python", "main.py"]