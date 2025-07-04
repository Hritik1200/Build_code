
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
total = 0
for i in range(inp_range):
    item = input(f"enter item {i+1}: ")
    price = int(input(f"enter price {i+1}: "))
    total = total+price
    menu = (f"{item} = {price}")
    menu_w_price.append(menu)
print(menu_w_price)

print("Do You Want to add GST [Y/N]")
gst_inp = input("enter yes or no : ")
print(gst_inp)
a = "yes"
if gst_inp == a:
    print(f"Total = {total}")
    print("GST = 18%")
    Final = ((total *18)/100)
    print(f"Final Total = {Final+total}")
else:
    print(menu_w_price)
    print(f"Total = {total}")
