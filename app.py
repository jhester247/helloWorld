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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print('First Name entered: ' + request.form.get('first_name'))
        print('Last Name entered: ' + request.form.get('last_name'))
        print('Email entered: ' + request.form.get('email'))

    # Must check the checkbox to see if the website rocks
    if request.form.get('agree_check'):
        print('Agree this website rocks entered: ' + request.form.get('agree_check'))
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
