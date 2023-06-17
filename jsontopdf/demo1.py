import json
from wkhtmltopdf import PDF

def json_to_pdf(json_data, output_file):
  """Converts JSON data to PDF where every field can be edited.

  Args:
    json_data: The JSON data to convert.
    output_file: The path to the output PDF file.

  Returns:
    The path to the output PDF file.
  """

  pdf = PDF()
  pdf.enable_edit()
  pdf.from_json(json_data)
  pdf.save(output_file)

  return output_file

if __name__ == '__main__':
  json_data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'phone': '123-456-7890',
  }

  output_file = 'output.pdf'

  json_to_pdf(json_data, output_file)

  print('The PDF file has been saved to {}.'.format(output_file))
