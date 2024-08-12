from fpdf import FPDF


class PDF(FPDF):
    def header(self):

        # Setting font: helvetica bold 20
        self.set_font("helvetica", "B", 20)
        # Printing title:
        self.cell(0, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)
    def set_auto_page_break(self, auto, margin=0):
        self.auto = auto
        self.b_margin = margin


def main():
    pdf = PDF(format=(210, 297))
    pdf.add_page()
    pdf.image("shirtificate.png")
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(50, 20, 'Powered by FPDF.', align='C')
    pdf.output("test.pdf")






if __name__ == "__main__":
    main()
