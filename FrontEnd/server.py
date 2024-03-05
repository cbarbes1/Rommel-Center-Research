from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('html/index.html')

@app.route('/index.html')
def index():
    return render_template('html/index.html')
    
@app.route('/Article.html')
def article():
    return render_template('html/Article.html')

@app.route('/ArticleAZ.html')
def articleaz():
    return render_template('html/ArticleAZ.html')

@app.route('/Faculty.html')
def faculty():
    return render_template('html/Faculty.html')

@app.route('/FacultyAZ.html')
def facultyaz():
    return render_template('html/FacultyAZ.html')

@app.route('/TopicAZ.html')
def topicaz():
    return render_template('html/TopicAZ.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(port=9999)