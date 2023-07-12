# pyapp

## Run

### Python
```shell
$ pip install pip --upgrade
$ pip install -r requirements.txt
$ uwsgi --http 0.0.0.0:3000 --wsgi-file app.py --callable app &
$ curl localhost:3000
```

### Docker
```shell
$ docker build -t dev-sareno/pyapp .
$ docker run dev-sareno/pyapp
```
