from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Specify the template folder
app.template_folder = 'templates'

app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('html/Version2/index.html')

@app.route('/html/Version2/<path:filename>')
def html(filename):
    html_folder = 'html/Version2'
    return render_template(f'{html_folder}/{filename}')

@app.route('/static/java/<path:filename>')
def static_files(filename):
    java_folder = 'java'
    return send_from_directory(app.static_folder, f'{java_folder}/{filename}')

@app.route('/static/json/<path:filename>')
def serve_json(filename):
    json_folder = 'json' 
    return send_from_directory(app.static_folder, f'{json_folder}/{filename}')

@app.route('/static/image/<path:filename>')
def img(filename):
    image_folder = 'image' 
    return send_from_directory(app.static_folder, f'{image_folder}/{filename}')

@app.route('/static/style/<path:filename>')
def css(filename):
    java_folder = 'style'
    return send_from_directory(app.static_folder, f'{java_folder}/{filename}')

@app.errorhandler(404)
def pageNotFound(error):
    print("Handling 404 Page Not Found")
    return render_template('html/errorPages/404.html'), 404

@app.errorhandler(500)
def internalServerError(error):
    print("Handling 500 Internal Server Error")
    return render_template('html/errorPages/500.html'), 500

if __name__ == '__main__':
    app.run(port=1111)
