import queue
import random
import time

#def queue = Queue()

def generate_request(rque,rid):
    rqst = f"Request #{rid}"
    rque.put(rqst)

def process_request(rque):
    if not rque.empty():
        rqst = rque.get()
        print(f"{rqst} Completed")
        time.sleep(0.5)
    else:
        print("No requests in Queue")

if __name__ == "__main__": 
    rqst_que = queue.Queue()
    rid = 1

    try:
        while True:
            time.sleep(1)
            

            if random.choice([True,False]):
                rid += 1
                generate_request(rqst_que,rid)

            if random.choice([True,False]):
                process_request(rqst_que)
    
    except KeyboardInterrupt:
        print("Abort by User")
