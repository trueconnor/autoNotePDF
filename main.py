
pdf_path = '01 2004 BC Abbott Methods of Discovery.pdf'

import fitz  # PyMuPDF


def extract_underlined_text(page):
    underlined_text = ""
    for annot in page.annots():
        subtype = annot.info.get("Subtype", b"").decode("utf-8")
        print(subtype)
        if subtype == "/Highlight":
            for quad_points in annot.vertices:
                for point in quad_points:
                    underlined_text += page.get_text("text", point) + " "
    return underlined_text


pdf_document = fitz.open(pdf_path)


for page_number in range(5):
    print("begin page " + str(page_number))
    page = pdf_document.load_page(page_number)
    highlighted_text = extract_underlined_text(page)
    if highlighted_text:
        print(f"Page {page_number + 1}: {highlighted_text.strip()}")

pdf_document.close()


