
# cd ../2048
# pip install -e .
# cd ../gym-2048
# pip install -e .


import gym
import gym_2048

env = gym.make('2048-v0')
observation = env.reset()

for t in range(500):
    env.render()
    # print(observation)
    action = env.action_space.sample()
    print(action)
    observation, reward, done, info = env.step(action)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
