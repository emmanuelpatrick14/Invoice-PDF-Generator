import pandas as pd
import glob
from pathlib import Path
from fpdf import FPDF

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    print(df)
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    # pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()
    filename = Path(filepath).stem
    print(filename)
    invoice_nr = filename.split('-')[0]
    # invoice_nr,date = filename.split('-')
    invoice_date = filename.split('-')[1]

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"Invoice nr {invoice_nr}", ln=1)

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"Date {invoice_date}", ln=1)

    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    # for the headers
    #  look into index obj
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family='Times', size=10,style='b')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=str(columns[0]), border=1,)
    pdf.cell(w=70, h=8, txt=str(columns[1]), border=1)
    pdf.cell(w=40, h=8, txt=str(columns[2]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[3]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[4]), border=1,ln=1)

    # add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1, align='M')
        pdf.cell(w=70, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=40, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1,ln=1)

    pdf.output(f"PDFs/{filename}.pdf")
