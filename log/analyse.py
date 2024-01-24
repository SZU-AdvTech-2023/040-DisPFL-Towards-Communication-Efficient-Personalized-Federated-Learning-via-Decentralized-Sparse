
def main():
    PREFIX = '################'
    PREFIX_2 = '@@@@@@@@@@@@@@@@'
    file = input('日志文件路径(log/...): ')
    with open(file) as f:
        line = f.readline()
        while line:

            if line.startswith(PREFIX):
                if line.startswith(PREFIX + 'Communication round'):
                    print('ROUND:', line.split()[-1])
                    line = f.readline()
                else:
                    print(line[len(PREFIX):], end='')
                    line = f.readline()
                    while not line.startswith(PREFIX) and not line.startswith(PREFIX_2):
                        print(line, end='')
                        line = f.readline()
            else:
                # skip
                line = f.readline()


if __name__ == '__main__':
    main()
