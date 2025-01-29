FROM python:3.13.1
RUN pip install poetry
COPY . /src 
WORKDIR  /src
RUN poetry install --no-root
EXPOSE 8502
ENTRYPOINT [ "poetry","run","main.py" ]