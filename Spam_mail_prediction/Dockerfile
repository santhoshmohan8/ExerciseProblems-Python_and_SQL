FROM continuumio/miniconda3

RUN conda install python=3.10

WORKDIR /app
COPY . /app

RUN pip install -r /app/requirements.txt
CMD ["uvicorn", "app:app","--host", "0.0.0.0", "--port", "3000"]