###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data information, and information into insight."
text = text.replace(",","").replace(".","").upper().split()


###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]
len(lst)
lst[0], lst[10]
lst[0:4]
lst.pop(8)
lst.append("B")
lst.insert(8, "N")
print(lst)


###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

dict.keys()
dict.values()
dict["Daisy"][1] = 13
dict.update({'Ahmet': ["Turkey", 24]})
dict.pop("Antonio")


###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2, 13, 18, 93, 22]
even_list = []
odd_list = []


def odd_even(i):
    for a in i:
        if a % 2 == 0:
            even_list.append(a)
        else:
            odd_list.append(a)
    return even_list, odd_list


even_list, odd_list = odd_even(l)


###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]

def universite(ogrenciler):
    for index, student in enumerate(ogrenciler):
        if index < 3:
            print("Mühendislik Fakültesi" + " " + str(index + 1) + ". öğrenci:" + "" + student)
        else:
            print("Tıp Fakültesi" + " " + str(index-2) + ". öğrenci:" + "" + student)

universite(ogrenciler)


###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################
ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

x = list(zip(ders_kodu, kredi, kontenjan))

for i in x:
    print("Kredisi "+ str(i[1]) +" olan "+ str(i[0]) + " kodlu dersin kontenjanı " + str(i[2])+" kişidir.")


###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kontrol(kume1,kume2):
    if kume1.issuperset(kume2) == True:
        print(kume1.intersection(kume2))
    else:
        print(kume2.difference(kume1))

kontrol(kume1,kume2)


###### LIST COMPRHENSIONs
# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

["NUM_" + column.upper() if df[column].dtype != "O" else column.upper() for column in df.columns]


# ###############################################
## GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.

[column.upper() + "_FLAG" if 'no' not in column else column.upper() for column in df.columns]


# ###############################################
## Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################
og_list = ["abbrev", "no_previous"]

new_cols = [column for column in df.columns if column not in og_list]

new_df = df[new_cols]
new_df.head(5).to_string(index=False)