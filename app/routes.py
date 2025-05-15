import os
import tempfile
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .utils import extract_text_from_pdf

main = Blueprint('main', __name__)

@main.route('/')
def upload_page():
    return render_template('upload.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No se seleccionó ningún archivo.')
        return redirect(url_for('main.upload_page'))

    file = request.files['file']
    if file.filename == '':
        flash('No se seleccionó ningún archivo.')
        return redirect(url_for('main.upload_page'))

    if file and file.filename.endswith('.pdf'):
        fd, temp_path = tempfile.mkstemp(suffix=".pdf")
        try:
            with os.fdopen(fd, 'wb') as temp_file:
                temp_file.write(file.read())

            extracted_text = extract_text_from_pdf(temp_path)
            return render_template('result.html', text=extracted_text)
        finally:
            os.remove(temp_path)

    flash('Solo se permiten archivos PDF.')
    return redirect(url_for('main.upload_page'))