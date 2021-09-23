from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

# Set routes dynamically with page_name attribute
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# Route for submitting form
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('thank_you.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'

# Writes data to a file
def write_to_file(data):
    with open('db.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

# Writes data to a csv
def write_to_csv(data):
    with open('db.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])




# @app.route('/index.html')
# def my_home2():
#     return render_template('index.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')




# Passing parameters to route
# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)


# @app.route('/blog')
# def blog():
#     return 'This is my blog page'
#
# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'hey look at my dog!'