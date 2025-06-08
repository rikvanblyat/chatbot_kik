import json

def load_faq(path="chatbot_QA_malay.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# Keyword mapping untuk semua 20 soalan
keyword_map = {
    # Soalan 1
    "AP11": "Bagaimana saya boleh memastikan semakan capaian pengguna, had kuasa memperaku, dan tugas kewangan di PTJ adalah selaras dengan peraturan AP11?",
    "semakan capaian": "Bagaimana saya boleh memastikan semakan capaian pengguna, had kuasa memperaku, dan tugas kewangan di PTJ adalah selaras dengan peraturan AP11?",
    "had kuasa": "Bagaimana saya boleh memastikan semakan capaian pengguna, had kuasa memperaku, dan tugas kewangan di PTJ adalah selaras dengan peraturan AP11?",

    # Soalan 2
    "maksud AP11": "Apakah maksud AP11 dan mengapa ia penting untuk dipatuhi dalam urusan kewangan?",
    "penting AP11": "Apakah maksud AP11 dan mengapa ia penting untuk dipatuhi dalam urusan kewangan?",

    # Soalan 3
    "baucar kewangan": "Bilakah baucar kewangan dalam sistem eP atau iGFMAS perlu dicetak?",
    "ep igfmas cetak": "Bilakah baucar kewangan dalam sistem eP atau iGFMAS perlu dicetak?",

    # Soalan 4
    "perihal bayaran": "Apakah perihal bayaran yang perlu dilengkapkan sebelum tuntutan bayaran boleh diproses?",

    # Soalan 5
    "CAA": "Apakah yang dimaksudkan dengan CAA dan bagaimana saya boleh menggunakannya dengan betul dalam sistem iGFMAS?",

    # Soalan 6
    "nombor akaun bank": "Bagaimana cara untuk memastikan nombor akaun bank, nama pembekal, atau penerima adalah tepat dengan dokumen sokongan yang disertakan?",
    "nama pembekal": "Bagaimana cara untuk memastikan nombor akaun bank, nama pembekal, atau penerima adalah tepat dengan dokumen sokongan yang disertakan?",

    # Soalan 7
    "salinan bil invois": "Adakah saya boleh menggunakan salinan bil atau invois sebagai dokumen sokongan jika bil asal telah hilang?",
    "bil hilang": "Adakah saya boleh menggunakan salinan bil atau invois sebagai dokumen sokongan jika bil asal telah hilang?",

    # Soalan 8
    "amaun invois": "Bagaimana untuk memastikan amaun dalam arahan pembayaran adalah sama dengan invois atau dokumen tuntutan?",
    "amaun arahan pembayaran": "Bagaimana untuk memastikan amaun dalam arahan pembayaran adalah sama dengan invois atau dokumen tuntutan?",

    # Soalan 9
    "pengesahan salinan dokumen": "Apakah langkah-langkah pengesahan yang perlu dilakukan jika menggunakan salinan dokumen sokongan untuk pembayaran?",

    # Soalan 10
    "pindaan invois bil": "Bolehkah dokumen utama seperti invois atau bil dibuat pindaan setelah ia diterima?",

    # Soalan 11
    "tarikh akhir pembayaran": "Bagaimanakah cara untuk menentukan tarikh akhir pembayaran mengikut peraturan 14 hari dalam AP103(a)?",
    "AP103": "Bagaimanakah cara untuk menentukan tarikh akhir pembayaran mengikut peraturan 14 hari dalam AP103(a)?",
    "14 hari": "Bagaimanakah cara untuk menentukan tarikh akhir pembayaran mengikut peraturan 14 hari dalam AP103(a)?",

    # Soalan 12
    "AP58": "Siapakah yang bertanggungjawab untuk menandakan kotak AP58(a) atau AP96 dalam sistem iGFMAS?",
    "AP96": "Siapakah yang bertanggungjawab untuk menandakan kotak AP58(a) atau AP96 dalam sistem iGFMAS?",

    # Soalan 13
    "TELAH BAYAR": "Apakah dokumen yang perlu dicap atau ditanda sebagai 'TELAH BAYAR' selepas pembayaran dibuat?",
    "selepas pembayaran": "Apakah dokumen yang perlu dicap atau ditanda sebagai 'TELAH BAYAR' selepas pembayaran dibuat?",

    # Soalan 14
    "modul eP": "Dalam proses pembayaran, bilakah saya perlu menggunakan modul eP dan bilakah saya perlu menggunakan iGFMAS?",
    "guna igfmas": "Dalam proses pembayaran, bilakah saya perlu menggunakan modul eP dan bilakah saya perlu menggunakan iGFMAS?",

    # Soalan 15
    "pengasingan tugas": "Apakah yang dimaksudkan dengan pengasingan tugas dalam proses kewangan, dan mengapa ia penting?",

    # Soalan 16
    "penerima bayaran sah": "Bagaimana saya boleh memastikan penerima bayaran adalah sah dan betul?",
    "sah penerima bayaran": "Bagaimana saya boleh memastikan penerima bayaran adalah sah dan betul?",

    # Soalan 17
    "pencegahan pembayaran berganda": "Apakah langkah pencegahan untuk mengelakkan pembayaran berganda (double payment)?",
    "double payment": "Apakah langkah pencegahan untuk mengelakkan pembayaran berganda (double payment)?",

    # Soalan 18
    "pelarasan bayaran": "Jika terdapat pelarasan bayaran, apakah prosedur yang perlu saya ikuti?",

    # Soalan 19
    "cap tarikh terima": "Bolehkah bayaran dibuat tanpa cap 'TARIKH TERIMA' pada dokumen?",

    # Soalan 20
    "dokumen sokongan lengkap": "Bagaimana saya boleh memastikan dokumen sokongan yang diperlukan untuk bayaran adalah lengkap sebelum dihantar?",
}

def cari_jawapan(user_input, faq_list):
    user_input = user_input.lower()
    matched_question = None

    # Cari keyword match
    for keyword, soalan in keyword_map.items():
        if keyword.lower() in user_input:
            matched_question = soalan
            break

    # Kalau ada match, return jawapan
    if matched_question:
        for item in faq_list:
            if item["Soalan"] == matched_question:
                return item["Jawapan"]

    # Kalau tak jumpa keyword, fallback
    return "Harap maaf, sila hubungi Pegawai kami di JANM Pulau Pinang untuk pertanyaan lanjut."
