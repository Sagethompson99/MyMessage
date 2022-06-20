from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hslkeurygw3i47wpyio7rygfserityw734tw6o83476tweri85858yrfgskufyvgshfgeri8'
bootstrap = Bootstrap(app)

# @app.errorhandler(404)
# def page_not_found(e):
#    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/marilyn', methods=['GET', 'POST'])
def marilyn():
    if request.method == 'POST':
        request_data = request.get_json()
        with open("messages_for_sage.txt", 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(request_data['message'] + '\n' + content)
        return render_template("marilyn.html")
    else:
        file = open("messages_for_marilyn.txt")
        return file.readline()

@app.route('/sage', methods=['GET', 'POST'])
def sage():
    if request.method == 'POST':
        request_data = request.get_json()
        with open("messages_for_marilyn.txt", 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(request_data['message'] + '\n' + content)
        return render_template("sage.html")
    else:
        file = open("messages_for_sage.txt")
        return file.readline()
