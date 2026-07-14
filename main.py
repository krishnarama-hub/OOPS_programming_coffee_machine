from coffeee_maker_machine import MENU, Coffee_maker, MoneyMachine

menu = MENU()
coffee_maker = Coffee_maker(300, 200, 100)
money_machine = MoneyMachine()

machine_on = True

while machine_on:

    print("\nAvailable Drinks:")
    menu.get_item()
    print()

    choice = input("\nWhat would you like? ").lower()

    if choice == "off":
        machine_on = False
        print("Coffee Machine Turned Off.")

    elif choice == "report":
        coffee_maker.report()
        print(f"Money: ${money_machine.report()}")

    else:
        drink = menu.find_drink(choice)

        if drink is None:
            continue

        if coffee_maker.is_resourse_sufficient(drink):

            if money_machine.make_payment(drink):

                coffee_maker.make_coffee(drink)
                print(f"\nHere is your {drink.name}. Enjoy! ☕")