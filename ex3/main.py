#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 16:23:20 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 17:29:50 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex3.GameEngine import GameEngine, AgressiveStrategy, FantasyCardFactory


if __name__ == "__main__":
    print("\n" + " DataDeck Game Engine ".center(79, "="))

# =============================================================================
# ================================ DATA =======================================
# =============================================================================

    print("\n" + "Configuring Fantasy Card Game...")

    game = GameEngine()

    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")
