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

from typing import Dict
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine():
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turn = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self,
                         factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        print(f"Factory: {self.factory.__class__.__name__}")
        print("Stategy:", self.strategy.__class__.__name__)

    def simulate_turn(self) -> Dict:
        self.turn += 1
        return {"turns_played": 1}

    def get_engine_status(self) -> Dict:
        return {"turns_simulated": self.turn,
                "strategy_used": self.strategy.get_strategy_name(),
                "total_damage": self.total_damage,
                "cards_created": self.cards_created
                }
