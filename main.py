class Collaborator():
    def __init__(self, name, adge, rating, male_female):
        self.name = name
        self.adge = adge
        self.rating = rating
        self.male_female = male_female

    def work(self):
        print(f"{self.name} работает")
        self.rating +=1
    def doesn_t_work(self):
        print(f"{self.name} НЕ работает")
        self.rating -= 1

    def info (self):
        print(f"сотрудник {self.name}")
        print(f"пол - {self.male_female}")
        print(f"возраст - {self.adge}")
        print(f"рейтинг - {self.rating}")
