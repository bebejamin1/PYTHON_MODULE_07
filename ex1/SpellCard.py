#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   SpellCard.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 11:32:25 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 13:06:00 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict


class SpellCard:
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = self.effect_type
        return (game_state)

    def resolve_effect(self, targets: list) -> Dict:
        pass
