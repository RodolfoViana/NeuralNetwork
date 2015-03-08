__author__ = 'rodolfo'

#This program creates a csv file


def buildFile():
    file_in = open("train_errors", "r")

    file_out = open("train_errors.csv", "a")
    ##file_in.map(lambda l: l.split(" ")).reduce(lambda l: )

    for line in file_in:
        for each_line in line.split(","):
            file_out.write(each_line.strip() + "\t")

    file_in.close()
    file_out.close()

# Main
def main():
    buildFile()
    pass


if __name__ == '__main__':
    main()