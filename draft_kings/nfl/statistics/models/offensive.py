class YardageStatistics:
    def __init__(self, passing: int, rushing: int, receiving: int):
        self.passing = passing
        self.rushing = rushing
        self.receiving = receiving


class KickReturnTouchdownStatistics:
    def __init__(self, punts: int, kickoffs: int, field_goals: int):
        if 0 > punts or 0 > kickoffs or 0 > field_goals:
            raise ValueError("touchdowns cannot be negative")

        self.punts = punts
        self.kickoffs = kickoffs
        self.field_goals = field_goals


class TouchdownStatistics:
    def __init__(self, passing: int, rushing: int, receiving: int, kick_returns: KickReturnTouchdownStatistics,
                 fumble_recoveries: int):
        if 0 > passing or 0 > rushing or 0 > receiving or 0 > fumble_recoveries:
            raise ValueError("touchdowns cannot be negative")

        self.passing = passing
        self.rushing = rushing
        self.receiving = receiving
        self.kick_returns = kick_returns
        self.fumble_recoveries = fumble_recoveries


class TwoPointConversionStatistics:
    def __init__(self, thrown: int, rushed: int, caught: int):
        if 0 > thrown or 0 > rushed or 0 > caught:
            raise ValueError("conversions cannot be negative")

        self.thrown = thrown
        self.rushed = rushed
        self.caught = caught


class ConversionStatistics:
    def __init__(self, two_point: TwoPointConversionStatistics):
        self.two_point = two_point


class ScoringStatistics:
    def __init__(self, touchdowns: TouchdownStatistics, conversions: ConversionStatistics):
        self.touchdowns = touchdowns
        self.conversions = conversions


class TurnoverStatistics:
    def __init__(self, interceptions: int, fumbles_lost: int):
        if 0 > interceptions or 0 > fumbles_lost:
            raise ValueError("turnovers cannot be negative")

        self.interceptions = interceptions
        self.fumbles_lost = fumbles_lost


class OffensiveStatistics:
    def __init__(self, yards: YardageStatistics, scoring: ScoringStatistics, turnovers: TurnoverStatistics,
                 receptions: int):
        if 0 > receptions:
            raise ValueError("receptions cannot be negative")

        self.yards = yards
        self.scoring = scoring
        self.turnovers = turnovers
        self.receptions = receptions
