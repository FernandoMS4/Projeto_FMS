FROM python:3.13
RUN pip install poetry
COPY . /src 
WORKDIR  /src
RUN poetry install --no-root
EXPOSE 8502
ENTRYPOINT [ "poetry","run","python","main.py", "--server.port=8502", "--server.address=0.0.0.0"]