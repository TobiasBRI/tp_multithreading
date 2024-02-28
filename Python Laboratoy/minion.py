import queue
import time

from manager import QueueClient


# Définit une classe Minion qui hérite de QueueClient.
class Minion(QueueClient):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            try:
                # Pause d'une seconde pour éviter une boucle infinie trop rapide
                time.sleep(1)
                # Récupère une tâche de la file sans attendre
                task = self.tasks.get_nowait()
            except queue.Empty:
                print("La file de tâches est vide.")
                time.sleep(5)  # Pause de 5 secondes avant de vérifier à nouveau
                continue

            # Exécute le travail associé à la tâche
            task.work()
            # Ajoute le résultat à la file de résultats
            self.results.put((task.identifier, task.time))

            # Affiche un message indiquant le traitement de la tâche
            print(
                f"Minion a traité la tâche {task.identifier} en {task.time} secondes."
            )


if __name__ == "__main__":
    m = Minion()
    m.run()
