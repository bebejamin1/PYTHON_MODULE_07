#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 16:23:20 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 17:30:00 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy

if __name__ == "__main__":
    print("\n" + " DataDeck Game Engine ".center(79, "="))

# =============================================================================
# ================================ DATA =======================================
# =============================================================================

    print("\n" + "Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game = GameEngine()

    game.configure_engine(factory, strategy)

    try:
        creature1 = factory.create_creature("dragon")
        creature2 = factory.create_creature("goblin")
        spell1 = factory.create_spell("fireball")
        artifact1 = factory.create_artifact("mana_ring")
        print(f"Available types: {factory.get_supported_types()}")
        creature3 = factory.create_creature("lightning bolt")
    except KeyError as e:
        print("Error: ", e)

    print("\n" + "Simulating aggressive turn...")
    creatures = [creature1, creature2, creature3]
    hand = []
    for creature in creatures:
        hand.append(f"{creature.name} ({creature.cost})")
    print("Hand:", end=" ")
    print(*hand, sep=", ")

    print("\n" + "Turn execution:" + "\n")
    # print("Strategy:", creature2.get_strategy_name())
