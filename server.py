from flask import Flask,redirect, render_template,request,send_from_directory
import csv
app = Flask(__name__)

@app.route("/")  
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')  
def html_page_redirection(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open("database_form.txt", "a+") as f:
#         email = data["email"]
#         subject = data["subject"]
#         message= data['message']
#         file = f.write(f'\n{email},{subject},{message}')

#database in a csv here:
def write_to_csv(data):
    with open("database.csv", "a+",newline='') as database:
        fieldnames = ['Email', 'Subject','Message']
        writer = csv.DictWriter(database, fieldnames=fieldnames)
        writer.writeheader()
        email = data["email"]
        subject = data["subject"]
        message= data['message']
        csv_writer = csv.writer(database ,delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL) # type: ignore
        csv_writer.writerow([email,subject,message])


@app.route('/form_submit', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank_you.html')
    else:
        return 'Something went wrong. Try Again!'
    

if __name__ == '__main__':
    app.run(debug=True)


# @app.route("/index.html")  
# def my_home_redirected():
#     return render_template('index.html')

# @app.route("/about.html")
# def about_page():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/components.html")
# def components_page():
#     return render_template('components.html')

# @app.route("/works.html")
# def works_page():
#     return render_template('works.html')


