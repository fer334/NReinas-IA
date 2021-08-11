import os
# read file by line and print it
def read_file(file_name):
    f = open(file_name)
    i = 0
    for line in f:
        # wait for user input
        if i % 7==0 or i%7==1:
            # clear the terminal screen
            input()
            os.system('clear')
        else:
            print(line)
        i+=1
    f.close()

read_file('a.txt')