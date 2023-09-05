while True:
    a, b, c, x, y, z = map(int, input().split())
    if a == 0:
        break
    
    if x == 0 or y == 0 or z == 0:
        print(x*x + y*y + z*z)
    else:
        t = float('inf')
        
        if a == x:
            t = min(t, (x + y)**2 + z**2, (x + z)**2 + y**2)
            t = min(t, (c + y)**2 + (a + c - z)**2, (b + z)**2 + (a + b - y)**2)
        if b == y:
            t = min(t, (x + y)**2 + z**2, (y + z)**2 + x**2)
            t = min(t, (a + z)**2 + (b + a - x)**2, (c + x)**2 + (b + c - z)**2)
        if c == z:
            t = min(t, (z + y)**2 + x**2, (x + z)**2 + y**2)
            t = min(t, (a + y)**2 + (c + a - x)**2, (b + x)**2 + (c + b - y)**2)
        
        print(t)
