#!/usr/bin/env python
# coding: utf-8

# In[10]:


islem = input("Çarpanlara Ayırma(ÇA) Mı Yoksa Diskriminant(D) Mı?: ")
if islem == "D":
    a = float(input("2. Derece Değerini Giriniz: "))
    b = float(input("1. Derece Değerini Giriniz: "))
    c = float(input("Sabit Değeri Giriniz: "))

    # diskriminant hesaplaması
    d = (b**2) - (4*a*c)

    # förmül kullanarak hesaplama
    if d >= 0:
        root1 = (-b + (d**0.5)) / (2*a)
        root2 = (-b - (d**0.5)) / (2*a)
    else:
        root1 = (-b + (abs(d)**0.5)*1j) / (2*a)
        root2 = (-b - (abs(d)**0.5)*1j) / (2*a)

    # sayı çok uzunsa sadeleştir
    def simplify(root, a):
        if type(root) == complex:
            return None
        elif float(root).is_integer():
            return int(root)
        else:
            for i in range(1, 10000):
                num = round(root * i)
                if num / i == root:
                    if i == 2*a:
                        return "{0}/{1}".format(num//2, a)
                    else:
                        return "{0}/{1}".format(num, i)
            return root

    # kökleri sadeleştir
    root1 = simplify(root1, a)
    root2 = simplify(root2, a)

    # köklerin sadeleştirilmiş olup olmadığını kontrol et
    if root1 is None or root2 is None:
        print("İşlemin sonuçu komplike olduğundan dolayı okunabilir bir hale sadeleştirilemedi.")
        print("Kök 1 = (-b + sqrt(b^2 - 4ac)i) / 2a = ({0} + sqrt({1}i)) / {2}".format(-b, abs(d), 2*a))
        print("Kök 2 = (-b - sqrt(b^2 - 4ac)i) / 2a = ({0} - sqrt({1}i)) / {2}".format(-b, abs(d), 2*a))
    else:
        # sonuçu formatlayarak sadeleştir
        if isinstance(root1, float):
            root1_str = format(root1, '.3f')
        else:
            root1_str = str(root1)
        if isinstance(root2, float):
            root2_str = format(root2, '.3f')
        else:
            root2_str = str(root2)

        # kökleri yaz
        print("X değerinin kökleri {0} ve {1}".format(root1_str, root2_str))
        
elif islem == "ÇA":
    import math

    a = float(input("x^2 Katsayısını Giriniz: "))
    b = float(input("x Katsayısını Giriniz: "))
    c = float(input("Sabit Terimi Giriniz: "))

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + (discriminant)**0.5) / (2*a)
        x2 = (-b - (discriminant)**0.5) / (2*a)
        if abs(x1) < 1e6 and abs(x2) < 1e6:
            print("Aradığınız Kökler", x1, "Ve", x2)
        else:
            try:
                x1_int = int(x1)
                x2_int = int(x2)
                x1_frac = x1 - x1_int
                x2_frac = x2 - x2_int
                common_denominator = 1
                while x1_frac != int(x1_frac) or x2_frac != int(x2_frac):
                    x1_frac *= 10
                    x2_frac *= 10
                    common_denominator *= 10
                x1_frac = int(x1_frac)
                x2_frac = int(x2_frac)
                gcd = math.gcd(common_denominator, math.gcd(x1_frac, x2_frac))
                simplified_common_denominator = common_denominator // gcd
                x1_frac = x1_frac // gcd
                x2_frac = x2_frac // gcd
                print("Aradığınız Kökler: ", x1_int, "+", x1_frac, "/",
                      simplified_common_denominator, "Ve", x2_int, "+", x2_frac,
                      "/", simplified_common_denominator)
            except ValueError:
                print("Kökler sadeleştirelemeyecek kadar büyük veya komplike.")
    elif discriminant == 0:
        x1 = -b / (2*a)
        if abs(x1) < 1e6:
            print("Aradığınız Kök: ", x1)
        else:
            try:
                x1_int = int(x1)
                x1_frac = x1 - x1_int
                common_denominator = 1
                while x1_frac != int(x1_frac):
                    x1_frac *= 10
                    common_denominator *= 10
                x1_frac = int(x1_frac)
                gcd = math.gcd(common_denominator, x1_frac)
                simplified_common_denominator = common_denominator // gcd
                x1_frac = x1_frac // gcd
                print("Aradığınız Kök: ", x1_int, "+", x1_frac, "/",
                      simplified_common_denominator)
            except ValueError:
                print("Kökler sadeleştirelemeyecek kadar büyük veya komplike.")
    else:
        real_part = -b / (2*a)
        imaginary_part = ((-discriminant)**0.5) / (2*a)
        if abs(real_part) < 1e6 and abs(imaginary_part) < 1e6:
            print("Aradığınız Kökler", real_part, "+", imaginary_part, "i Ve",
                  real_part, "-", imaginary_part, "i")
        else:
            print("Kökler sadeleştirelemeyecek kadar büyük veya komplike.")
input("Program bitti. Çıkmak için Enter tuşuna basın...")


# In[ ]:




