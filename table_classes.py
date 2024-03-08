import dataclasses


@dataclasses.dataclass
class Player:
    id: int
    name: str
    elo: int

@dataclasses.dataclass
class Fighter:
    id: int
    name: str
    elo: int

@dataclasses.dataclass
class Elo:
    id: int
    value: int
    fighter_id: int
    player_id: int


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

