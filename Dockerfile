FROM python:3.9.7

WORKDIR /home/

RUN git clone https://github.com/leslie33kim/my_portfolio.git

WORKDIR /home/my_portfolio/

RUN pip install -r requirements.txt 

RUN echo "SECRET_KEY=django-insecure-zl^xg8j945-+9i5g8qc-i959vv(-_1=9vm=a))oqj*9pv!q^da" > .env 

RUN python manage.py migrate 

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

