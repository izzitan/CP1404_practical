def main():
    while True:
        number_of_items = int(input("Number of items: "))
        if number_of_items <= 0:
            print("Invalid input")
        else:
            break
    total_price = [0]
    for i in range(number_of_items):
        while True:
            price = float(input("Price of item: "))
            if price <= 0:
                print("Invalid input")
            else:
                total_price.append(price)
                break
    if sum(total_price) >= 100:
        discount_price = sum(total_price) * 0.9
    else:
        discount_price = sum(total_price)
    print("Total price for {} items is ${:0.2f}".format(number_of_items, discount_price))


main()
