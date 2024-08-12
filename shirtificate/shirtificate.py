from fpdf import FPDF



def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)

    user_input = input("Name: ")




if __name__ == "__main__":
    main()
