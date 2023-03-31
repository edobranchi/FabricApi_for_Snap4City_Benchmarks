import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":
    path = "C:/Users/branchi/PycharmProjects/pythonProject/device_insertion_result/"
    rows=0;
    filenames = glob.glob(path + "\*.csv")
    print('File names:', filenames)

    plotdf = pd.DataFrame()
    df = pd.concat(map(pd.read_csv, filenames), ignore_index=True)
    dfplot=pd.DataFrame(columns=['n','time'])
    row_list = []
    for index, row in df.iterrows():
        time=row['elapsed_time']
        print(rows,time)
        row_list.append(dict(time=time))
        rows+=1


    df4 = pd.DataFrame(row_list, columns=['time'])
    df4.plot(y='time')
    plt.show(block=True)
    plt.interactive(False)

    print("Done!")
    #for index, row in df.iterrows():
        #print(rows, row['name'], row['type'], row['organization'])