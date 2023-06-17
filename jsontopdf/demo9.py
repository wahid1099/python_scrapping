from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
import json

def create_pdf_form(output_path, field_data):
    c = canvas.Canvas(output_path)
    
    # Set up the form
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, "Form ")
    
    # Add form fields
    c.drawString(50, 700, "type:")
    c.drawString(150, 700, field_data.get('type', 'wahid'))
    
    c.drawString(50, 650, "name:")
    c.drawString(150, 650, field_data.get('name', ''))
    
    c.drawString(50, 600, "title:")
    c.drawString(150, 600, field_data.get('title', ''))
    
    c.drawString(50, 550, "description:")
    c.drawString(150, 550, field_data.get('title', ''))
    
    
    c.drawString(50, 500, "element_uuid:")
    c.drawString(150, 500, field_data.get('element_uuid', ''))
    
    c.drawString(50, 450, "inputType:")
    c.drawString(150, 450, field_data.get('inputType', ''))
    
    # Create form fields
    c.setFont("Helvetica-Bold", 12)
    c.acroForm.textfield(name='type', tooltip='type', x=150, y=705, width=200, height=20,value=field_data.get('type', ''))
    c.acroForm.textfield(name='name', tooltip='name', x=150, y=655, width=200, height=20)
    c.acroForm.textfield(name='title', tooltip='title', x=150, y=605, width=200, height=20)
    c.acroForm.textfield(name='description', tooltip='description', x=150, y=555, width=200, height=20)
    c.acroForm.textfield(name='element_uuid', tooltip='element_uuid', x=150, y=505, width=200, height=20)
    c.acroForm.textfield(name='inputType', tooltip='inputType', x=150, y=455, width=200, height=20)
    
    c.save()

# Example usage
output_file = 'form_template2.pdf'
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

create_pdf_form(output_file, field_data)
