class Robot:
    abilities = []
    region = ""
    id = 0

    @property
    def serial_number(self):
        return f"{self.__class__.region.lower()}_{self.__class__.id}"

    def save_ability(self, ability):
        self.__class__.abilities.append(ability)
        if isinstance(self, RoboCat):
            if ability not in self.skills:
                self.skills.append(ability)
            return True

    def remove_ability(self, ability):
        if ability in self.__class__.abilities:
            self.__class__.abilities.remove(ability)
        if isinstance(self, RoboCat):
            if ability in self.skills:
                self.skills.remove(ability)
                return True


class Cat:
    def __init__(self, name, age, bread, skills=[]):
        self.name = name
        self.age = age
        self.bread = bread
        self.skills = skills

    @property
    def knowledge_level(self):
        return len(self.skills)

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
            return True

    def forget_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
            return True


class RoboCat(Cat, Robot):
    def __init__(self, name, age, bread):
        self.abilities = []
        if bread.lower() in {"aegean", "aphrodite giant", "asian semi-longhair", "birman"}:
            Robot.region = "Europe"
        elif bread.lower() in {"american bobtail", "american curl", "american ringtail", "american shorthair"}:
            Robot.region = "USA"
        else:
            Robot.region = "China"
        super().__init__(name, age, bread)

    def add_skill(self, skill):
        print(f"Received skill: {skill}")
        print(f"Cat add skill result: {super().add_skill(skill)}")
        print(f"Robot save ability result: {self.save_ability(skill)}")

    def remove_skill(self, skill):
        print(f"Received skill: {skill}")
        print(f"Cat forget skill result: {self.forget_skill(skill)}")
        print(f"Robot remove ability result: {self.remove_ability(skill)}")
