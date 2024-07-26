class zomato:
    def __init__(self,food_preferences):
        self.food_preferences=food_preferences
    def food_filter(self):
        restaurents={
            "seafood_cave":{"fish","sdcdv","dcedcd"},
            "burger_king":{"burger","pizza","fedfcdv"},
            "Lassy_shop":{"lassy","grg","gedrgrg"},
        }
        best_match_food=set()
        best_match_restaurent=None
        for restaurent,menu in restaurents.items():
            common_foods=food_preferences.intersection(menu)
            if len(best_match_food)<len(common_foods):
                best_match_food=common_foods
                best_match_restaurent=restaurent
        print(best_match_food)
        return best_match_restaurent
    
food_preferences={"burger","pizza","fish"}
zomato=zomato(food_preferences)
restaurent=zomato.food_filter()
print(f"the best match restaurent is {restaurent}")