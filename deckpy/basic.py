'''
	DeckPy is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	DeckPy is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with DeckPy: see gpl3.txt at the top of the program directory.
	If not, see <http://www.gnu.org/licenses/>.
'''
import deckpy.log
from functools import reduce
import logging

# Set up logging facilities.
dp_log = deckpy.log.stderr_logger(__name__)

if __name__ == "__main__":	
	proceed = input("This module should not be directly executed, but instead imported. Proceed? (y/n)")
	if proceed != "y":
		raise SystemExit

class System:
	def __init__(self, name, distribution):
		self.name = name
		self.order_dict = order_dict

		if type(distribution) is list:
			self.distribution = {}

			for card in distribution:
				self.distribution[card] += 1 if self.distribution.get(card, False) else 1
		else:
			self.distribution = distribution

	dp_log.debug("System %s created.")

# Cards.
class Card:
	def __init__(self, rank):
		self.rank = rank

class SuitCard(Card):
	def __init__(self, rank, suit):
		super().__init__(rank)
		self.suit = suit

class Deck:
	def __init__(self, name, system, num_decks):
		self.name = name
		self.system = system
		self.num_decks = decks

		self.cards = list(reduce(lambda l, k: l.extend([k[0]] * k[1]), list(iter(system.distribution.items())), []))



