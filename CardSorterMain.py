import Deck
deckInstance = Deck.Deck("testName", "testSource", 0, "my notes")
UserDecision = input("What would you like to do?/n 1) View Decks /n 2) Create Deck /n 3) Delete Deck")


if UserDecision == "1":
    print ("Creating New Deck: ")
    tempDeck = deckInstance.createDeck()
    tempDeck.printDeck()    


elif UserDecision == "2":
    print ("user entered two!")


elif UserDecision == "3":
    print ("Cannot Delete decks yet")


else:
    print ("Invalid input  " + UserDecision)
