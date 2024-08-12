from fpdf import FPDF



def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(50, 20, 'Powered by FPDF.', align='C')
    pdf.output("test.pdf")






if __name__ == "__main__":
    main()
