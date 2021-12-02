from submarine import Submarine

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    sub = Submarine()
    for line in lines:
        sub.parse(line)

    print(sub.score)
