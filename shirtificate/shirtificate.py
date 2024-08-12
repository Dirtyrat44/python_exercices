from fpdf import FPDF
from fpdf.enums import Align

class PDF(FPDF):
    def header(self):

        # Setting font: helvetica bold 50
        self.set_font("helvetica", "B", 50)
        # Printing title:
        self.cell(0, 70, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)
    def set_auto_page_break(self, auto, margin=0):
        self.auto = auto
        self.b_margin = margin


def main():
    user_input = input("Name: ")
    pdf = PDF(format=(210, 297))
    pdf.add_page()
    pdf.image("shirtificate.png", x=15, y=78, w=180, keep_aspect_ratio=True)
    pdf.set_font('helvetica', 'B', 25)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(0, 200, user_input, align='C')
    pdf.output(f"{user_input}.pdf")






if __name__ == "__main__":
    main()
