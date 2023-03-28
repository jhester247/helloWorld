from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World From James Hester! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favorite-course') # added a new template
def favorite():
    print('Favorite Course Entered: ' + request.args.get('favorite_course'))
    print('Favorite Professor Entered: ' + request.args.get('favorite_professor'))
    return render_template('favorite-course.html')



if __name__ == '__main__':
    app.run()
