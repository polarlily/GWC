from random import *
Sides = ("Coleslaw","Potato Salad","Green Bean Casserole","Mashed Potato","Fries","Bread Rolls")
Main_courses = ("Grilled Fillet","Teriyaki Chicken","Pork Chops","Fries","Chicken Enchilidas","Spaghetti","Chicken Alfredo","Lasagna","Tacos","Burrito Pie")
Desserts = ("Cherry Pie","Apple Pie","Cupcakes","Cookies - White Macadamia","Cookies - Sugar","Cookies - Chocolate","Red Velvet Cake","Brownies")


#a = randint(0, len(Sides)-1)
b = randint(0, len(Main_courses)-1)
c = randint(0, len(Desserts)-1)

def choosefood(menu):
    for food in menu:
        a = randint(0, len(food)-1)
        print(menu[a])

choosefood(Sides)

#choosefood(Sides)
#repeatlist(Main_courses[b])
#repeatlist(Desserts[c])



#print(Sides[a], Main_courses[b], Desserts[c])
