#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ArtifactCard.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 11:32:37 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 16:14:41 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict


class ArtifactCard:
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = self.effect
        return (game_state)

    def activate_ability(self) -> Dict:
        return {f"{self.effect}": self}
