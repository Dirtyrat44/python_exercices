from fpdf import FPDF


class PDF(FPDF):
    def header(self):

        # Setting font: helvetica bold 16
        self.set_font("helvetica", "B", 16)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=1, align="C")
        # Performing a line break:
        self.ln(20)


def main():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(50, 20, 'Powered by FPDF.', align='C')
    pdf.output("test.pdf")






if __name__ == "__main__":
    main()
