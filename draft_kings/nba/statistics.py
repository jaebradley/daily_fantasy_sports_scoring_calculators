class Statistics:
    def __init__(self, points_scored: int, three_pointers_made: int, assists: int, rebounds: int, steals: int,
                 blocks: int, turnovers: int):
        if points_scored < 3 * three_pointers_made:
            raise ValueError("Points scored is contradicted by three-pointers made")

        if 0 > points_scored or 0 > three_pointers_made or 0 > assists or 0 > rebounds or 0 > steals or 0 > blocks \
                or 0 > turnovers:
            raise ValueError("Statistical values cannot be negative")

        self.points_scored = points_scored
        self.three_pointers_made = three_pointers_made
        self.assists = assists
        self.rebounds = rebounds
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Statistics):
            return other.points_scored == self.points_scored and other.three_pointers_made == self.three_pointers_made \
                   and other.assists == self.assists and other.rebounds == self.rebounds and other.steals == self.rebounds \
                   and other.blocks == self.blocks and other.turnovers == self.turnovers

        return False

    def __str__(self):
        return f'Points Scored: {self.points_scored} | Three-Pointers Made: {self.three_pointers_made} | Assists: ' \
               f'{self.assists} | Rebounds: {self.rebounds} | Steals: {self.steals} | Blocks: {self.blocks} | ' \
               f'Turnovers: {self.turnovers}'

    def __repr__(self):
        return f'Statistics(points_scored={self.points_scored}, three_pointers_made={self.three_pointers_made}, ' \
               f'assists={self.assists}, rebounds={self.rebounds}, steals={self.steals}, blocks={self.blocks}, ' \
               f'turnovers={self.turnovers})'
