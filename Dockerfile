# Dockerfile for book_catalog microservice

# Uses official Python image as container base
FROM python:3.9.19-slim

# Sets book_catalog folder as working directory
WORKDIR /book_catalog

# Copy the requirements file to the working directory
COPY ./book_catalog/requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copies everything into working directory from ./book_catalog folder
COPY ./book_catalog .

# Expose the port on which the application will run
EXPOSE 4001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4001"]