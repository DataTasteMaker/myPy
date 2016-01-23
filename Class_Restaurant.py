class Restaurant:
    restcount = 0
    def __init__(self, name, Cuisine, Price, Facility):
        self.name = name
        self.Price = Price
        self.cuisine = Cuisine
        self.Facility = Facility
        Restaurant.restcount = Restaurant.restcount + 1

    def getName(self):
        return self.name

    def setName(self, Name):
        self.name = Name

    def AvgPrice(self):
        tmp = ""
        tmp = self.name.split(" ")
        print ""
        print "The Average price for 2 persons is " , self.Price 
        print ".................... by ", tmp[0] , " Management"
        print ""

    def RestaurantType(self):
        return self.cuisine

    def isExpensive(self):
        if (self.Price > 1000):
            return True
        return False

    def ServesAlcohol(self):
        tmp = ""
        tmp = self.name.split(" ")
        if self.Facility.count("Alcohol") > 0:
            print ""
            print "Yes, we serve Alcohol"
            print ".................... by ", tmp[0] , " Management"
            print ""
        else:
            print ""
            print "Sorry!, we don't serve Alcohol"
            print ".................... by ", tmp[0] , " Management"
            print ""

    def HomeDeliver(self):
        tmp = ""
        tmp = self.name.split(" ")
        if self.Facility.count("Home Delivery") > 0:
            print ""
            print  "Yes, we do delivery, only if within 1.5 kms"
            print ".................... by ", tmp[0] , " Management"
            print ""
        else:
            print ""
            print "Sorry!, we do not deliver"
            print ".................... by ", tmp[0] , " Management"
            print ""



rst1 = Restaurant("Greens, Malad, 1234567890", ["Indian","Chinese"], 2000, ["Home Delivery"])
rst2 = Restaurant("Master Chef, Borivali, 9876543210", ["Indian, Thai, Italian"],2500, ["Home Delivery"])
rst3 = Restaurant("5Spice, Andheri, 9856473210", ["Chinese"],3000, ["Alcohol"])
rst4 = Restaurant("5Spice, Bandra, 3210985647", ["Chinese, Punjabi"],3500, ["Home Delivery", "Alcohol"])
rst5 = Restaurant("Samudra, Powai, 8810985647", ["Punjabi", "Chinese"],5000, ["Alcohol"])

rst1.ServesAlcohol()
rst2.ServesAlcohol()
rst3.ServesAlcohol()
rst4.ServesAlcohol()
rst5.ServesAlcohol()

rst1.HomeDeliver()
rst2.HomeDeliver()
rst3.HomeDeliver()
rst4.HomeDeliver()
rst5.HomeDeliver()

rst4.AvgPrice()

print "Total Restaurants : " + str(Restaurant.restcount)
