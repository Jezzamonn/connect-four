# Connect Four Assignment!
This is the base python code for a Connect Four game. It's a mini-assignment, where you need to implement both your own board and your own AI to beat the existing AI players.

I've already implemented the code that creates the board and draws it to the screen. I also added a ranking system so you can see how your AI compares to the existing (bad) AIs I created.

# Downloading the code

The simplest way to download the code is to click the green `<> Code` button, and then choose the `Download ZIP` option.

# Install the dependencies

This depends on a small number of third-party libraries, which are listed in [requirements.txt](requirements.txt). These are formatted so they work with Python's `pip` tool, so you can install them by doing the following:

1. Unzip the Downloaded code.
2. Open a terminal, and change directory into the unzip'd folder.
  - On Mac, you can do this by typing `cd ` ('c' 'd' space) and then dragging the folder from the finder into the terminal window. After dragging the file, the command should look like `jez@Jezs-MacBook ~ % cd /Users/jez/Downloads/connect-four-main`.
3. Run `python3 -m pip install -r requirements.txt`.

# Running the game

Run the file game.py to run the game. A window will appear, and two random AI players will be chosen to face off against each other. After one player wins, the rankings of the players will be updated. Hold space to speed everything up to run lots of games and get a good rating of the different AI players against each other.

Of course, the board hasn't been properly implemented yet so the game won't really work properly yet!

# Assignment Part 1

For the first part of the assignment, you need to create the logic for the board. There is an interface class in [board.py](board.py), and your implementation should go in [impl/izboard.py](impl/izboard.py). (There's a dummy version in [jezimpl/jezboard.py](jezimpl/jezboard.py), however it returns random values instead of having the actual logic for the game).

Each method has comments explaining what it should do in [board.py](board.py).

When you've successfully implemented the board, modify the code in [game.py](game.py) to initialize the board to `IzBoard()` instead of `JezBoard()`. There's a TODO comment to help you know where to update the code. You'll also need to update the imports at the top of the file to import `IzBoard` too.

Now when you run the game, you should see the players place moves on the board, and see the rankings of the existing AI players compared to each other. Some AI players should be pretty clearly better than others.

# Assignment Part 2

For the second part of the assignment, now you have to create an AI player! Your challenge is to create a player that is better than the existing AI players, but otherwise it's open as to how you want to implement it. Treat this as an open-ended puzzle.

Each existing AI player is pretty bad and has some clear weaknesses, so without needing any complicated logic you should be able to exploit those and beat them all. Your AI player can read the state of the board, and you're welcome to add extra variables inside the AI player class to do things like count how many moves have been made or something similar if you thing that would be helpful.

Once you've create an AI class, modify [game.py](game.py) and add your class to the list of player_classes. You'll need to update the imports too, and note that you shouldn't create a new instance of the class (so, don't write `IzAIPlayer()` ❌) but just list the class name itself (`IzAIPlayer()` ✅).

## Assignment Part 2 Side Project?

You could also create an "AI" player that just asks for what move to make in the console. Now people can play the game! This could be handy when you start to start figuring out strategies for your AI.

## Assignment Part 2 Extra Work

If you want to get advanced and make a challenging AI that a human would find interesting, you can try reading about the [Minimax strategy](https://en.wikipedia.org/wiki/Minimax), and implement something like that. Note that this is definitely more complicated than the rest of the assignment.
