import numpy as np

# 8x8 배열 생성
array = np.array(
    [[4.5, 6.5, 6.5, 6.5, 5.5, 4.5, 3.5, 2.5],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.5,0.5, 7.5,14.5,22.5,23.5,24.5,16.5],
    [0.5,0.5, 7.5,14.5,22.5,23.5,24.5,16.5],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [-3.5,-5.5,-12.5,-19.5,-26.5,-26.5,-26.5,-17.5]]
)  # 랜덤 값으로 8x8 배열 생성

# 평균 풀링 함수 정의
def average_pooling(arr, kernel_size=3, stride=1):
    output_dim = ((arr.shape[0] - kernel_size) // stride + 1, 
                  (arr.shape[1] - kernel_size) // stride + 1)
    pooled_array = np.zeros(output_dim)

    for i in range(0, arr.shape[0] - kernel_size + 1, stride):
        for j in range(0, arr.shape[1] - kernel_size + 1, stride):
            window = arr[i:i+kernel_size, j:j+kernel_size]
            pooled_array[i // stride, j // stride] = round(np.mean(window),2    )

    return pooled_array

# 평균 풀링 적용
pooled_array = average_pooling(array)
print("Original Array:\n", array)
print("\nPooled Array:\n", pooled_array)