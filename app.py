#how to import flask things
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice 
from stories import Story
app=Flask(__name__)
app.config["SECRET_KEY"]="mookster21"
debug=DebugToolbarExtension(app)


@app.route('/home')
def home_page():
    story_template=request.args.get("story_template")
    print(story_template)
    return render_template('home.html')

@app.route("/template")
def templates_page():
    template = request.form["template"]
    print(template)
    return render_template("template_stories.html")

@app.route('/')
def root_page():
    return render_template('home.html')

@app.route("/story")
def submit():
    place_answer=request.args.get("place")
    noun_answer=request.args.get("noun")
    verb_answer=request.args.get("verb")
    adjective_answer=request.args.get("adjective")
    plural_noun_answer=request.args.get("plural_noun")
    story=request.args.get("story")
    # print(request.args)
    prompts=["place","noun","verb","adjective","plural_noun"]
    new_story=Story(prompts,story)
    answers={new_story.prompts[0]:place_answer,
             new_story.prompts[1]:noun_answer,
             new_story.prompts[2]:verb_answer,
             new_story.prompts[3]:adjective_answer,
             new_story.prompts[4]:plural_noun_answer
    }
    print("incoming answer object")
    for prompt_and_answer in answers.items():
        print(prompt_and_answer)
    print(answers)
    # answers seems ok!
    print("incoming template information")
    print(new_story.template)
    print(type(new_story.template))

    madlib=new_story.generate(answers)

    return render_template("story.html",place=place_answer,noun=noun_answer,verb=verb_answer,adjective=adjective_answer,plural_noun=plural_noun_answer,madlib=madlib,story=story)

# @app.route("/greeting-2")
# def get_greeting2():
#     username=request.args["username"]
#     # this line needs to be a get request because if there is no input for unchecked in the html form then we can't the get request.args and will throw keys errors
#     wants=request.args.get("wants_compliments")
#     nice_thing=choice(COMPLIMENTS)
#     return render_template("greeting-2.html",username=username,compliment=nice_thing,wants_compliments=wants) 
