# Use the official Python image as the base image
FROM python:3.10.6

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code into the container
COPY . /app/

# Expose the port that the app will run on
EXPOSE 5000

# Start the Gradio app when the container starts
ENTRYPOINT python app.py
