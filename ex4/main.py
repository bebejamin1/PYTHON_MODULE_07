#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/01 13:55:59 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/02 09:09:58 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import Rarity


def main():
    tournament = TournamentPlatform()
    print("Registering Tournament Cards..." + "\n")

    dragon = TournamentCard("dragon_001", "Fire Dragon", 5,
                            Rarity.COMMON.value, 1200, 10, 15)
    wizard = TournamentCard("wizard_001", "Ice Wizard", 5,
                            Rarity.COMMON.value, 1150, 5, 12)
    print(tournament.register_card(dragon) + "\n")
    print(tournament.register_card(wizard) + "\n")

    print("Creating tournament match...")
    print("Match result:",
          tournament.create_match(dragon.id_card, wizard.id_card))

    print("\n" + "Tournament Leaderboard:")
    players_class = tournament.get_leaderboard()
    i = 1
    for player in players_class:
        print(f"{i}. {player}")
        i += 1

    print(dragon.get_tournament_stats())

    print("\n" + "Platform Report:")
    print(tournament.generate_tournament_report())


if __name__ == "__main__":
    print("\n" + " DataDeck Tournament Platform ".center(79, "=") + "\n")
    main()
    print("\n" + " Tournament Platform Successfully Deployed! ".center(79, "=")
          + "\n" + "All abstract patterns working together harmoniously!")
