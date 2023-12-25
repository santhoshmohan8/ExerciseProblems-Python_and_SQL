FROM continuumio/miniconda3

RUN conda install python=3.10

WORKDIR /app
COPY . /app

RUN pip install -r /app/requirements.txt
CMD ["uvicorn", "app:app","--host", "0.0.0.0", "--port", "3000"]

# docker build -t tag_name .
# docker images tag_name
# docker run -e 3000 -p3000:3000 tag_name