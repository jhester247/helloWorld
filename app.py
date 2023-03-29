from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/favorite-course')
def favorite():
    favorite_course = request.args.get('favorite_course')
    favorite_professor = request.args.get('favorite_professor')
    print('Favorite Course Entered: ' + favorite_course)
    print('Favorite Professor Entered: ' + favorite_professor)
    return render_template('favorite-course.html', favorite_course=favorite_course, favorite_professor=favorite_professor)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        agree_check = request.form.get('agree_check')

        if not first_name or not last_name or not email or not agree_check:
            return render_template('contact.html', error_message='Please fill out all required fields')

        print('First Name entered: ' + first_name)
        print('Last Name entered: ' + last_name)
        print('Email entered: ' + email)
        print('Agree this website rocks entered: ' + agree_check)

        return render_template('contact.html', form_submitted=True, first_name=first_name, last_name=last_name, email=email)

    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
