g = {complex(i, j): c for j, r in enumerate(open('day16.txt'))    
                      for i, c in enumerate(r.strip())}
print(g)d