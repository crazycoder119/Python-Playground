# us dollars to pound converter

def us_dollar_to_pounds_converter(dollars):
    pounds = lambda dollars : dollars * 0.92
    return pounds(dollars)


def main():
    print("This is us dollars to pund converter ....")
    dollars = eval(input("Please enter the amount in dollars : "))
    pounds = us_dollar_to_pounds_converter(dollars)
    print("The", dollars,"dollars is equals to", pounds, "pounds")

main()