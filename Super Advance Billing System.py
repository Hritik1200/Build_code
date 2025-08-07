# -- User input section
# Enter Product 1 -
# Samosa
# Enter Samosa Price :
# 300/-
# Enter Samosa QT :
# 3
# -----------------------------
# Do you Want to add more [Y/N]
# Y
# Enter Product 2 -
# Kachori
# Enter Kachori Price :
# 100/-
# Enter Kachori QT :
# 2
# ----------------------------
# Do you Want to add more [Y/N]
# Y
# Enter Product 3 -
# Jalebi
# Enter Jalebi Price :
# 200/-
# Enter Jalebi QT :
# 4
# Do you Want to add more [Y/N]
# N

# Do You Want to add GST [Y/N]
# [note : if user select `N` Print bill without GST]
# [Note User select yes `Y`]
# Enter GST % = 18

# Select Offer :
# 1. FLAT 2% OFF
# 2. FLAT 4% OFF
# 3. FLAT 8% OFF
# [Note if user Select offer = then offer apply into bill] 
# if user select [ 1 ]

# -------Out put -------

# 1. Samosa = 900/-
# 2. Kachori = 200/-
# 3. Jalebi = 800/-
# -------------------
# Total = 1900
# GST = 18%
# offer = 2%
# -------------------
# Final Total = 2197.16/-
# -------------------


grand_t = 0
menu_w_price = []
item_num = 1
while True:
    item = input(f"enter item {item_num}= ").upper()
    try:
        price = int(input(f"enter price {item_num}= "))
        qty = int(input(f"enter quantity {item_num} = "))
    except ValueError:
        print("Please enter valid numeric values for price and quantity.")
        continue
    total = price * qty
    grand_t += total
    menu = (f"{item}:₹{price} x {qty} = {total}")
    menu_w_price.append(menu)
    should_continue = input("do you want to add products [Y/N]= ").strip().upper()
    print(should_continue)
    if should_continue == "Y":
        item_num += 1
    else:
        for a in menu_w_price:
            print(a)
        print(f"Final Total = {grand_t}")
        gst_input = input("Do You Want to add GST [Y/N] = ").strip().upper()
        print(gst_input)
        if gst_input == "Y":
            print("GST = 18%")
            final = ((grand_t*18)/100)
            gst_final = final+grand_t
            print(f"Total After GST = {gst_final}")
            print('''Select Offer :
        1. FLAT 2% OFF
        2. FLAT 4% OFF
        3. FLAT 8% OFF''')
            offer = int(input("Enter offer no = "))
            if offer == 1:
                flat_2 = (gst_final)*0.02
                print(f"Total price = {gst_final}")
                print(f"FLAT 2% OF = -{flat_2}")
                after_dis1 = gst_final-flat_2
                print(f"Total After Discount = {after_dis1}")

            elif offer == 2:
                flat_4 = (gst_final)*0.04
                print(f"Total price = {gst_final}")
                print(f"FLAT 4% OFF = -{flat_4}")
                after_dis1 = gst_final-flat_4
                print(f"Total After Discount = {after_dis1}")

            else:
                flat_8 = (gst_final)*0.08
                print(f"Total price = {gst_final}")
                print(f"FLAT 8% OFF = -{flat_8}")
                after_dis1 = gst_final-flat_8
                print(f"Total After Discount = {after_dis1}")

        break





