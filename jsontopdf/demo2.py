import json
import pdfkit

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
    {
        "type": "text",
        "name": "question3",
        "title": "Date",
        "description": "Answer",
        "element_uuid": "ea779941-d1c1-4b8e-b99e-5e9c0a2a1353",
        "inputType": "date"
    },
]

pdf = pdfkit.from_json(json_data)

with open("editable_pdf.pdf", "wb") as f:
    f.write(pdf)