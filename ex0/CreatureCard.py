# from ex0.Card import Card


class CreatureCard:

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        # super().__init__(name, cost, rarity)
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.attack = attack
        self.health = health
        self.type = "Creature"
# infos
        print("{" + f"'name': {self.name}, 'cost': {self.cost}, "
                    f"'rarity': {self.rarity}, \n'type': {self.type}, "
                    f"'attack': {self.attack}, 'health': {self.health}" + "}")

    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target) -> dict:
        pass
