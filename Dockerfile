FROM python:3-alpine3.17
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host=0.0.0.0"]