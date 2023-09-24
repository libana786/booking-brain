from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfReader, PdfWriter
import io

# Define the input and output file names
input_pdf = "sample.pdf"
output_pdf = "modified_single_page.pdf"
name = "Gooses"
tel = "07777777777"
p_type = "PPP"
p_ref = "95689485"
eth_ratio = "94694"
z_ratio = "94694"
m_ratio = "94694"
total = "94694"


# Function to replace text
def replace_text(input_pdf, output_pdf,name, tel, p_type , p_ref , eth_ratio, z_ratio, m_ratio, total):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    
    # Open the existing PDF file
    pdf_reader = PdfReader(input_pdf)

    # Create a canvas to modify the PDF
    can.setFont("Helvetica", 12)
    can.drawString(220, 642, name)  # Replace text at coordinates (100, 100)
    can.drawString(220, 622, tel)  # Replace text at coordinates (100, 100)
    can.drawString(220, 602, p_type)  # Replace text at coordinates (100, 100)
    can.drawString(220, 582, p_ref)  # Replace text at coordinates (100, 100)
    can.drawString(437, 468, eth_ratio)  # Replace text at coordinates (100, 100)
    can.drawString(437, 446, z_ratio)  # Replace text at coordinates (100, 100)
    can.drawString(437, 423, m_ratio)  # Replace text at coordinates (100, 100)
    can.drawString(437, 404, total)  # Replace text at coordinates (100, 100)

    can.showPage()
    can.save()

    # Merge the modified canvas with the original PDF
    packet.seek(0)
    new_pdf = PdfReader(packet)
    output_pdf_writer = PdfWriter()

    page = pdf_reader.pages[0]
    page.merge_page(new_pdf.pages[0])
    output_pdf_writer.add_page(page)

    # Save the modified PDF to the output file
    with open(output_pdf, "wb") as output_file:
        output_pdf_writer.write(output_file)


# Call the replace_text function
replace_text(input_pdf, output_pdf, name,tel, p_type, p_ref, eth_ratio, z_ratio, m_ratio, total)

print("PDF modification complete.")
