def fibonaccI(n):
    if n <= 1 :
        return 1
    return fibonaccI(n-1) + fibonaccI(n-2)

if __name__ == "__main__":
    print(fibonaccI(23))