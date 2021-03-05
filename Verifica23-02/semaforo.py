import time
class semaforo(object):
    def __init__(self) -> None:
        super().__init__()

    VERDE = '\033[92m'
    GIALLO = '\033[93m'
    ROSSO = '\033[91m'
    ENDC = '\033[0m'
    
    #tempo sempre in secondi
    def rosso(self, tempo):
        print(f"{self.ROSSO}Semaforo ROSSO per {tempo} secondi.{self.ENDC}")
        time.sleep(tempo)

    def giallo(self, tempo):
        print(f"{self.GIALLO}Semaforo GIALLO per {tempo} secondi.{self.ENDC}")
        time.sleep(tempo)

    def verde(self, tempo):
        print(f"{self.VERDE}Semaforo VERDE per {tempo} secondi.{self.ENDC}")
        time.sleep(tempo)

    def luci_spente(self,tempo):
        print(f"Semaforo con tutte le luci spente.")
        time.sleep(tempo)
    

