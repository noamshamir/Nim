# Nim
*A terminal-based versoin of the classic number Nim with a bot that plays perfectly*

## Table of Contents
- [Running Nim](#running-nim)
- [Playing Nim](#playing-nim)
- [The Winning Algorithm](#the-winning-strategy)

## Running Nim
1. Clone the repository `git clone https://github.com/yourusername/uncle-game.git`
2. Make sure you have python3 installed
3. Install the Copy library `pip3 install copy`
4. Run the main file `python3 game.py`

## Playing Nim
- While Nim can be played starting with any amount of rows with any amount of matches per row, this version has 4 rows with odd matches in the starting position.
    - Row 1: |
    - Row 2: | | | 
    - Row 3: | | | | |
    - Row 4: | | | | | | |
- Each turn, the player may remove as many matches from a single row as they wish
- The game is lost by the player who takes the last match. Effectively, this means that one wins by leaving one match remaining after their turn.

## The Winning Strategy
_Spoiler alert: this section will reveal the winning strategy_
<span class="spoiler"></span>
 <details>
 <summary>Click to reveal the solution</summary>
 
 My computer player's algorithm is based off the winning strategy for Nim. It's simple enough that human's can implement it as well.
 
### Steps to implement the strategy
_These same steps are used by my program_
1. Sort all the rows into powers of two. Examples: 
    - Row 2 has 3 matches. The greatest power of two less than that is 2. After that, we are left with 1 match, which is a power of two. Therefore, the binary representation is [2, 1]
    - Row 4 has 6 matches. The greatest power of two less than that is 4. After that, we are left with 2 matches, which is a power of two. Therefore, the binary representation is [4, 2]
    - Row 4 has 7 matches. The greatest power of two less than that is 4. After that, we are left with 3 matches. The greatest power of two less than that is 2. After that, we are left with 1 match, which is a power of two. Therefore, the binary representation is [4, 2, 1]
2. Make the board only binary pairs. We do this by taking the binaries of all the rows, and finding a move so that, at the end of our turn, all that is left is pairs of binaries. Example:
    - The board's row's binary representations are so: {[1],[2],[4, 1],[4, 2, 1]}
    - We can group all the numbers into pairs by sorting: [1, 1, 1, 2, 2, 4, 4]
    - After removing all the pairs ([1, 1], [2, 2], and [4, 4]) we are left with an extra 1. This means we must take away a 1. One of the rows that has a 1 is the first row. Therefore, our move would be taking away 1 match from row 1 (though we could take a single match from any row with a 1 in its binary representation)
3. For the program: iterate over every possible next move, and check which produce a result satisfactory for step #2. 
4. In the endgame, this strategy will fail. Therefore, for situations in which the game will be over in 2 or less moves, one must use common sense.
</details>
