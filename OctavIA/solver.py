# solver
def solve(line):
    if line['1'] == line['ref']: return 1
    if line['2'] == line['ref']: return 2
    return 3


def solveDf(df):
    df['v'] = df.apply(solve, axis=1)
    return df