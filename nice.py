from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi</title>
      </head>
      <body>
        <h1>Hi! This is the home page.</h1>
        <a href="/hello">There is also a Hello page</a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label><br><br>
          Compliment Type:
            <select name="compliment">
              <label><option value="awesome">Awesome</option></label>
              <label><option value="terrifc">Terrific</option></label>
              <label><option value="fantastic">Fantastic</option></label>
              <label><option value="neato">Neato</option></label>
              <label><option value="fantabulous">Fantabulous</option></label>
              <label><option value="wowza">Wowza</option></label>
            </select><br><br>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment_type = request.args.get("compliment")

    compliment = choice(AWESOMENESS)

    print x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment_type)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=False)
