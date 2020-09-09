import time
from copy import deepcopy

import pygame
import math


class Rompecabezas:
    def __init__(self):
        
        pygame.init()
        pygame.font.init()
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.dist = 200
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Rompecabezas 8 piezas')
        self.screen.fill(self.black)

    def empezar(self):

        # self.puzzle_numbers = self.generate_puzzle.generate_puzzle()
        # self.generate_puzzle.draw_puzzle(self.puzzle_numbers)
        # solve_button = Button(self.screen, (255, 255, 153), 450, 100, 100, 50, "Solve")
        # solve_button.draw((255, 255, 0))

        # self.h_digit_x = 100
        # self.h_digit_y = 100

        self.finish = False
        self.you_win = False

        while not self.finish:
            # self.highlight.move_count("8 Puzzle Puzzle", 130, 10)
            # solve_button.draw((255, 255, 0))

            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()
                # print(event)
                if event.type == pygame.QUIT:
                    self.finish = True

                if (event.type == pygame.KEYDOWN):
                    # if (event.key == pygame.K_RIGHT):
                    #     # print "*** RIGHT ***"
                    #     self.you_win = self.highlight.highlight_digit_to_be_swapped(100, 0, "RIGHT",
                    #                                                                 self.puzzle_numbers)
                    #     self.generate_puzzle.draw_puzzle(self.puzzle_numbers)

                    # if (event.key == pygame.K_LEFT):
                    #     # print "*** LEFT ***"
                    #     self.you_win = self.highlight.highlight_digit_to_be_swapped(-100, 0, "LEFT",
                    #                                                                 self.puzzle_numbers)
                    #     self.generate_puzzle.draw_puzzle(self.puzzle_numbers)

                    # if (event.key == pygame.K_DOWN):
                    #     # print "*** DOWN ***"
                    #     self.you_win = self.highlight.highlight_digit_to_be_swapped(0, 100, "DOWN",
                    #                                                                 self.puzzle_numbers)
                    #     self.generate_puzzle.draw_puzzle(self.puzzle_numbers)

                    # if (event.key == pygame.K_UP):
                    #     # print "*** UP ***"
                    #     self.you_win = self.highlight.highlight_digit_to_be_swapped(0, -100, "UP",
                    #                                                                 self.puzzle_numbers)
                    #     self.generate_puzzle.draw_puzzle(self.puzzle_numbers)
                    pass

                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     if solve_button.isOver(pos):
                #         print "You Clicked Solve button"
                #         self.solution = Solution(self.puzzle_numbers)

                #         path = self.get_sol()

                #         print "BOARD PATH: %s" % deepcopy(self.solution.sol_stack)
                #         for i, puzzle in enumerate(reversed(path)):
                #             # print puzzle
                #             self.screen.fill(self.black)
                #             self.highlight.move_count("8 Puzzle Puzzle", 130, 10)
                #             solve_button.draw((255, 255, 0))
                #             self.generate_puzzle.draw_puzzle(puzzle)
                #             self.highlight.move_count("Moves: %s" % str(i))
                #             pygame.display.update()
                #             # self.clock.tick(30)

                #             time.sleep(0.4)
                #         self.you_win = True

                # if event.type == pygame.MOUSEMOTION:
                #     if solve_button.isOver(pos):
                #         solve_button.color = (0, 204, 0)
                #     else:
                #         solve_button.color = (255, 255, 0)

                # if self.you_win:
                #     self.highlight.move_count("8 Puzzle Puzzle", 130, 10)
                #     self.highlight.move_count("You Win !!!", 130, 450)
                #     pygame.display.update()
                #     self.clock.tick(30)
                #     time.sleep(2)
                #     self.screen.fill(self.black)
                #     self.puzzle_numbers = self.generate_puzzle.generate_puzzle()
                #     self.highlight.m_count = 0
                #     self.you_win = self.highlight.highlight_digit_to_be_swapped(0, -100, "UP",
                #                                                                 self.puzzle_numbers)
                #     self.generate_puzzle.draw_puzzle(self.puzzle_numbers)

                #     self.you_win = False
                #     self.finish = False

            pygame.display.update()

        # pygame.quit()
        # quit()


if __name__ == "__main__":
    rompecabezas = Rompecabezas()
    rompecabezas.empezar()