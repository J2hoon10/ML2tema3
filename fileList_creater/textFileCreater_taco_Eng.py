import random

script = []

f = open(r"Eng_대사 정보.txt", 'rt', encoding='UTF8')
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    script.append(line)
f.close()

f = open('all.txt', 'w')

filepath = (r"Eng_temp")
for i in range(1, 201+1):
    f.write(filepath)
    f.write("/")
    if i < 10:
        f.write("")
        f.write(str(i))
        f.write(".wav")
    elif i >= 10 and i < 100:
        f.write("")
        f.write(str(i))
        f.write(".wav")
    elif i >= 100:
        f.write("")
        f.write(str(i))
        f.write(".wav")
    f.write("|")
    f.write(script[i-1])
    f.write("\n")

f.close()

with open(r"all.txt", 'rt', encoding='cp949') as f:
    lines = f.readlines()

random.shuffle(lines)

with open(r"train.txt", 'w', encoding='UTF-8') as f:
    for data in lines[:160]:
        f.write(data)

with open(r"dev.txt", 'w', encoding='UTF-8') as f:
    for data in lines[160:]:
        f.write(data)
        