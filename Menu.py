# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 17:14:10 2022

@author: PC_RC
"""

class parent():
    
    def __init__(self):
        print("This is a parent class")
        
    def menu(dish):
        if dish == "burger":
            print("You can add following toppings")
            print("More Cheese | Add Jalapeno")
        elif dish == "iced_americano":
            print("You can add the following toppings")
            print("Add chocolate syrup | Add caramel syrup")
        else :
            print("Please enter a valid dish. Available: burger and iced_americano.")
            
    def final_amount(dish, add_ons):
        if dish == "burger" and add_ons == "cheese":
            print("You added more cheese. You need to pay $250")
        elif dish == "burger" and add_ons == "jalapeno":
            print("You added jalapeno. You need to pay $350")
        elif dish == "iced_americano" and add_ons == "chocolate_syrup":
            print("You added chocolate_syrup. You need to pay $250")
        elif dish == "iced_americano" and add_ons == "caramel_syrup":
            print("You added caramel_syrup. You need to pay $450")
  
            
class child1(parent):
    
    def __init__(self, dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)
        

class child2(parent):
    
    def __init__(self, dish, addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish, self.addons)
        
        
child1_object = child1("burger")
child1_object.get_menu()

child2_object = child2("burger", "jalapeno")
child2_object.get_final_amount()
        
            