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


def main():
    print("\n" + "Configuring Fantasy Card Game...")

    # For Configuring Fantasy Card Game
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game = GameEngine()

    game.configure_engine(factory, strategy)

    dragon = factory.create_creature("dragon")
    goblin = factory.create_creature("goblin")
    _ = factory.create_spell("fireball")
    _ = factory.create_artifact("mana_ring")
    print(f"Available types: {factory.get_supported_types()}")
    lightning_bolt = factory.create_creature("lightning bolt")
    enemy = factory.create_creature("enemy")

    print("\n" + "Simulating aggressive turn...")
    creatures = [dragon, goblin, lightning_bolt]
    hand = create_hand(creatures)
    print("Hand:", end=" ")
    print(*hand, sep=", ")

    print("\n" + "Turn execution:")
    print("Strategy:", strategy.get_strategy_name())

    hand = [goblin, lightning_bolt]
    battlefield = [enemy]
    hand_turn = create_hand_turn(hand)
    battlefield_turn = create_hand_turn(battlefield)
    ex_turn = strategy.execute_turn(hand_turn, battlefield_turn)
    game.turn += 1
    game.cards_created += len(creatures)
    game.total_damage += ex_turn["damage_dealt"]

    print("Action:", ex_turn)

    print("\n" + "Game Report:")
    print(game.get_engine_status())


if __name__ == "__main__":
    print("\n" + " DataDeck Game Engine ".center(79, "=") + "\n")
    main()
    print("\n" + "Abstract Factory + Strategy Pattern: "
                 "Maximum flexibility achieved!")
