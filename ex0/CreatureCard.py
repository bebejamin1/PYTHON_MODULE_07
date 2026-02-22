#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   CreatureCard.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 0002/10/03 00:00:00 by          #+         #+#    #+#            #
#   Updated: 2026/02/22 11:24:22 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0 import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = "Creature summoned to battlefield"
        return (game_state)

    def attack_target(self, target) -> Dict:
        result = {}
        result["attacker"] = self.name
        result["target"] = target.name
        result["damage_dealt"] = self.attack
        if (self.attack >= target.health):
            result["combat_resolved"] = True
        else:
            result["combat_resolved"] = False
        self.health -= target.attack
        return (result)

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return (info)
