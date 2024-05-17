This is a README for a basic FastAPI server that will be deployed as part of a Kubernetes Cluster

## FastAPI Server

### Prerequisites
- Python3.10
- Pip3 

To install the dependencies run `pip3 install -r requirements.txt`

To run the server locally `python3 main.py`

#### To run with docker
```
docker build -t fastapi-server .
docker run -p 8082:8082 fastapi-server
```
(To run this in the background add the -d flag)
