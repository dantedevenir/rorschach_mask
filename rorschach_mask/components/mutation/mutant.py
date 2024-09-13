from os import getenv
from ..transformation.metamorphosis import Metamorphosis
from nite_howl import NiteHowl
import time
#export ROOT_PATH=/samba-data;export ENV_PATH=/samba-data/.env;export BROKER=localhost:9092;export TOPIC=molina;export GROUP=tmp
from .minute import minute

class Mutant:
    
    def __init__(self):
        broker = getenv('BROKER')
        topic = getenv('TOPIC')
        group = getenv('GROUP')
        self.howler = NiteHowl(broker, group, topic)

    def catch(self):
        radar_generator = self.howler.radar()
        while True:
            try:
                minute.register(f"Searching topics...")
                table, topic = next(radar_generator)
                df_transform = Metamorphosis.from_pandas(table.to_pandas(), topic)
                self.howler.send(f'{topic}_transform', df=df_transform.breed)
            except StopIteration:
                # Si radar_generator se agota, crea una nueva instancia
                radar_generator = self.howler.radar()
            # Pausa breve para no saturar el bucle
            time.sleep(0.1)