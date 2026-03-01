#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   AggressiveStrategy.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 16:22:46 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 16:40:57 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict, List
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        turn = {}
        turn["cards_played"] = [card.name for card in hand]
        turn["mana_used"] = sum(card.cost for card in hand)
        turn["targets_attacked"] = [enemy.name for enemy in battlefield]
        turn["damage_dealt"] = sum(card.attack for card in hand)
        return (turn)

    def get_strategy_name(self) -> str:
        return (__class__.__name__)

    def prioritize_targets(self, available_targets: List) -> List:
        return {available_targets[1]}
