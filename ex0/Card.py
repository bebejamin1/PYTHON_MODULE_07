#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Card.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 10:11:28 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 16:17:26 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        pass

    def get_card_info(self) -> Dict:
        info = {}
        info["name"] = self.name
        info["cost"] = self.cost
        info["rarity"] = self.rarity
        return (info)

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        else:
            return False
