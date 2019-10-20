
def main():
    value = []
    with open('filesystem_new.txt') as f:
        line = f.readline()
        cnt = 1
        while line:
            value.append(int(line.split()[0]))
            line = f.readline()
            cnt += 1
        value.sort(reverse = True)
        print(value)
    f.close()

    

if __name__ == '__main__':
    main()
