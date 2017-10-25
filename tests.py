from bowling import score, split_frames, frame_score, get_next_throws


def test_split_frame():
    assert split_frames('5/ 5/ X X X') == ['5/', '5/', 'X', 'X', 'X']


def test_frame_only_score_strike():
    assert frame_score('X') == (10, 2)


def test_frame_only_score_spare():
    assert frame_score('5/') == (10, 1)


def test_frame_only_score_miss():
    assert frame_score('9-') == (9, 0)


def test_frame_only_score():
    assert frame_score('53') == (8, 0)


def test_get_next_throws_strike_spare():
    assert get_next_throws(['5/', '5/', 'X', '5/', 'X'], 2, 2) == '5/'


def test_get_next_throws_spare_strike():
    assert get_next_throws(['5/', '5/', 'X', '5/', 'X'], 1, 1) == 'X'


def test_get_next_throws_empty():
    assert get_next_throws(['5/', '5/', 'X', '5/', 'X'], 1, 0) == ''


def test_all_strikes():
    assert score('X X X X X X X X X X X X') == 300


def test_all_spares():
    assert score('5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5') == 150


def test_all_nine_misses():
    assert score('9- 9- 9- 9- 9- 9- 9- 9- 9- 9-') == 90


def test_all_misses():
    assert score('-- -- -- -- -- -- -- -- -- --') == 0


def test_most_misses():
    assert score('-- -- -- -- -/ 11 -- -- -- --') == 13


def test_game_score_two_strikes():
    assert score('9- 9- 9- X X 54 9- 9- 9- 9-') == 116
