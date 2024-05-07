class phone():
    # sinif = "Iphone"
    def __init__(self,seriya,nov,sIM_kart,emeliiyat_sistemi,yaddas,qiymet,duym):
        self.seriya = seriya
        self.nov = nov
        self.sIM_kart = sIM_kart
        self.emeliiyat_sistemi = emeliiyat_sistemi
        self.yaddas = yaddas
        self.qiymet = qiymet
        self.duym = duym


    def duym_olcu(self):
        if self.duym > 6:
            return f"{self.seriya} telefonun duymu standart deyil"
        else:
            return f"{self.seriya} telefonun duymu standartdir"


Iphone13 = phone ("Iphone13","Smartfon",1,"Apple IOS",256,1500,6)
Iphone14 = phone ("Iphone14","Smartfon",1,"Apple IOS",256,1700,6)
Iphone15 = phone ("Iphone15","Smartfon",1,"Apple IOS",512,2500,7)

print(f"{Iphone13.seriya} adli telefon {Iphone13.nov} novludur.{Iphone13.sIM_kart} kartlidir ve emeliyyat sistemi {Iphone13.emeliiyat_sistemi} sisteme malikdir,yaddasi {Iphone13.yaddas}-dir.qiymeti ise {Iphone13.qiymet} manatdir .{Iphone13.duym_olcu()}")

print(f"{Iphone14.seriya} adli telefon {Iphone14.nov} novludur.{Iphone14.sIM_kart} kartlidir ve emeliyyat sistemi {Iphone14.emeliiyat_sistemi} sisteme malikdir,yaddasi {Iphone14.yaddas}-dir.qiymeti ise {Iphone14.qiymet} manatdir .{Iphone14.duym_olcu()}")

print(f"{Iphone15.seriya} adli telefon {Iphone15.nov} novludur.{Iphone15.sIM_kart} kartlidir ve emeliyyat sistemi {Iphone15.emeliiyat_sistemi} sisteme malikdir,yaddasi {Iphone15.yaddas}-dir.qiymeti ise {Iphone15.qiymet} manatdir .{Iphone15.duym_olcu()}")