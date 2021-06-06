class Statistics:
    def __init__(self, points_scored, three_pointers_made, assists, rebounds, steals, blocks, turnovers):
        if points_scored < 3 * three_pointers_made:
            raise ValueError("points scored is less than three-pointers made")

        if 0 > points_scored or 0 > three_pointers_made or 0 > assists or 0 > rebounds or 0 > steals or 0 > blocks \
                or 0 > turnovers:
            raise ValueError("statistical values cannot be negative")

        self.points_scored = points_scored
        self.three_pointers_made = three_pointers_made
        self.assists = assists
        self.rebounds = rebounds
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
