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
