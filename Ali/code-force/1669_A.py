for _ in range(int(input())):
  x = int(input())
  if x >= 1900:
    print("Division 1")
  elif 1600 <= x < 1900:
    print("Division 2")
  elif 1400 <= x < 1600:
    print("Division 3")
  elif x < 1400:
    print("Division 4")