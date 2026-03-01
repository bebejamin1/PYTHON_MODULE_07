#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   FantasyCardFactory.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 16:22:58 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 16:41:59 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex3.CardFactory import CardFactory
from typing import Dict
from ex0.Card import Card, Rarity

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


creatures = {
    "dragon": CreatureCard("Fire Dragon", 5, Rarity.RARE.value, 5, 10),
    "goblin": CreatureCard("Goblin Warrior", 2, Rarity.COMMON.value, 3, 4),
    "lightning bolt": CreatureCard("Lightning Bolt", 3, Rarity.EPIC.value,
                                   5, 8),
    "enemy": CreatureCard("Enemy Player", 4, Rarity.COMMON.value, 2, 10)
}

spells = {
    "fireball": SpellCard("fireball", 1, Rarity.COMMON.value, "fire"),
    "freezer": SpellCard("freezer", 1, Rarity.EPIC.value, "ice"),
    "flash": SpellCard("flash", 1, Rarity.LEGENDARY.value, "lighting")
}

artifacts = {
    "mana_ring": ArtifactCard("mana_ring", 1, Rarity.COMMON.value, 4, "ring")
}


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.creatures = []
        self.spells = []
        self.artifacts = []

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        try:
            if (name_or_power not in creatures):
                raise KeyError(f"Error: {name_or_power} does not exist")
        except (KeyError) as e:
            print("Error:", e)
            return
        else:
            creature = creatures[name_or_power]
            self.creatures.append(name_or_power)
            return (creature)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        try:
            if (name_or_power not in spells):
                raise KeyError(f"Error: {name_or_power} does not exist")
        except (KeyError) as e:
            print("Error:", e)
            return
        else:
            spell = spells[name_or_power]
            self.spells.append(name_or_power)
            return (spell)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        try:
            if (name_or_power not in artifacts):
                raise KeyError(f"Error: {name_or_power} does not exist")
        except (KeyError) as e:
            print("Error:", e)
            return
        else:
            artifact = artifacts[name_or_power]
            self.artifacts.append(name_or_power)
            return (artifact)

    def create_themed_deck(self, size: int) -> Dict:
        pass

    def get_supported_types(self) -> Dict:
        return {"creatures": self.creatures, "spells": self.spells,
                "artifacts": self.artifacts}
