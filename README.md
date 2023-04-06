# flask_jwt

## Runing

env varibles:
 * `JWT_SECRET_KEY` - a secret key for verify JWT
 * `DATABASE_URI` - a database type

### Create VENV:
```bash
$ python3 -m venv
$ source env/bin/activate
```

### Installing requirements
```bash
$ pip3 install -r requirements.txt
```

### Database init
```bash
$ flask db init
$ flask db migrate
$ flask seed run
```

### Run server
```bash
$ python3 run.py
```


