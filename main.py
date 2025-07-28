from tabulate import tabulate
from colorama import Fore, Style, init
import datetime

# 🛠️ Initialize colorama
init(autoreset=True)

# 📤 Save output to file (Optional)
def save_to_file(input_table, output_table, driver_profit, fair_fare, fare_per_passenger):
    filename = f"wagon_fare_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("=== 📥 INPUT SUMMARY ===\n")
        file.write(tabulate(input_table, headers=["Input", "Value"], tablefmt="grid"))
        file.write("\n\n=== 📤 OUTPUT REPORT ===\n")
        file.write(tabulate(output_table, headers=["Output", "Value"], tablefmt="grid"))

        if fare_per_passenger > fair_fare:
            file.write("\n\n⚠️  Overcharging detected. This goes against Islamic fairness principles.\n")
        elif fare_per_passenger < fair_fare:
            file.write("\n\nℹ️  Undercharging. Driver may not earn a fair amount.\n")
        else:
            file.write("\n\n✅  Current fare is fair according to the calculation.\n")
    print(Fore.GREEN + f"\n📁 Report saved as: {filename}")

# 🔍 Validate float input
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "❌ Invalid input. Please enter a valid number.")

# 🔍 Validate integer input
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(Fore.RED + "❌ Invalid input. Please enter a valid integer.")

# 🏛️ Islamic Fair Profit Range
def get_fair_profit_range(distance):
    if distance <= 10:
        return (200, 400)
    elif distance <= 20:
        return (400, 600)
    elif distance <= 30:
        return (600, 800)
    elif distance <= 40:
        return (800, 1000)
    else:
        return (1000, 1500)

# 🔢 Main Function
def wagon_fare_calculator():
    print(Fore.CYAN + Style.BRIGHT + "\n=== 🚐 Wagon Fare Profit Calculator ===\n")

    # 📝 Inputs
    distance_km = get_valid_float("📍 Enter total distance (in km): ")
    petrol_price_per_litre = get_valid_float("⛽ Enter petrol price per litre (Rs.): ")
    fuel_average = get_valid_float("🚐 Enter fuel average of wagon (km per litre): ")
    passengers = get_valid_int("👥 Enter total number of passengers: ")
    fare_per_passenger = get_valid_float("🎫 Enter current fare per passenger (Rs.): ")
    metropolitan_tax = get_valid_float("🏛️ Enter metropolitan (Toll) tax (Rs.): ")

    # 📘 Islamic Fair Profit Range (shown before asking desired profit)
    fair_min, fair_max = get_fair_profit_range(distance_km)
    print(Fore.BLUE + f"\n📘 Recommended Fair Profit Range for {distance_km:.0f} km: Rs. {fair_min} – Rs. {fair_max}")

    # 💡 Islamic Guidance
    print(Fore.YELLOW + "\n💬 According to Islamic teachings:")
    print(Fore.YELLOW + "✅ A fair profit is allowed based on distance.")
    print(Fore.YELLOW + "❌ Taking excessive profit is considered zulm (injustice).\n")

    # 🤝 Desired profit input
    desired_profit = get_valid_float("🤝 Enter your desired profit (Rs.): ")

    # 📗 Teaching based on distance range
    if desired_profit < fair_min:
        print(Fore.YELLOW + "⚠️  This profit is below the recommended range. You might be undercharging.")
    elif desired_profit > fair_max:
        print(Fore.RED + "❌ This profit is too high for this distance. May be considered zulm (injustice) in Islam.")
    else:
        print(Fore.GREEN + "✅ Your desired profit is within the fair Islamic range for this distance.")

    # 📊 Calculations
    petrol_needed = distance_km / fuel_average
    petrol_cost = petrol_needed * petrol_price_per_litre
    total_expense = petrol_cost + metropolitan_tax
    total_collected = passengers * fare_per_passenger
    driver_profit = total_collected - total_expense
    fair_fare = (total_expense + desired_profit) / passengers

    # 📋 Input Table
    input_table = [
        ["Total Distance (km)", f"{distance_km} km"],
        ["Petrol Price per Litre", f"Rs. {petrol_price_per_litre}"],
        ["Wagon Fuel Average", f"{fuel_average} km/litre"],
        ["Total Passengers", f"{passengers}"],
        ["Current Fare per Passenger", f"Rs. {fare_per_passenger}"],
        ["Metropolitan Tax", f"Rs. {metropolitan_tax}"],
        ["Desired Profit", f"Rs. {desired_profit}"]
    ]

    # 📊 Output Table
    output_table = [
        ["Fuel Needed", f"{petrol_needed:.2f} litres"],
        ["Petrol Cost", f"Rs. {petrol_cost:.2f}"],
        ["Total Expenses", f"Rs. {total_expense:.2f}"],
        ["Total Collected Fare", f"Rs. {total_collected:.2f}"],
        ["Driver's Current Profit", f"Rs. {driver_profit:.2f}"],
        ["Suggested Fair Fare per Passenger", f"Rs. {fair_fare:.2f}"]
    ]

    # 🖨️ Display Tables
    print(Fore.MAGENTA + Style.BRIGHT + "\n=== 📥 INPUT SUMMARY ===")
    print(Fore.WHITE + tabulate(input_table, headers=["Input", "Value"], tablefmt="fancy_grid"))

    print(Fore.MAGENTA + Style.BRIGHT + "\n=== 📤 OUTPUT REPORT ===")
    print(Fore.WHITE + tabulate(output_table, headers=["Output", "Value"], tablefmt="fancy_grid"))

    # ⚖️ Fairness Message
    if fare_per_passenger > fair_fare:
        print(Fore.RED + "\n⚠️  Overcharging detected. This goes against Islamic fairness principles.")
    elif fare_per_passenger < fair_fare:
        print(Fore.YELLOW + "\nℹ️  Undercharging. Driver may not earn a fair amount.")
    else:
        print(Fore.GREEN + "\n✅ Current fare is fair according to the calculation.")

    # 💾 Ask to Save
    choice = input(Fore.CYAN + "\n💾 Do you want to save this report to a file? (y/n): ").strip().lower()
    if choice == 'y':
        save_to_file(input_table, output_table, driver_profit, fair_fare, fare_per_passenger)

# 🏁 Run Program
wagon_fare_calculator()
