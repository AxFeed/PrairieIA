#Dataframe
import pandas as pd

class Dataframe:
    def __init__(self):
        self = self

    def generate(self, keys, winrate):
        df = pd.DataFrame(index=keys, columns=keys)

        k = 0
        for human_strategy in keys:
            for robot_strategy in keys:
                df.loc[human_strategy, robot_strategy] = winrate[k]
                k += 1

        df = df.astype(float)

        return df