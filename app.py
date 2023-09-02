from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story_choices

app = Flask(__name__)
app.config['SECRET_KEY'] = "bananas"

debug = DebugToolbarExtension(app)

@app.route('/')
def get_story_selection():
    stories = story_choices.values()

    return render_template("index.html", stories=stories)

@app.route('/story_prompt')
def get_prompts():

    story_id = request.args["story_id"]
    story = story_choices[story_id]

    prompts = story.prompts

    return render_template('story_prompt.html', story_id=story_id, prompts=prompts)

@app.route('/story')
def show_story():
    story_id = request.args["story_id"]
    story = story_choices[story_id]

    text = story.generate(request.args)

    return render_template('story.html', text=text)