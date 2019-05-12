import random

class Creature:
    def __init__(self,name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name,self.level
        )

    def get_defense_roll(self):
        return random.randint(1,12) * self.level


class Wizard(Creature):

    def __repr__(self):
        return "Wizerd: {} of level {}".format(
            self.name,self.level
        )
    def attack(self,creature):
        print("The wizard {} attacks {}!".format(self.name,creature.name

        ))

        my_roll = self.get_defense_roll()
        creature_roll = creature.get_defense_roll()

        print("You roll {}...".format(my_roll))
        print("Creature rolls {} ...".format(creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has defeated {}".format(creature.name))
            return True
        else:
            print("The wizard has been defeated by {}".format(creature.name))
            return False


class SmallAnimal(Creature):
    def get_defense_roll(self):
        base_roll = super().get_defense_roll()

        return base_roll / 2

class Dragon(Creature):
    def __init__(self,name,level,scaliness,breaths_fire):
        super().__init__(name,level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defense_roll(self):
        base_roll = super().get_defense_roll()
        # fire_modifier = VALUE_IF_TRUE if SOME_TEST else VALUE IF_FALSE
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier






