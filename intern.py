def find_qualified_games(game_data, true_shooting_cutoff, player_count):
    # Function to calculate True Shooting Percentage
    def true_shooting_percentage(player):
        two_pointers = player['fieldGoal2Made'] * 2
        three_pointers = player['fieldGoal3Made'] * 3
        free_throws = player['freeThrowMade']
        total_points = two_pointers + three_pointers + free_throws
        total_attempts = player['fieldGoal2Attempted'] + player['fieldGoal3Attempted'] + 0.44 * player[
            'freeThrowAttempted']

        if total_attempts == 0:
            return 0  # To Avoid the division by zero if the player didn't attempt any shots
        return (total_points / (2 * total_attempts)) * 100

    # Dictionary to store the qualified players for each gameID
    qualified_games = {}

    # To Process the  each player's data in game_data
    for player in game_data:
        game_id = player['gameID']
        ts_percentage = true_shooting_percentage(player)

        # If player's True Shooting percentage meets the cutoff,then store the game_id
        if ts_percentage >= true_shooting_cutoff:
            if game_id not in qualified_games:
                qualified_games[game_id] = 0
            qualified_games[game_id] += 1

    # To Find the games where at least <player_count> players meet the True Shooting cutoff
    result = [game_id for game_id, count in qualified_games.items() if count >= player_count]

    # Sorting the games by most recent date
    game_dates = {player['gameID']: player['gameDate'] for player in game_data}
    result.sort(key=lambda game_id: game_dates[game_id], reverse=True)

    return result


# Test Case 1
def test_case_1():
    game_data = []
    qualified_games = find_qualified_games(game_data, 57, 1)
    print(f"Test Case 1: result {qualified_games}")
    assert qualified_games == []


# Test Case 2
def test_case_2():
    game_data = [
        {'gameID': 1, 'playerID': 5, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 2,
         'fieldGoal3Attempted': 7, 'fieldGoal3Made': 2, 'freeThrowAttempted': 3, 'freeThrowMade': 3},
        {'gameID': 2, 'playerID': 5, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 5,
         'fieldGoal3Attempted': 5, 'fieldGoal3Made': 1, 'freeThrowAttempted': 2, 'freeThrowMade': 2},
    ]
    qualified_games = find_qualified_games(game_data, 53, 1)
    print(f"Test Case 2: result {qualified_games}")
    assert qualified_games == [2]


# Test Case 3
def test_case_3():
    game_data = [
        {'gameID': 9, 'playerID': 42, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3,
         'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 4, 'freeThrowMade': 3},
        {'gameID': 10, 'playerID': 34, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 7,
         'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
    ]
    qualified_games = find_qualified_games(game_data, 0, 1)
    print(f"Test Case 3:result {qualified_games}")
    assert qualified_games == [10, 9]


# Test Case 4
def test_case_4():
    game_data = [
        {'gameID': 9, 'playerID': 24, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 14, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 4, 'freeThrowMade': 3},
        {'gameID': 9, 'playerID': 35, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 1, 'freeThrowAttempted': 4, 'freeThrowMade': 2},
        {'gameID': 9, 'playerID': 34, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 3, 'freeThrowMade': 1},
        {'gameID': 9, 'playerID': 42, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 4, 'freeThrowMade': 0},
        {'gameID': 10, 'playerID': 24, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 7, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 8, 'freeThrowMade': 1},
        {'gameID': 10, 'playerID': 42, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 7, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 1, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
        {'gameID': 10, 'playerID': 25, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 4, 'freeThrowMade': 3},
        {'gameID': 10, 'playerID': 33, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 6, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
        {'gameID': 6, 'playerID': 34, 'gameDate': '02/11/2023', 'fieldGoal2Attempted': 12, 'fieldGoal2Made': 6, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 1, 'freeThrowAttempted': 6, 'freeThrowMade': 6},
        {'gameID': 6, 'playerID': 25, 'gameDate': '02/11/2023', 'fieldGoal2Attempted': 9, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 2, 'freeThrowAttempted': 2, 'freeThrowMade': 0},
        {'gameID': 5, 'playerID': 42, 'gameDate': '01/06/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 3, 'freeThrowMade': 3},
        {'gameID': 4, 'playerID': 34, 'gameDate': '01/22/2023', 'fieldGoal2Attempted': 18, 'fieldGoal2Made': 5, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 3, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
    ]
    qualified_games = find_qualified_games(game_data, 52, 1)
    print(f"Test Case 4: result {qualified_games}")
    assert qualified_games == [6, 10, 5]


#test_case_5:
def test_case_5():
    game_data = [
        {'gameID': 6, 'playerID': 34, 'gameDate': '02/11/2023', 'fieldGoal2Attempted': 12, 'fieldGoal2Made': 6, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 1, 'freeThrowAttempted': 6, 'freeThrowMade': 6},
        {'gameID': 6, 'playerID': 25, 'gameDate': '02/11/2023', 'fieldGoal2Attempted': 9, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 2, 'freeThrowAttempted': 2, 'freeThrowMade': 0},
        {'gameID': 9, 'playerID': 24, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 14, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 3, 'freeThrowAttempted': 4, 'freeThrowMade': 4},
        {'gameID': 9, 'playerID': 35, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 1, 'freeThrowAttempted': 4, 'freeThrowMade': 2},
        {'gameID': 9, 'playerID': 34, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 3, 'freeThrowMade': 1},
        {'gameID': 9, 'playerID': 42, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 4, 'freeThrowMade': 0},
        {'gameID': 10, 'playerID': 24, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 7, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 5, 'freeThrowMade': 4},
        {'gameID': 10, 'playerID': 42, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 6, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 1, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
        {'gameID': 10, 'playerID': 25, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 4, 'freeThrowMade': 3},
        {'gameID': 10, 'playerID': 33, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 7, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
        {'gameID': 5, 'playerID': 42, 'gameDate': '01/06/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 3, 'freeThrowMade': 3},
        {'gameID': 4, 'playerID': 34, 'gameDate': '01/22/2023', 'fieldGoal2Attempted': 18, 'fieldGoal2Made': 5, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 3, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
    ]
    qualified_games = find_qualified_games(game_data, 46, 3)
    print(f"Test Case 5: result {qualified_games}")
    assert qualified_games == [10]

#test_case_6:
def test_case_6():
    game_data = [
        {'gameID': 6, 'playerID': 34, 'gameDate': '02/11/2023', 'fieldGoal2Attempted': 12, 'fieldGoal2Made': 0, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 6, 'freeThrowMade': 6},
        {'gameID': 9, 'playerID': 35, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 1, 'freeThrowAttempted': 4, 'freeThrowMade': 2},
        {'gameID': 10, 'playerID': 24, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 7, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 5, 'freeThrowMade': 4},
        {'gameID': 10, 'playerID': 42, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 6, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 1, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
        {'gameID': 10, 'playerID': 25, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 4, 'freeThrowMade': 3},
        {'gameID': 10, 'playerID': 33, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 7, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
        {'gameID': 5, 'playerID': 42, 'gameDate': '01/06/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 3, 'freeThrowMade': 3},
        {'gameID': 4, 'playerID': 34, 'gameDate': '01/22/2023', 'fieldGoal2Attempted': 3, 'fieldGoal2Made': 0, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 2, 'freeThrowMade': 0},
    ]
    qualified_games = find_qualified_games(game_data, 1, 1)
    print(f"Test Case 6: result {qualified_games}")
    assert qualified_games == [6, 10, 5, 9]


# Running all the test cases
test_case_1()
test_case_2()
test_case_3()
test_case_4()
test_case_5()
test_case_6()
