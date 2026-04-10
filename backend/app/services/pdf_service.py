import fitz


def extract_text_from_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    pages = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")
        if text.strip():
            pages.append(f"[Page {page_num}]\n{text}")

    doc.close()
    return "\n\n".join(pages)