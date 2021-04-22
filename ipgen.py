import random

def pub_ip(pip_quantity_input):   
    for x in range(pip_quantity_input):
        octet1 = random.randint(1, 254)
        octet2 = random.randint(1, 254)
        octet3 = random.randint(1, 254)
        octet4 = random.randint(1, 254)
        if((octet1 == 10) or (octet1 == 172 and (octet2 >= 16 or octet2 <= 31)) or (octet1 == 192 and octet2 == 168)):
            pub_ip(x)
        else:
            print(octet1, ".", octet2, ".", octet3, ".", octet4)

    print("Done. ")
def priv_ip(privip_quantity_input):
    for x in range(privip_quantity_input):
        type = random.randint(1, 3)
        if(type == 1):
            octet1 = 10
            octet2 = random.randint(1, 254)
            octet3 = random.randint(1, 254)
            octet4 = random.randint(1, 254)
            print(octet1, ".", octet2, ".", octet3, ".", octet4)
        if(type == 2):
            octet1 = 172
            octet2 = random.randint(16, 31)
            octet3 = random.randint(1, 254)
            octet4 = random.randint(1, 254)
            print(octet1, ".", octet2, ".", octet3, ".", octet4)
        if(type == 3):
            octet1 = 192
            octet2 = 168
            octet3 = random.randint(1, 254)
            octet4 = random.randint(1, 254)
            print(octet1, ".", octet2, ".", octet3, ".", octet4)
    print("Done. ")

main_input = input("Options: \n[1] Public IPv4\n[2] Private IPv4\n> ")

if(main_input == "1"):
    pip_quantity_input = input("Quantity? ")
    pub_ip(int(pip_quantity_input))

if(main_input == "2"):
    privip_quantity_input = input("Quantity? ")
    priv_ip(int(privip_quantity_input))

