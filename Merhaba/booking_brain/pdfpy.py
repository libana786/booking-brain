import PyPDF2

# Define the input and output file names
input_pdf = "sample.pdf"
output_pdf = "modified_single_page.pdf"

# Open the input PDF file
with open(input_pdf, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the first (and only) page
    page = pdf_reader.pages[0]

    # Extract text from the page
    text = page.extract_text()

    # Replace 'A1' with 'Liban'
    modified_text = text.replace("A1", "Liban")
    print(modified_text)

    # Create a new PDF writer
    pdf_writer = PyPDF2.PdfWriter()

    # Create a new page with the modified text
    modified_page = PyPDF2.pdf.PageObject.create_text(pdf_writer, modified_text)
    
    # Merge the modified page with the original page
    modified_page.merge_page(page)

    # Add the modified page to the output PDF
    pdf_writer.add_page(modified_page)

    # Save the modified PDF to the output file
    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

print("PDF modification complete.")