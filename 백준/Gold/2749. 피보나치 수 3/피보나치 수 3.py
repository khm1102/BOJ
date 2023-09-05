def main():
    fibo = [0] * 1500000
    
    n = int(input())
    
    fibo[0] = 0
    fibo[1] = 1
    
    for i in range(2, 1500000):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 1000000
    
    print(fibo[n % 1500000])

if __name__ == "__main__":
    main()
