class Deck:

    def __init__ (self, _name, _source, _price, _notes):
        self.name = _name
        self.source = _source
        self.price = _price
        self.notes = _notes


    def printDeck (self):
        print("New Deck created! ")
        print("Deck name: " + self.name)
        print ("Deck source: " + self.source)
        print ("Deck price: " + self.price)
        print ("Deck Notes: " + self.notes)

    def createDeck(self): 
        name = input("What is the name of the deck?")
        source = input("Where did you get this deck?")
        price = input("What is the price?")
        notes = input("Please give any notes: ")
        tempDeck = Deck(name, source, price, notes)
        return tempDeck

