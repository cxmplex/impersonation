ROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

COPY . /usr/src/app

# install requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available
EXPOSE 8080

# Define environment variable
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:8080 --config gunicorn_config.py"

# Run main.py when the container launches using gunicorn
CMD ["gunicorn", "main:app"]