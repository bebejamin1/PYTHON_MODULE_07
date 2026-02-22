#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Magical.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 13:32:42 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 14:13:12 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict, List
from abc import ABC, abstractmethod


class Magical(ABC):

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        pass
