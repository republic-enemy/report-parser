import glob, pdb

for dirc in glob.glob('*.htm*'):
    file = open(dirc)
    line = file.readline()
    nam = 0
    cpu = 0
    ram = 0
    cpuv = 0
    ramv = 0
    for line in file:
        line = line.strip('\n')
        if 'Имя компьютера' in line and nam == 0:
            nam = line.rsplit(">", 1)[1]
            print(nam)
        if ('Тип ЦП' in line and '<A' not in line) and cpu == 0:
            cpu = line.rsplit(">", 1)[1]
            print(cpu)
        if 'Системная память' in line and ram == 0:
            ram = line.rsplit(">", 1)[1]
            print(ram)
        if ('Core Intel Core i' in line or 'Core Intel Xeon' in line) and cpuv == 0:
            cpuv = 1
            # print(cpuv)
        if 'Размер&' in line and ('Г' or 'М' in line):
            ramv = ramv+int(line[:-3].rsplit(">", 1)[1])
            # print(ramv)
    if cpuv > 0 and ramv > 3:
        print('not object of upgrade')
    else:
        dmp = open('123.txt', 'a')
        dmp.write(nam+' ')
        dmp.write(cpu+' ')
        dmp.write(ram+'\n')
        dmp.close()
