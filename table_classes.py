import dataclasses


@dataclasses.dataclass
class Player:
    name: str
    elo: int

@dataclasses.dataclass
class Fighter:
    name: str
    elo: int

@dataclasses.dataclass
class Elo:
    id: int
    value: int
    fighter_name: str
    player_name: str


@dataclasses.dataclass
class Games:
    winner: str
    loser: str
    winner_fighter: str
    loser_fighter: str
    winner_kills: int
    loser_kills: int
@dataclasses.dataclass
class EloOfPlayerFighter:
    player_name: str
    fighter_name: str
    elo: int

