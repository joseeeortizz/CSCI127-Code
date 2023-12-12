############################################
def prob4():
    verse = "jam tomorrow and jam yesterday,"
    print("The rule is,")
    c = mystery(verse) #2
    w = enigma(verse, c)
    print(c, w)


def mystery(v):
    print(v) # how many times it is present on the code
    c = v.count("jam")
    return (c)


def enigma(v, c):
    print("but never", v[-1])
    for _ in range(c):
        print("jam")
    return ("day.")


prob4()


############################################

############################################
def totalWithTax(food, tip):
    tax = 0.1 * food
    return (food + tax + tip)


lunch = float(input("Enter lunch total: "))
l_tip = float(input("Enter lunch tip: "))
l_total = totalWithTax(lunch, l_tip)
print("Lunch total is", l_total)

dinner = float(input("Enter dinner total: "))
d_tip = float(input("Enter dinner tip: "))
d_total = totalWithTax(dinner, d_tip)
print("Dinner total is", d_total)


############################################

############################################
def month_string(month_num):
    months = ["January", "February", "March", "April", \
              "May", "June", "July", "August", "September", \
              "October", "November", "December"]

    return (months[month_num - 1])


def main():
    n = int(input("Enter the number of the month: "))
    month_name = month_string(n)
    print("The month is", month_name)


main()
############################################