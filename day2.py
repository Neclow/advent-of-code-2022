"""Day 2 of AoC."""
import pandas as pd

OPP_PLAY = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
MY_PLAY = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
WIN = 6
DRAW = 3

MY_LOSS = {
    'Paper': 'Rock',
    'Rock': 'Scissors',
    'Scissors': 'Paper'
}

MY_POINTS = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

def find_my_play(result, opponent):
    """Find what I played depending on the expected result

    The value was mapped from MY_PLAY

    Parameters
    ----------
    result : str
        Expected result
    opponent : str
        What the opponent played

    Returns
    -------
    str
        What I played
    """
    if result == MY_PLAY['X']: # loss
        return MY_LOSS[opponent]
    elif result == MY_PLAY['Y']: # draw
        return opponent
    elif result == MY_PLAY['Z']:
        return next(iter(set(MY_LOSS) - {opponent, MY_LOSS[opponent]}))
    else:
        raise ValueError(f'Unexpected value for {result}.')

if __name__ == '__main__':
    results = pd.read_csv(
        'input/day2.txt',
        sep=" ",
        header=None,
        names=['Opponent', 'Me']
    ).replace(OPP_PLAY).replace(MY_PLAY)

    # Part 1
    results['loss'] = results.Opponent.replace(MY_LOSS) == results.Me

    results['draw'] = DRAW * (results.Opponent == results.Me)

    results['win'] = WIN * ((~results.loss) & (~results.draw))

    results['total_points'] = results.win + results.draw + results.Me.replace(MY_POINTS)

    print(results.total_points.sum())

    # Part 2
    results['Me2'] = results.apply(lambda x: find_my_play(x.Me, x.Opponent), axis=1)

    results['loss2'] = results.Opponent.replace(MY_LOSS) == results.Me2

    results['draw2'] = DRAW * (results.Opponent == results.Me2)

    results['win2'] = WIN * ((~results.loss2) & (~results.draw2))

    results['total_points2'] = results.win2 + results.draw2 + results.Me2.replace(MY_POINTS)

    print(results.total_points2.sum())
