def warmup():
    #Dictionary of prices
    bulbs_prices = dict([("daffodil", 0.35), ("tulip", 0.33), ("crocus", 0.25), ("hyacinth", 0.75), ("bluebell", 0.50)])

    #Dictionary of Mary's order
    Marys_order = dict([("daffodil", 50), ("tulip", 100)])

    #Updates the prices of the tulips due to demand
    bulbs_prices["tulip"] = round((bulbs_prices["tulip"] * 1.25),2) #Raises prices by 25% and rounds to 2 decimal places

    #Updating Mary's order
    Marys_order.update([("hyacinth",30)])

    #Uses the lambda function to sort the order names "x[0]" in alphabetical order. Note the lambda function provides the user the
    #ability to use functions inside of another function, list or dictionary without looping over anything
    bulbs_sorted = dict(sorted(bulbs_prices.items(), key=lambda x: x[0].lower()))
    order_sorted = dict(sorted(Marys_order.items(), key=lambda x: x[0].lower()))

    #Displaying and calculating the order for Mary
    total = 0
    num_bulbs = 0
    print("\nYou have purchased the following bulbs:")
    for x in bulbs_sorted.keys(): #Loops over the dictionary keys of the bulbs
        val1 = bulbs_sorted[x]
        for y in order_sorted.keys(): #Loops over the dictionary keys of the order
            val2 = order_sorted[y]
            if x == y: #Checks to see if the keys match values
                total += val1*val2 #Adds the order value to the total
                num_bulbs += val2 #Adds the number of bulbs to the num_bulbs variable
                #As per the instructions:
                #field width: 5 left-aligned
                #field width: 4 right-aligned
                #field width: 6 right-aligned 2 decimal places 
                print("{:<5}".format(y[0:3].upper()) + " * " + "{:>4}".format(str(val2)) + " = $" + "{:>6.2f}".format(val1*val2))
   
    #Display Mary's order
    print("\nThank you for purchasing {:1} bulbs from Bluebell Greenhouses\n Your total comes to ${:1.2f}".format(num_bulbs,total))

warmup()