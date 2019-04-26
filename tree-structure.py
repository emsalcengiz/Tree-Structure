liste = []

f = open('triangle1.txt', 'r')
for line in f.readlines():  # txt dosyasındaki elemanları satır satır okuyoruz.
    line = line.split(' ')  # line dizisini boşluğa göre parçalıyoruz.
    #print(line) #/yorum satırını kaldır. bu ifadede \n var.
    line[len(line) - 1] = line[len(line) - 1].splitlines()[0]  #\n leri silmek için.
    #splitlines \n leri siliyor ama dönüş değeri olarak bir sizi döndürüyor. Dizi döndürdüğü için bize dizinin sıfırıncı elemanı lazım
    line = list(map(int, line))  # string diziyi int dizisine çeviriyoruz.
    liste.append(line)  #listeye ekleniyor/birleştirme
f.close()


#for i in range(len(liste)):
#    print(liste[i])
# elemanları listeye doğru atıyor

index = 0
maxTop = 0

for i in range(len(liste)):
    if i == 0:
        maxTop += liste[i][index]
    else:
        if liste[i][index] > liste[i][index + 1]:
            maxTop += liste[i][index]
        else:
            maxTop += liste[i][index + 1]
            index = index + 1


print(maxTop)
