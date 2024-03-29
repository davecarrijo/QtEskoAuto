# importing the required modules
import PyPDF2

def PDFrotate(origFileName, newFileName, rotation):

    # creating a pdf File object of original pdf
    pdfFileObj = open(origFileName, 'rb')

    # creating a pdf Reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # creating a pdf writer object for new pdf
    pdfWriter = PyPDF2.PdfWriter()

    # rotating each page
    for page in range(len(pdfReader.pages)):

        # creating rotated page object
        pageObj = pdfReader.pages[page]
        pageObj.rotate(rotation)

        # adding rotated page object to pdf writer
        pdfWriter.add_page(pageObj)

        # new pdf file object
        newFile = open(newFileName, 'wb')

        # writing rotated pages to new file
        pdfWriter.write(newFile)

    # closing the original pdf file object
    pdfFileObj.close()

    # closing the new pdf file object
    newFile.close()


def main():

    # original pdf file name
    origFileName = 'example.pdf'

    # new pdf file name
    newFileName = f"{origFileName} Altered.pdf"

    # rotation angle
    rotation = 180

    # calling the PDFrotate function
    PDFrotate(origFileName, newFileName, rotation)

if __name__ == "__main__":
    # calling the main function
    main()
