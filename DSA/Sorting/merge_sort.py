"""
合併排序法(Merge Sort)原理是會先將原始資料分割成兩個資料列，
接著再將兩個資料繼續分割成兩個資料列，依此類推，直到無法再分割，
也就是每組都只剩下一筆資料時，再兩兩合併各組資料，
合併時也會進行該組排序，每次排序都是比較最左邊的資料，
將較小的資料加到新的資料列中，
依此類推，直到最後合併成一個排序好的資料列為止。
"""

data = [30, 10, 40, 70, 50, 90, 60, 20]
def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)/2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1