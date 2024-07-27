FROM python:3.9-slim

WORKDIR /myportfolio

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000