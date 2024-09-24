from os import getenv
from ..transformation.metamorphosis import Metamorphosis
from nite_howl import NiteHowl, minute
import time
import pandas as pd

class Receiver:
    
    def __init__(self):
        broker = getenv('BROKER')
        topic = getenv('TOPIC')
        group = getenv('GROUP')
        self.howler = NiteHowl(broker, group, str(topic).split(","), "mask")

    def catch(self):
        radar_generator = self.howler.radar()
        while True:
            try:
                table, topic, key, headers, type = next(radar_generator)
                if topic == "mask":
                    buttefly = Metamorphosis.from_pandas(table, key)
                    minute.register("info", "So beauty! I catch a butterfly, now i send the breed...")
                    self.howler.send("delve", msg=buttefly.breed, key=key, headers=headers)
                else:
                    minute.register("info", f"That larva '{key}' won't need me.")
            except StopIteration:
                radar_generator = self.howler.radar()
            time.sleep(0.1)