import Deck
instanceOfDeck = Deck.Deck("Bicycle", "Kickstarter", 2.5, "boiler plate deck")
ListOfDecks = list[instanceOfDeck]
class SaveUpdateDeck:


    def getOldDecks():
        try:
            with open("DeckStorage\sample.txt", 'r') as file:
                content = file.read()
                print(content)
                return content
        except FileNotFoundError:
            print("something went wrong trying to find the file")
            return None
        
    def printNewDeck(deck: Deck.Deck):
        try:
            with open("DeckStorage\sample.txt", 'a') as file:
                file.write(deck.name + deck.source + deck.price + deck.notes)
                file.write("\n")
                print("Successfully wrote new deck")
        except FileNotFoundError:
            print("Could not write to file")
    
        
SaveUpdateDeck.getOldDecks()
        
