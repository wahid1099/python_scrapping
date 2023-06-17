from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfform

def create_pdf_form(output_path, field_data_list):
    c = canvas.Canvas(output_path, pagesize=letter)

    # Enable AcroForm fields
    c.acroForm = pdfform.AcroForm()

    # Set up the form
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, "Form")

    y_start = 700  # Starting y-coordinate for the form fields

    for idx, field_data in enumerate(field_data_list):
        # Add form fields
        c.drawString(50, y_start - (idx * 100), "type:")
        c.drawString(150, y_start - (idx * 100), field_data.get('type', ''))

        c.drawString(50, y_start - (idx * 100) - 50, "name:")
        c.drawString(150, y_start - (idx * 100) - 50, field_data.get('name', ''))

        c.drawString(50, y_start - (idx * 100) - 100, "title:")
        c.drawString(150, y_start - (idx * 100) - 100, field_data.get('title', ''))

        # Create form fields
        c.acroForm.textfield(
            name=f'type_{idx}',
            tooltip='type',
            x=150, y=y_start - (idx * 100) + 5, width=200, height=20,
            textColor='black', borderColor='black', fillColor='white',
            value=field_data.get('type', '')
        )
        c.acroForm.textfield(
            name=f'name_{idx}',
            tooltip='name',
            x=150, y=y_start - (idx * 100) - 45, width=200, height=20,
            textColor='black', borderColor='black', fillColor='white',
            value=field_data.get('name', '')
        )
        c.acroForm.textfield(
            name=f'title_{idx}',
            tooltip='title',
            x=150, y=y_start - (idx * 100) - 95, width=200, height=20,
            textColor='black', borderColor='black', fillColor='white',
            value=field_data.get('title', '')
        )

    # Save the form and close the canvas
    c.acroForm.update()
    c.save()


# Example usage
output_file = 'form_template.pdf'
field_data_list = [
    {
        'type': 'text',
        'name': 'question1',
        'title': 'Color 1',
    },
    {
        'type': 'text',
        'name': 'question2',
        'title': 'Color 2',
    },
    {
        'type': 'text',
        'name': 'question3',
        'title': 'Color 3',
    },
]
create_pdf_form(output_file, field_data_list)
