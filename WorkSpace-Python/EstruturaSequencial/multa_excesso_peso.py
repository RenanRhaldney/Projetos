weight = float(input("Inform how much Kilos of fish you fished.\n"))
excess = weight - 50
fine = excess * 4

print("you fished {}Kg more than should, so you will have to pay a fine R${}".format(excess, round(fine, 2)))