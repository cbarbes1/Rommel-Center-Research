from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('html/index.html')

@app.route('/html/<path:filename>')
def html(filename):
    html_folder = 'html'
    return render_template(f'{html_folder}/{filename}')

@app.route('/static/java/<path:filename>')
def static_files(filename):
    java_folder = 'java'
    return send_from_directory(app.static_folder, f'{java_folder}/{filename}')

@app.route('/static/json/<path:filename>')
def serve_json(filename):
    json_folder = 'json' 
    return send_from_directory(app.static_folder, f'{json_folder}/{filename}')

if __name__ == '__main__':
    app.run(port=1111)