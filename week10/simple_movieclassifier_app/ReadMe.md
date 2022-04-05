## 1. Add the pickle file to the project directory 
```
simple_movieclassifier_app/pkl_objects/model.pkl
```

## 2. Create Python Virtual Environment
```
python -m venv .
```
or
```
virtualenv .
```

## 3. Activate Virtual Enviromment
Linux
```
source bin/activate
```

Windows
```
source Scripts/activate
```

## 4. Install Dependencies 
```
pip install -r requirements.txt
```

## 5. Run the app  

- in Windows command prompt:
```
C:\path\to\app>set FLASK_ENV=development
flask run
```

- in Mac command line: 
```
export FLASK_ENV=development
flask run
```

## 6. Deactivate Virtual Environment 
```
deactivate 
```