import matplotlib.pyplot as plt
import numpy as np

# 가로축과 세로축에 사용할 라벨 설정
x_labels = ['i - 1', 'i', 'i + 1']
t_labels = ['j   ', 'j + 1']

# 라벨에 해당하는 값들 생성
x_values = np.arange(len(x_labels))
t_values = np.arange(len(t_labels))

# 격자 그리기
plt.grid(which='both', axis='both', linestyle='-', linewidth=3, markersize=5, zorder=1)

# 초록색 점 찍기
plt.scatter([x_values[0], x_values[1], x_values[2]], [t_values[0], t_values[0], t_values[0]], c='green', marker='o', s=200, label='(i, j)', zorder=3)

# 빨간색 점 찍기
plt.scatter([x_values[1]], [t_values[1]], c='red', marker='o', s=200, label='(i, j+1)', zorder=3)

# 가로축과 세로축 라벨 설정 및 글자 크기 늘리기
plt.xticks(x_values, x_labels, fontsize=20)
plt.yticks(t_values, t_labels, fontsize=20)

# 그리드를 정사각형으로 만들기
plt.axis('equal')
plt.title("Explicit Method Calculation Direction",fontsize = 22)
plt.ylabel("Time (s)",fontsize = 15)
plt.xlabel("Position (m)",fontsize = 15)
# 화살표 추가
arrow_params = dict(facecolor='black', edgecolor='black', head_width=0.05, head_length=0.1, length_includes_head = False, zorder=2)
plt.arrow(x_values[0], t_values[0], 0.89, 0.89, **arrow_params)
plt.arrow(x_values[1], t_values[0], 0, 0.85, **arrow_params)
plt.arrow(x_values[2], t_values[0], -0.89,0.89, **arrow_params)

# 그래프 표시
plt.show()