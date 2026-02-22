#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Combatable.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 13:32:32 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 14:15:33 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict
from abc import ABC, abstractmethod
from ex0 import Card


class Combatable(ABC):
    def __init__(self, attack: int) -> None:
        self.attack = attack

    @abstractmethod
    def attack(self, target: Card) -> Dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        pass
