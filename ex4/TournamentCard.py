#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   TournamentCard.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/01 13:42:36 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/02 09:10:09 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, id_card: str, name: str, cost: int, rarity: str,
                 rating: int, damage: int, health: int):
        super().__init__(name, cost, rarity)
        self.win = 0
        self.loose = 0
        self.total_damage = 0
        self.total_attack = 0
        self.id_card = id_card
        self.rating = rating
        self.damage = damage
        self.health = health

    def get_tournament_stats(self) -> Dict:
        return {"win": self.win, "loose": self.loose,
                "total damage inflicted": self.total_attack,
                "total damage suffered": self.total_damage}

# =============================================================================
# ================================ Card =======================================
# =============================================================================

    def play(self, game_state: Dict) -> Dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = "Creature summoned to battlefield"
        return (game_state)

# =============================================================================
# ============================ Combatable =====================================
# =============================================================================

    def attack(self, target: Card) -> Dict:
        result = {}
        try:
            if (self.health <= target.damage):
                raise ValueError("Lost before starting")
            result["attacker"] = self.name
            result["target"] = target.name
            result["damage"] = self.damage
            self.total_attack += self.damage
            result["combat_type"] = "melee"
            return (result)
        except (ValueError, AttributeError) as e:
            print("ERROR:", e)
        self.health -= target.damage
        return

    def defend(self, incoming_damage: int) -> Dict:
        damage_blocked = 3
        damage_t = incoming_damage - damage_blocked
        self.total_damage += damage_t
        result = {}
        if (self.health > 0):
            self.health -= damage_t
            result["damage"] = damage_t
            if (self.health <= 0):
                result["alive"] = False
            else:
                result["alive"] = True
            return (result)
        return

    def get_combat_stats(self) -> Dict:
        combats_stats = {}
        combats_stats["win"] = self.win
        combats_stats["loose"] = self.loose
        return (combats_stats)

# =============================================================================
# ============================= Rankable ======================================
# =============================================================================

    def calculate_rating(self) -> int:
        self.rating -= (16 * self.loose)
        self.rating += (16 * self.win)
        return (self.rating)

    def update_wins(self, wins: int) -> None:
        self.win += wins

    def update_losses(self, losses: int) -> None:
        self.loose += losses

    def get_rank_info(self) -> Dict:
        return {"name": self.name, "rank": self.rating}
