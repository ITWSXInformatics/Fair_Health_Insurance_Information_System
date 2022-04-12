# After Initially Cloning:


### Install backend dependencies from project root:
```
cd backend
```
create a python virtual environment to install dependencies:
```
python3 -m virtualenv venv
```
activate the virtual environment:
```
source venv/bin/activate
```
install dependencies specified by requirements.txt
```
pip3 install -r requirements.txt
```
### Install frontend dependencies from project root:

```
cd frontend
```
Install javascript dependencies:
```
npm install
```
# Running the app:
Make sure you have the python virtual environment activated so the backend can access the required dependencies:
activate the virtual environment:
```
source venv/bin/activate
```

### Run backend from project root:
```
cd backend
python3 app/run_gunicorn.py --bind localhost:5000 wsgi:app --timeout 500
```
### Run frontend from project root:
```
cd frontend
npm run dev --host
```
To deactivate the virtual environment:
```
deactivate
```

