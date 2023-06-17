from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
import json

def create_pdf_form(output_path, field_data):
    c = canvas.Canvas(output_path)
    
    # Set up the form
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, "Form ")
    
    y = 705  # Initial y-coordinate
    
    # Iterate over each field dictionary
    for field in field_data:
        # Add field label
        c.drawString(50, y, 'name')
        
        # Create form field
        c.setFont("Helvetica-Bold", 12)
        c.acroForm.textfield(name=field.get('name', ''), tooltip=field.get('name', ''), x=150, y=y, width=200, height=20, value=field.get('name', ''))
        
        y -= 50  # Decrease y-coordinate for the next field
    
    c.save()

# Example usage
output_file = 'form_template2.pdf'
json_data = [
    {
        "type": "text",
        "name": "question1",
        "title": "Text",
        "element_uuid": "f19c67ad-2f86-44a4-b8c6-8c1590dbfeba"
    },
    {
        "type": "text",
        "name": "question2",
        "title": "Color",
        "description": "Answer",
        "element_uuid": "5dba1e21-a0a8-4ca6-a9ea-8ef8076cab37",
        "inputType": "color"
    },
    # Add more fields here...
]

# Convert JSON data to a list of dictionaries
field_data = json.loads(json.dumps(json_data))

create_pdf_form(output_file, field_data)
