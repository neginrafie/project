FROM python:3.12.4

WORKDIR /var/www

COPY /sql_app/requirements.tex .

RUN pip install -r reguirements.tex

COPY sql_app .

CMD ["fastapi", "run", "main.py"]