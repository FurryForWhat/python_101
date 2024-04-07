def hanoi(stack, start_point, end_point,supportive_point):
    if stack == 1:
        print(f"Disk 1 Moving {start_point} to {end_point}")
    else:
        hanoi(stack-1,start_point,supportive_point,end_point)
        print(f"Disk {stack} Moving {start_point} to {end_point}")
        hanoi(stack-1,supportive_point,end_point,start_point)
hanoi(3,'A','C','B')