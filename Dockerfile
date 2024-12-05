# This sets up the container with Python 3.10 installed.
FROM python:3.10-slim

# This sets the home/app directory as the working directory for any RUN, CMD, ENTRYPOINT, or COPY instructions that follow.
WORKDIR /home/app

# This copies everything in your current directory to the /app directory in the container.
COPY . .

# This command install and update packge essential in the container.
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common

# Install packge necessary for run dash    
RUN pip3 install -r requirements.txt

# Expose port 8501
EXPOSE 8501

# Tool check health of container
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# This command init container and run streamlit app
ENTRYPOINT ["streamlit", "run"]

# This command is the parameter for entrypoint
CMD ["home.py"]