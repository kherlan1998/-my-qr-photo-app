from flask import Flask, render_template, send_from_directory
import os

# We tell Flask to look for everything in the current directory (.)
app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

# This part is the "secret" page people see after scanning the QR
@app.route('/view/<int:photo_id>')
def view_photo(photo_id):
    return render_template('photo.html', photo_id=photo_id)

# This helper allows Flask to find your images in the main folder
@app.route('/<path:filename>')
def custom_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
