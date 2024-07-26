class product:
    cal_to_klg=4.184 #CLASSVARIABLE(WHEN THE VALUE SAME FOR ALL THE OBJECTS)
    def __init__(self,name,calories,price_per_kg):
        self.name=name
        self.calories=calories
        self.price_per_kg=price_per_kg
    def get_total_price(self,weight):
        return self.price_per_kg * weight
    def get_cal_to_klg(self):
        return self.calories * self.cal_to_klg
    
apple=product("apple",150,220)

print(apple.get_total_price(5))

print(apple.get_cal_to_klg())


        