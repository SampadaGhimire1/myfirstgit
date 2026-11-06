class order:
    def __init__(self,i,p):
        self.item=i
        self.price=p
    def __gt__(self,second):
        if(self.price>second.price):
            print("order 1>order 2")
        else:
            print("order 2>order 1")

o1=order("fghjk",90)
o2=order("fghjk",50)
o1>o2