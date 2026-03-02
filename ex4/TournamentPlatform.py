#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   TournamentPlatform.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/01 13:51:03 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/02 09:08:45 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict, List

from .TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self):
        self.cr_card = {}
        self.matches_played = 0
        self.total_rating = 0
        self.nb_card = 0

    def register_card(self, card: TournamentCard) -> str:
        try:
            if (isinstance(card, TournamentCard)):
                self.cr_card[card.id_card] = card
                self.nb_card += 1
                return (f"{card.name} (ID: {card.id_card}):" + "\n"
                        f"- Interfaces: {card.__class__.__name__}" + "\n"
                        f"- Rating: {card.rating}" + "\n"
                        f"- Record: {card.win}-{card.loose}")
            else:
                raise AttributeError("Not the good object")
        except AttributeError as e:
            print("Error:", e)
            return

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        result = {}
        try:
            card1 = self.cr_card[card1_id]
            card2 = self.cr_card[card2_id]
            self.matches_played += 1
        except (KeyError, TypeError) as e:
            print(f"❌​ Error: {e} unknown, match canceled")
            return

        while (card1.health > 0 and card2.health > 0):
            card1.attack(card2)
            card2.defend(card1.damage)

        if (card1.health <= 1):
            card2.update_wins(1)
            card1.update_losses(1)
            card1.calculate_rating()
            card2.calculate_rating()
            result["winner"] = card2_id
            result["loser"] = card1_id
            result["winner_rating"] = card2.rating
            result["loser_rating"] = card1.rating
            self.total_rating += card1.rating + card2.rating

        if (card2.health <= 1):
            card1.update_wins(1)
            card2.update_losses(1)
            card1.calculate_rating()
            card2.calculate_rating()
            result["winner"] = card1_id
            result["loser"] = card2_id
            result["winner_rating"] = card1.rating
            result["loser_rating"] = card2.rating
            self.total_rating += card1.rating + card2.rating

        return (result)

    def get_leaderboard(self) -> List:
        sorted_cards = sorted(self.cr_card.values(),
                              key=lambda card: card.rating, reverse=True)
        leaderboard = []
        for card in sorted_cards:
            leaderboard.append(f"{card.name} - Rating: {card.rating} "
                               f"({card.win}-{card.loose})")
        return (leaderboard)

    def generate_tournament_report(self) -> Dict:
        report = {}
        try:
            report["total_cards"] = self.nb_card
            report["matches_played"] = self.matches_played
            report["avg_rating"] = self.total_rating / self.nb_card
            report["platform_status"] = "active"
        except ZeroDivisionError as e:
            print("Error:", e)
        return (report)
