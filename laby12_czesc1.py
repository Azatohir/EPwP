# laby 12 czesc 1

# krok 0
import pandas as pd

# krok 1
df = pd.read_csv("./lab12_files/US_Baby_Names_right.csv")

# krok 2
print("Rekordow jest: ", df.shape[0])
baby_names = df["Name"]

# krok 3
print(df.head(10))

# krok 4
print(df.columns)
df = df.drop(columns=['Unnamed: 0', 'Id'])
print(df.columns)

# krok 5
print("Dziewczynek jest: ",len(df[df["Gender"] == 'F']))
print("Chlopcow jest: ",len(df[df["Gender"] == 'M']))
if len(df[df["Gender"] == 'F'])-len(df[df["Gender"] == 'M']) > 0:
    print("Wiecej jest dziewczynek")
else:
    print("Wiecej jest chlopcow")

# krok 6
df = df.sort_values(by=['Name'])
print(df.head())
names_count = df[["Name", "Count"]]
names_count = names_count.groupby("Name")["Count"].sum()
names_count = names_count.sort_values(ascending=False)
print(names_count.head(10))

# krok 7
import matplotlib.pyplot as plt
najczestrze_ogolne = names_count.head(10).reset_index()
ypoints = najczestrze_ogolne["Count"]
xpoints = najczestrze_ogolne["Name"]
plt.bar(xpoints, ypoints)
plt.title("10 ogolnych")
plt.show()

names_count = df[df["Gender"] == 'F']
names_count = names_count.groupby("Name")["Count"].sum()
names_count = names_count.sort_values(ascending=False)
najczestrze_ogolne = names_count.head(10).reset_index()
ypoints = najczestrze_ogolne["Count"]
xpoints = najczestrze_ogolne["Name"]
plt.bar(xpoints, ypoints)
plt.title("10 kobiecych")
plt.show()

names_count = df[df["Gender"] == 'M']
names_count = names_count.groupby("Name")["Count"].sum()
names_count = names_count.sort_values(ascending=False)
najczestrze_ogolne = names_count.head(10).reset_index()
ypoints = najczestrze_ogolne["Count"]
xpoints = najczestrze_ogolne["Name"]
plt.bar(xpoints, ypoints)
plt.title("10 meskich")
plt.show()

# krok 8
print("Roznych imion jest: ",names_count.shape[0])

# krok 9
names_count = df[["Name", "Count"]]
names_count = names_count.groupby("Name")["Count"].sum()
names_count = names_count.sort_values(ascending=False)
names_count = names_count.reset_index()
prawdopodobienstwo = names_count.shape[0]
def nasz_generator(l = 100):
    prawdopodobienstwo = names_count.shape[0]
    r = {}
    for i in range(l):
        z = random.randint(0, prawdopodobienstwo)
        zm = df["Name"][z]
        if zm in r:
            r[zm] += 1
        else:
            r[zm] = 1
    return r

# krok 10
from statistics import median,stdev
zbiorek = dict(nasz_generator(100000))
war = sorted(zbiorek.values())
zbiorek = sorted(zbiorek.items(), key=lambda x: x[1])
print("Najczestrze imie: ",zbiorek.pop())
print("Srednia: ", sum(war)/len(war))
print("Mediana: ", median(war))
print("Odchylenie stanadrdowe: ",stdev(war))
