import gym
from gym import error, spaces, utils
from gym.utils import seeding

try:
    from twenty48 import Game, GameOver
except ImportError as e:
    raise error.DependencyNotInstalled("{}. (HINT: you can install twenty48 from github.com/bakera81/2048.)".format(e))


class Twenty48Env(gym.Env):

    metadata = {'render.modes': ['human']}

    def __init__(self, board_size=4):
        self.game = Game()
        self.action_space = spaces.Discrete(4)

    def _step(self, action):
        done = False
        reward = 0.0

        if action == 0:
            reward = self.game.down()
        elif action == 1:
            reward = self.game.up()
        elif action == 2:
            reward = self.game.right()
        elif action == 3:
            reward = self.game.left()
        else:
            raise error.Error("Unsupported action: {0}".format(action))

        done = self.game.is_over()

        observation = self.game
        reward = float(reward)
        info = self.game.sequence[-1]

        return observation, reward, done, info


    def _reset(self):
        self.game = Game()

    def _render(self, mode='human', close=False):
        print(self.game.board)
