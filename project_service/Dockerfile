FROM python:3.6-alpine as base

FROM base as builder

RUN mkdir /install
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /install
COPY ../requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
COPY . /app
RUN apk --no-cache add libpq
WORKDIR /app

ENV DOCKER=1

CMD ["python", "manage.py", "db", "init"]
CMD ["python", "manage.py", "db", "migrate"]
CMD ["python", "manage.py", "db", "upgrade"]
CMD ["python", "manage.py", "runserver"]