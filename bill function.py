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

bill(3000,18,20)