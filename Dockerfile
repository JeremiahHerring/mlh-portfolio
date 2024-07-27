FROM python:3.9-slim

WORKDIR /myportfolio

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV URL=localhost:5000
ENV MYSQL_HOST=localhost
ENV MYSQL_USER=myportfolio
ENV MYSQL_PASSWORD=mypassword
ENV MYSQL_DATABASE=myportfoliodb

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000