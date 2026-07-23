import abc

class Creature(abc.ABC):
    @abc.abstractmethod
    def attack(self):
        pass

    def describe():
        print("")


class Flameling(Creature):
    def attack(self):
        return("The Flameling is attacking.")
    
class Pyrodon(Creature):
    def attack(self):
        return("The Pyrodon is attacking")
    
class Aquabub(Creature):
    def attack(self):
        return("The Aquabub is attacking")
    
class Tarragon(Creature):
    def attack(self):
        return("The Tarragon is attacking")


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self):
        pass

    @abc.abstractmethod
    def create_evolved(self):
        pass

class FlameFactory(CreatureFactory):
    def create_flame(self) -> Creature:
        return Flameling()
    
    def create_pyrodon(self) -> Creature:
        return Pyrodon()