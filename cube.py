class Cube:
    COLORS = ['yellow', 'white', 'green', 'blue', 'red', 'magenta']

    def __init__(self, size=3):
        self.size = size
        self.state = self._init_state()

    def _init_state(self):
        state = []
        for i in range(6):
            state.append(self._build_face(self.COLORS[i]))
        return state

    def _build_face(self, color):
        return [[color] * self.size] * self.size




