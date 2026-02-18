from flask import Flask, render_template, send_from_directory
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=base_dir, static_folder=base_dir)

@app.route('/')
def index():
    # This shows the Welcome page with the QR code
    return render_template('index.html')

@app.route('/view/<int:photo_id>')
def view_photo(photo_id):
    # This shows the motorcycle/selfie page
    return render_template('photo.html', photo_id=photo_id)

@app.route('/<path:filename>')
def custom_static(filename):
    return send_from_directory(base_dir, filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
