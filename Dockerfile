# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY alembic.ini .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME WorldOfGamesBonus

# Run alembic upgrade head on container startup
CMD ["alembic", "upgrade", "head"]
