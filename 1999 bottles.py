#Eva Deng
#10/24/24
#19 99 Bottles

#init
def bottles():
    milk = 99
    for i in range(99):
        print(str(milk) + " bottles of milk on the wall ")
        milk=milk-1
    milk=1
    print(str(milk) + " bottle of milk on the wall")
    print("Take it done pass it around\nNo more bottles of milk on the wall\nBoo Hoo!")

#main
bottles()
