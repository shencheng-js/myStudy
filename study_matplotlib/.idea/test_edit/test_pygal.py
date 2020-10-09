from sai import Sai
import pygal
sai6 = Sai()

results = []
frecuency = []

for i in range(50000):
    results.append(sai6.pao())

for value in range(1,sai6.face+1):
    frecuency.append(results.count(value))

hist = pygal.Bar()
hist._title = "骰子投掷情况"
hist.x_labels =[1,2,3,4,5,6]

hist.add("D6",frecuency)
hist.render_to_file("second.svg")