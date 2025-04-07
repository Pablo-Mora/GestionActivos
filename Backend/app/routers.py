from flask import Blueprint, request, jsonify, send_from_directory, render_template
from app.documents_handler import generate_document_from_template, allowed_file
from app.excel_handler import export_to_excel
import os
import uuid
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/api/submit-form', methods=['POST'])
def submit_form():
    """
    Recibe datos del formulario, genera un documento Word basado en una plantilla
    y devulve un enlace para descargar el documento.
    """

    try:
        # Obtener datos del formulario
        form_data = request.form_to_dict()

        # Generar nombre unico para el archivo
        timestamp = datetime.now().strftime("%Y%m%d")
        unique_id = str(uuid.uuid4())[:8]
        filename = f"activo_{timestamp}_{unique_id}.docx"

        # Ruta de la plantilla y archivo de salida
        template_path = os.path.join('templates', 'plantilla_activo.docx')
        output_path = os.path.join(bp.config['UPLOAD_FOLDER'], filename)

        # Generar decumento
        generate_document_from_template(template_path, output_path, form_data)


        # Guardar en la base de datos
        query = """
        INSERT INTO Activos (nombre, descripción, fecha_adquisicion, )

