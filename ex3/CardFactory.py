#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   CardFactory.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 16:22:35 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 16:35:28 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from ex0.Card import Card
from typing import Dict


class CardFactory(ABC):
    def __init__(self, name: str, spells: str, artifact: str):
        self.name = name
        self.spells = spells
        self.artifact = artifact

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict:
        pass
