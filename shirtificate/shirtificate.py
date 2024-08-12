from fpdf import FPDF
from fpdf.enums import Align

class PDF(FPDF):
    def header(self):

        # Setting font: helvetica bold 20
        self.set_font("helvetica", "B", 25)
        # Printing title:
        self.cell(0, 40, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)
    def set_auto_page_break(self, auto, margin=0):
        self.auto = auto
        self.b_margin = margin


def main():
    pdf = PDF(format=(210, 297))
    pdf.add_page()
    pdf.image("shirtificate.png", x=15, y=78, w=180, keep_aspect_ratio=True)
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 20, 'Powered by FPDF.', align='C')
    pdf.output("test.pdf")






if __name__ == "__main__":
    main()
