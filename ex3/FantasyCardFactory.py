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
from ex0.Card import Card


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_themed_deck(self, size: int) -> Dict:
        pass

    def get_supported_types(self) -> Dict:
        pass
