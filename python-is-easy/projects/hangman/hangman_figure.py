class HangmanFigure:
    def __init__(self):
        self.figure = ['' for _ in range(6)]
        self.figure_count = 0

    def render(self):
        print(''.join(self.figure))
    
    def render_next(self):
        self.figure_count += 1
        count = self.figure_count
        if count == 1:
            self.figure[0] = " O \n" 
        elif count == 2:
            self.figure[1] = " | \n"
        elif count == 3:
            self.figure[1] = "/| \n"
        elif count == 4:
            self.figure[1] = "/|\ \n"
        elif count == 5:
            self.figure[2] = "/  \n"
        elif count == 6:
            self.figure[2] = "/ \ \n"
        self.render()