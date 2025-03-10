# from typing import List

class shoppingcart:
    def __init__(self,max_size:int):
        self.items=[]
        self.max_size=max_size
    def add(self,item:str):
        if self.size()==self.max_size:
            raise OverflowError("cannot add more items")
        self.items.append(item)
    def size(self):
        return len(self.items)
    def get_items(self):
        return  self.items
    def get_total_price(self,price_map):
        total_price=0
        for item in self.items:
            total_price +=price_map.get(item)
        return total_price
        
        
