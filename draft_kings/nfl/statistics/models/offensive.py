class YardageStatistics:
    def __init__(self, passing: int, rushing: int, receiving: int):
        self.passing = passing
        self.rushing = rushing
        self.receiving = receiving


class TouchdownStatistics:
    def __init__(self, passing: int, rushing: int, receiving: int, kick_returns: int, fumble_recoveries: int):
        self.passing = passing
        self.rushing = rushing
        self.receiving = receiving
        self.kick_returns = kick_returns
        self.fumble_recoveries = fumble_recoveries


class ScoringStatistics:
    def __init__(self, touchdowns: TouchdownStatistics, two_point_conversions: int):
        self.touchdown = touchdowns
        self.two_point_conversions: two_point_conversions


class TurnoverStatistics:
    def __init__(self, interceptions: int, fumbles_lost: int):
        self.interceptions = interceptions
        self.fumbles_lost = fumbles_lost


class OffensiveStatistics:
    def __init__(self, yards: YardageStatistics, scoring: ScoringStatistics, turnovers: TurnoverStatistics,
                 receptions: int):
        self.yards = yards
        self.scoring = scoring
        self.turnovers = turnovers
        self.receptions = receptions
