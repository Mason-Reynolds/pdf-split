import sys
import os
import shutil

sys.path.append("./pypdf-6.14.2")

from pypdf import PdfReader, PdfWriter
from tkinter import Tk, filedialog

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) > 1:
    input = sys.argv[1]
else:
    Tk().withdraw()
    input = filedialog.askopenfilename(
        title="Select a PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )

if not input:
    print("No file selected.")
    exit()

if not os.path.exists(input):
    raise FileNotFoundError(f"{input} does not exist")

def split(input_pdf, output_prefix):
    """Split the given PDF by its bookmarks (outlines) or page by page if no bookmarks."""

    reader = PdfReader(input_pdf)

    output_dir = os.path.join(
        os.path.dirname(input),
        "output_pdfs"
    )

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    os.makedirs(output_dir)
    

    def flatten_bookmarks(bookmarks, parent_page=0):
        """Flatten nested bookmarks into (title, page_number) tuples."""
        flat = []
        for bm in bookmarks:
            if isinstance(bm, list):
                # Nested bookmarks
                flat.extend(flatten_bookmarks(bm, parent_page))
            else:
                title = bm.title if hasattr(bm, 'title') else str(bm)
                page_num = reader.get_destination_page_number(bm) if hasattr(bm, 'title') else parent_page
                flat.append((title, page_num))
        return flat

    # Extract bookmarks if exist
    try:
        bookmarks = reader.outline
        flat_bookmarks = flatten_bookmarks(bookmarks)
    except Exception as e:
        print(type(e).__name__, e)
        raise

    # If no bookmarks, fallback: split by page
    if not flat_bookmarks:
        for i, page in enumerate(reader.pages, start=1):
            writer = PdfWriter()
            writer.add_page(page)
            output_path = os.path.join(output_dir, f"{i}.pdf")
            writer.write(output_path)
            print(f"Saved: {output_path}")
        return

    # Split PDFs by bookmarks
    for i, (title, start_page) in enumerate(flat_bookmarks):
        end_page = flat_bookmarks[i+1][1] if i + 1 < len(flat_bookmarks) else len(reader.pages)
        writer = PdfWriter()
        for p in range(start_page, end_page):
            writer.add_page(reader.pages[p])
        invalid = '<>:"/\\|?*'
        safe_title = "".join(c for c in title if c not in invalid).strip()
        output_path = os.path.join(output_dir, f"{safe_title}.pdf")
        writer.write(output_path)
        print(f"Saved: {output_path}")

split(input, "output_pdfs")