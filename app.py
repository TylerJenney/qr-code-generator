from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_img_filename = None

    if request.method == 'POST':
        data = request.form.get('data')
        if data:
            img = qrcode.make(data)
            qr_img_filename = 'qr.png'
            img.save(os.path.join('static', 'generated', qr_img_filename))

    return render_template('index.html', qr_img=qr_img_filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
