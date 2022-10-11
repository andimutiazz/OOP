def luas_segitiga(alas, tinggi):
    hitung = 1/2 * alas* tinggi
    # return hitung
    print(hitung)


# print(luas_segitiga(5, 10)+10)
# print(luas_segitiga(5, 15)+10)



def coba_coba(*ica):
    print(ica[1])


coba_coba(10, 11,9)

# kwaargs
def coba2(**kwargs):
    print(kwargs['asal'])


coba2(nama="Ica", asal="Sumbawa")