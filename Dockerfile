FROM python:3.11
WORKDIR /app
COPY requirement.txt . 
RUN pip install --default-timeout=200 --no-cache-dir -r requirement.txt

COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]