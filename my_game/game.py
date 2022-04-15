'''
Classes
'''


class Location:
    '''
    Class for creating location in the game
    and for the main interactions between them
    '''
    # linked_location is dictionary which include all
    # transition between location
    linked_location = {}

    def __init__(self, name: str) -> None:
        '''
        name: name of the location
        description: brief description of the location
        characters: characters on location
        items: items on location
        keys: item whick you need to go in this location
        '''
        self.name = name
        self.description = None
        self.item = None
        self.characters = None
        self.keys = None
        self.reason = None

    def set_description(self, description:str) -> None:
        '''
        Set description to the location
        '''
        self.description = description


    def link_location(self, location:object, direction:str) -> None:
        '''
        Update dictionary linked_location with possible
        transitions between location.
        '''
        if direction == "straight": opposite = "back"
        if direction == "back": opposite = "straight"
        if direction == "right": opposite = "left"
        if direction == "left": opposite = "right"
        self.direction = direction
        if self.name not in Location.linked_location:
            Location.linked_location[self.name] = {}
        Location.linked_location[self.name].update({self.direction: location})
        if location.name not in Location.linked_location:
            Location.linked_location[location.name] = {}
        Location.linked_location[location.name].update({opposite: self})


    def set_character(self, character:object) -> None:
        '''
        Set chararacters on the loction
        '''
        self.characters = character
        # if self.characters is not None:
        #     self.characters.update({character: character.name})
        # else:
        #     self.characters = {character : character.name}


    def set_item(self, item:object) -> None:
        '''
        Set item on the location
        '''
        self.item = item

    def set_key(self,key: str) -> None:
        '''
        Set key to location if it`s closed
        '''
        self.keys = key


    def set_reason(self, reason:str) -> None:
        '''
        Set reason why this location is closed
        '''
        self.reason = reason


    def get_reason(self) -> str:
        '''
        Get reason why this location is closed
        '''
        print(self.reason)
        print('I return back')


    def try_to_move(self) -> str:
        '''
        Return key to this location
        '''
        return self.keys


    def get_character(self) -> dict:
        '''
        Function return dictionary of character which
        located on current location or None
        '''
        return self.characters


    def get_item(self) -> str:
        '''
        Function return item which are on location
        '''
        return self.item
    

    def get_details(self) -> str:
        '''
        Print details about room.
        Print character and item which are located in the room
        '''
        print(f"{self.name}\n--------------------\n{self.description}")
        for link in Location.linked_location[self.name]:
            print(f"The {Location.linked_location[self.name][link].name} is {link}")


    def move(self, vector: str) -> object:
        '''
        vector: direction in which we are moving
        Change location function
        '''
        return Location.linked_location[self.name][vector]


class Character:
    '''
    Class for creating units which participate in game process
    '''
    def __init__(self, name: str, description: str) -> None:
        '''
        name: name of character
        description: description of character
        phraze: words which character says
        '''
        self.name = name
        self.description = description
        self.phraze = None
    
    
    def set_conversation(self, phraze:str) -> None:
        '''
        Set conversation to the character
        '''
        self.phraze = phraze


    def describe(self) -> str:
        '''
        Print brief description of character
        '''
        print(f"{self.name} is here !\n{self.description}")


    def talk(self) -> str:
        '''
        Print character conversation
        '''
        print(f"[{self.name} says]: {self.phraze}")


class Allies(Character):
    '''
    Positive character which can give you something
    '''
    def __init__(self, name: str, description: str) -> None:
        '''
        Create object of class Allies
        item: item which can person gave you
        cost: item what character want
        '''
        super().__init__(name, description)
        self.item = None
        self.cost = None

    def set_item(self, item: object) -> None:
        '''
        Set item to character
        '''
        self.item = item


    def set_cost(self, cost: str) -> None:
        '''
        Set cost to item which character have
        '''
        self.cost = cost


    def give_cost(self, cost: str) -> bool:
        '''
        You gave to the character item
        '''
        return self.cost == cost


    def get_item(self) -> str:
        '''
        Return name of the item which he have
        '''
        return self.item


class Enemy(Character):
    '''
    Represent class Charactrer as enemy
    '''
    # Counter
    win = 0

    def __init__(self, name: str, description: str) -> None:
        '''
        Create object of class Enemy
        weakness: item which help to kill enemy
        '''
        super().__init__(name, description)
        self.weakness = None


    def fight(self, item:str) -> bool:
        '''
        Return result of the fight between hero and enemy
        '''
        if item == self.weakness:
            print(f"You feld {self.name} off with the {item}")
        else:
            print(f"{self.name} crushes you, puny adventurer!")
        return item in self.weakness

    def set_weakness(self, weakness:list) -> None:
        '''
        Set weakness to the enemy
        '''
        self.weakness = weakness

    def get_defeated(self) -> int:
        '''
        Counter of defeated enemy
        '''
        Enemy.win += 1
        return Enemy.win


class Item:
    '''
    Class Item. This object player can use
    with different purpose
    '''
    def __init__(self, name:str) -> None:
        '''
        Create item
        '''
        self.name = name
        self.description = None


    def set_description(self, description: str) -> None:
        '''
        Function set description of item
        '''
        self.description = description


    def describe(self) -> str:
        '''
        Function print description of item
        '''
        print(f"The [{self.name}] is here - {self.description}")


    def get_name(self) -> str:
        '''
        Function return name of item
        '''
        return self.name


# class Weapon(Item):
#     '''
#     Use to fight with enemy
#     '''
#     def __init__(self, name: str) -> None:
#         super().__init__(name)


# class Support(Item):
#     '''
#     Item which use to treat player
#     '''
#     def __init__(self, name: str) -> None:
#         super().__init__(name)


#     def treat(self) -> bool:
#         return True