#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   EliteCard.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 13:32:52 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 16:10:10 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from enum import Enum


class Efficacity(Enum):
    SUPER_EFFECTIVE = "Super effective"
    NOT_VERY_EFFECTIVE = "not_very_effective"
    NORMAL_EFFICIENCY = "Normal efficiency"
# =============================================================================
# ========================== Methods / Class ==================================
# =============================================================================

# ================================ Child ======================================
# ============================== EliteCard ====================================
# =============================================================================


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, rarity,
                 damage: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        play = self.is_playable(game_state["mana available"])
        if (play is True):
            game_state["card_played"] = self.name
            game_state["mana_used"] = self.cost
            game_state["effect"] = "STOOOOOOORM!"
            return (game_state)
        game_state["card_played"] = None
        game_state["mana_used"] = 0
        game_state["effect"] = "NO EFFECT"
        return (game_state)

    def get_card_info(self):
        return (super().get_card_info())

# =============================================================================
# =============================== COMBAT ======================================
# =============================================================================

    def attack(self, target: Card) -> Dict:
        result = {}
        try:
            if (self.health <= target.damage):
                raise ValueError("Lost before starting")
            result["attacker"] = self.name
            result["target"] = target.name
            result["damage"] = self.damage
            result["combat_type"] = "melee"
            return (result)
        except (ValueError, AttributeError) as e:
            print("ERROR:", e)
        self.health -= target.damage
        return

    def defend(self, incoming_damage: int) -> Dict:
        if (self.health > 0):
            damage_blocked = 3
            result = {}
            result["defender"] = self.name
            result["damage_taken"] = incoming_damage - damage_blocked
            result["damage_blocked"] = incoming_damage - result["damage_taken"]
            self.health -= result["damage_taken"]
            if (self.health <= 0):
                result["still_alive"] = False
            else:
                result["still_alive"] = True
            return (result)
        return

    def get_combat_stats(self) -> Dict:
        if (self.damage <= 3):
            efficacity = Efficacity.NOT_VERY_EFFECTIVE.value
        elif (self.damage <= 6):
            efficacity = Efficacity.NORMAL_EFFICIENCY.value
        elif (self.damage > 6):
            efficacity = Efficacity.SUPER_EFFECTIVE.value
        return {
            "remaining health": self.health,
            "damage": self.damage,
            "efficiency": efficacity
               }

# =============================================================================
# ================================ MAGIC ======================================
# =============================================================================

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        result = {}
        result["caster"] = self.name
        result["spell"] = spell_name
        result["targets"] = [target.name for target in targets]
        result["mana_used"] = sum([target.cost for target in targets])
        return (result)

    def channel_mana(self, amount: int) -> Dict:
        return {"channeled": self.cost, "mana_used": amount}

    def get_magic_stats(self) -> Dict:
        return {
            "efficiency": Efficacity.NORMAL_EFFICIENCY,
            "spell damage": 3,
            "spell cost": 4,
               }
