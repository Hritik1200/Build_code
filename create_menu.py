
# -- User input section
# Enter Product List Size : 4
# Enter Product 1 -
# Samosa
# Enter Product 2 -
# Kachori
# Enter Product 3 -
# Fafda
# Enter Product 4 -
# Jalebi

# Enter Samosa Price :
# 300/-
# Enter Kachori Price :
# 100/-
# Enter Fafda Price :
# 100/-
# Enter Jalebi Price :
# 200/-

# --- output

# samosa = 300
# kachori = 100
# fafda = 100
# jalebi = 200

inp_range = int(input("enter range : "))
menu_w_price = []

for i in range(inp_range):
    item = input("enter item : ")
    price = int(input("enter price : "))
    menu = [f"{item} = {price}"]
    menu_w_price.append(menu)
print(menu_w_price)
