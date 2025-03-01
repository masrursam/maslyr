# List of phrases to mix and match
phrases = [
    "Saya sangat puas dengan layanan LayerEdge, semoga terus maju!",
    "LayerEdge adalah platform yang luar biasa, saya sangat merekomendasikannya!",
    "Terima kasih LayerEdge, semoga sukses selalu!",
    "LayerEdge memberikan pengalaman terbaik dalam dunia crypto, saya sangat senang!",
    "Proyek LayerEdge sangat menjanjikan, saya yakin akan sukses besar!",
    "Airdrop LayerEdge sangat menguntungkan, terima kasih atas kesempatannya!",
    "LayerEdge adalah solusi masa depan untuk teknologi blockchain!",
    "Saya bangga menjadi bagian dari komunitas LayerEdge, semoga terus berkembang!",
    "LayerEdge memberikan layanan yang cepat dan efisien, saya sangat terkesan!",
    "Token LayerEdge memiliki potensi besar, saya sangat antusias menunggu perkembangannya!",
    "Saya sangat senang bisa bergabung dengan proyek LayerEdge!",
    "LayerEdge memberikan harapan baru untuk masa depan crypto!",
    "Terima kasih LayerEdge atas transparansi dan profesionalismenya!",
    "Saya yakin LayerEdge akan menjadi pemimpin di industri blockchain!",
    "Komunitas LayerEdge sangat solid dan suportif!",
    "LayerEdge adalah proyek yang patut diperhatikan oleh semua investor!",
    "Saya sangat merekomendasikan LayerEdge kepada teman-teman saya!",
    "LayerEdge memberikan peluang besar untuk berkembang di dunia crypto!",
    "Saya sangat terkesan dengan visi dan misi LayerEdge!",
    "LayerEdge adalah platform yang bisa diandalkan untuk masa depan!",
]

# Generate 1,000 lines
with open("layeredge_proof_messages.txt", "w", encoding="utf-8") as file:
    for i in range(10000):
        line = f'                "{phrases[i % len(phrases)]}",\n'
        file.write(line)

print("File 'layeredge_proof_messages.txt' has been created with 1,000 lines!")