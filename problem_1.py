from enum import Enum
import numpy as np



class Result(Enum):
    """result of the game"""
    HEAD = 1
    TAIL = 0


class Game():
    def __init__(self, id, prob):

        self._id = id
        self._rnb = np.random
        self._rnb.seed(id)

        self._Prob = prob #head
        self._Results = Result.HEAD
        self._Time = 0
        self._Reward = 0


    def simulate(self, n_time_steps):

        t = 0 # simulate time

        while t < n_time_steps:
            if self._rnb.sample() < self._Prob:
                self._Results = Result.HEAD
                self._Time += 1

                #incremate time
                t += 3
            t+=1


    def get_reward(self):
        self._Reward =  - 250 + self._Time *100
        return self._Reward



class Cohort:
    def __init__(self, id, total_times, prob):

        self._id = id
        self._total_times = total_times
        self._Prob = prob

        self._games = [] #list of games
        self._gameTimes = [] # list of playing times

        #populate the cohort

        for i in range(total_times):
            #create the game
            game = Game(id*total_times+1, prob)
            # add the game to the cohort
            self._games.append(game)


    def simlate(self, n_time_steps):

        #simulate all the games
        for games in self._games:
            games.simulate(n_time_steps)

            value = games.get_reward()
            self._gameTimes.append(value)


    def get_ave_game_time(self):
        return sum(self._gameTimes)/len(self._gameTimes)









