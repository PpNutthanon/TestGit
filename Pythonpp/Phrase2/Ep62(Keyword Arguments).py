#Keyword Arguments
def displayData(fname,lname,city):
    print("Hello",fname,lname)
    print("You live in",city)
displayData("Ikkyu","Chutiphon","Bangkok")
#จะสลับตำแหน่งการใส่ input ได้มั้ย => ใช้ keyword arguments
displayData(city="Chonburi",lname="Nutthanon",fname="Pp")
displayData(lname="AB",city="BKK",fname="LL")