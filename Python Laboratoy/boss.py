import queue
import time

from manager import QueueClient
from task import Task


class Boss(QueueClient):
    def __init__(self):
        super().__init__()

    def submit_task(self, task_id, task_size):
        task = Task(
            task_id, task_size
        )  # Create a new task with ID and size in parameters
        # Ajoute la tâche à la file de tâches du client
        self.tasks.put(task)
        print(f"Le Boss a ajouté la tache {task_id} à la file.")

    def run(self):
        while True:
            try:
                # Récupère un résultat de la file de résultats
                result_id, result_time = self.results.get_nowait()
                print(
                    f"Le Boss a récupéré le résultat {result_id} en {result_time} secondes."
                )
            except queue.Empty:
                print("La file est vide.")
                time.sleep(5)  # 5 seconds pause before checking again
                continue


if __name__ == "__main__":
    boss = Boss()
    for i in range(15):
        boss.submit_task(i, 5000)  # Submit a task with ID i and size of 5000
    boss.run()
