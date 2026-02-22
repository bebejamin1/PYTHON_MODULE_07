#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 13:33:02 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 15:58:47 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


if __name__ == "__main__":

    print(" DataDeck Ability System ".center(79, "="))

    print(f"- {Card.__name__}: {[m for m in dir(Card) if m[0] != '_']}")
    print(f"- {Combatable.__name__}: "
          f"{[m for m in dir(Combatable) if m[0] != '_']}")
    print(f"- {Magical.__name__}: {[m for m in dir(Magical) if m[0] != '_']}")

# =============================================================================
# =============================== ARCANE ======================================
# =============================================================================

    print("\n" + "Playing Arcane Warrior (Elite Card):")

    card = EliteCard("Arcane Warrior", 3, "Legendary", 5, 6)
    target1 = EliteCard("Enemy1", 2, "Legendary", 5, 10)
    target2 = EliteCard("Enemy2", 2, "Legendary", 5, 10)
    targets = [target1, target2]
    total_mana = card.cost + target1.cost + target1.cost

# =============================================================================
# =============================== COMBAT ======================================
# =============================================================================

    print("\n" + "Combat phase:")
    try:
        print("Attack result:", card.attack(target1))
        print("Defense result:", card.defend(target1.damage))
    except NameError as e:
        print(e)

# =============================================================================
# ================================ MAGIC ======================================
# =============================================================================

    print("\n" + "Magic phase:")
    print("Spell cast:", card.cast_spell("Fireball", targets))
    print("Mana channel:", card.channel_mana(total_mana))

    print("\n" + "Multiple interface implementation successful!")
