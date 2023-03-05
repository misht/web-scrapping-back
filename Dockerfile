# Defines a base for our image
FROM python:3.9-alpine

# Sets the working directory for instructions (ADD, COPY, CMD, RUN and ENTRYPOINT)
WORKDIR /usr/src/app

# Executes the commands in a new layer on top of the current image and commits the result.
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all the files to the container
COPY . .

# Expose the app in the port 5000
EXPOSE 5000

# Define the program that is run once the container is started.
# --Host is used to enable the server in public mode
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]

# To execute: (You should be inside web-scrapping-back directory)
# docker build --tag web-scrapping-back .
# docker run -p 5000:5000 web-scrapping-back