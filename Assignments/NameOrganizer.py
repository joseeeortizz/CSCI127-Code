# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 19, 2023
# This program prints an organized name according to the prompt

def main():
    names = input("Please enter your list of names : ")
    namesList = names.split(";")
    for name in namesList:
        str = name.split(",")
        print(str[1], "", str[0])

if __name__ == '__main__':
    main()
