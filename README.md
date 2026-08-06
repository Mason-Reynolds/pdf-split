pdfs.py intellectual property of Mason Reynolds, Clallam PUD District No. 1

-----------------------------------Requirements--------------------------------

You will need Python 3.14.6 or newer. Download Python at:
    https://www.python.org/downloads/

You will also need pypdf. To obtain, open Command Prompt (hit Windows, type 
"cmd" and hit Enter), and in the black box, type "python -m pip install pypdf".

-------------------------------------How To------------------------------------

Step 1. Scan your documents as one big stack, so they're all in one PDF.

Step 2. Open the source PDF and place a bookmark at the start of each new 
document (be sure to remove any blank pages using Organize Pages). Name the 
bookmark anything, but it's recommended to name the bookmark as follows:
    1Name of First Document
    2Name of Second Document
Therefore they are sorted such that the sequence is the same as the source pdf 
and the paper stack, and when adding to NeoGov, the only change that needs to 
be made is removing the number.

Step 3. Save the bookmarked pdf as something distinct from the original.

Step 4. Run pdfs.py. You can do this by double-clicking the file, or 
right-clicking and selecting "Open With..." -> "Python"

Step 5. It will open a black box, and then open a file select prompt. Select 
your source pdf.

Step 6. The documents will be split and sent an "output_pdfs" folder in the 
same directory as the source pdf. If there is already an "output_pdfs" folder, 
it will be deleted along with anything inside it to make room for the new 
output folder.