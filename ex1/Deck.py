#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Deck.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 11:32:49 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 12:52:04 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        try:
            index = [card.name for card in self.cards].index(card_name)
            self.cards.pop(index)
            return (True)
        except ValueError as e:
            print("Error:", e)
            return (False)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        try:
            return self.cards.pop(0)
        except IndexError:
            print("There are no more cards")
            return

    def get_deck_stats(self) -> Dict:
        creatures = spells = artifacts = cost = 0
        total_cards = len(self.cards)
        for card in self.cards:
            if isinstance(card, CreatureCard):
                creatures += 1
            if isinstance(card, SpellCard):
                spells += 1
            if isinstance(card, ArtifactCard):
                artifacts += 1
            cost += card.cost

        try:
            avg_cost = (cost / total_cards)
            return {"total_cards": total_cards, "creatures": creatures,
                    "spells": spells, "artifacts": artifacts,
                    "avg_cost": round(avg_cost, 1)}
        except ZeroDivisionError as e:
            print("Error:", e)
            return {"total_cards": total_cards, "creatures": creatures,
                    "spells": spells, "artifacts": artifacts}
