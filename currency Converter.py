def main():
    print("This program converts US dollars to Indian Rupees (INR)")
    print()

    dollars = eval(input("Enter amount in US dollars: "))

    inr = convert_to_inr(dollars)

    print("That is", inr, "Indian Rupees.")

convert_to_inr = lambda dollars: dollars * 73.78  

main()
