#Name: Nguyen Vo
#PISD: 1673509


class Team:
    def __init__(self,):
        self.teamname = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

if __name__ == "__main__":
    team = Team()
    teamName = input()
    teamWins = int(input())
    teamLoss = int(input())

    team.teamname = teamName
    team.team_wins = teamWins
    team.team_losses = teamLoss

    if team.get_win_percentage() > 0.5:
        print('Congratulations, Team', team.teamname, 'has a winning average!')
    else:
        print('Team', team.teamname, 'has a losing average.')