# Use a base image with Python and Conda pre-installed
FROM continuumio/miniconda3

# Set a working directory in the container
WORKDIR /app

# Copy the entire project folder to the container
COPY . /app

# Create a Conda environment based on the environment.yml file
RUN conda env create -f environment.yml

# Activate the Conda environment
SHELL ["conda", "run", "-n", "motionformer", "/bin/bash", "-c"]

# Command to train your model or any necessary script
# CMD ["python", "tools/run_net.py"]
