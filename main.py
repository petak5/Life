import tkinter as tk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.SIZE = 50		# Size of the grid
        self.X = self.SIZE
        self.Y = self.SIZE
        self.WIDTH = 15		# Width and
        self.HEIGHT = 15	# height of the cell

        self.c = tk.Canvas(
                self, 
                bg = "red",
                height = self.HEIGHT*self.SIZE,
                width = self.WIDTH*self.SIZE
        )
        self.c.pack()

        self.grid = [[0 for i in range(self.SIZE)] for j in range(self.SIZE)]
        self.neighbours = [[0 for i in range(self.SIZE)] for j in range(self.SIZE)]

        self.grid[4][4] = 1
        self.grid[5][4] = 1
        self.grid[6][4] = 1
        self.grid[5][5] = 1
        self.grid[6][5] = 1
        self.grid[7][5] = 1
        self.grid[4][8] = 1
        self.grid[5][8] = 1
        self.grid[6][8] = 1

        self.grid[20][20] = 1
        self.grid[20][21] = 1
        self.grid[19][21] = 1
        self.grid[19][22] = 1
        self.grid[18][20] = 1

        # the main loop
        self.update_board()

    def update_board(self):
        self.c.delete(tk.ALL)
        self.run()

        # call this function again in one second
        self.after(100, self.update_board)

    def impact_neighbours(self, x, y):      # adds 1 to every neighbour if alive
        if x > 0:
            self.neighbours[x-1][y] += 1
        if x < self.X-1:
            self.neighbours[x+1][y] += 1
        if y > 0:
            self.neighbours[x][y-1] += 1
        if y < self.Y-1:
            self.neighbours[x][y+1] += 1

        # Diagonal
        if x > 0 and y > 0:
            self.neighbours[x-1][y-1] += 1
        if x > 0 and y < self.Y-1:
            self.neighbours[x-1][y+1] += 1
        if x < self.X-1 and y > 0:
            self.neighbours[x+1][y-1] += 1
        if x < self.X-1 and y < self.Y-1:
            self.neighbours[x+1][y+1] += 1
        return
    def main(self):
        for x in range(self.X):
            for y in range(self.Y):
                if self.grid[x][y] == 1:
                    self.impact_neighbours(x, y)

        for x in range(self.X):
            for y in range(self.Y):
                if self.neighbours[x][y] < 2:
                    self.grid[x][y] = 0
                if self.neighbours[x][y] > 3:
                    self.grid[x][y] = 0
                if self.neighbours[x][y] == 3:
                    self.grid[x][y] = 1

    def draw(self):
        for x in range(self.X):
            for y in range(self.Y):
                color = "white"
                if self.grid[x][y] == 1:
                    color = "black"
                self.c.create_rectangle(y*self.HEIGHT, x*self.WIDTH, y*self.HEIGHT+self.HEIGHT, x*self.WIDTH+self.WIDTH, fill=color)

    def run(self):
        self.draw()
        self.c.pack()

        self.neighbours = [[0 for i in range(self.SIZE)] for j in range(self.SIZE)]
        self.main()

if __name__== "__main__":
    app = App()
    app.mainloop()
