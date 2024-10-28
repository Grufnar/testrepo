
#tings = []
tings = ["item1", "item2", "item3", "item4", "item5"]
tings2 = tings.insert(-1, "and")
full = tings[0]


def ztring(conc):
    for i in range(0, len(conc)):
        print(conc[i])
        global full
        if i == (len(conc) - 1):
            full = (full + " " + conc[i])
        else:
            full = (full + ", " + conc[i])
    
#   print(full)

ztring(tings)

print(full)
