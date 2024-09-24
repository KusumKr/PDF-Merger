import os
from pypdf import PdfWriter

def merge_pdfs(pdf_list, output_file):
    """
    Merges a list of PDF files into a single PDF.

    Args:
        pdf_list (list): List of PDF file paths to be merged.
        output_file (str): Output file path where the merged PDF will be saved.
    """
    pdf_merger = PdfWriter()

    # Iterate over the list of PDFs and append each to the merger
    for pdf in pdf_list:
        if os.path.exists(pdf):
            with open(pdf, 'rb') as file:
                pdf_merger.append(file)
        else:
            print(f"Error: {pdf} not found!")

    # Write the merged PDF to the output file
    with open(output_file, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

    print(f"PDFs successfully merged into: {output_file}")


def get_pdf_files():
    """
    Get PDF file paths from the user.

    Returns:
        list: List of PDF file paths provided by the user.
    """
    pdf_files = []
    print("Enter the PDF file paths (type 'done' when finished):")

    while True:
        pdf_file = input("Enter PDF file path: ").strip()

        if pdf_file.lower() == 'done':
            break
        elif not pdf_file.endswith('.pdf'):
            print("Please enter a valid PDF file.")
        else:
            pdf_files.append(pdf_file)

    return pdf_files


def main():
    """
    Main function to handle the PDF merging process.
    """
    print("Welcome to the PDF Merger")

    # Get the list of PDF files to merge
    pdf_files = get_pdf_files()

    if len(pdf_files) < 2:
        print("Error: You need at least 2 PDFs to merge.")
        return

    # Ask for the output file name
    output_file = input("Enter the name of the output PDF file (e.g., merged.pdf): ").strip()

    if not output_file.endswith('.pdf'):
        print("Error: Output file must have a .pdf extension.")
        return

    # Call the merge function
    merge_pdfs(pdf_files, output_file)


if __name__ == "__main__":
    main()