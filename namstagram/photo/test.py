p = 0
n = 0

for i in range(n):

    if n % 3 == 0:

        q = i + 4 if n < 40 else None

    else:

        q = i + 40

    p += float(q) / 1000

if __name__ == "__main__":