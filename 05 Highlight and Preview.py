import fitz  # PyMuPDF
import tempfile
import os

def highlight_and_preview(pdf_path, text_to_highlight):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Search for the text to highlight
    for page in doc:
        text_instances = page.search_for(text_to_highlight)
        for inst in text_instances:
            # Add annotations to highlight the text
            highlight = page.add_highlight_annot(inst)

    # Save the modified PDF to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    temp_file.close()
    doc.save(temp_file.name)
    doc.close()

    # Open the temporary PDF file in a PDF viewer
    os.system(f"start {temp_file.name}")

# Example usage:
pdf_path = "sample.pdf"
text_to_highlight = """The left pane displays the available bookmarks for this PDF. You may need to enable the 
display of bookmarks in Adobe Acrobat Reader by clicking Window > Show Bookmarks. 
Selecting a date from the left pane displa"""

highlight_and_preview(pdf_path, text_to_highlight)
