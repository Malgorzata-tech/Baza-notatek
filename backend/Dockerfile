FROM python:3.12-slim # Use a slim Python image for a smaller footprint

WORKDIR /app

COPY requirements.txt .  # Copy the requirements file to the working directory
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]