from fpdf import FPDF



def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(60, 10, 'Powered by FPDF.', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.output("test.pdf")

    




if __name__ == "__main__":
    main()
