FROM python:3

COPY src/ /vCase/src/
ADD main.py /vCase/

WORKDIR /vCase/

CMD ["python", "main.py"]