# Nama: Muhammad Al-Faraby Moidady,Nim: F55123018

# Pseudocode Mrge sort
# Procedure BubbleSort(arr)
#     n = length(arr)
#     for i = 0 to n-1 do
#         for j = 0 to n-i-2 do
#             if arr[j] > arr[j+1] then
#                 Swap(arr[j], arr[j+1])
#             end if
#         end for
#     end for
# End Procedure
# 

# Pseudocode Buble sort
# Procedure MergeSort(arr)
#     if length(arr) > 1 then
#         mid = length(arr) / 2
#         left = arr[0:mid]
#         right = arr[mid:length(arr)]

#         MergeSort(left)
#         MergeSort(right)

#         i = 0, j = 0, k = 0
#         while i < length(left) and j < length(right) do
#             if left[i] < right[j] then
#                 arr[k] = left[i]
#                 i = i + 1
#             else
#                 arr[k] = right[j]
#                 j = j + 1
#             end if
#             k = k + 1
#         end while

#         while i < length(left) do
#             arr[k] = left[i]
#             i = i + 1
#             k = k + 1
#         end while

#         while j < length(right) do
#             arr[k] = right[j]
#             j = j + 1
#             k = k + 1
#         end while
#     end if
# End Procedure
# 

# code program
import random
import time

# Merge Sort (Algoritma Pengurutan Rekursif)
def merge_sort(arr):
    if len(arr) <= 1:  # Jika array hanya memiliki 1 atau 0 elemen, langsung kembalikan
        return arr
    mid = len(arr) // 2  # Temukan titik tengah
    left = merge_sort(arr[:mid])  # Pisahkan dan urutkan setengah kiri
    right = merge_sort(arr[mid:])  # Pisahkan dan urutkan setengah kanan
    return merge(left, right)  # Gabungkan hasilnya

def merge(left, right):
    result = []
    i = j = 0
    # Gabungkan dua array yang sudah terurut
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # Tambahkan elemen sisa dari kiri
    result.extend(right[j:])  # Tambahkan elemen sisa dari kanan
    return result

# Bubble Sort (Algoritma Pengurutan Bertahap)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Menandakan apakah ada pertukaran
        # Lakukan iterasi untuk tiap pasangan elemen berturut-turut
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # Jika elemen kiri lebih besar, tukar
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Jika tidak ada pertukaran, array sudah terurut
            break
    return arr

# Main program
if __name__ == "__main__":
    # Generate random array of 100 integers untuk Bubble Sort
    arr_bubble = [random.randint(0, 1000) for _ in range(100)]  # Tepat 100 elemen untuk Bubble Sort
    arr_merge = [random.randint(0, 1000) for _ in range(100)]  # Tepat 100 elemen untuk Merge Sort

    # Time complexity untuk Bubble Sort
    start_time_bubble_sort = time.perf_counter()
    bubble_sort(arr_bubble)
    end_time_bubble_sort = time.perf_counter()
    time_complexity_bubble = end_time_bubble_sort - start_time_bubble_sort

    # Time complexity untuk Merge Sort
    start_time_merge_sort = time.perf_counter()
    merge_sort(arr_merge)
    end_time_merge_sort = time.perf_counter()
    time_complexity_merge = end_time_merge_sort - start_time_merge_sort

    # Menampilkan hasil pengurutan dan waktu eksekusi
    print(f"Hasil pengurutan Bubble Sort adalah sebagai berikut: {arr_bubble}\n")
    print(f"Hasil pengurutan Merge Sort adalah sebagai berikut: {arr_merge}\n")

    print(f"Time Complexity untuk Bubble Sort adalah {time_complexity_bubble:.10f} detik\n")
    print(f"Time Complexity untuk Merge Sort adalah {time_complexity_merge:.10f} detik\n")
