from myData import DataSeq

def SelectionSort(ds):
    assert isinstance(ds, DataSeq), "Type Error"

    Length = ds.length
    for i in range(Length):
        for j in range(i, Length):
            if ds.data[j] < ds.data[i]:
                ds.Swap(i,j)


if __name__ == "__main__":
    ds=DataSeq(128,time_interval=1, sort_title="selectSort")
    ds.Visualize()
    ds.StartTimer()
    SelectionSort(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()