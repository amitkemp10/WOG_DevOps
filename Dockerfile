FROM python:alpine
WORKDIR /wog_app
COPY main_score.py .
COPY Scores.txt .
CMD python main_score.py
