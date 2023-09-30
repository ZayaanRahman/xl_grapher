import numpy as np
import matplotlib.pyplot as plt
import sys
import processing as proc


def main():

    # separate arg vals with space to make filename
    file_name = " ".join(sys.argv[1:])
    # file_name = "Test File.xlsx"  # TEMPORARY

    data = proc.get_data(file_name)

    # options loop
    while True:
        args = parse_args(input("xl_grapher: "))

        # terminate loop
        if args[0] == "end":
            print("ending...")
            break

        # provide commands
        if args[0] == "help":
            help()

        # print current data
        elif args[0] == "data":
            print(data)

        # make a graph with matplotlib
        elif args[0] == "graph":
            print("graphing...")
            if len(args) == 3:
                plt.scatter(data[args[1]], data[args[2]])
                plt.xlabel(args[1])
                plt.ylabel(args[2])
                plt.grid(True)

                plt.show()
            else:
                print("invalid argument.")

        # make a histogram
        elif args[0] == "histo":
            print("histo")

        # print mean
        elif args[0] == "mean":
            if len(args) == 2:
                print(np.mean(data[args[1]]))
            else:
                print("invalid argument.")

        # print the POPULATION standard deviation
        elif args[0] == "std":
            if len(args) == 2:
                print(np.std(data[args[1]], ddof=1))
            else:
                print("invalid argument.")

        # print the standard error of the mean, or standard deviation of the mean
        elif args[0] == "sem":
            if len(args) == 2:
                print(np.std(data[args[1]], ddof=1) /
                      np.sqrt(len(data[args[1]])))
            else:
                print("invalid argument.")

        # print median
        elif args[0] == "median":
            if len(args) == 2:
                print(np.median(data[args[1]]))
            else:
                print("invalid argument.")

        # print mode; excluded for now bc not in numpy

        # unfamiliar command
        else:
            print("unfamiliar command.")


# return array of user arguments
# form of arguments: "function arg1, arg2, arg3"
def parse_args(user_input):
    args = [user_input.split()[0]]  # first arg is "function"
    args = args + [arg.strip() for arg in user_input[len(args[0]):].split(',')]
    return args

# print help info
def help():
    print("\nCommands are issued in the form of 'function_name arg1, arg2, arg3'.")
    print("Args must be separated by commas, if needed.\n")

    print("general")
    print("------------")
    print("help: list possible functions")
    print("end: end program")
    print("data: print current data\n")

    print("graphing")
    print("------------")
    print("graph: make a scatter plot of arg1 vs arg2")
    print("histo: make a histogram of arg1\n")  # FIX

    print("statistics")
    print("------------")
    print("mean: print the mean of arg1")
    print("std: print the standard deviation of arg1")
    print("sem: print the standard error of the mean of arg1")
    print("median: print the median of arg1")
    print("mode: print the mode of arg1\n")


if __name__ == "__main__":
    main()
