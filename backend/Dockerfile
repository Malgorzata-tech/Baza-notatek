# Slim Python image for a smaller footprint
FROM python:3.12-slim 

WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]