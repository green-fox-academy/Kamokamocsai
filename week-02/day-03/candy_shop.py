shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list. 
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)

# shop_items[1] = "Croissant"
# shop_items[3] = "Ice cream"

for i in shop_items:
    if i is 2:
        shop_items[i-1] = "Croissant"
    elif i == False:
        shop_items[i-1] = "Ice cream"


print(shop_items)