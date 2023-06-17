from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_pdf_template(output_path):
    c = canvas.Canvas(output_path, pagesize=letter)

    # Add form fields
    c.drawString(100, 700, "type:")
    c.rect(200, 700, 200, 20, stroke=1, fill=0)

    c.drawString(100, 650, "name:")
    c.rect(200, 650, 200, 20, stroke=1, fill=0)
    
    c.drawString(100, 600, "title:")
    c.rect(200, 600, 200, 20, stroke=1, fill=0)
    
    c.drawString(100, 550, "description:")
    c.rect(200, 550, 200, 20, stroke=1, fill=0)
    
    
    c.drawString(100, 500, "element_uuid:")
    c.rect(200, 500, 200, 20, stroke=1, fill=0)
    
    c.drawString(100, 450, "inputType:")
    c.rect(200, 450, 200, 20, stroke=1, fill=0)

    # Add more form fields as needed

    c.save()

# Example usage
output_path = 'pdfs/template.pdf'  # Output path for the template
generate_pdf_template(output_path)
