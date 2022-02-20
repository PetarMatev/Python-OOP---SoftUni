from player import Player


class Guild:

    # constructor for Guild Class
    def __init__(self, name: str):
        self.name = name
        self.players = []

    # Method to assign a player to a particular guild
    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        else:
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."
            else:
                return f"Player {player.name} is in another guild."

    # Method to Kick a Player out of Particular Guild
    def kick_player(self, player_name: str):
        for anyone in self.players:
            if anyone.name == player_name:
                anyone.guild = "Unaffiliated"
                self.players.remove(anyone)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    # Method to print out Info for a guild.
    def guild_info(self):
        main_info = [f"Guild: {self.name}"]
        for player_ in self.players:
            main_info.append(player_.player_info())
        return "\n".join(main_info)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
