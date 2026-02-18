
def main():
	capacity = 60.0
	fuel = capacity / 2

	while True:
		print("\nMenu:")
		print("1. Add fuel (liters)")
		print("2. Remove fuel (liters)")
		print("3. Show current percent full")
		print("4. Exit")
		choice = input("Choose an option: ").strip()

		if choice == '1':
			val = input("Liters to add: ").strip()
			try:
				amt = float(val)
			except ValueError:
				print("Error: invalid amount!")
				continue
			if fuel + amt > capacity:
				print("Error: too much fuel!")
			else:
				fuel += amt

		elif choice == '2':
			val = input("Liters to remove: ").strip()
			try:
				amt = float(val)
			except ValueError:
				print("Error: invalid amount!")
				continue
			if fuel - amt < 0:
				print("Error: not enough fuel!")
			else:
				fuel -= amt

		elif choice == '3':
			percent = (fuel / capacity) * 100
			print(f"{percent:.2f}% full")

		elif choice == '4':
			print("Exiting.")
			break

		else:
			print("Invalid option; please choose 1-4.")


if __name__ == '__main__':
	main()

