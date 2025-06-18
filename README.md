# fastapi-be
## 1.Clone the repo
## 2. setup virtual environment 
python -m venv venv

## 3.Activate the virtual environment
source venv/bin/activate
## 4. install dependencies
pip install -r requirements.txt
## 5. run the server
uvicorn main:app --reload
## 6.swagger docs
http://127.0.0.1:8000/docs

