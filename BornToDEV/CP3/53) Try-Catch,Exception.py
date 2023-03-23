import sys
randomlist= ["a",0,2]
for entry in randomlist:
        try:
            print("The Entry is:",randomlist)
            r =1/int(entry)
            break
        except:
              print("Opp",sys.exc_info()[0],"Occured")
              print("Next Entry")
              print()
print("The reciprocal of",entry,"is",r)