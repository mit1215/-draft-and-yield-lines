import matplotlib.pyplot as plt
import numpy as np

# 設定1~14月的數據
months = range(1, 15)
draft = [0.3, 0.8, 1.3, 1.6, 2, 2.3, 2.5, 2.7, 2.9, 3, 3.2, 3.4, 3.6, 3.8]
yield_data = [0.18, 1.2, 2.52, 3.03, 3.9, 4.57, 4.76, 4.84, 4.91, 4.95, 5.05, 5.31, 5.51, 6.61]

# 計算[0.3,3]線的斜率和截距
slope_draft = (draft[-1] - draft[0]) / (months[-1] - months[0])
intercept_draft = draft[0] - slope_draft * months[0]


# 繪製Σyield_data線、[0.3,3]的切線
plt.plot(months, yield_data, 'o-', label='Σyield')
plt.plot([months[0], months[-1]], [draft[0], draft[-1]], 'r--', label='Σdraft')

# 設定標題和坐標軸標籤
plt.title('Σdraft and Σyield lines')
plt.xlabel('Months')
plt.ylabel('ΣQ')

# 顯示圖例和圖形
plt.legend()
plt.show()
