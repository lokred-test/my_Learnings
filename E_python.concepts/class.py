class product:
    calories_to_kilogrums=4.184
    def __init__(self,name,price_per_kg,calories):
        self.name=name
        self.price_per_kg=price_per_kg
        self.calories=calories
    def get_total_cost(self,weight):
        return self.price_per_kg*weight
    def get_kilogrums(self):
        return  self.calories_to_kilogrums * self.calories

banana=product("banana",50,30)
apple=product("apple",200,80)

print(banana.get_total_cost(5))
print(apple.get_total_cost(5))
