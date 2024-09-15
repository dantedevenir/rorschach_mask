from os import getenv
from ..transformation.metamorphosis import Metamorphosis
from nite_howl import NiteHowl, minute
import time
#export ROOT_PATH=/samba-data;export ENV_PATH=/samba-data/.env;export BROKER=localhost:9092;export TOPIC=molina;export GROUP=tmp

class Receiver:
    
    def __init__(self):
        broker = getenv('BROKER')
        topic = getenv('TOPIC')
        group = getenv('GROUP')
        self.howler = NiteHowl(broker, group, topic, "mask")

    def catch(self):
        radar_generator = self.howler.radar()
        while True:
            try:
                minute.register("info", f"Searching topics...")
                table, topic, key = next(radar_generator)
                df_transform = Metamorphosis.from_pandas(table.to_pandas(), topic)
                self.howler.send(topic, df=df_transform.breed, key="delve")
            except StopIteration:
                radar_generator = self.howler.radar()
            time.sleep(0.1)