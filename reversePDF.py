# This program reverses reverses a PDF's pages and saves it as 'reverse_{filename}'.
# requires PyPDF2; install with "pip install PyPDF2" or "pip3 install PyPDF2 "

#!/usr/local/bin/python3
from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()

    mainFile = paths
    # insertFile = paths[1]

    # insertFile_pdf_reader = PdfReader(insertFile)
    # insert = insertFile_pdf_reader.pages[0]

    try:
        pdf_reader = PdfReader(mainFile)
    except FileNotFoundError:
        print("File not found. Re-enter file path.")
        main()
            
    

    for i in range(1):
        
        # for page in range(pdf_reader.getNumPages()):
        # print(len(pdf_reader.pages))
        totalPages = len(pdf_reader.pages)-1
        page = totalPages
        while page >= 0:
            # print(page)
            pdf_writer.add_page(pdf_reader.pages[page])
            page-=1

        #     print(len(pdf_reader.pages))
        #     pdf_writer.add_page(insert)
        #     pdf_writer.add_page(pdf_reader.pages[page])


    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

    print("Success!")
    main()


# if __name__ == '__main__': # keep for script
def main():
    print()
    print("***This program reverses reverses a PDF's pages and saves it as 'reverse_{filename}'.***")
    print()

    file1 = input("Enter the file name or path: ")
    merge_pdfs(file1, output=f'reversed_{file1}')



main()
