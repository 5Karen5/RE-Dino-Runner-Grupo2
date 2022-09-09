from dino_runner.components.game import Game

if __name__ == "__main__":

    game= Game()

    game.show_menu()

    while game.running:
        if not game.playing:
            game.show_menu(game.death_count)


   
   
   
    # game = Game()
    # game.run()
  