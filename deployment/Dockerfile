
FROM python:3.11
WORKDIR /app
COPY backend/ .
RUN pip install fastapi uvicorn pymongo python-jose stripe
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
