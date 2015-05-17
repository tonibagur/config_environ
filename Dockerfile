
FROM python:2.7
RUN mkdir /code
RUN mkdir /templates
COPY replace_environ.py /code/

CMD ["python2.7","/code/replace_environ.py"]  
