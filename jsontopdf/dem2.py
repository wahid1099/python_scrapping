from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
import json



def create_pdf_form(output_path, field_data):
    c = canvas.Canvas(output_path)

    # Set up the form
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, "Form ")
    
    c.drawString(50, 700, "type:")

    

    # Create form fields
    c.setFont("Helvetica-Bold", 12)
    c.acroForm.textfield(name='type', tooltip='type', x=150, y=705, width=200, height=20)
    c.acroForm.textfield(name='name', tooltip='name', x=150, y=655, width=200, height=20)
    c.acroForm.textfield(name='title', tooltip='title', x=150, y=605, width=200, height=20)
    c.acroForm.textfield(name='description', tooltip='description', x=150, y=555, width=200, height=20)
    c.acroForm.textfield(name='element_uuid', tooltip='element_uuid', x=150, y=505, width=200, height=20)
    c.acroForm.textfield(name='inputType', tooltip='inputType', x=150, y=455, width=200, height=20)

    # Populate form fields with JSON data
    form = c.acroForm
    form.type = field_data.get('type', '')
    form.name = field_data.get('name', '')
    form.title = field_data.get('title', '')
    form.description = field_data.get('description', '')
    form.element_uuid = field_data.get('element_uuid', '')
    form.inputType = field_data.get('inputType', '')

    c.save()




# Example JSON data
json_data = {
    'type': 'Form Type',
    'name': 'John Doe',
    'title': 'Form Title',
    'description': 'Form Description',
    'element_uuid': '123456',
    'inputType': 'text',
}

# Convert JSON data to a dictionary
field_data = json.loads(json.dumps(json_data))
output_file = 'data.pdf'

# Call create_pdf_form with updated field_data
create_pdf_form(output_file, field_data)
