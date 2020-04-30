from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None,post_id=None):
#     return render_template('index.html',name=username,post_id=post_id)
@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
        with open('database.csv', mode= 'a', newline='') as databasecsv:
            email = data['email']
            subject = data['subject']
            message = data['message']
            csv_writer = csv.writer(databasecsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email,subject,message])

def write_to_file(data):
    with open('database.txt', mode= 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data= request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'No se guardo su informacion'
    else:
        'algo salio mail intenta nuevamente'
    return 'form submitted ok'

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

# @app.route('/index.html')
# def index():
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/componets.html')
# def components():
#     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/blog')
# def blog():
#     return 'Este es un blog'

# @app.route('/blog/2020/dog')
# def blog2():
#     return 'Este es un blog de perros'