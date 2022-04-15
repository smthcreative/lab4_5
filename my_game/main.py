'''
Main file
'''

from game import *

# from my_game.game import Location

# from my_game.game import Support, Weapon

# Start location
start_loc = Location('Bedroom')
start_loc.set_description('It`s already morning')
candy = Item('candy')
candy.set_description('Little kids like sweats')
start_loc.set_item(candy)

# Second location
porch = Location('Porch')
porch.set_description('This simple porch with with closed door')
pasport = Item('pasport')
print("Please enter your name:")
name = input()
pasport.set_description(f'Identity document: {name}')
# porch.set_item(pasport)

# Third location
basement = Location("Basement")
basement.set_description('A damp room with lots of moisture and mice.')
basement.set_key('flashlight')
basement.set_reason('It`a dark room, I can`t see anything. Maybe I need flashlight')
gun = Item('gun')
gun.set_description('You can kill someone with this gun')
basement.set_item(gun)

# Four location
hallway = Location('Hallway')
hallway.set_description('Long, very long ...')

# Five location
kitchen = Location('Kitchen')
kitchen.set_description('Big room full of disches')
mama = Allies('Mom', 'She look bored')
mama.set_conversation('I need a bread, go buy it in shop')
mama.set_cost('bread')
mama.set_item(pasport)
kitchen.set_character(mama)
food = Item('meat')
food.set_description('Big peace of meat')
kitchen.set_item(food)

# Six location
bathroom = Location("Bathroom")
bathroom.set_description('Just a toilet with washbasin and lavatory pan')
# bandage = Support('bandage')
# bandage.set_description('Second chanse to looser')


# Seven location
room = Location('Living rooom')
room.set_description('Spacious room with TV')
dad = Allies('Dad', 'Watch TV')
dad.set_conversation('I`m hungry ...')
dad.set_cost('meat')
key = Item('key')
key.set_description('Open door')
dad.set_item(key)
room.set_character(dad)

# Eight location
yard = Location('Green yard')
yard.set_description('little green yard of my house')
boy = Enemy('Boy', 'Play football')
boy.set_conversation('Go away from here')
boy.set_weakness(['candy', 'gun'])
yard.set_character(boy)
yard.set_key('key')
yard.set_reason('The door is closed')

# Nine location
food_shop = Location('Food shop')
food_shop.set_description('Food shop, you can buy food')
seller_food = Allies('Seller', 'Sell')
seller_food.set_conversation('Give me money or get out of here')
seller_food.set_cost('money')
bread = Item('bread')
bread.set_description('Tasty bread')
seller_food.set_item(bread)
food_shop.set_character(seller_food)

# Ten location
store = Location("Household shop")
store.set_description('You can buy tool')
store.set_key('pasport')
store.set_reason('Without pasport I can`t buy anything in this store')
flashlight = Item('flashlight')
flashlight.set_description('It`s flashlight')
seller_tool = Allies('Seller', 'Sell')
seller_tool.set_conversation('Give me money or get out of here')
seller_tool.set_cost('money')
seller_tool.set_item(flashlight)
store.set_character(seller_tool)

# Eleven location
final = Location('Street')
final.set_description('Ukrainian street')
mosk = Enemy('москаль', 'сидить')
mosk.set_conversation('Я тупий москаль')
mosk.set_weakness(['gun'])
final.set_character(mosk)


# Transaction
start_loc.link_location(porch, 'right')
porch.link_location(basement, 'right')
porch.link_location(hallway, 'straight')
porch.link_location(yard, 'back')
hallway.link_location(kitchen, 'left')
hallway.link_location(room, 'right')
hallway.link_location(bathroom, 'straight')
yard.link_location(food_shop, 'left')
yard.link_location(store, 'right')
yard.link_location(final, 'back')


current_room = start_loc
backpack = ['money']


dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")
    

    if command == "bag":
        print(*backpack)
        command = input("> ")


    if command in ["left", "right", "back", "straight"]:
        # Move in the given direction
        # next_room is room in which we try to go
        try:
            next_room = current_room.move(command)
        except KeyError:
            print('There is no passage here')
            continue
        if next_room.try_to_move() == None:
            current_room = next_room
        else:
            print(next_room.try_to_move())
            if next_room.try_to_move() in backpack:
                current_room = next_room
            else:
                next_room.get_reason()


    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == 'give':
        if inhabitant is not None and isinstance(inhabitant, Allies):
            stuff = input('What you want to give: ')
            if stuff in backpack:
                if inhabitant.give_cost(stuff):
                    print(f'Thank you! Take {inhabitant.get_item().name}')
                    print("You put the " + inhabitant.get_item().name + " in your backpack")
                    print(inhabitant.get_item().description)
                    backpack.append(inhabitant.get_item().name)
                    inhabitant.set_item(None)
                    inhabitant.set_conversation('...')
                    inhabitant.set_cost(None)
                else:
                    print(f"[{inhabitant.name} says]: I don`t need it")
            else:
                print('You don`t have it in your backpack')
        else:
            print('There is not anybody to give something')

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            print('You have:', *backpack)
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.characters = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == 'help':
        print('You can: take, give, fight, move, talk, bag')
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)

