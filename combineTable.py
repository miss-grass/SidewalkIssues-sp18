import numpy as np
import pandas as pd

total_size = 1509
to_csv = True


def main():
    filename1 = '/Users/Miss-grass/Documents/CSE495/Sp18/output/output_0-1000.npy'
    filename2 = '/Users/Miss-grass/Documents/CSE495/Sp18/output/output_1000-1509.npy'
    # filename3 = 'final_output/output_2500-2700.npy'
    data1 = np.load(filename1)
    data2 = np.load(filename2)
    # data3 = np.load(filename3)
    data = np.zeros(((data1.shape[0]+data2.shape[0]), 10), dtype=object)
    i = 0
    for item in data1:
        data[i] = item
        i += 1
    for item in data2:
        data[i] = item
        i += 1
    # for item in data3:
    #    data[i] = item
    #    i += 1
    df = pd.DataFrame(data)
    # print(df)
    #start = int(filename1[24:int(filename1.index('-'))])
    #end = int(filename2[(int(filename2.index('-'))+1):int(filename2.index('.'))])
    # print(start)
    # print(end)
    if to_csv:
        savename = '/Users/Miss-grass/Documents/CSE495/Sp18/output/output_0-1500.csv'
        df.to_csv(savename, header=['starting coordinate', 'ending coordinate', 'vertices', 'issues ID',
                                    'severe issue', 'minor issue', 'total distance', 'ave_severe_issue/meter',
                                    'ave_minor_issue/meter', 'elevation'])

    else:
        savename = '/Users/Miss-grass/Documents/CSE495/Sp18/output/output_0-1000.npy'
        np.save(savename, data)



if __name__ == '__main__':
    main()
