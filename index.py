from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hslkeurygw3i47wpyio7rygfserityw734tw6o83476tweri85858yrfgskufyvgshfgeri8'
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/marilyn', methods=['GET', 'POST'])
def success():
    return render_template("marilyn.html")

@app.route('/sage', methods=['GET', 'POST'])
def success():
    return render_template("sage.html")