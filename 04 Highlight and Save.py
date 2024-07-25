import fitz  # PyMuPDF

def highlight_text(pdf_path, text_to_highlight, output_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Search for the text to highlight
    for page in doc:
        text_instances = page.search_for(text_to_highlight)
        for inst in text_instances:
            # Add annotations to highlight the text
            highlight = page.add_highlight_annot(inst)

    # Save the modified PDF
    doc.save(output_path)
    doc.close()

# Example usage:
pdf_path = "sample.pdf"
output_path = "highlighted_output.pdf"
text_to_highlight = """The left pane displays the available bookmarks for this PDF. You may need to enable the  
display of bookmarks in Adobe Acrobat Reader by clicking Window > Show Bookmarks. 
Selecting a date from the left pane displa"""

highlight_text(pdf_path, text_to_highlight, output_path)
