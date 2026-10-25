FROM python:3.9-slim

WORKDIR /app

# Copy the backend code, requirements, and the serialized best model
COPY app.py requirements.txt best_model.pkl /app/

# Install the necessary python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 8000 for Flask
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
