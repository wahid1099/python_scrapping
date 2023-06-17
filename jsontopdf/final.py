import json
import PyPDF2

def fill_pdf_form(template_path, output_path, data):
    with open(template_path, 'rb') as template_file:
        template_pdf = PyPDF2.PdfFileReader(template_file)
        writer = PyPDF2.PdfFileWriter()

        # Loop through each page of the template PDF
        for page_num in range(template_pdf.getNumPages()):
            page = template_pdf.getPage(page_num)

            # Update form fields with data
            if '/AcroForm' in page:
                form = page['/AcroForm'].getObject()
                fields = form['/Fields']
                for field in fields:
                    field_name = field['/T'][1:-1]  # Remove the parentheses around field name
                    if field_name in data:
                        field.update({
                            PyPDF2.generic.NameObject("/V"): PyPDF2.generic.createStringObject(str(data[field_name])),
                            PyPDF2.generic.NameObject("/Ff"): PyPDF2.generic.createStringObject("1")  # Make the field editable
                        })

            writer.addPage(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)





template_path = 'pdfs/template.pdf'  # Path to your template PDF form
output_path = 'pdfs/filled_form.pdf'  # Output path for the filled form
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

# data = json.loads(json_data)
fill_pdf_form(template_path, output_path, json_data)
