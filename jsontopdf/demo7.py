import pdfrw
import json

def fill_pdf_form(template_path, output_path, field_data):
    template_pdf = pdfrw.PdfReader(template_path)
    
    for page in template_pdf.pages:
        if "/Annots" in page:
            for annotation in page["/Annots"]:
                if annotation["/Subtype"] == "/Widget" and annotation["/FT"] == "/Tx":
                    field_name = annotation["/T"]
                    if field_name in field_data:
                        field_value = field_data[field_name]
                        annotation.update(pdfrw.PdfDict(V=field_value))

    pdfrw.PdfWriter().write(output_path, template_pdf)
template_file = 'form_template.pdf'

output_file = 'filled_form.pdf'
field_data = {
        "type": "text",
        "name": "question2",
        "title": "Color",
        "description": "Answer",
        "element_uuid": "5dba1e21-a0a8-4ca6-a9ea-8ef8076cab37",
        "inputType": "color"
}
fill_pdf_form(template_file, output_file, field_data)
