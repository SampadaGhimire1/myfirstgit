def checkword():
    data=True
    n=1
    with open("race.txt", "r") as g:
        while data:
            data=g.read()
            if("learning" in data):
                print("found at", n)
                return
            else:
                n+=1
                print("not found")

checkword()