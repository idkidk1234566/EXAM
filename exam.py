# #8kyu
#What's the real floor?
def get_real_floor(n):
    if n<= 0:
        return n #unda dagvebrunebina n im shemtxvevashi tu es n naklebi an toli iqneboda 0ze 1 aseve unda udrides 0s
    elif n < 13:
        return n - 1 # tu ricxvi aris 13 ze naklebia erti unda gamoakldes
    else:
        return n - 2 # xolo danarchen shemtxvevashi ki  2 unda gamoakldes anu tu zeda piroba falsia mashin amoqmeddeba es


#8kyu
#Holiday VIII - Duty Free
def duty_free(price, discount, holiday_cost):
    percent = (price * discount) / 100 #ricxvis procentis gamosatlelad fasi gavamravle discountze da gavye  100ze
    
    num = holiday_cost // percent    #shemdeg ki girebuleba gavye percentze rata pasuxi migvego
    return int(num)  # aq ki integerad gadavaqcie da sabolood davabrune shedegi


# #7kyu
#Last Survivor
def last_survivor(letters, coords): 
    letters = list(letters)
    for i in coords:
        integer = int(i)
        letters.pop(integer)
    return ''.join(letters)

# listad gadavaqcie lettersi shemdeg ki coords gadavuare da shevqmeni cvladi sadac i gadavaqcie integerad radgan integeri ar meordeba forshi shevinaxe cvladshi
#shemdeg lettersidan amovige es i da sabollood  carieli brchyali davumate letters rata ar iyos spacebi da sabolood davabrune es

#7kyu
#Credit card issuer checking
def get_issuer(number):
    string = str(number) #gadavaqcie stringad rata shemezlo shemdeg len is gamoyeneba
    lenght = len(string) #gavige stringad gadaqceuli numberis leni
    if lenght == 15 and string.startswith(('34','37')):
        return "AMEX" # tu leni iqneboda 15 da es ricxvi daiwyeboda 34it an 37 it mashin daabrunebda AMEX s
    elif lenght == 16 and string.startswith(("51","52","53","54","55")):
        return "Mastercard" #tu leni iqneboda 16 da ricxvi daiwyeboda am ricxvebit mashin daabrunebda Mastercards
    elif lenght == 16 and string.startswith(("6011")):
        return "Discover" #tu leni iqneboda 16  da ricxvi daiwyeboda 6011 it mashin daabrunebda Discovers
    elif lenght == 16 and string.startswith(("4")):
        return "VISA" #tu leni iqneboda 16 xolo ricxvi daiwyeboda 4 it daabrunebda VISA s
    elif lenght == 13 and string.startswith(("4")):
        return "VISA" # aqac vizas daabrunebda ogond im shemtxvevashi tu leni iqneboda 13 da daiwyeboda 4 it
    else:
        return "Unknown" #xolo tu zeda kodidan arcerti ar emtxveva ricxvs elses saxit gamoutans Unknown s
