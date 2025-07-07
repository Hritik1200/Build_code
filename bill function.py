def bill (price,tax,quantity):
    pw_qua = price*quantity
    gst_amount = pw_qua*tax/100
    total_amount = (pw_qua + gst_amount)
    print("----bill----------")
    print(f"Amount = {price}")
    print(f"Quantity = {quantity}")
    print(f"Total = {pw_qua}")
    print(f"GST = {tax}%")
    print(f"GST Amount = {gst_amount}")
    print(f"Total Amount + GST = {total_amount}")

bill(3000,18,20)   # change values according to you


#  TO print multiple bills 

price = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]  # change values according to you
tax = [2,4,6,8,12,18,16,12,10,8]   ## change values according to you
quantity = [10,20,30,40,50,60,70,80,90,100]  # change values according to you

size = len(price)

for i in range(size):
    bill(price[i],tax[i],quantity[i])

