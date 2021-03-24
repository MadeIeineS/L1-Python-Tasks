pin = int("0456")
start = int("0000")

while start <= 9999:
    if start == pin:
     print(f"{start:04d}")
     break
    else:
     start += 1


