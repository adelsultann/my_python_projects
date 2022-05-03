from game import Game


if __name__ == "__main__":

    game = Game()
    while game.running:
        game.curr_menu.display_menu()
        while game.playing:
            game.handle_events()
            game.update()
            game.draw()



    #
    # while True:
    #     game.curr_menu.display_menu()
    #     while game.running:
    #         game.handle_events()
    #         game.update()
    #         game.draw()