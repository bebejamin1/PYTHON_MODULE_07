#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 11:33:05 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 13:08:43 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    # =========================================================================
    # ============================ DATA =======================================
    # =========================================================================

    print(" DataDeck Deck Builder ".center(79, "="))

    deck = Deck()

    try:
        spell = SpellCard("Lightning Bolt", 3, "Rare",
                          "Deal 3 damage to target")
        artifact = ArtifactCard("Mana Crystal", 2, "Rare", 2,
                                "Permanent: +1 mana per turn")
        creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    except ValueError as e:
        print(f"Error: {e}")

    card_list = [spell, artifact, creature]
    for card in card_list:
        deck.add_card(card)

    # =========================================================================
    # ========================= DECK STATS ====================================
    # =========================================================================

    print("\n" + "Building deck with different card types...")
    print("Deck stats:", deck.get_deck_stats())

    # =========================================================================
    # ========================== DRAWING ======================================
    # =========================================================================

    print("\n" + "Drawing and playing cards:" + "\n")

    game_state = {}

    for card in card_list:
        print(f"Drew: {card.name} ({type(card).__name__})")
        print("Play result:", card.play(game_state), "\n")

    print("Polymorphism in action: Same interface, different card behaviors!")
