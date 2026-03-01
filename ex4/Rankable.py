#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   Rankable.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/01 13:40:17 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/01 13:43:47 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict
from abc import ABC, abstractmethod


class Rankable(ABC):

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict:
        pass
