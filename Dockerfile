FROM python:alpine
RUN pip install flask
RUN pip pip install selenium
RUN pip install webdriver-manager
WORKDIR /wog_app
COPY main_score.py .
COPY Scores.txt .
CMD python main_score.py
