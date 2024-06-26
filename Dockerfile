# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the current directory to the working directory in the container
COPY . .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make alembic command available
RUN echo "export PATH=$PATH:/root/.local/bin" >> /root/.bashrc

# Expose the port on which your Flask app will run (assuming it's 5000)
EXPOSE 5000

# Set the command to run your flask app
CMD ["python", "MainScores.py"]
