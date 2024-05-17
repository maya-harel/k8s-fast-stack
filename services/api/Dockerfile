FROM python:3.10.10-buster

# set the working directory to src
WORKDIR /src

# copy the requirements file and install
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r requirements.txt

# copy the rest of the app
COPY . /src

CMD ["python3", "main.py"]
