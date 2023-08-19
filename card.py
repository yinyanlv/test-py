import collections
from random import choice 

Card = collections.namedtuple('Card', ['suit', 'rank'])

suit_values = dict(红桃=3, 黑桃=2, 方块=1, 梅花=0)

class FrenchDeck:
    suits = '红桃 黑桃 方块 梅花'.split(' ')
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    def __init__(self):
        self._cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

def sort(card):
    val = FrenchDeck.ranks.index(card.rank)
    # 间隔4  
    return val * len(suit_values) + suit_values[card.suit]

if __name__ == '__main__':
    a = FrenchDeck()
    print(len(a))
    print(choice(a))
    print(a[:3])
    print(a[2::13])
    for i in sorted(a, key=sort):
        print(i)
    