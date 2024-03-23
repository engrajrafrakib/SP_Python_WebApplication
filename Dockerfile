FROM python

WORKDIR /SP_Python_WebApplication

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /SP_Python_WebApplication

CMD ["python","app.py"]