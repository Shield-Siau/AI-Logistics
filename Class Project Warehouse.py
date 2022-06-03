class Product: #Parent of the class Product
    def __init__(self, name, width, length, height, weight_of_case, UPC, quantity):   #the __init__() is a method. Initializer, constructor.
        self.name = name   #parameters are the variables attached to the method.
        self.width = width
        self.length = length
        self.height = height
        self.weight_of_case = weight_of_case
        self.UPC = UPC
        self.quantity = quantity
        print("Product Created.")

"""
class Toilet_Paper(Product): #This is just to test the inheritance of the value
    pass #This would be considered the sibling of the Product class

class Snacks(Product): #This is just to test the inheritance of the value
    pass #This would be considered the sibling of the Product class
"""
class New_Product: #Parent of the class New_Product
    def __init__(self, new_name, new_width, new_length, new_height, new_weight_of_case, new_UPC, new_quantity):
        self.new_name = new_name  # parameters are the variables attached to the method.
        self.new_width = new_width
        self.new_length = new_length
        self.new_height = new_height
        self.new_weight_of_case = new_weight_of_case
        self.new_UPC = new_UPC
        self.new_quantity = new_quantity
        print("New Product Created.")
"""
class Drinks(New_Product): #This is just to test the inheritance of the value
    pass #This would be considered the sibling of the Product class
"""
p = Product(input("Name of Product: "), float(input("Width of case: ")), float(input("Length of case: ")), float(input("Height of case: ")),
            float(input("Weight of case: ")), input("Enter UPC: "), input("Enter amount of pieces: "))  #This is how you create a new product.

weight_of_case = p.weight_of_case #This gets the attribute within p.

def casesremaining(total_cases, cases_selected):
    return total_cases - cases_selected #if user enters more cases than are available to select, user should get a message saying "you canot select more cases than you have

def totalweight(weight_of_case, total_cases):
    return weight_of_case * total_cases

def weight_of_cases_selected(cases_selected, weight_of_case):
    return cases_selected * weight_of_case

total_cases = int(input("Enter amount of total cases on pallet: "))
total_weight = totalweight(float(weight_of_case), float(total_cases))
application = 1
yes = "yes"
no = "no"

print("Product added to pallet.")

print("Total weight of pallet is: {:.2f}.".format(total_weight))
print("Total amount of cases on a pallet is: ", total_cases)

while application == 1: #Could use "for cases in pallet():"
    case_selection = (input("Do you want to select a case? yes/no: "))
    if case_selection == yes:
        select = int(input("How many cases would you like to select? "))
        cases_selected = select
        total_weight_of_cases_selected = weight_of_cases_selected(float(cases_selected), float(weight_of_case))

        def remainingweight(total_weight, total_weight_of_cases_selected):
            return total_weight - total_weight_of_cases_selected

        remaining_weight = remainingweight(float(total_weight), float(total_weight_of_cases_selected))
        if cases_selected == select:
            total_cases_remaining = casesremaining(int(total_cases), int(cases_selected))
            total_cases = total_cases_remaining #Forgot to update the original variable from input.
            total_weight = remaining_weight #Same here. Remember to update variables as the program goes.
            print("Total weight now is: {:.2f}".format(remaining_weight))
            print("You know have ", total_cases_remaining, " cases remaining.")
        #work on this
            if cases_selected > total_cases: 
                print("You cannot select more than what is available on the pallet.")
                print("You need to order more.") #make a def or modify the actual def already in place.
                yes = "yes" or "y" or "Yes"
                no = "no" or "n" or "No"
                order_more = input("Would you like to order more? yes/no")
                continue
        if total_cases == 0: #new part 10/1/2020
            print("Your total amount of cases on the pallet is ", total_cases_remaining, ".")
            print("You have no more cases on the pallet.")
            no = "no"
            add = "add"
            change = "change"
            add_cases = input("Would you like to add more cases on the pallet, or change product? (add/change/no) ")
            if add_cases == add:
                cases_to_add = int(input("How many cases would you like to add? "))
                total_cases = cases_to_add+total_cases_remaining
                total_weight = weight_of_case * cases_to_add
                print("You have added to your pallet, ", cases_to_add, " more cases.")
                print("Your total cases on pallet now is: ", total_cases, ".")
                print("Your total weight of pallet now is: {:.2f}.".format(total_weight))
            elif add_cases == change: 
                new_p = New_Product(input("Name of Product: "), float(input("Width of case: ")), float(input("Length of case: ")), float(input("Height of case: ")),
                                    float(input("Weight of case: ")), input("Enter UPC: "), input("Enter amount of pieces: "))
                weight_of_case = new_p.new_weight_of_case  # This gets the attribute within p.
                total_cases = int(input("Enter amount of total cases on pallet: "))  # problem is not changing the value after input.
                total_weight = totalweight(float(weight_of_case), float(total_cases))
                print("New Product added to pallet.")
                print("Total weight of pallet is: {:.2f}.".format(total_weight))
                print("Total amount of cases on a pallet is: ", total_cases)
                continue
            else:
                if add_cases == no:
                    print("Thank you for using our application.")
                    break
    else:
        if case_selection == no or application == 0:
            print("Thank you for using our application.")
            break
