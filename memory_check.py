import psutil

CPU = psutil.cpu_count()
print(CPU)

while True:
    cpu_percent = psutil.cpu_percent(10)
    print(cpu_percent)