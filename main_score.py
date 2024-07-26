from flask import Flask
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read().strip()
    except FileNotFoundError:
        score = BAD_RETURN_CODE
    except Exception as e:
        score = BAD_RETURN_CODE
        print(f"Error reading score: {e}")

    if score == BAD_RETURN_CODE:
        content = f"<h1 style='display: inline;'>ERROR: </h1><h1 style='display: inline;'>{score}</h1>"
        color = "red"
    else:
        content = f"<h1 style='display: inline;'>The score is: </h1><h1 style='display: inline;'>{score}</h1>"
        color = "black"

    html_content = f"""
    <html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <div id="score" style="color: {color}">{content}</div>
    </body>
    </html>
    """
    return html_content


app.run("0.0.0.0", port=5000)
