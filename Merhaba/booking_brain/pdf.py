from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

def generate_receipt(pdf_file_path):
    # Create a SimpleDocTemplate object with the PDF file path and page size (e.g., letter).
    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    story = []

    # Define styles for text elements.
    styles = getSampleStyleSheet()

    # Create the header with logo and company information.
    header = [
        Image("logo.png", width=50, height=50),  # Replace "logo.png" with your logo file path
        Paragraph("Company Name<br/>Address<br/>Tel: 123-456-7890", styles['Normal']),
    ]
    header_table = Table([header], colWidths=[2.5 * inch, 3 * inch])
    header_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))

    # Create the footer with email address and telephone numbers.
    footer = Paragraph("Email: example@example.com<br/>Tel: 987-654-3210", styles['Normal'])

    # Create the body with payment information and transaction detail table.
    payment_info = Paragraph("Payment Information:", styles['Heading2'])
    transaction_table_data = [
        # Define your transaction data here as a list of lists.
        # Each inner list represents a row in the table.
        ["Transaction Date", "Description", "Amount"],
        ["2023-09-18", "Product 1", "$100.00"],
        ["2023-09-19", "Product 2", "$50.00"],
        # Add more rows as needed.
    ]
    transaction_table = Table(transaction_table_data, colWidths=[1.5 * inch, 3 * inch, 1.5 * inch])
    transaction_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('ALIGN', (2, 1), (-1, -1), 'RIGHT'),
    ]))

    # Add elements to the story in the desired order.
    story.extend([header_table, Spacer(1, 12), payment_info, Spacer(1, 12), transaction_table, Spacer(1, 36), footer])

    # Build the PDF document.
    doc.build(story)

if __name__ == "__main__":
    generate_receipt("receipt.pdf")
