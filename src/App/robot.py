import time,random
Robot_Name = input("Enter the Bot Name : ")
target = int(input("Enter the distance to the Target (in meters) : "))

distance_travelled = []
direction_taken = []
distance = 0

while target > distance:
    obstacle = input("is there any obstacle is there? (y/n) : ").lower()

    if obstacle == 'y':
        which_obstacle = input("is obstacle is human(h) or else(e) ? (h/e)").lower()

        if which_obstacle == "h":
            print("Human Detected...")
            print("Bot stopped...")
            print("Waiting...")
            time.sleep(2)
            print("Time over...Bot moving Forward...")
            direction = random.choice(['Forward','Left','Right'])
            steps = 2
            distance += steps
            direction_taken.append(direction)
            distance_travelled.append(steps)
        else:
            direction = random.choice(['Forward','Left','Right'])
            print(f'other Obstacke found Taking Direction : {direction}')
            steps = 4
            distance += steps
            distance_travelled.append(steps)
            direction_taken.append(direction)

    else:
        steps = 6
        distance += steps
        direction = random.choice(['Forward','Left','Right'])
        print(f'No Obstacle found... Taking Direction : {direction}')
        distance_travelled.append(steps)
        direction_taken.append(direction)

print(f'Bot Name : {Robot_Name}')
print(f'Target : {target}')
print(f'Distance Travelled : {distance}')
print(f'distance_travelled : {distance_travelled}')
print(f'direction_taken : {direction_taken}')