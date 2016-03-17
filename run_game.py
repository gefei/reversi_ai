#!/usr/bin/env python3
from sys import argv
import time
from game.reversi import Reversi
from agents import random_agent, monte_carlo_agent, human_agent, test_carlo_agent
from util import *


def main():

    board_size = (8, 8)
    bot_time = 10
    agent_args = {
        'BlackAgent': test_carlo_agent.MonteCarloAgent,
        'WhiteAgent': test_carlo_agent.MonteCarloAgent,
        'print': False,
        'white_time': bot_time,
        'black_time': bot_time
    }

    amount = 1
    if len(argv) > 1 and argv[1].isdigit():
        amount = int(argv[1])
    if len(argv) > 2 and argv[2].isdigit():
        agent_args['white_time'] = int(argv[2])
        agent_args['black_time'] = int(argv[2])
    if 'print' in argv:
        agent_args['print'] = True
    if 'white' in argv:
        agent_args['WhiteAgent'] = monte_carlo_agent.MonteCarloAgent
        agent_args['BlackAgent'] = human_agent.HumanAgent
    elif 'black' in argv:
        agent_args['BlackAgent'] = monte_carlo_agent.MonteCarloAgent
        agent_args['WhiteAgent'] = human_agent.HumanAgent

    summary = []
    white_wins = 0
    black_wins = 0
    start = time.time()
    for t in range(1, amount + 1):
        print('starting game {} of {}'.format(t, amount))
        reversi = Reversi(board_size, **agent_args)
        winner, white_score, black_score = reversi.play_game()
        if winner == WHITE:
            white_wins += 1
        elif winner == BLACK:
            black_wins += 1
        print('game {} complete.'.format(t))
        message = '{} wins! {}-{}'.format(
            color_name[winner], white_score, black_score)
        print(message)
        summary.append(message)

    print('time: {} minutes'.format((time.time() - start) / 60))
    print('summary: {} games played'.format(len(summary)))
    for each in summary:
        print(each)
    print('Black won {}%'.format(black_wins / (black_wins + white_wins) * 100))

if __name__ == '__main__':
    main()
