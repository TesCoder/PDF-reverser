# This program exports in reverse order (last page will be first and first page will be last) and saves it as 'reversed_{filename}'.
# requires PyPDF2; install with "pip install PyPDF2" or "pip3 install PyPDF2 "

#!/usr/local/bin/python3
from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()

    mainFile = paths

    try:
        pdf_reader = PdfReader(mainFile)
    except FileNotFoundError:
        print("File not found. Re-enter file path.")
        main()
            
    for i in range(1):
        totalPages = len(pdf_reader.pages)-1
        page = totalPages
        while page >= 0:
            pdf_writer.add_page(pdf_reader.pages[page])
            page-=1

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

    print("Success!")
    main()


# if __name__ == '__main__': # keep for script
def main():
    print()
    print("***This program exports in reverse order (last page will be first and first page will be last) and saves it as 'reversed_{filename}'.***")
    print()

    file1 = input("Enter the file name or path: ")
    merge_pdfs(file1, output=f'reversed_{file1}')



main()
