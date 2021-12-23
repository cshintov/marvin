import time
import threading
from tqdm import tqdm

def wait(duration):
    """ Duration in seconds """
    for _ in tqdm(range(duration), desc="waiting...", ascii=True):
        time.sleep(1)

t1 = threading.Thread(target=wait, args=(10,))
t1.start()
t1.join()
