import math
# Function for Basic EOQ Model
def basic_eoq(lmbda, A, IC):
    return math.sqrt((2 * lmbda * A) / IC)

# Function for EOQ Model with Quantity Discounts (EPQ)
def epq(lmbda, A, IC, psi):
    return math.sqrt(((2 * lmbda * A) * psi) / (IC * (psi - lmbda)))

# Function for EOQ Model with Shortages
def eoq_with_shortages(lmbda, A, IC, pi):
    return math.sqrt(((2 * lmbda * A) * (IC + pi)) / (IC * pi))

# Function for EOQ Model with Shortages and Finite Production Rate
def eoq_with_shortages_and_finite_production(lmbda, A, IC, pi, psi):
    return math.sqrt((2 * lmbda * A * (IC + pi) * psi) / (IC * (psi - lmbda) * pi))

# Dictionary to map model choices to functions
eoq_models = {
    1: {"name": "Basic EOQ Model", "function": basic_eoq},
    2: {"name": "EOQ Model with Quantity Discounts (EPQ)", "function": epq},
    3: {"name": "EOQ Model with Shortages", "function": eoq_with_shortages},
    4: {"name": "EOQ Model with Shortages and Finite Production Rate", "function": eoq_with_shortages_and_finite_production}
}

# Main program loop
def eoq_calculator():
    repeat = True
    while repeat:
        print("Welcome to Inventory Management - Economic Order Quantity (EOQ) Calculator")
        for key, model in eoq_models.items():
            print(f"{key}. {model['name']}")

        choice = int(input("Enter your choice (1-4): "))

        # Check if the choice is valid
        if choice in eoq_models:
            model = eoq_models[choice]
            print(f"You selected: {model['name']}")

            # Prompt for the necessary inputs based on the chosen model
            if choice == 1:
                demand = float(input("Enter annual demand: "))
                ordering_cost = float(input("Enter ordering cost per order: "))
                holding_cost = float(input("Enter holding cost per unit: "))
                result = model["function"](demand, ordering_cost, holding_cost)
            
            elif choice == 2:
                demand = float(input("Enter annual demand: "))
                ordering_cost = float(input("Enter ordering cost per order: "))
                holding_cost = float(input("Enter holding cost per unit: "))
                production_rate = float(input("Enter production rate: "))
                result = model["function"](demand, ordering_cost, holding_cost, production_rate)
            
            elif choice == 3:
                demand = float(input("Enter annual demand: "))
                ordering_cost = float(input("Enter ordering cost per order: "))
                holding_cost = float(input("Enter holding cost per unit: "))
                shortage_cost = float(input("Enter shortage cost per unit per year: "))
                result = model["function"](demand, ordering_cost, holding_cost, shortage_cost)
            
            elif choice == 4:
                demand = float(input("Enter annual demand: "))
                ordering_cost = float(input("Enter ordering cost per order: "))
                production_rate = float(input("Enter production rate: "))
                holding_cost = float(input("Enter holding cost per unit: "))
                shortage_cost = float(input("Enter shortage cost per unit per year: "))
                result = model["function"](demand, ordering_cost, holding_cost, shortage_cost, production_rate)

            print(f"The result for {model['name']} is: {result}")

        else:
            print("Invalid choice. Please enter a valid option.")

        # Ask if the user wants to repeat
        repeat = input("Do you want to calculate another model? Enter 'yes' for yes and 'no' for no: ").lower() == 'yes'

# Call the function to run the program
eoq_calculator()