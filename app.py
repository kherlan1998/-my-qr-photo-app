from flask import Flask, render_template, send_from_directory
import os

# This tells Flask to look for html and images in your main folder
app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view/<int:photo_id>')
def view_photo(photo_id):
    return render_template('photo.html', photo_id=photo_id)

@app.route('/<path:filename>')
def custom_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
