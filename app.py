from flask import Flask, make_response, render_template, request, url_for, redirect
from createForm import *
import string

app = Flask(__name__)
guessCount = 0
starting()

@app.get("/")
def intro():
	return render_template("intro.html")

@app.get("/guess")
def showForm():
	return render_template(str.format("updatedForm{number}.html", number=guessCount))

@app.post("/guess")
def processForm():
	global guessCount
	guessCount += 1
	inWordUpdate(request.form["inWords"])
	notInWordUpdate(request.form["notInWords"])
	wordPositionsUpdate(request.form["order"])
	updateForm(guessCount) 
	filterFrame()
	return redirect(url_for('showCandidates', number=guessCount))

@app.get("/candidates/<int:number>") 
def showCandidates(number):
	if(number > guessCount):
		return ("<p>You haven't guessed this much yet!</p>"), 404
	return showFrame(number)
