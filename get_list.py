# -*- coding: utf-8 -*-
import pandas as pd


def get_links(archivo):
    TextFileReader = pd.read_csv(archivo, sep=';', chunksize=50000)
    dfList = []
    for df in TextFileReader:
        dfList.append(df)

    df = pd.concat(dfList, sort=False)
    links = df['Registro'].values
    return links


def run():

    links = get_links()
    print(links)


if __name__ == '__main__':
    run()
