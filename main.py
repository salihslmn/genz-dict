meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    # DOĞRU KULLANIM: Kelimenin anlamını yazdırır
    print(meme_dict[word])
else:
    # DOĞRU KULLANIM: Hata mesajını yazdırır
    print("Bu kelime bulunamadı.")
