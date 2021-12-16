print("Informed the voleu from their spending fixed.")

food = float(input("Food: R$"))
light = float(input("Light: R$"))
internet = float(input("Internet: R$"))
water = float(input("Water: R$"))
gas = float(input("Gas: R$"))
sum = food + light + internet + water + gas

print(f"\nFood: R${food:.2f}\n"
      f"Light: R${light:.2f}\n"
      f"Internet: R${internet:.2f}\n"
      f"Water: R${water:.2f}\n"
      f"Gas: R${gas:.2f}\n\n"
      f"Sum: R${sum:.2f}")
