import re
  
(N,M) = map(int,input().strip().split())

matrix = []
  
for i in range(N):
    matrix.append(input())
  
phrase = ""
  
for j in range(M):
    for i in range(N):
        phrase += str(matrix[i][j])
  
print(re.sub(r'\b[^a-zA-Z0-9]+\b', ' ', phrase))
