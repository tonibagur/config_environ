
FROM python
MKDIR /code
MKDIR /templates
COPY replace_environ.py /code

CMD ["/usr/bin/python","/code/replace_environ.py"]  
