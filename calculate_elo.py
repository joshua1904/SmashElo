import math

K_FACTOR = 32


def calculate_expected(player_rating, opponent_rating):
    return 1 / (1 + math.pow(10, (opponent_rating - player_rating) / 400))


def update_ratings(player_rating, opponent_rating, player_win):
    expected_score = calculate_expected(player_rating, opponent_rating)
    if player_win:
        actual_score = 1
    else:
        actual_score = 0
    new_rating = player_rating + K_FACTOR * (actual_score - expected_score)
    return int(new_rating)


def reverse_elo(current_elo_looser: int, current_elo_winner) -> tuple | None:
    """return value (loser elo, winner_elo)"""  #
    possible_start_value_looser = current_elo_looser + K_FACTOR
    possible_start_value_winner = current_elo_winner - K_FACTOR
    for i in range(1, K_FACTOR + 1):
        possible_start_value_winner += 1
        for i in range(1, K_FACTOR + 1):
            possible_start_value_looser -= 1
            loser_elo = update_ratings(possible_start_value_looser, possible_start_value_winner, False)
            winner_elo = update_ratings(possible_start_value_winner, possible_start_value_looser, True)
            if loser_elo == current_elo_looser and winner_elo == current_elo_winner:
                return possible_start_value_looser, possible_start_value_winner
        possible_start_value_looser = current_elo_looser + K_FACTOR
    return None
