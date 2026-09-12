<<<<<<< HEAD
all_products=[]
for i in  range(2):
    E_Commerce=dict()
    order_id=int(input("Enter order id:"))
    Product_name=input("Enter product_name:")
    Price=float(input("Enter Price:"))
    Qty=int(input("Enter Qty:"))
    City=input("Enter City:")
    Payment_Method=input("Enter COD,UPI,Net_Banking:")
    if Payment_Method not in("COD","UPI","Net_Banking"):
        print("Invalid Payment Method")
        break
    amount=Price*Qty
    

    
=======
all_products=[]
for i in  range(2):
    E_Commerce=dict()
    order_id=int(input("Enter order id:"))
    Product_name=input("Enter product_name:")
    Price=float(input("Enter Price:"))
    Qty=int(input("Enter Qty:"))
    City=input("Enter City:")
    Payment_Method=input("Enter COD,UPI,Net_Banking:")
    if Payment_Method not in("COD","UPI","Net_Banking"):
        print("Invalid Payment Method")
        break
    amount=Price*Qty
    

    
>>>>>>> d9ee51f0cc5c114ccd731eff574942c21419d1af
    