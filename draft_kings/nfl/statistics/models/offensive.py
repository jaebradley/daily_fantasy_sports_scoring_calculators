class YardageStatistics:
    def __init__(self, passing: int, rushing: int, receiving: int):
        self.passing = passing
        self.rushing = rushing
        self.receiving = receiving


class KickReturnTouchdownStatistics:
    def __init__(self, punts: int, kickoffs: int, field_goals: int):
        self.punts = punts
        self.kickoffs = kickoffs
        self.field_goals = field_goals


class TouchdownStatistics:
    def __init__(self, passing: int, rushing: int, receiving: int, kick_returns: KickReturnTouchdownStatistics,
                 fumble_recoveries: int):
        self.passing = passing
        self.rushing = rushing
        self.receiving = receiving
        self.kick_returns = kick_returns
        self.fumble_recoveries = fumble_recoveries


class TwoPointConversionStatistics:
    def __init__(self, thrown: int, rushed: int, caught: int):
        self.thrown = thrown
        self.rushed = rushed
        self.caught = caught


class ConversionStatistics:
    def __int__(self, two_point: TwoPointConversionStatistics):
        self.two_point = two_point


class ScoringStatistics:
    def __init__(self, touchdowns: TouchdownStatistics, conversions: ConversionStatistics):
        self.touchdowns = touchdowns
        self.conversions = conversions


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
