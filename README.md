
# PDF Splitter (`pdfs.py`)

**Copyright Mason Reynolds, Clallam PUD District No. 1. All rights reserved.**

---

## Requirements

### Python

Python **3.14.6 or newer** is required.

Download Python from:

	https://www.python.org/downloads/

### pypdf

Install the required package by opening **Command Prompt** and running:

```bash
python -m pip install pypdf
```
---

## Instructions

### 1. Scan Documents

Scan all documents for a single employee into one PDF file.

Before creating bookmarks, remove any blank pages using Adobe Acrobat's **Organize Pages** tool (or another PDF editor).

### 2. Create Bookmarks

Place a bookmark at the beginning of each document.

Bookmarks may be named anything, but it is recommended to prefix each bookmark with a sequential number so the output files remain in the same order as the original PDF and paper file.

Example:

```text
1Employee Change Form
2Payroll Adjustment
3Insurance Enrollment
```

When uploading the split documents to NeoGov, simply remove the leading number from each filename.

### 3. Save the PDF

Save the bookmarked PDF using a different filename than the original scanned PDF.

### 4. Run the Program

Launch `pdfs.py` by either:

* Double-clicking the file, or
* Right-clicking the file and selecting **Open With → Python**

### 5. Select the PDF

A file selection window will open.

Browse to and select the bookmarked PDF you created in Step 3.

### 6. Retrieve the Output

The program creates an **output_pdfs** folder in the same directory as the selected PDF.

If an **output_pdfs** folder already exists, it and **all of its contents** will be deleted before new files are created. Be sure to move or back up any files you wish to keep before running the program.

Each bookmarked section of the PDF is exported as a separate PDF using its bookmark name as the filename.

```
```
