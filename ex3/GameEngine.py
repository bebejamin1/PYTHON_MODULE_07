#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   GameEngine.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 16:23:08 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 17:28:52 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from typing import Dict

# FantasyCardFactory
data = [
        CreatureCard("dragon", 5, Rarity.LEGENDARY.value, 7, 6),
        CreatureCard("goblin", 2, Rarity.COMMON.value, 3, 5),
        CreatureCard("Lightning Bolt", 3, Rarity.LEGENDARY.value, 5, 5)
       ]


class GameEngine():
    def __init__(self) -> None:
        self.turn = 0
        self.factory = None
        self.strategy = None

    def configure_engine(self,
                         factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        print("Factory:", factory)
        print("Stategy:", strategy)

    def simulate_turn(self) -> Dict:
        self.turn += 1
        pass

    def get_engine_status(self) -> Dict:
        return {"turns_simulated": self.turn, "strategy_used": self.strategy,
                }
