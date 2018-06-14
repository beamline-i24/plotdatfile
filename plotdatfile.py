import os, sys
import numpy as np
import matplotlib.pyplot as plt

def dat_file_scrape(full_file_path, header_skip=7, xcol=0, ycol=2):
    print full_file_path
    x, y = [], []
    f = open(full_file_path, 'rU')
    for line in f.readlines()[header_skip:]:
        entry = line.split()
        x.append(float(entry[xcol]))
        y.append(float(entry[ycol]))
    x = np.array(x)
    y = np.array(y)
    return x, y

def get_files(path='.', suffix='dat'):
    dats_list = [x for x in os.listdir(path) if x.endswith(suffix)]
    dats_list = sorted(dats_list)
    dat_dict = {}
    for i, fid in enumerate(dats_list):
        dat_dict[i] = fid
        print i, fid

    dat_choice = raw_input('Choose your dat, dats separated by a space or "all": ').rstrip(' ')
    if 'all' in dat_choice:
        dat_fids_list = dats_list
    else:
        dat_fids_list = [dat_dict[int(x)] for x in dat_choice.split(' ')] 
    return dat_fids_list


def main(args):
    for arg in args:
        print arg

    #path = get_directory

    dat_fids_list = get_files()


    fig = plt.figure()
    fig.subplots_adjust(left   = 0.05,
                        bottom = 0.05,
                        right  = 0.95, 
                        top    = 0.95,
                        wspace = 0.00, 
                        hspace = 0.00)

    num_colors = len(dat_fids_list)
    cm = plt.get_cmap('gist_rainbow')
    ax = fig.add_subplot(111, axisbg='k')
    ax.set_color_cycle([cm((1.0 * i) / num_colors) for i in range(num_colors)])

    for fid in dat_fids_list:
        x, y = dat_file_scrape(fid)
        ax.plot(x, y, linewidth=2, label=fid)

    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())
    plt.title('Fancy Title')
    plt.xlabel('xlabel')
    plt.ylabel('ylabel')
    leg = plt.legend(loc='lower left', title='legend', fancybox=True)
    frame = leg.get_frame()
    frame.set_facecolor('beige')
    plt.show()

if __name__ == '__main__':
    main(sys.argv)

plt.close()
