# Alperen CİVAN H5200039

# cumle değişkeni string türünde olacak olup kullanıcı tarafından alınacak
# letters isimli dictionary'miz boş olarak yaratılıyor, kullanıcının girdiği
# cümledeki her bir harf için bu dictionary'e ekleme yapacağız

# büyük ve küçük harf ayrımı istemediğiniz için cumle değişkenimizdeki
# varsa büyük harfleri küçük harfe çeviriyoruz.

# letters isimli dictionarymizde harf yoksa dictionary'mize ekliyoruz ve 1 değerini veriyoruz
# varsa dictionarymizdeki değeri 1 arttırıyoruz.
# dictionarymizdeki her bir harf için bastırma işlemlerini gerçekleştiriyoruz
cumle = input("Lütfen bir cümle giriniz : ")
letters = {}
for letter in cumle.lower():
    if letter not in letters:
        letters[letter] = 1;
    else:
        letters[letter] = letters[letter] + 1;
for letterItem in letters.keys():
    print('[', letterItem, '] : ', letters[letterItem])