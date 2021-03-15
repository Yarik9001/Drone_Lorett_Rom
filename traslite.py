from math import sin, cos, radians


def trans_trek(old_name: str, new_name: str, deb=False):
    '''
    old_neme - original satellite track file name
    new_name - final filename of the satellite track
    '''
    try:
        with open(old_name) as file:
            file = file.read().split('\n')
            file_new = open(new_name, 'w')
            for i in file[:6]:
                file_new.write(f'{i}\n')
            for i in file[6:-1]:
                mass = i.split()
                for a in range(len(mass)):
                    mass[a] = '.'.join(mass[a].split(':'))
                x = round(1 + sin(radians(float(mass[1]))), 4)
                y = round(1 + cos(radians(float(mass[2]))), 4)
                time = mass[0]
                file_new.write(f'{time}   {x}   {y}\n')
            file_new.close()
    except:
        print('Satellite track translation error')


trans_trek('test_trek_old.txt.txt', 'new.txt')
