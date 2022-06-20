# Alperen Civan - H5200039

# Date classımını oluşturuyoruz
# gün ay ve yılı sayısal olarak tanımladık
# class çağırıldığında çalışacak olan __init__ fonksiyonu içerisinde
# parametreleri, objeye atadık.
# check date fonksiyonunu kullanarak sonuc değerine atıyoruz
# eğer checkDate fonksiyonu bir hata tespit ederse, ValueError hatası verecektir.
# eğer girilen tarihte bir hata tespit edilmediyse
# __str__ fonksiyonu sayesinde objenin sonuc değerine atadığımız tarihi bize mesaj
# olarak bastıracaktır.

class Date:
    day = 0
    month = 0
    year = 0
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.sonuc = checkDate(self.day, self.month, self.year)
    def __str__(self):
        return "The date is " + self.sonuc
    def weekofday(self):
        # kendimize referans noktası olan
        # 1,1,2000 tarihini baz alıyoruz çünkü bundan önceki bir değeri
        # zaten kabul etmiyoruz. Bu sebeple bir hataya sebep olmayacaktır.
        donen = checkDate(self.day, self.month, self.year)
        if(len(donen)>1):
            currentDate = {
                "day": 1,
                "month": 1,
                "year": 2000,
                "dayNumber": 6
            }
            while (currentDate["year"] != self.year or currentDate["month"] != self.month or currentDate[
                "day"] != self.day):
                if (currentDate["year"] != self.year):
                    if (currentDate["year"] % 4 != 0):
                        currentDate["year"] += 1
                        if(currentDate["dayNumber"] < 7):
                            currentDate["dayNumber"] +=1
                        else:
                            currentDate["dayNumber"] = 1
                    else:
                        currentDate["year"] += 1
                        if (currentDate["dayNumber"] < 7):
                            currentDate["dayNumber"] += 2
                        else:
                            currentDate["dayNumber"] = 2
                elif (currentDate["month"] != self.month):
                    if (currentDate["month"] == 1 or currentDate["month"] == 3 or currentDate["month"] == 5 or currentDate["month"] == 7 or currentDate["month"] == 8 or currentDate["month"] == 10 or currentDate["month"] == 12 ):
                        if(currentDate["month"] == 12):
                            currentDate["month"] = 1
                        else:
                            currentDate["month"] += 1
                        currentDate["dayNumber"] = 31 % 7
                    elif (currentDate["month"] == 4 or currentDate["month"] == 6 or currentDate["month"] == 9 or currentDate["month"] == 11):
                        currentDate["month"] += 1
                        currentDate["dayNumber"] = 30 % 7
                    elif (currentDate["month"] == 2):
                        currentDate["month"] += 1
                        currentDate["dayNumber"] = 30 % 7
                elif (currentDate["day"] != self.day):
                    currentDate["day"] += 1
                    if (currentDate["dayNumber"] < 7):
                        currentDate["dayNumber"] += 1
                    else:
                        currentDate["dayNumber"] = 1
            if(currentDate["dayNumber"] ==1):
                print("Monday")
            elif(currentDate["dayNumber"] ==2):
                print("Tuesday")
            elif(currentDate["dayNumber"] ==3):
                print("Wednesday")
            elif (currentDate["dayNumber"] == 4):
                print("Thursday")
            elif (currentDate["dayNumber"] == 5):
                print("Friday")
            elif (currentDate["dayNumber"] == 6):
                print("Saturday")
            elif (currentDate["dayNumber"] == 7):
                print("Sunday")
    def addday(self, day):
        checkDate(self.day, self.month, self.year)
        cday = self.day
        cmonth = self.month
        cyear = self.year

        monthTotalDays = {
            1: 31, 2: 28, 3: 31, 4: 30,
            5: 31, 6: 30, 7: 31, 8: 31,
            9: 30, 10: 31, 11: 30, 12: 31
        }
        while(day >= 1):
            #print(str(cday) + "-" + str(cmonth) + "-" + str(cyear))
            #print(str(cday) + "-" + str(monthTotalDays[cmonth]))
            if( monthTotalDays[cmonth] == cday ):
                if(cmonth < 12):
                    cmonth = cmonth + 1
                    cday = 1
                else:
                    cmonth = 1
                    cday = 1
                    cyear += 1

            else:
                cday += 1
            day -= 1
        print(str(cday) + "-" + str(cmonth) + "-" + str(cyear))

def checkDate(day, month, year):
    if (day > 31 or day < 1):
        raise ValueError("The date is not valid")
    elif (month > 12 or month < 1):
        raise ValueError("The date is not valid")
    elif (year < 2000 or (year == 2000 and day == 1 and month == 1)):
        raise ValueError("The date is not valid")
    elif ((month == 4 and day > 30) or (month == 6 and day > 30) or (month == 9 and day > 30) or (month == 1 and day > 30)):
        raise ValueError("The date is not valid")
    elif (month == 2 and day > 28):
        if (day > 29):
            raise ValueError("The date is not valid")
        elif (year % 100 == 0 and year % 4 != 0):
            raise ValueError("The date is not valid")
        elif (year % 100 == 0 and year % 400 != 0):
            raise ValueError("The date is not valid")
        else:
            return F"{day}-{month}-{year}"
    else:
        return F"{day}-{month}-{year}"


