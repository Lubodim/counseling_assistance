
speed = int(input())

if 0< speed <= 15:
    print("slow")
elif 15 < speed <= 55:  #speed > 15 and speed <= 55:
    print("average")
elif 55 < speed <= 100:
    print("fast")
elif 100< speed <= 150:
    print("ultra fast")
elif speed > 150:
    print("extremely fast")
else:
    print("invalid speed")