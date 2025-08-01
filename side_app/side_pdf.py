import pandas as pd
import glob
from fpdf import FPDF 
from pathlib import Path
import os

# Step 1: Create folder to store output PDF
os.makedirs("PDF", exist_ok=True)

# Step 2: Collect all .txt files in current directory
filepaths = glob.glob("Text+Files/*.txt")

# Step 3: Create FPDF object
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Step 4: Loop through each file and add content to PDF
for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem     # Extract filename without extension
    name = filename.title()            # Capitalize the title
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=0, h=10, txt=name, ln=1)

# Step 5: Save the final PDF file in the "PDF" folder
pdf.output("PDF/output.pdf")
