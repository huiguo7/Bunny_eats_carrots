# Bunny_eats_carrots

Input: An N x M matrix of a garden. Each cell contains a positive integer representing the number of carrots in that part of the garden.

Output: The number of carrots Bunny eats before falling asleep.

Conditions: Bunny starts in the center of the garden. If there are more than one center cell, Bunny starts in the cell with the largest number of carrots. There will never be a tie for the highest number of carrots in a center cell. Bunny eats all of the carrots in his cell, then looks left, right, up, and down for more carrots. Bunny always moves to the adjacent cell with the highest carrot count. If there are no adjacent cells with carrots, Bunny falls asleep.

To run the program:
python3 Bunny_eats_carrots.py -i garden.txt
