def split_frames(inp):
    """
    split input data to frames
    :param inp: str of space separated frames
    :return: list of frames
    """
    return inp.split(' ')


def frame_score(frame):
    """
    Calculate frame score without look ahead score
    :param frame: str
    :return: (score_of_frame, look_ahead)
    """
    if frame.endswith('/'):
        return (10, 1)

    strikes = frame.count('X')
    return (
        sum([int(throw) for throw in frame.strip('-').strip('X')]) + strikes*10,
        2 if strikes else 0
    )


def get_next_throws(frames, i, steps):
    """
    get next throws as frame of size steps
    :param frames:
    :param i: index of reference frame
    :param steps: how many steps to take
    :return: next throws as str
    """
    return ''.join(frames[i+1:])[:steps]


def score(game):
    """
    Calculate game score
    :param game: str containing frames seperated by spaces
    :return: total game score
    """
    frames = split_frames(game)

    game_score = 0

    for i in range(10):
        score, steps = frame_score(frames[i])
        # add frame score plus points of next "steps" throws
        game_score += score + frame_score(get_next_throws(frames, i, steps))[0]
    return game_score
