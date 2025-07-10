for _ in range(int(input())):
  arr = list(map(int, input().split()))
  a = arr[0]
  cnt = 0
  for i in range(1, 4):
    if arr[i] > a:
      cnt += 1
  print(cnt)
  
  
  


  