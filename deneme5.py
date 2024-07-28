import re


def find_exact_match_entities(entities, text, current_text_len):

    #TODO: Birleşik Krallık = İngiltere çevirisi yapılmış araştır.
    #TODO: HMS Queen Elizabeth = HMS Kraliçe Elizabeth
    #TODO: Transliteration bu text ile test et. Text=USS Enterprise CVN-65 (CVN-65) ve Birleşik Krallık HMS Victory CVN-65, 1 Haziran 2022'de katıldı, USS Missouri (BB-63), Naida Hakirevic Prevljak tarafından yine 31 Ocak 2024'te Pearl Harbor'a ulaştı. HMS Victory (H41) gemisinin de geldiği gün tatbikata HMS Queen Elizabeth aktif olarak katıldı.

    def rearrange_entity_coordinates(hash_idx):
        match = res[hash_idx]
        start = match.start()
        end = match.end()
        match_key = match.group() + "*_*" + entity['entity_name']
        entity['matched_text'] = tr_entity_text
        entity['trans_start_index'] = start
        entity['trans_end_index'] = end
        matched_entities[match_key] = hash_idx

    matched_entities = dict()
    cached_matched_entities = dict()

    for entity in entities['trans_entities']:
        tr_entity_text = entity['translated_entity_text']
        text = entities['trans_sentence']
        entity_key = tr_entity_text + "*_*" + entity['entity_name']
        try:
            if matched_entities[entity_key] is not None:
                res = cached_matched_entities[entity_key]
            else:
                res = [m for m in re.finditer(tr_entity_text, text)]
                cached_matched_entities[entity_key] = res
        except KeyError:
            res = [m for m in re.finditer(tr_entity_text, text)]
            cached_matched_entities[entity_key] = res
        res_len = len(res)
        try:
            if matched_entities[entity_key] < res_len:
                rearrange_entity_coordinates(hash_idx=matched_entities[entity_key])
                # idx_ = matched_entities[entity_key]
                # match = res[idx_+1]
                # start = match.start()
                # end = match.end()
                # match_key = match.group() + "*_*" + entity['entity_name']
                # entity['matched_text'] = tr_entity_text
                # entity['trans_start_index'] = start
                # entity['trans_end_index'] = end
                # matched_entities[match_key] = idx_
        except KeyError:
            if res_len:
                rearrange_entity_coordinates(hash_idx=0)
                # idx_ = 0
                # match = res[0]
                # start = match.start()
                # end = match.end()
                # match_key = match.group() + "*_*" + entity['entity_name']
                # entity['matched_text'] = tr_entity_text
                # entity['trans_start_index'] = start
                # entity['trans_end_index'] = end
                # matched_entities[match_key] = idx_


    return entities['trans_entities']

if __name__ == '__main__':
    text="""USS Enterprise CVN-65 (CVN-65) ve Birleşik Krallık HMS Victory CVN-65, 1 Haziran 2022'de katıldı, USS Missouri (BB-63), Naida Hakirevic Prevljak tarafından yine 31 Ocak 2024'te Pearl Harbor'a ulaştı. HMS Victory (H41) gemisinin de geldiği gün tatbikata HMS Queen Elizabeth aktif olarak katıldı. Amiral John Doe operasyonları denetliyordu. İşbirliği yapan tarafları 30 Nisan 2024'te resmi olarak açıklayan Birleşik Krallık Savunma Tedarik Bakanı James Cartlidge, Birleşik Krallık Hükümeti, Kraliyet Donanması ve Tip 26 denizaltı karşıtı savaş firkateyninin tasarımcısı ve üreticisi olan Birleşik Krallık savunma başbakanı BAE Systems'in "ortak çalıştığını" belirtti. Norveç'in gelecekteki yüzey savaşçısı gereksinimlerini desteklemenin yolları hakkında. Cartlidge yazılı yanıtında, "Tip 26 Küresel Savaş Gemisi tasarımının dünya çapındaki diğer donanmalara da benzer bir gereksinimle tanıtılmasını aktif olarak destekliyoruz" dedi. Nisan ayı başlarında Norveç, denizaltı karşıtı helikopterlere sahip beş yeni fırkateyn, en az beş yeni denizaltı ve on büyük ve 18 küçük gemiye kadar standartlaştırılmış bir gemi sınıfına yönelik minimum ihtiyacın ana hatlarını çizerek önümüzdeki yıllardaki denizcilik ihtiyaçlarının ana hatlarını çizdi. Bu daha küçük gemiler muhtemelen kıyı devriyesi korvet/gemi sınıflandırmasında yer alacaktır. “Norveç, güçlü bir denizcilik mirasına sahip bir denizcilik ülkesidir. Norveç Başbakanı Jonas Gahr Støre 5 Nisan'da "Hükümet Donanmayı yeni fırkateynler, denizaltılar ve diğer gemilerle güçlendirmeyi taahhüt ediyor" dedi. Ayrıca Bakınız: John Healey yeni İşçi Partisi hükümetinde savunmaya nasıl liderlik edecek? Hindistan, savunma üretimindeki dönüm noktasını aşarak kendine güven konusunda bir değişime işaret ediyor. Pic Açıklama, Norveç Hükümeti'nin ülke parlamentosuna 2036'ya kadar harcamaları artırmayı, askeri teçhizatı modernleştirmeyi ve modernleştirmeyi teklif ettiği, her dört yılda bir yayınlanan uzun vadeli savunma planlama belgesinin bir parçasıydı. hizmetleri genelindeki platformlar. Birleşik Krallık'ın Tip 26 tasarımı seçilirse, bu, Kanada ve Avustralya'nın kendi ulusal filo yenileme planlarının bir parçası olarak ve ana hizmeti Birleşik Krallık Kraliyet Donanması tarafından benimsenmesinden sonra gemi sınıfı için üçüncü ihracat başarısını temsil edecek. Yaklaşık 7.000 ton (t) yer değiştiren Type 26 tasarımı (Birleşik Krallık ve Avustralya hizmetlerinde sırasıyla City ve Hunter sınıfları olarak bilinecektir), denizaltı karşıtı savaş (ASW) yeteneklerine vurgu yapan gelişmiş, çok amaçlı bir yüzey savaşçısıdır. Tasarımların hiçbiri şu anda hizmette olmasa da, Birleşik Krallık Kraliyet Donanması için sekiz adet, Avustralya Kraliyet Donanması için altı adet ve Kanada Kraliyet Donanması için en fazla 15 adet inşa edilecek. BAE Systems, 2019'da Birleşik Krallık'ın Tip 31 ihtiyacı için Leander sınıfı olarak adlandırılan 'uzatılmış' Khareef sınıfı korvet teklifini kaybetmiş olduğundan portföyünde başka modernize edilmiş fırkateyn tasarımı bulunmuyor. Tip, denizaltı karşıtı olarak tasarlanmamıştı. savaş firkateyni ve genel amaçlı bir savaş gemisi olması amaçlanıyor. Nansen sınıfı: Norveç'in mevcut firkateyn tipi Norveç'in mevcut ana yüzey muharebe gücü, 2018'de HNoMS Helge Ingstad'ın Norveç'teki bir ticari gemiyle çarpışmasının ardından batmasının ardından beş gemilik bir filodan oluşan dört Nansen sınıfı ASW fırkateyninden oluşuyor. fiyort. Beş Nansen sınıfı denizaltı karşıtı savaş fırkateyni, İspanya'nın Navantia şirketi tarafından Norveç Donanması için inşa edildi. Gemiler şunlardır: HNoMS Fridtjof Nansen (hizmette), Roald Amundsen (hizmette), Otto Sverdrup (hizmette), Helge Ingstad (kayıp) ve Thor Heyerdahl (hizmette). Fridjof Nansen sınıfı firkateyni HNoMS Thor Heyerdahl, 2019'da Norveç Denizi'nden geçiyor. Kredi: ABD Donanması/Kitle İletişim Uzmanı 2. Sınıf Cameron Stoner Yaklaşık 5.100 tonluk yer değiştiren ve 133 metre uzunluğa sahip olan bu tip, ASW operasyonları için optimize edilmiş ancak anti - sekiz hücreli Mk41 fırlatmalı Evolved Sea Sparrow Missile ve kutuyla çalıştırılan Naval Strike Missile sistemleri aracılığıyla hava ve yüzey savunma yetenekleri. Kaybolmasından bu yana sınıfının ilki olan HNoMS Fridtjof Nansen'in denize indirilmesi Haziran 2004'te gerçekleştirildi; beşinci ve son geminin denize indirilmesi ise Şubat 2009'da gerçekleşti. Norveç, savunma harcamalarını kademeli olarak artırıyor GlobalData'nın 2023'ün 4. çeyreğinde Norveç'in savunmasına ilişkin analizi Harcamaların ayrıntılı açıklamasında, ülkenin savunma bütçesinin 2023-28 arasında 1,6 milyar dolarlık bir artışla 2023'teki 7,6 milyar dolardan 2028'de 9,2 milyar dolara yükselmesi bekleniyor. Birçok Avrupa ülkesinde olduğu gibi Norveç de, kıtadaki zorlu güvenlik ortamının ortasında, Rusya'nın Şubat 2022'de Ukrayna'yı geniş çaplı işgalinden bu yana savunma harcamalarını artırmaya çalışıyor. Norveç ayrıca daha önce 2026 yılına kadar NATO'nun GSYİH'ya oranı olarak %2'lik savunma harcaması temel çizgisine ulaşmayı taahhüt etmişti; ancak buna yalnızca 2030 zaman diliminde ulaşılması muhtemel. Nisan ayında NATO, 2024 yılında Müttefiklerin üçte ikisinin, GSYH'lerinin en az %2'sini savunmaya yatırma hedefini tutturmasının veya aşmasının beklendiğini açıkladı. 2014'te bu rakam sadece üç ülkeydi. Geçtiğimiz on yılda NATO'nun Avrupalı ​​üyeleri savunmaya yatırım yapma hedefini artırdılar. NATO rakamlarına göre savunmaya kolektif yatırım 2014'te toplam GSYH'nin %1,47'sinden 2024'te %2'ye yükseldi; bu dönemde savunmaya toplam 380 milyar dolardan fazla yatırım yapıyorlar. USS Enterprise CVN-65 (CVN-65) ve Birleşik Krallık HMS Victory CVN-65, 1 Haziran 2022'de katıldı, USS Missouri (BB-63), Naida Hakirevic Prevljak tarafından yine 31 Ocak 2024'te Pearl Harbor'a ulaştı. HMS Victory (H41) gemisinin de geldiği gün tatbikata HMS Queen Elizabeth aktif olarak katıldı."""
    entities={'source_language': 'en', 'target_language': 'tr', 'trans_entities': [{'original_entity_text': 'CVN-65', 'translated_entity_text': 'CVN-65', 'entity_name': 'Hull-Number', 'entity_coordinate': (19, 25)}, {'original_entity_text': 'CVN-65', 'translated_entity_text': 'CVN-65', 'entity_name': 'Hull-Number', 'entity_coordinate': (27, 33)}, {'original_entity_text': 'CVN-65', 'translated_entity_text': 'CVN-65', 'entity_name': 'Hull-Number', 'entity_coordinate': (58, 64)}, {'original_entity_text': 'BB-63', 'translated_entity_text': 'BB-63', 'entity_name': 'Hull-Number', 'entity_coordinate': (113, 118)}, {'original_entity_text': 'H41', 'translated_entity_text': 'H41', 'entity_name': 'Hull-Number', 'entity_coordinate': (228, 231)}, {'original_entity_text': 'USS', 'translated_entity_text': 'USS', 'entity_name': 'Capital-Test', 'entity_coordinate': (4, 7)}, {'original_entity_text': 'CVN', 'translated_entity_text': 'CVN', 'entity_name': 'Capital-Test', 'entity_coordinate': (19, 22)}, {'original_entity_text': 'CVN', 'translated_entity_text': 'CVN', 'entity_name': 'Capital-Test', 'entity_coordinate': (27, 30)}, {'original_entity_text': 'UK', 'translated_entity_text': 'İngiltere', 'entity_name': 'Capital-Test', 'entity_coordinate': (43, 45)}, {'original_entity_text': 'HMS', 'translated_entity_text': 'HMS', 'entity_name': 'Capital-Test', 'entity_coordinate': (46, 49)}, {'original_entity_text': 'CVN', 'translated_entity_text': 'CVN', 'entity_name': 'Capital-Test', 'entity_coordinate': (58, 61)}, {'original_entity_text': 'USS', 'translated_entity_text': 'USS', 'entity_name': 'Capital-Test', 'entity_coordinate': (99, 102)}, {'original_entity_text': 'BB', 'translated_entity_text': 'BB', 'entity_name': 'Capital-Test', 'entity_coordinate': (113, 115)}, {'original_entity_text': 'HMS', 'translated_entity_text': 'HMS', 'entity_name': 'Capital-Test', 'entity_coordinate': (215, 218)}, {'original_entity_text': 'HMS', 'translated_entity_text': 'HMS', 'entity_name': 'Capital-Test', 'entity_coordinate': (271, 274)}, {'original_entity_text': 'USS Enterprise ', 'translated_entity_text': 'USS Kurumsal', 'entity_name': 'Ship-Name', 'entity_coordinate': (4, 19)}, {'original_entity_text': 'HMS Victory ', 'translated_entity_text': 'HMS Zaferi', 'entity_name': 'Ship-Name', 'entity_coordinate': (46, 58)}, {'original_entity_text': 'USS Missouri', 'translated_entity_text': 'USS Missouri', 'entity_name': 'Ship-Name', 'entity_coordinate': (99, 111)}, {'original_entity_text': 'HMS Victory', 'translated_entity_text': 'HMS Zaferi', 'entity_name': 'Ship-Name', 'entity_coordinate': (215, 226)}, {'original_entity_text': 'HMS Queen Elizabeth ', 'translated_entity_text': 'HMS Kraliçe Elizabeth', 'entity_name': 'Ship-Name', 'entity_coordinate': (271, 291)}, {'original_entity_text': 'Naida Hakirevic Prevljak', 'translated_entity_text': 'Naida Hakireviç Prevljak', 'entity_name': 'person', 'entity_coordinate': (170, 194)}, {'original_entity_text': 'Pearl Harbor', 'translated_entity_text': 'Inci liman', 'entity_name': 'location', 'entity_coordinate': (131, 143)}, {'original_entity_text': 'June 1, 2022', 'translated_entity_text': '1 Haziran 2022', 'entity_name': 'Date', 'entity_coordinate': (81, 93)}, {'original_entity_text': 'January 31, 2024', 'translated_entity_text': '31 Ocak 2024', 'entity_name': 'Date', 'entity_coordinate': (149, 165)}], 'trans_sentence': "USS Enterprise CVN-65 (CVN-65) ve Birleşik Krallık HMS Victory CVN-65, 1 Haziran 2022'de katıldı, USS Missouri (BB-63), Naida Hakirevic Prevljak tarafından yine 31 Ocak 2024'te Pearl Harbor'a ulaştı. HMS Victory (H41) gemisinin de geldiği gün tatbikata HMS Queen Elizabeth aktif olarak katıldı.", 'org_sentence': 'The USS Enterprise CVN-65 (CVN-65) and the UK HMS Victory CVN-65 participated on June 1, 2022, the USS Missouri (BB-63) arrived at Pearl Harbor also January 31, 2024, by Naida Hakirevic Prevljak Later that day, the HMS Victory (H41) also arrived during the exercise, the HMS Queen Elizabeth participated actively.'}
    res = find_exact_match_entities(entities=entities, text=text, current_text_len=len(text))
    print("fin")