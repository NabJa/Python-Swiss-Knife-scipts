import sys
import getopt
import os
import re
from PyPDF2 import PdfFileMerger


def main(argv):

    try:
        opts, args = getopt.getopt(argv, "d:o:n:")

        assert opts != [] or args != [], "No arguments given! Use like: merge_pdf.py -d <directory> -o <output-directory> -n <result name>"

        merger = PdfFileMerger()

        directory = os.path.dirname(os.path.realpath(__file__))
        output = os.path.dirname(os.path.realpath(__file__))
        name = "merged_result.pdf"

        for opt, arg in opts:
            if opt == "-d":
                directory = arg

            elif opt == "-o":
                output = arg

            elif opt == "-n":
                name = arg

        for pdf in os.listdir(directory):
            if re.search(r"(\.pdf)$", pdf):
                merger.append(open(os.path.join(directory, pdf), 'rb'))

        with open(os.path.join(output, name), 'wb') as fout:
            merger.write(fout)

    except getopt.GetoptError:
        print("merge_pdf.py -d <directory> -o <output-directory> -n <result name>")


if __name__ == "__main__":
    main(sys.argv[1:])
