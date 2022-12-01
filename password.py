i=1
passwordmatched=False
password=""

while i<=3:
    password=input("enter the password:")
    if password=="abc":
          passwordmatched=True
          break
    i=i+1
if passwordmatched==True:
    print("Login Succesfull!")
else:
    print("Access denied!")