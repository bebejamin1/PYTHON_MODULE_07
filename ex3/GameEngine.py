#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   GameEngine.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 16:23:08 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 17:16:11 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0 import CreatureCard, Rarity
from typing import Dict

data = [
        CreatureCard("Dragon", 5, Rarity.LEGENDARY.value, 7, 6),
        CreatureCard("Goblin", 2, Rarity.COMMON.value, 3, 5),
        CreatureCard("Lightning Bolt", 3, Rarity.LEGENDARY.value, 5, 5)
       ]


class GameEngine():
    def __init__(self) -> None:
        self.factory = None
        self.strategy = "No strategy used"
        self.turn = 0
        self.cards_created = 0
        self.total_damage = 0
        self.hand1 = []
        self.hand2 = []

    def configure_engine(self,
                         factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        pass

    def get_engine_status(self) -> Dict:
        pass
