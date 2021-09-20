from daily_fantasy_sports_scoring_calculators.draft_kings.nfl.statistics.models.defensive import DefensiveStatistics
from shared.calculators.scoring import StatisticalValueCalculator


class SacksCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.sacks


class InterceptionsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.turnovers.interceptions


class FumbleRecoveriesCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.turnovers.fumble_recoveries


class PuntReturnTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.scoring.touchdowns.kick_returns.punts


class KickoffReturnTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.scoring.touchdowns.kick_returns.kickoffs


class FieldGoalReturnTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.scoring.touchdowns.kick_returns.field_goals


class InterceptionReturnTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.scoring.touchdowns.turnovers.interceptions


class FumbleRecoveryTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.scoring.touchdowns.turnovers.fumble_recoveries


class BlockedPuntReturnTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.scoring.touchdowns.blocked_kicks.punts


class BlockedFieldGoalReturnTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.scoring.touchdowns.blocked_kicks.field_goals


class SafetiesCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.scoring.safeties


class BlockedKicksCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.blocked_kicks


class ConversionReturnsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.scoring.conversion_returns


class PointsAllowedCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: DefensiveStatistics):
        return statistics.points_allowed
