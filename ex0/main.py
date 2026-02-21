#! /bin/python3.10

# Exercice 0 : Base des cartes - Maîtriser les classes de base abstraites
# importations absolues
# from ex0.Card import Card
# from ex1.SpellCard import SpellCard
# N'utilisez jamais d'importations relatives
# telles que from ..ex0.Card import Card

from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":

    print("\n" + " DataDeck Card Foundation ".center(79, "="))

    print("\n" + "Testing Abstract Base Class Design:")

    print("\n" + "CreatureCard Info:")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("\n" + "Playing Fire Dragon with 6 mana available:")

    print("\n" + "Fire Dragon attacks Goblin Warrior:")

    print("\n" + "Testing insufficient mana (3 available):")

    print("\n" + "Abstract pattern successfully demonstrated!")
