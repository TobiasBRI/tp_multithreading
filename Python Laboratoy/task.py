import time

import numpy as np


class Task:
    def __init__(self, identifier, size=None):
        self.identifier = identifier
        self.size = np.random.randint(300, 3_000)
        self.a = np.random.rand(
            self.size, self.size
        )  # Random matrix of size (size x size)
        self.b = np.random.rand(self.size)  # Random vector of size (size)
        self.x = np.zeros((self.size))  # Result vector initialized to zeros
        self.time = 0  # Calcul time initialized to zéro

    def work(self):
        start = time.perf_counter()  # Record task's starting time
        self.x = np.linalg.solve(self.a, self.b)  # Solve linear system : Ax = B
        self.time = time.perf_counter() - start  # Calculate spent time to solve
