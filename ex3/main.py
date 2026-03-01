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

from typing import Dict


def create_hand(creatures: Dict) -> Dict:
    hand = []
    for creature in creatures:
        try:
            hand.append(f"{creature.name} ({creature.cost})")
        except AttributeError as e:
            print("Error:", e)
    return (hand)


def create_hand_turn(creatures: Dict) -> Dict:
    hand = []
    for creature in creatures:
        try:
            hand.append(creature)
        except AttributeError as e:
            print("Error:", e)
    return (hand)


if __name__ == "__main__":
    print("\n" + " DataDeck Game Engine ".center(79, "=") + "\n")

# =============================================================================
# ================================ DATA =======================================
# =============================================================================

    print("\n" + "Configuring Fantasy Card Game...")

    # For Configuring Fantasy Card Game
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game = GameEngine()

    game.configure_engine(factory, strategy)

    # For Available types and Simulating aggressive turn
    creature1 = factory.create_creature("dragon")
    creature2 = factory.create_creature("goblin")
    creature3 = factory.create_creature("lightning bolt")
    creatures = [creature1, creature2, creature3]

    spell1 = factory.create_spell("fireball")
    artifact1 = factory.create_artifact("mana_ring")

    # For Turn execution
    enemy = factory.create_creature("enemy")
    hand = [creature2, creature3]
    battlefield = [enemy]
    hand_turn = create_hand_turn(hand)
    battlefield_turn = create_hand_turn(battlefield)

# =============================================================================
# =============================== PRINT =======================================
# =============================================================================

    print(f"Available types: {factory.get_supported_types()}")

    print("\n" + "Simulating aggressive turn...")
    hand = create_hand(creatures)
    print("Hand:", end=" ")
    print(*hand, sep=", ")

    print("\n" + "Turn execution:")
    print("Strategy:", strategy.get_strategy_name())
    turn = strategy.execute_turn(hand_turn, battlefield_turn)
    game.turn += 1
    print("Action:", turn)

    print("\n" + "Game Report:")
    game.cards_created += len(creatures)
    game.total_damage += turn["damage_dealt"]
    print(game.get_engine_status())

    print("\n" + "Abstract Factory + Strategy Pattern: "
                 "Maximum flexibility achieved!")
