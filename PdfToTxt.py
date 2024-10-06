# pip install pdfminer.six
from pdfminer.high_level import extract_text

pdf_path = "path/file_name.pdf"
txt_output_path = "path/file_name.txt"

extracted_text = extract_text(pdf_path)

with open(txt_output_path, "w", encoding="utf-8") as text_file:
    text_file.write(extracted_text)

txt_output_path