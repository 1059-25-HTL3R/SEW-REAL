import matplotlib.pyplot as plt

plt.scatter([1,3,3,4],[1,2,3,4],s=400)


class Hallo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        fig, ax = plt.subplots()
        plt.plot(self.x, self.y)

        ax.spines['left'].set_position('center')
        plt.show()

gustav:Hallo = Hallo([1,-3,2,4,5],[1,2,3,4,2])
gustav.show()
