def generate_bill():
    print("\n====== Generate New Bill ======")

    name = input("Enter customer name: ")
    units = float(input("Enter electricity units used: "))

    print("\nConnection Type")
    print("1. Domestic")
    print("2. Commercial")
    choice = input("Enter choice (1/2): ")

    # Energy Charge
    if choice == "1":
        type_conn = "Domestic"
        fixed_charge = 75

        if units <= 100:
            energy_bill = units * 1.5
        elif units <= 200:
            energy_bill = 100 * 1.5 + (units - 100) * 2.5
        elif units <= 300:
            energy_bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
        else:
            energy_bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 6

    elif choice == "2":
        type_conn = "Commercial"
        fixed_charge = 150

        if units <= 100:
            energy_bill = units * 2.5
        elif units <= 200:
            energy_bill = 100 * 2.5 + (units - 100) * 4
        elif units <= 300:
            energy_bill = 100 * 2.5 + 100 * 4 + (units - 200) * 6
        else:
            energy_bill = 100 * 2.5 + 100 * 4 + 100 * 6 + (units - 300) * 8
    else:
        print("Invalid choice")
        return

    subtotal = energy_bill + fixed_charge
    gst = subtotal * 0.18
    total_bill = subtotal + gst

    print("\n========== BILL RECEIPT ==========")
    print("Customer Name :", name)
    print("Connection    :", type_conn)
    print("Units Consumed:", units)
    print("Energy Charge : ₹", round(energy_bill,2))
    print("Fixed Charge  : ₹", fixed_charge)
    print("GST (18%)     : ₹", round(gst,2))
    print("-------------------------------")
    print("Total Payable : ₹", round(total_bill,2))

    # Save to file
    with open("records.txt", "a") as file:
        file.write("\n-----------------------------\n")
        file.write("Customer Name : " + name + "\n")
        file.write("Connection    : " + type_conn + "\n")
        file.write("Units         : " + str(units) + "\n")
        file.write("Total Bill    : Rs." + str(round(total_bill,2)) + "\n")

    print("\nBill saved successfully!")


def view_records():
    print("\n====== Previous Records ======")
    try:
        with open("records.txt", "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("No records found yet.")


# -------- Main Menu --------
while True:
    print("\n===== Electricity Billing Menu =====")
    print("1. Generate New Bill")
    print("2. View Previous Bills")
    print("3. Exit")

    option = input("Enter option: ")

    if option == "1":
        generate_bill()
    elif option == "2":
        view_records()
    elif option == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid option")