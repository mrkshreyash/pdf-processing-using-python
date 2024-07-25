import fitz  # PyMuPDF
import tempfile
import os

def highlight_and_preview(pdf_path, text_to_highlight):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Search for the text to highlight
    highlighted_page = None
    for page in doc:
        text_instances = page.search_for(text_to_highlight)
        if text_instances:
            highlighted_page = page.number
            for inst in text_instances:
                # Add annotations to highlight the text
                highlight = page.add_highlight_annot(inst)
            break  # Stop searching after finding the first occurrence

    if highlighted_page is None:
        print("Text not found in the PDF.")
        return

    # Save the highlighted page to a temporary PDF file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    temp_file.close()
    temp_pdf = fitz.open()
    temp_pdf.insert_pdf(doc, from_page=highlighted_page-1, to_page=highlighted_page)
    temp_pdf.save(temp_file.name)
    temp_pdf.close()
    doc.close()

    # Open the temporary PDF file in a PDF viewer
    os.system(f"start {temp_file.name}")

# Example usage:
pdf_path = "sample.pdf"
text_to_highlight = """The left pane displays the available bookmarks for this PDF. You may need to enable the 
display of bookmarks in Adobe Acrobat Reader by clicking Window > Show Bookmarks. 
Selecting a date from the left pane displa"""

highlight_and_preview(pdf_path, text_to_highlight)
