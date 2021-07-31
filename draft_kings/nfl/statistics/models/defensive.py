class TouchdownStatistics:
    def __init__(self, interceptions: int, kick_returns: int, blocked_kicks: int, fumble_recoveries: int):
        self.interceptions = interceptions
        self.kick_returns = kick_returns
        self.blocked_kicks = blocked_kicks
        self.fumble_recoveries = fumble_recoveries


class ScoringStatistics:
    def __int__(self, touchdowns: TouchdownStatistics, safeties: int, conversion_returns: int):
        self.touchdowns = touchdowns
        self.safeties = safeties
        self.conversion_returns = conversion_returns


class TurnoverStatistics:
    def __int__(self, interceptions: int, fumble_recoveries: int):
        self.interceptions = interceptions
        self.fumble_recoveries = fumble_recoveries


class DefensiveStatistics:
    def __init__(self, scoring: ScoringStatistics, turnovers: TurnoverStatistics, sacks: int, blocked_kicks: int,
                 points_allowed: int):
        self.scoring = scoring
        self.turnovers = turnovers
        self.sacks = sacks
        self.blocked_kicks = blocked_kicks
        self.points_allowed: points_allowed
