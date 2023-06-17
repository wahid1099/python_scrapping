from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
import json

def create_pdf_form(output_path, field_data):
    c = canvas.Canvas(output_path)
    
    # Set up the form
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, "Form ")
    
    y = 705 
    
    for field in field_data:
        # Check if the current field will fit on the page
        if y < 50:
            print("page finished")
            c.showPage()  # Move to a new page
            y = 750  # Reset the y-coordinate
        print('value of y',y)
        print('field of y',field)
        c.drawString(50, y, "type:")
        c.drawString(50, y-50, "name:")
        c.drawString(50, y-100, "title:")
        c.drawString(50, y-150, "description:")
        c.drawString(50, y-200, "element_uuid:")
        c.drawString(50, y-250, "inputType:")
        
        c.acroForm.textfield(name=field.get('type', ''), tooltip='Form Type', x=150, y=y, width=200, height=20, value=field.get('type', ''))
        c.acroForm.textfield(name=field.get('name', ''), tooltip='name', x=150, y=y-50, width=200, height=20, value=field.get('name', ''))
        c.acroForm.textfield(name=field.get('title', ''), tooltip='title', x=150, y=y-100, width=200, height=20, value=field.get('title', ''))
        c.acroForm.textfield(name=field.get('description', ''), tooltip='description', x=150, y=y-150, width=200, height=20, value=field.get('description', ''))
        c.acroForm.textfield(name=field.get('element_uuid', ''), tooltip='element_uuid', x=150, y=y-200, width=200, height=20, value=field.get('element_uuid', ''))
        c.acroForm.textfield(name=field.get('inputType', ''), tooltip='inputType', x=150, y=y-250, width=200, height=20, value=field.get('inputType', ''))
        
        y -= 325  # D
    
    c.save()

# Example usage
output_file = 'form_template2.pdf'
json_data=[
    {
        "type": "text",
        "name": "question1",
        "title": "Text",
        "element_uuid": "f19c67ad-2f86-44a4-b8c6-8c1590dbfeba",
         "inputType": "color"
    },
    {
        "type": "text",
        "name": "question2",
        "title": "Color",
        "description": "Answer",
        "element_uuid": "5dba1e21-a0a8-4ca6-a9ea-8ef8076cab37",
        "inputType": "color"
    },
    {
        "type": "text",
        "name": "question3",
        "title": "Date",
        "description": "Answer",
        "element_uuid": "ea779941-d1c1-4b8e-b99e-5e9c0a2a1353",
        "inputType": "date"
    },
    {
        "type": "text",
        "name": "question4",
        "title": "Date Time Local",
        "description": "Answer",
        "element_uuid": "35dfda37-b8ec-4e85-85a8-781b2405ea1d",
        "inputType": "datetime-local"
    },
    {
        "type": "text",
        "name": "question5",
        "title": "Email",
        "description": "Answer",
        "element_uuid": "8c594bc8-05b8-4cfc-bcfa-ecd898425fbe",
        "inputType": "email"
    },
    {
        "type": "text",
        "name": "question6",
        "title": "Number",
        "description": "Answer",
        "element_uuid": "1d8a8f6f-6e88-436f-a299-227d7b67d592",
        "inputType": "number"
    },
    {
        "type": "text",
        "name": "question7",
        "title": "Password",
        "description": "Answer",
        "element_uuid": "4acb4568-8ce8-4e26-b00e-4961cb4bf7ad",
        "inputType": "password"
    },
    {
        "type": "text",
        "name": "question8",
        "title": "Range",
        "description": "Answer",
        "element_uuid": "95c42fd5-4ebf-47bd-8844-e6cbb26a263c",
        "inputType": "range"
    },
    {
        "type": "text",
        "name": "question9",
        "title": "Tel",
        "description": "Answer",
        "element_uuid": "69eab168-1cc2-42fb-8505-8b1cb1201778",
        "inputType": "tel"
    },
    {
        "type": "text",
        "name": "question10",
        "title": "Time",
        "element_uuid": "cb5c47f2-a206-49ef-9639-b63ed57d26b2",
        "inputType": "time"
    },
    {
        "type": "text",
        "name": "question11",
        "title": "url",
        "element_uuid": "9c5bd63d-f28b-494c-9667-236b24b39f1f",
        "inputType": "url"
    }]  # Example JSON data


# Convert JSON data to a dictionary
field_data = json.loads(json.dumps(json_data))

create_pdf_form(output_file, field_data)
