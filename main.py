meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO": "untuk menjadi agresif/marah",
            }

print(meme_dict['LOL'])

for i in range(7):
  word = input("\n\nketik kata yang kamu tidak mengerti(gunakan huruf kapital semua!): ")
  
  if word in meme_dict.keys():
    print(meme_dict[word])
  
  else:
    print("erorr")
    
