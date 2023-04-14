email = "   some.@.email@gmail.com.   "

email = email.strip()
split_email = email.split(".")
print(split_email)
for st in split_email:
    if(st == "" or st == "@"):
        split_email.remove(st)

email = ".".join(split_email)

split_email = email.split("@")
for st in split_email:
    if(st == ""):
        split_email.remove(st)

if(len(split_email) != 2):
    print("Invalid email")
    exit()
    
domain = split_email[1]
split_domain = domain.split(".")
if(len(split_domain) != 2):
    print("Invalid email")
    exit()


print(email)