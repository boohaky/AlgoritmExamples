def f(n):
    if n == 0:
        return 1
    else:
        return f(n-1)*n


if __name__ == '__main__':
    print(f(6))
