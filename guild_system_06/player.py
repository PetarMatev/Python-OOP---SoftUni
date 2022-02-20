class Player:

    # create constructor for class Player.
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    # Create a method to add skill.
    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills.keys():
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    # Create Method to return player's info.
    def player_info(self):
        info_dict = [f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}"]
        for key, value in self.skills.items():
            info_dict.append(f"==={key} - {value}")
        return "\n".join(info_dict)
