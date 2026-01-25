Stock = {}

while True:
 print('details')
 print("1. display stock")
 print('2. add products')
 print('3. update quantity')
 print('4. sell product')
 print('5. exit')

#display stock
 choice = int(input("enter your choice"))
 if choice == 1:
  if not Stock:
   print("no stock")
  else:
   print("product details")
   for pid, details in Stock.items():
    print(f"id:{pid},name: {details['name']},price: {details['price']},quantity: {details['quantity']}")

#add products
 elif choice == 2:
  pid = int(input("enter the product id"))
  if pid in Stock:
   print("product exists")
  else:
   name = input("enter the name")
   quantity = int(input("enter the quantity"))
   price = float(input("enter the price"))
   
   Stock[pid]={
    'name':name,
    'quantity' :quantity,
    'price': price
   }
   print("product added successfully")

   #update quantity
 elif choice == 3:
    pid = input("enter product id")
    if pid in Stock:
      new_quantity = int(input("enter the quantity"))
      Stock[pid]['quantity'] = new_quantity
      print("stock updates successfully")
    else:
     print("not updated")

 elif choice == 5:
        print("Exiting program...")
        break

 else:
        print("Invalid choice")
