FROM python:alpine
RUN pip install flask
WORKDIR /wog_app
COPY main_score.py .
COPY Scores.txt .
CMD python main_score.py
