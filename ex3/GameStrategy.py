#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   GameStrategy.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 16:22:23 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 16:30:26 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Dict, List


class GameStrategy(ABC):

    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        pass
