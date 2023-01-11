from tasks import add
import time

result = add.delay(10, 20)

ready = result.ready()
counter = 0

t = time.time()
result.wait()

print("it took {:4f} s to get the result {} from task".format(time.time() - t, result.get()))    