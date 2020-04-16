from flask import Flask, render_template, request, redirect
from so import get_jobs
from indeed import get_jobs

app = Flask("Scrapper")

db = {}


@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        exisitingJobs = db.get(word)
        if exisitingJobs:
            jobs = exisitingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", 
    searchingBy= word,
    resultsNumber = len(jobs),
    jobs = jobs
    )

app.run(host="0.0.0.0")
