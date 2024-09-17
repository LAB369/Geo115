# Nested If-Else Statements Example: Age Category
def age_category():
    age = int(input("Enter your age: "))
    if age < 13:
        print("You are a child.")
    elif 13 <= age < 20:
        print("You are a teenager.")
    elif 20 <= age < 65:
        print("You are an adult.")
    else:
        print("You are a senior.")

# Multiple Conditions Example: Positive, Negative, or Zero
def number_check():
    number = int(input("Enter a number: "))
    if number > 0:
        print("Positive number")
    elif number == 0:
        print("Zero")
    else:
        print("Negative number")

# Boolean Operations Example: Valid Email
def email_validation():
    email = input("Enter your email: ")
    if "@" in email and "." in email:
        print("Valid email address")
    else:
        print("Invalid email address")

#select one of the following from the programs
def main():
    print("Select an option:")
    print("1. Age Category")
    print("2. Positive, Negative, or Zero")
    print("3. Valid Email")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        age_category()
    elif choice == 2:
        number_check()
    elif choice == 3:
        email_validation()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()