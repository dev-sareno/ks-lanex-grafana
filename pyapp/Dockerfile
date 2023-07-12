FROM python:3.11.4-bullseye
EXPOSE 8001
EXPOSE 9090
WORKDIR /app
COPY . .
RUN pip install pip --upgrade
RUN pip install -r requirements.txt
CMD ["uwsgi", "--http", "0.0.0.0:3000", "--wsgi-file", "app.py", "--callable", "app"]
