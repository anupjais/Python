import time

attamps = 0
wait_time = 1
max_retries = 5

while attamps<max_retries:
    print("Attampt : ",attamps+1," - wait time : ",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attamps+=1

