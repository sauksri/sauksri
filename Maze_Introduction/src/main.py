import sys
from Maze import Maze

if __name__ == "__main__":
    
    m = Maze(input("Enter maze file: "))
    print("Maze:")
    m.print()
    print("Solving...")
    m.solve()
    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print()
    m.output_image("maze.png", show_explored=True)
