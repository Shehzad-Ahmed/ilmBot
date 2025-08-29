FROM python:3.12

WORKDIR /code

RUN pip install --upgrade pip

COPY ./pyproject.toml /code/pyproject.toml
# Conditionally copy poetry.lock if it exists
RUN if [ -f poetry.lock ]; then cp poetry.lock /code/poetry.lock; fi


RUN pip install poetry==2.1.1 \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --without dev

COPY ./src /code/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
