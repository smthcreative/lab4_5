'''
Program
'''


class Room:
    '''
    Class Room represent room in which main character can be located
    '''
    # Dictionary in which all transition are
    # Transition are represented in the form of a dictionary
    # {'Kitchen': {'west': '<room1>', 'east': '<room2>'}, '<room1.name>':{'east': '<Kitchen>'}}

    linked_room = {}

    def __init__(self, name:str) -> None:
        '''
        Create a new object of class Room
        '''
        self.name = name
        self.character = None
        self.item = None
        self.description = None
        self.room = None
        self.direction = None


    def set_description(self, description:str) -> None:
        '''
        Set description to the room
        '''
        self.description = description


    def link_room(self, room:object, direction:str) -> None:
        '''
        Update dictionary linked_room with possible
        transitions between rooms.
        '''
        if direction == "south": opposite = "north"
        if direction == "north": opposite = "south"
        if direction == "west": opposite = "east"
        if direction == "east": opposite = "west"
        self.room = room
        self.direction = direction
        self.opposite = opposite
        if self.name not in Room.linked_room:
            Room.linked_room[self.name] = {}
        Room.linked_room[self.name].update({self.direction: self.room})
        if room.name not in Room.linked_room:
            Room.linked_room[room.name] = {}
        Room.linked_room[room.name].update({self.opposite: self})


    def set_character(self, character:object) -> None:
        '''
        Set chararacter on the room
        '''
        self.character = character


    def set_item(self, item:object) -> None:
        '''
        Set item on the room
        '''
        self.item = item


    def get_details(self) -> str:
        '''
        Print details about room.
        Print character and item which are located in the room
        '''
        print(f"{self.name}\n--------------------\n{self.description}")
        for link in Room.linked_room[self.name]:
            print(f"The {Room.linked_room[self.name][link].name} is {link}")


    def get_character(self) -> object:
        '''
        Return character which are in room
        '''
        return self.character


    def get_item(self)-> str:
        '''
        Return item which are in room
        '''
        return self.item


    def move(self, side:str) -> object:
        '''
        Function change room
        '''
        return Room.linked_room[self.name][side]


class Character:
    '''
    Class Character
    '''
    def __init__(self, name:str, description:str) -> None:
        '''
        Initialize object of class Character with
        two parameter
        '''
        self.name = name
        self.description = description


class Allies(Character):
    '''
    Child class of Character
    '''
    def __init__(self, name: str, description: str) -> None:
        '''
        Create object of class Allies
        '''
        super().__init__(name, description)


class Enemy(Character):
    '''
    Class Enemy
    '''
    # Counter of win
    win = 0

    def __init__(self, name:str, description:str) -> None:
        '''
        Initialize object of class Enemy
        '''
        super().__init__(name, description)
        self.phraze = None
        self.weakness = None


    def set_conversation(self, phraze:str) -> None:
        '''
        Set conversation to the character
        '''
        self.phraze = phraze


    def set_weakness(self, weakness:str) -> None:
        '''
        Set weakness to the enemy
        '''
        self.weakness = weakness


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


    def fight(self, item:str) -> bool:
        '''
        Return result of the fight between hero and enemy
        '''
        if item == self.weakness:
            print(f"You feld {self.name} off with the {item}")
        else:
            print(f"{self.name} crushes you, puny adventurer!")
        return item == self.weakness


    def get_defeated(self) -> int:
        '''
        Count defeated character
        '''
        Enemy.win += 1
        return Enemy.win




class Item:
    '''
    Class Item
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
