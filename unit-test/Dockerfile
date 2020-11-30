FROM python:3
ADD requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /unit-test
COPY . .
ENTRYPOINT ["python3"]
CMD  ["unit_testing.py"]


