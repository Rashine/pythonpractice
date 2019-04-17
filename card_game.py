# import random

# class Card:
#     suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
#     value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#     cards = []
#     for s in suit:
#         for v in value:
#             cards.append((s, v))
#     def __init__(self):
#         if Card.cards == []:
#             print ("No more cards, or you need to buy a new deck.")
#         self.card = Card.cards.pop(0)
#     def __repr__(self):
#         return f"{self.card[1]} of {self.card[0]}"
#     def __str__(self):
#         return f"{self.card[1]} of {self.card[0]}"

# class Deck:
#     counter = 52
#     def __init__(self):
#         self.mycards = []
#         for i in range(52):
#             self.mycards.append(Card())
#     def __repr__(self):
#         return f"Deck of {Deck.counter} cards"
#     def __str__(self):
#         return f"Deck of {Deck.counter} cards"
#     def _deal(self):
#         if Deck.counter > 0:
#             Deck.counter -= 1
#             return self.mycards.pop(0)
#         else:
#             raise ValueError("All cards have been dealt")
#     def shuffle(self):
#         if Deck.counter == 52:
#             random.shuffle(self.mycards)
#             return self.mycards
#         else:
#             raise ValueError("Only full decks can be shuffled")
#     def deal_card(self):
#         return self._deal()
#     def deal_hand(self, num):
#         if num >= 1 and (Deck.counter - num) >= 0:
#             thishand = []
#             for i in range(num):
#                 thishand.append(self._deal())
#             return thishand
#         else:
#             raise ValueError("All cards have been dealt")
# import random

# class Card:
#     suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
#     value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#     cards = []
#     for s in suit:
#         for v in value:
#             cards.append((s, v))
#     def __init__(self):
#         if Card.cards == []:
#             print ("No more cards, or you need to buy a new deck.")
#         self.card = Card.cards.pop(0)
#     def __repr__(self):
#         return self.card[1]+" of "+self.card[0]
#     def __str__(self):
#         return self.card[1]+" of "+self.card[0]

# class Deck:
#     counter = 52
#     def __init__(self):
#         self.mycards = []
#         for i in range(52):
#             self.mycards.append(Card())
#     def __repr__(self):
#         return "Deck of "+str(Deck.counter)+" cards"
#     def __str__(self):
#         return "Deck of "+str(Deck.counter)+" cards"
#     def _deal(self):
#         if Deck.counter > 0:
#             Deck.counter -= 1
#             return self.mycards.pop(0)
#         else:
#             raise ValueError("All cards have been dealt")
#     def shuffle(self):
#         if Deck.counter == 52:
#             random.shuffle(self.mycards)
#             return self.mycards
#         else:
#             raise ValueError("Only full decks can be shuffled")
#     def deal_card(self):
#         return self._deal()
#     def deal_hand(self, num):
#         if num >= 1 and (Deck.counter - num) >= 0:
#             thishand = []
#             for i in range(num):
#                 thishand.append(self._deal())
#             return thishand
#         else:
#              raise ValueError("All cards have been dealt")

import random


class Card:
    def __init__(self, value, suit):
        self.suit, self.value = suit, value

    def __repr__(self):
        return self.value + ' of ' + self.suit


class Deck:
    def __init__(self):
        suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        value = [
            'A',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            'J',
            'Q',
            'K',
            ]
        self.cards = [] 
        for s in suit:
            for v in value:
                self.cards.append(Card(s, v))

    def __repr__(self):
        return 'Deck of ' + str(self.count()) + ' cards'

    def _deal(self, n):
        if self.count() > 0 and n >= 0:
            if n == 0:
                print("That's funny.")
            else:
                takes = min(self.count(), n)
                thishand = self.cards[-takes:]
                self.cards = self.cards[:-takes]
                return thishand
        else:
            raise ValueError('All cards have been dealt')

    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.cards)
            return self.cards
        else:
            raise ValueError('Only full decks can be shuffled')

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, n):
        return self._deal(n)

    def count(self):
        return len(self.cards)