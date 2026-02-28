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

    print("Factory:", FantasyCardFactory.__name__)
    print("Strategy:", AggressiveStrategy.__name__)
    print("Available types:", game)
