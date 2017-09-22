from io import BytesIO
from flask import Flask, request, render_template, send_file
from PIL import Image
from processor import process_image
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number_of_colors = int(request.form['number_of_colors'])
        f = request.files['image_file']
        image = process_image(Image.open(f), number_of_colors)
        bytes_io = BytesIO()
        image.save(bytes_io, 'PNG')
        bytes_io.seek(0)
        return send_file(bytes_io, mimetype='image/png')
    else:
        return render_template('home.html')

if __name__ == '__main__':
  app.run()
