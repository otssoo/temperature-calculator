# farenhati kelwin celsjusz newtony delislea reaumura rankine romera
print('Welcome in temperature calculator.\n You can calculate Kelvin (K), Fahrenheit (F), Celsius (C), Newton (N), Delisle (De), Rømer (Ro), Réaumur(Re), Rankine(R) \n')



def enter():
    enter = input('Enter the temperature unit to start from:\n').lower()
    if enter == str("k" or "kelvin"):
        kelwin()
    elif enter == str("f" or "fahrenheit"):
        fahrenheit()
    elif enter == str('c' or 'celsius'):
        celsius()
    elif enter == str('n'or "newton"):
        newton()
    elif enter == str('de'or "delisle"):
        delisle()
    elif enter == str('ro' or "romer"or'Rømer'):
        romer()
    elif enter == str('re'or "Réaumur"or'Ré'):
        reaumur()
    elif enter == str('r' or "Rankine"):
        rankine()
    else:
        print('Select the temperature unit!')
        return enter

def kelwin():
    enterk = input('Enter the temperature in Kelvin:\n')
    point = input("How many zeros after the decimal point?\n")
    bef = float(enterk)-273.15
    ktf = (bef*1.8)+32
    ktc = bef
    ktn = ((ktc*33)/100)
    ktde = ((373.15 - (float(enterk)))*1.5)
    ktro = bef*(21/40)+7.5
    ktre =  bef*0.8
    ktr = float(enterk)*1.8

    print('Farenheit',round(ktf,int(point)), '°F')
    print('Celsius:', round(ktc,int(point)), '°C')
    print('Newton:', round(ktn, int(point)), '°N')
    print('Delisle:', round(ktde, int(point)), '°De')
    print('Rømer:', round(ktro, int(point)), '°Ro')
    print('Réaumur:', round(ktre, int(point)), '°Re')
    print('Rankine:', round(ktr, int(point)), '°Ra')
def fahrenheit():
    enterf = input('Enter the temperature in Farenheit:\n')
    point = input("How many zeros after the decimal point?\n")
    bef = float(enterf)-32
    ftk = ((float(enterf)+459.67)*(5/9))
    ftc = bef/1.8
    ftn = bef * (11/60)
    ftde = (212-float(enterf))*(5/6)
    ftro = bef*(7/24)+7.5
    ftre = bef * (4/9)
    ftr = float(enterf)+459.67


    print('Kelvin',round(ftk,int(point)), '°K')
    print('Celsius:', round(ftc,int(point)), '°C')
    print('Newton:', round(ftn, int(point)), '°N')
    print('Delisle:', round(ftde, int(point)), '°De')
    print('Rømer:', round(ftro, int(point)), '°Ro')
    print('Réaumur:', round(ftre, int(point)), '°Re')
    print('Rankine:', round(ftr, int(point)), '°Ra')
def celsius():
    enterc = input('Enter the temperature in Celsius:\n')
    point = input("How many zeros after the decimal point?\n")
    ctk = float(enterc)+273.15 #
    ctf = (float(enterc)*1.8)+32 #
    ctn = float(enterc)*0.33
    ctde = (100-float(enterc))*1.5
    ctro = (float(enterc)*(21/40))+7.5
    ctre = float(enterc)*(4/5)
    ctr = (float(enterc) + 273.15)*(9/5) #
    print('Kelvin', round(ctk, int(point)), '°K')
    print('Fahrenheit:', round(ctf, int(point)), '°F')
    print('Newton:', round(ctn, int(point)), '°N')
    print('Delisle:', round(ctde, int(point)), '°De')
    print('Rømer:', round(ctro, int(point)), '°Ro')
    print('Réaumur:', round(ctre, int(point)), '°Re')
    print('Rankine:', round(ctr, int(point)), '°Ra')
def newton():
    entern = input('Enter the temperature in newton:\n')
    point = input("How many zeros after the decimal point?\n")
    ntk = float(entern)*(100/33)+273.15
    ntf = float(entern)*(60/11)+32
    ntc = float(entern) * (100/33)
    ntde = (33 - float(entern)) * (50/11)
    ntro = (float(entern) * (35 / 22)) + 7.5
    ntre = float(entern) * (80 / 33)
    ntr = (float(entern)) * (60 / 11) + 491.67  #

    print('Kelvin', round(ntk, int(point)), '°K')
    print('Fahrenheit:', round(ntf, int(point)), '°F')
    print('Celsius:', round(ntc, int(point)), '°C')
    print('Delisle:', round(ntde, int(point)), '°De')
    print('Rømer:', round(ntro, int(point)), '°Ro')
    print('Réaumur:', round(ntre, int(point)), '°Re')
    print('Rankine:', round(ntr, int(point)), '°Ra')
def delisle():
    entern = input('Enter the temperature in delisle:\n')
    point = input("How many zeros after the decimal point?\n")
    dtk = 373.15-(float(entern) * (2/3))
    dtf = 212-float(entern) * (6/5)
    dtc = 100-float(entern) * (2/3)
    dtn = 33 - float(entern) * (11 / 50)
    dtro = 60- float(entern) * (7 / 20)
    dtre = 80 - float(entern) * (8 / 15)
    dtr = 671.67 - (float(entern)) * (6/5)

    print('Kelvin', round(dtk, int(point)), '°K')
    print('Fahrenheit:', round(dtf, int(point)), '°F')
    print('Celsius:', round(dtc, int(point)), '°C')
    print('Newton:', round(dtn, int(point)), '°N')
    print('Rømer:', round(dtro, int(point)), '°Ro')
    print('Réaumur:', round(dtre, int(point)), '°Re')
    print('Rankine:', round(dtr, int(point)), '°Ra')
def romer():
    enterro = input('Enter the temperature in Rømer:\n')
    point = input("How many zeros after the decimal point?\n")
    rotk = (float(enterro) - 7.5)*(40/21)+ 273.15
    rotf = (float(enterro) -7.5) * (24 / 7) + 32
    rotc =  (float(enterro)-7.5) * (40 / 21)
    rotn = (float(enterro)-7.5) * (22 / 35)
    rotd = (60 - float(enterro)) * (20 / 7)
    rotre = (float(enterro) -7.5)* (32 / 21)
    rotr = (float(enterro)-7.5) * (24 / 7) + 491.67

    print('Kelvin', round(rotk, int(point)), '°K')
    print('Fahrenheit:', round(rotf, int(point)), '°F')
    print('Celsius:', round(rotc, int(point)), '°C')
    print('Newton:', round(rotn, int(point)), '°N')
    print('Delisle:', round(rotd, int(point)), '°D')
    print('Réaumur:', round(rotre, int(point)), '°Re')
    print('Rankine:', round(rotr, int(point)), '°Ra')
def reaumur():
    enterro = input('Enter the temperature in Réaumur:\n')
    point = input("How many zeros after the decimal point?\n")
    retk = float(enterro) * (5 / 4) + 273.15
    retf = float(enterro)* (9 / 4) + 32
    retc = float(enterro)* (5 / 4)
    retn = float(enterro)  * (33 / 80)
    retd = (80 - float(enterro)) * (15 / 8)
    retro = float(enterro) * (21 / 32) +7.5
    retr = float(enterro)  * (9 / 4) + 491.67

    print('Kelvin', round(retk, int(point)), '°K')
    print('Fahrenheit:', round(retf, int(point)), '°F')
    print('Celsius:', round(retc, int(point)), '°C')
    print('Newton:', round(retn, int(point)), '°N')
    print('Delisle:', round(retd, int(point)), '°D')
    print('Rømer:', round(retro, int(point)), '°Ro')
    print('Rankine:', round(retr, int(point)), '°Ra')
def rankine():
    enterro = input('Enter the temperature in Rankine:\n')
    point = input("How many zeros after the decimal point?\n")
    ratk = float(enterro) * (5 / 9)
    ratf = float(enterro) - 459.67
    ratc = (float(enterro)-491.67) * (5 / 9)
    ratn = (float(enterro)-491.67) * (11 / 60)
    ratd = (671.67 - float(enterro)) * (5 / 6)
    ratro = (float(enterro)-491.67) * (7 / 24) + 7.5
    ratre = (float(enterro)-491.67) * (4 / 9)

    print('Kelvin', round(ratk, int(point)), '°K')
    print('Fahrenheit:', round(ratf, int(point)), '°F')
    print('Celsius:', round(ratc, int(point)), '°C')
    print('Newton:', round(ratn, int(point)), '°N')
    print('Delisle:', round(ratd, int(point)), '°D')
    print('Rømer:', round(ratro, int(point)), '°Ro')
    print('Réaumur:', round(ratre, int(point)), '°Re')


enter()