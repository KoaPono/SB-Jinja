from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "bananas"

debug = DebugToolbarExtension(app)

@app.route('/')
def get_prompts():
    prompts = story.prompts

    return render_template('index.html', prompts=prompts)

@app.route('/story')
def show_story():
    text = story.generate(request.args)

    return render_template('story.html', text=text)