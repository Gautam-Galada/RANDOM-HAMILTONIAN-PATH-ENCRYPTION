import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
from suite import *
from decryption import *
import numpy as np
import time
import cv2
import shutil


UPLOAD_FOLDER = "{{url_for('uploads')}}"
UPLOAD_FOLDER = "static//uploads"



ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if os.path.exists(UPLOAD_FOLDER):
     shutil.rmtree(UPLOAD_FOLDER)  # delete output folder
os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")

def home():
	return render_template("index.html")

@app.route("/predict",methods=['POST','GET'])
def predict():
	if request.method=="POST":
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			x_0 = np.double(0.123456789)
			alpha = np.double(10.45678)
			beta = np.double(10.123)
			img = cv2.imread("static//uploads//image.jpg", cv2.IMREAD_GRAYSCALE)
			


			encrypted_img, hamiltonian_swap_order = encryption(img, x_0, alpha, beta)
			cv2.imwrite('static//uploads//encrypt.png', encrypted_img)
			encrypted_img = cv2.imread("encrypt.png", cv2.IMREAD_GRAYSCALE)

			decrypted_img = decryption(encrypted_img, x_0, alpha, beta, hamiltonian_swap_order)
			cv2.imwrite('static//uploads//decrypt.png', decrypted_img)

	return render_template("index.html",img1='static\\uploads\\encrypt.png', img2="static\\uploads\\decrypt.png")

		# return 'ok'			

if __name__ == "__main__":
	app.run(debug=True)
