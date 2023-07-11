FROM python:3.11-alpine
EXPOSE 8001
EXPOSE 9090
WORKDIR /app
COPY . .
RUN pip install pip --upgrade
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
