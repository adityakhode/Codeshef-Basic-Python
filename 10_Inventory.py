t=int(input())
for j in range (t):
    n=int(input())
    l = [[],[]] #empty 2D array
    for _ in range (n):
        item = input().split() #taken inputs
        item_name=item[0] #taken first input as item_name
        item_quantity=int (item[1]) #taken second input as item_quantity
        l[0].append(item_name) #added name to first list
        l[1].append(item_quantity)# added quantity to the second
        m=int(input())
        for _ in range(m):
            op = input()
            a=op.find(" ") #located spaces
            b=op[a+1:] #accessed the first object
            b=b.split(" ")
            name =b[0]
            num = int (b[1])
            op=op[:a]
            if op == "ADD": ##ADD operation
                if name not in l[0]: #checking if the object is in the first list
                    l[0].append(name )#adding new object
                    l[1].append(num)
                    print(f"ADDED Item {name}")
                else:
                    new=l[0].index(name)#accessed index of that object
                    l[1][new]+=num #added quantity to existing quantity
                    print(f"UPDATED Item {name}")
            elif op=="DELETE": ##DELETE OPERATION
                if name not in l[0]:
                    print(f"Item {name } does not exist")
                else:
                    new=l[0].index(name)
                    if num <= l[1][new]:
                        l[1][new] -= num
                        print(f"DELETED Item {name}")
                    else:
                        print(f"Item {name} could not be DELETED")
            total = sum(l[1])# calculated the total sum of elements in the second list
            print(f"Total Items in Inventory: {total}")