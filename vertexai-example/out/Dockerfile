# Start with the base image, which contains the Python interpreter and essential libraries
FROM python:3.9

# Install the application requirements
RUN pip install --user -r requirements.txt

# Set the working directory to the application source code directory
WORKDIR /usr/src/app

# Copy the application source code into the container
COPY . .

# Expose the port used by the application
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]