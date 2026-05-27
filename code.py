import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def make_rv(N=10000):
	plt.rcParams['font.family'] = 'Malgun Gothic'
	plt.rcParams['axes.unicode_minus'] = False

	# 1) 가우시안 랜덤변수 10,000개 생성
	mean_int = 5
	deviation_int = 3
	i = np.random.normal(mean_int, deviation_int, N)
	return i

def rv_N_X(i):
	# 2) 결과 시각화
	plt.figure(figsize=(10,6))
	plt.plot(i, '.', markersize=2)
	plt.grid(True)
	plt.xlabel('N')
	plt.ylabel('X')
	plt.title('10000개의 가우시안 랜덤변수')

def rv_histogram(i):
	# 3) 히스토그램 생성
	plt.figure(figsize=(10,6))
	plt.hist(i, bins=20, color='blue', edgecolor='black')

	plt.grid(True)
	plt.title('변수 i의 히스토그램')

def rv_normalization(i):
	# 4) 정규화
	plt.figure(figsize=(15,6))
	
	# 1. 실제 i에 대한 PDF
	plt.subplot(1, 2, 1)
	plt.hist(i, bins=500, density=True, color='blue', alpha=0.7)
	plt.title('실제 i에 대한 PDF')
	plt.grid(True, alpha=0.3)

	# 2. 정규분포로 가정한 i의 평균과 분산을 가지는 PDF
	mean_i, std_i = np.mean(i), np.std(i)
	plt.subplot(1, 2, 2)
	x = np.linspace(mean_i - 4*std_i, mean_i + 4*std_i, 200)
	plt.plot(x, norm.pdf(x, mean_i, std_i), 'r-', linewidth=2)
	plt.title('정규분포로 가정한 i의 평균과 분산을 가지는 PDF')
	plt.grid(True, alpha=0.3)

def problem_5_6(i, N=10000, float_min:float=None, float_max:float=None):
	# 구간 확률 구하기
	if (float_min==None) & (float_max==None):
		count = np.sum(i)
	elif not float_min:
		count = np.sum(i <= float_max)
	elif not float_max:
		count = np.sum(i >= float_min)
	else:
		count = np.sum((i>=float_min) & (i<=float_max))
	prob = (count/N)*100
	return prob

def problem_7(mean_val, std_val, float_max): # 7번 문제를 위해 단순하게 작성함
	Z = (float_max - mean_val) / std_val
	
	# norm에 Q함수가 따로 없어서 1-f로 대체함
	q_value = (1 - norm.cdf(abs(Z))) * 100

	return Z, q_value

# 1) 가우시안 랜덤변수 생성
i = make_rv()

# 2) rv_N_X(i)
# 3) rv_histogram(i)
# 4) rv_normalization(i)


# 5) 2부터 8까지 구간확률
print(f'5) Pa = {problem_5_6(i, float_min=2, float_max=8)}')
# 6) -4.2까지 구간확률
print(f'6) Pa = {problem_5_6(i, float_max=-4.2)}')

# 7) Q함수를 이용해 구한 -4.2까지 구간확률
Z, prob = problem_7(5, 3, -4.2)
print(f'Z = {Z:.6f} \nQ함수를 이용해 구한 이론적 확률 = {prob:.6f}')

"""
#+)
N = 500000
i = make_rv(N=N)
# -4.2까지 구간확률
print(f'실제값) Pa = {problem_5_6(i, N=N, float_max=-4.2)}')
prob = problem_7(5, 3, -4.2)[1]
print(f'이론값) Pa = {prob:.6f}')
"""