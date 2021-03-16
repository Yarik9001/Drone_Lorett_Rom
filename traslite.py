
import matplotlib.pyplot as plt


def trans_trek(old_name: str, new_name: str, deb=False):
    '''
    old_neme - original satellite track file name
    new_name - final filename of the satellite track
    '''
    from math import sin, cos, radians , tan
    FOKUS = 1.4 
    try:
        with open(old_name) as file:  # open old
            file = file.read().split('\n')  # reading
            file_new = open(new_name, 'w')  # creating a new file
            for i in file[:3]:  # system information recording
                file_new.write(f'{i}\n')
            file_new.write('Time (UTC)  X (metr)  Y (metr)\n\n')
            for i in file[6:-1]:  # translation and recording of coordinates
                mass = i.split()
                for a in range(len(mass)):
                    mass[a] = '.'.join(mass[a].split(':'))
                azimuth = radians(float(mass[1]))
                elevation = radians(float(mass[2]))
                x = 1 - (FOKUS / tan(elevation)) * cos(azimuth) # translation
                y = 1 - (FOKUS / tan(elevation)) * sin(azimuth)
                time = mass[0]
                file_new.write(f'{time}\t{x}\t{y}\n')  # write new data
            file_new.close()
    except:
        print('Satellite track translation error')


trans_trek('test_trek_old.txt.txt', 'new.txt')


def track_show(name: str):
    ''' Function for visualizing the satellite track '''
    x, y = [], []
    with open(name) as file:
        file = file.read().split('\n')[6:-1]
        for i in file:
            print(i)
            i = i.split('\t')
            x.append(float(i[1]))
            y.append(float(i[2]))
        print(x)
        print(y)
        plt.title('Track show')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.plot(y, x)
        plt.show()


track_show('new.txt')
