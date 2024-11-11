This is a simple REST API implementation using Flask that provides the following features:

## Endpoints

1. GET /: Returns a welcome message
2. GET /add-two/<number>: Adds 2 to the provided number
3. POST /multiply: Multiplies an array of numbers

## Setup

1. Install requirements:
   bash
   pip install -r requirements.txt


2. Run the application:
   bash
   python app.py


## Usage Examples

### GET endpoint
bash
curl http://localhost:8090/add-two/5


### POST endpoint
bash
curl -X POST -H "Content-Type: application/json" -d '{"numbers":[2,3,4]}' http://localhost:8090/multiply


## Note
The API runs on port 8090 by default. Change this in app.py to match your country's area code if needed.
