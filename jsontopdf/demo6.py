from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfform

def generate_editable_pdf(output_path, form_fields):
    c = canvas.Canvas(output_path, pagesize=letter)

    c.setFont('Helvetica', 12)

    # Add form fields
    for field_data in form_fields:
        field_type = field_data['type']
        field_name = field_data['name']
        field_title = field_data['title']
        field_value = field_data.get('value', '')

        if field_type == 'text':
            c.drawString(100, 700, field_title)
            c.rect(200, 685, 200, 20, stroke=1, fill=0)
            c.setFont('Helvetica', 10)
            c.drawString(205, 688, field_value)
            c.setFont('Helvetica', 12)
            c.acroForm.textfield(name=field_name, tooltip=field_title, x=200, y=685, width=200, height=20)
        elif field_type == 'checkbox':
            c.acroForm.checkbox(name=field_name, tooltip=field_title, x=200, y=685, buttonStyle='check',
                                borderStyle='bevelled', value=field_value)
            c.drawString(220, 688, field_title)

    c.save()

# Example usage
output_path = 'pdfs/editable_form.pdf'  # Output path for the editable form
form_fields = [
    {
        "type": "text",
        "name": "question1",
        "title": "Text",
        "value": "Sample Text"
    },
    {
        "type": "checkbox",
        "name": "question2",
        "title": "Checkbox",
        "value": True
    },
    # Add more form fields as needed
]

generate_editable_pdf(output_path, form_fields)
