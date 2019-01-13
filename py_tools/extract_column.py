import sys, getopt

def main(argv):
    inputfile = ""
    outputfile = ""
    column = 0
    seperator = " "

    try:
        opts, args = getopt.getopt(argv, "i:o:c:s:")

        for opt, arg in opts:
            if opt == "-i":
                inputfile = arg
            elif opt == "-o":
                outputfile = arg
            elif opt == "-c":
                column = int(arg)
            elif opt == "-s":
                seperator = arg

        f = open(inputfile, "r")

        lines = f.readlines()
        results = []
        for line in lines:
            results.append(line.split(seperator)[column])
        f.close()

        if outputfile == "":
            print(results)
        else:
            f = open(outputfile, "w")
            for r in results:
                f.write(r)
                f.write("\n")
            f.close()

    except getopt.GetoptError:
        print("extract_column.py -i <inputfile> -o <outputfile> -c <column> -s <seperator>")
        exit(2)

    except FileNotFoundError:
        print("You need to input an txt file. Usage is as follows:")
        print("extract_column.py -i <inputfile> -o <outputfile> -c <column> -s <seperator>")


if __name__ == "__main__":
    main(sys.argv[1:])
