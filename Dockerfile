FROM 192.168.132.129:5000/python:v3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8062
CMD ["python","app.py"]







