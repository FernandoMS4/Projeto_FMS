FROM python:3.13
RUN apt-get update && apt-get install -y wait-for-it
RUN pip install poetry
COPY . /src 
WORKDIR  /src
RUN poetry install --no-root
EXPOSE 8502
CMD ["wait-for-it", "db:3306", "--", "poetry", "run", "python", "main.py", "--server.port=8502", "--server.address=0.0.0.0"]
