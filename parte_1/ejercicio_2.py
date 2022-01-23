names_pokemon = ["audino", "bagon", "baltoy", "banette", "bidoof", "braviary", "bronzor", "carracosta", "charmeleon",
"cresselia", "croagunk", "darmanitan", "deino", "emboar", "emolga" ,"exeggcute", "gabite" ,"girafarig",
"gulpin", "haxorus" ,"heatmor", "heatran" ,"ivysaur" ,"jellicent" ,"jumpluff", "kangaskhan", "kricketune",
"landorus", "ledyba" ,"loudred" ,"lumineon" ,"lunatone", "machamp" ,"magnezone", "mamoswine",
"nosepass", "petilil", "pidgeotto", "pikachu", "pinsir","poliwrath", "poochyena", "porygon", "porygonz",
"registeel" ,"relicanth", "remoraid", "rufflet", "sableye", "scolipede", "scrafty", "seaking", "sealeo", "silcoon",
"simisear", "snivy", "snorlax", "spoink", "starly", "tirtouga", "trapinch", "treecko", "tyrogue", "vigoroth", "vulpix",
"wailord", "wartortle", "whismur", "wingull", "yamask"]

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letters_first = {}


for i in abc:
    dict_letter = {}
    list_letter = []
    for names in names_pokemon:
        if i == names[0]:
            list_letter.append(names)

    dict_letter = {
        i: list_letter
    }
    letters_first.update(dict_letter)

count1 = 0

def letters(name):
    flag = 0
    lis = []
    for n in letters_first.items():
        if name[-1] == n[0]:
            lis.append(name)
            count_n = 0
            while (flag==0):
                for n in letters_first.items():
                    if name[-1] == n[0]:
                        try:
                            coun = lis.count(n[1][count_n])
                        except:

                            if count_n-1==-1:
                                return lis
                            try:
                                coun = lis.count(n[1][count_n-1])
                            except:
                                if count_n-2==-1:
                                    return lis
                                coun = lis.count(n[1][0])
                        if coun == 1:
                            if len(n[1]) > 1:
                                count_n += 1
                        try:
                            name = n[1][count_n]
                        except:
                            count_n = count_n - 1
                            name = n[1][count_n-1]
                        lis.append(name)
    return lis

list_names = []
for name in names_pokemon:
    list_name = sum(1 for i in letters(name) if str(i))
    list_names.append((name, letters(name), list_name))

numero_mayor = [int(num[2]) for num in list_names]
count2 = 0
for name in list_names:
    
    if name[2]==max(numero_mayor):
        count2 += 1
        print(f"\n Secuencia N.{count2}: \n")
        for n in name[1]:
            print(n)




