#! /bin/python3.10
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/22 10:10:48 by bbeaurai            #+#    #+#            #
#   Updated: 2026/02/22 11:30:56 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from ex0 import CreatureCard

if __name__ == "__main__":
    stamina = 6
    game_state = {}

    print("\n" + " DataDeck Card Foundation ".center(79, "="))

    print("\n" + "Testing Abstract Base Class Design:")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    target = CreatureCard("Goblin Warrior", 3, "rare", 7, 2)

# =============================================================================
# ======================== CreatureCard Info: =================================
# =============================================================================

    print("\n" + "CreatureCard Info:")
    print(creature.get_card_info())

# =============================================================================
# ============= Playing Fire Dragon with 6 mana available =====================
# =============================================================================

    print("\n" + "Playing Fire Dragon with 6 mana available:")
    print("Playable:", creature.is_playable(stamina))
    print("Play result:", creature.play(game_state))

# =============================================================================
# ================= Fire Dragon attacks Goblin Warrior ========================
# =============================================================================

    print("\n" + "Fire Dragon attacks Goblin Warrior:")
    print("Attack result:", creature.attack_target(target))
    stamina -= creature.cost

# =============================================================================
# ===================== Testing insufficient mana =============================
# =============================================================================

    print("\n" + f"Testing insufficient mana ({stamina} available):")
    if (creature.is_playable(stamina) is False):
        print("Playable: False" + "\n"
              "Oops! You don't have enough stamina to play "
              f"{stamina}/{creature.cost}🪫​.")
    else:
        print("Playable: True")
        print("Play result:", creature.play(game_state))

    print("\n" + "Abstract pattern successfully demonstrated!")
