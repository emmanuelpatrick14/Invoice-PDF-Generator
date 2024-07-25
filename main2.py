import pandas as pd
import glob
from pathlib import Path
from fpdf import FPDF

filepaths = glob.glob("text/*.txt")
# get the files
pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    # print(filepath)
    filename = Path(filepath).stem
    filename = filename.title()
    print(filename)

    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()
    pdf.set_font(family='Times', size=12, style='B')
    pdf.cell(w=50, h=8, txt=f"{filename}")

pdf.output("output.pdf")
