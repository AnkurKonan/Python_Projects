import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
y = [1,4,2,5,8,6,3]
colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan', 'magenta']

plt.figure(figsize=(8,5), dpi=100)
bars = plt.bar(x, y, color=colors)
patterns = ['/', 'O', '*', '|', '||', '-', 'x']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
  
plt.title('Bar Graph', fontdict={'fontname': 'Apple Braille Outline 8 Dot', 'fontsize': 15})
plt.savefig('BarGraph.png', dpi=300)
plt.show()
