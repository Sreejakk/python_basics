cone_type = [{'Plain Cone':1.5},{'Waffle Cone':2},{'Cup':1}]
scoop_toppings=[{'Peanuts':0.75},{'Caramel Sauce':0.5},{'Rainbow Sprincles':0.5},
                    {'Pecan':1},{'Chocolate Sprincles':0.5}]
scoop_price=0.5
scoop_flavours=['Vanila','Strawberry','Chocolate','Caramel','Mint','Coffee','Rainbow','Bubble gum']

def order():
    # num_icecreams=None
    # while num_icecreams is None:
    #     icecreams=input("Enter number of icecreams-")
    #     num_icecreams = check_num(icecreams)
    #     if num_icecreams<=0 or num_icecreams>3:
    #         print("greater than 0 less than or equals to 3")
    #         num_icecreams =  None
    
    # print("Number of icecreams",num_icecreams)

    # ice_creams = [[1, {'Plain Cone': 1.5}, [{'Caramel': 0.5}, {'Chocolate': 0.5}], [{'Pecan': 1}, {'Chocolate Sprincles': 0.5}]], [2, {'Waffle Cone': 2}, [{'Chocolate': 0.5}, {'Strawberry': 0.5}], [{'Peanuts': 0.75}]]]

    # for i in range(num_icecreams):
    #     sel_cone = select_cone_type()
    #     sel_scoops = scoops()
    #     sel_toppings = select_scoop_topping()
    #     ice_creams.append([i+1,sel_cone,sel_scoops,sel_toppings])
    total_price = 0
    for icecream in ice_creams:
        ice_cream_price = 0 
        for i in range(len(icecream)):
            if i == 0:
                print("Ice cream: ",icecream[i])py
            if i == 1:
                k = None
                for j,v in icecream[i].items():
                    k = j
                    ice_cream_price += v
                print("----Cone Type: {} - ${}".format(k,v))
            if i == 2:
                for j in icecream[i]:
                    for l,m in j.items():
                        ice_cream_price += m
                        print("----Scoop Flv:{} - ${} ".format(l,m))
            if i == 3:
                for o in icecream[i]:
                    for p,q in o.items():
                        ice_cream_price += q
                        print("----Scoops Top:{} - ${}".format(p,q))
        print("Ice Cream Price: ${}".format(ice_cream_price))
        total_price += ice_cream_price
        print("\n")
    print("Total Price: ",total_price)
def select_cone_type():
    print("Select cone type-")
    i = 0
    for cone in cone_type:        
        for ty,price in cone.items():
            i += 1
            print(i,ty,price)
    cone_id=None
    
    while cone_id is None:
        coneID = input("Enter2 cone ID : ")
        coneID=check_num(coneID)
        if coneID==1 or coneID==2 or coneID==3:
            print(coneID)
            cone_id = coneID
        else:
            print('Input should be inbetween 1 and 3')
            cone_id = None
    return cone_type[cone_id-1]

def scoops():
    num_scoops=None
    while num_scoops is None:
        scoops=input("Enter number of scoops-")
        num_scoops=check_num(scoops)
        if num_scoops<=0 or num_scoops>3:
            print("Greater than 0 and in between 3")
            num_scoops=None
    for i in range(len(scoop_flavours)):
        print(i,scoop_flavours[i],scoop_price)
    selected_scoops = []

    for i in range(num_scoops):
        selected_scoops.append({select_scoop_flavour():scoop_price})

    return selected_scoops

def select_scoop_flavour():
    print("Select scoop flavour-")
    scoop_id=None
    while scoop_id is None:
        scoopID = input("Enter scoop ID : ")
        scoopID=check_num(scoopID)
        if scoopID>=1 or scoopID>8:
            scoop_id = scoopID
        else:
            print('Input should be inbetween 1 and 8')
            scoop_id = None
    return scoop_flavours[scoop_id]

def select_scoop_topping():
    num_topping=None
    while num_topping is None:
        num_topping=input("Number of topping-")
        num_topping=check_num(num_topping)
        if num_topping<1 or num_topping>3:
            print("Select only between 1 and 3")
            num_topping=None

    selected_toppings=[]


    for i in range(num_topping):
        k=0
        for topping in scoop_toppings:
            for ty,price in topping.items():
                k += 1
            print(k,ty,price)
        topping_id=None
        while topping_id is None:
            topping_id=input("Select topping ID:")
            topping_id=(check_num(topping_id))
            if topping_id < 1 or topping_id>len(scoop_toppings):
                print("Invalid scoop Id , Select only between 1 and 5")
                topping_id=None
        selected_toppings.append(scoop_toppings[topping_id-1])
    return selected_toppings

def check_num(num):
    try:
        num = int(num)
        return num
    except ValueError as err:
        print(err)
        return None
# select_cone_type()
order()
#scoops()
# select_scoop_flavour()
#select_scoop_topping()
    