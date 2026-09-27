# -*- coding: utf-8 -*-
"""
First72 訪日旅行者向けページ 翻訳辞書
---------------------------------------------
言語を追加するときは FOREIGN に同じキー構成で1ブロック足す。
LANG_META に載っていても FOREIGN に無い言語は生成・表示されない。
"""

LANG_META = {
    "ja":      {"label": "日本語",   "dir": "foreign",  "html_lang": "ja"},
    "en":      {"label": "English",  "dir": "en",       "html_lang": "en"},
    "zh-hans": {"label": "简体中文", "dir": "zh-hans",  "html_lang": "zh-Hans"},
    "zh-hant": {"label": "繁體中文", "dir": "zh-hant",  "html_lang": "zh-Hant"},
    "ko":      {"label": "한국어",   "dir": "ko",       "html_lang": "ko"},
}

FOREIGN = {
# =============================================================
# 日本語（原文）
# =============================================================
"ja": {
    "meta_title": "訪日旅行中の逮捕・刑事弁護｜First72 ― 外国籍の旅行者とご家族へ",
    "meta_desc":  "旅行中に日本で逮捕された外国籍の方とご家族へ。逮捕から起訴までの流れ、帰国・再来日への影響、旅行者に多い事件（万引き、暴行、大麻、盗撮、無免許運転など）を解説。通訳人の手配に対応。全国対応。",
    "sub":        "訪日旅行者の刑事弁護",
    "hdr_mail":   "メール",

    "tag":   "訪日旅行中の方・ご家族の方へ",
    "h1":    "旅行中に日本で逮捕されたら、<br><em>最初の72時間</em>が重要です。",
    "lead":  "日本では、逮捕から起訴・不起訴の判断まで、最長23日間身柄を拘束されることがあります。予定していた便で帰国できるか、また日本に来られるか。早い段階から弁護士が関わることが、釈放の時期や処分の内容、将来の来日にも影響します。",
    "cta_mail": "メールで相談する",
    "cta_tel":  "電話",
    "note":  "通訳人の手配に対応／全国対応（交通費・日当は別途、日程は調整のうえ）／費用は海外送金でお受けします",

    "tl_eyebrow": "Procedure",
    "tl_h2":      "逮捕から裁判までの流れ",
    "big1_u": "時間", "big1_label": "逮捕から勾留請求まで",
    "big2_u": "日",   "big2_label": "逮捕から起訴・不起訴の判断まで（最長）",
    "tl_lead":    "逮捕されると、次の時間制限のもとで手続が進みます。最初の72時間は、ご家族が面会できないことも多く、弁護士が本人と会える重要な期間です。",
    "steps": [
        ("逮捕", "最大48時間",
         "警察で取調べを受け、この間に事件が検察官へ送られます（送致）。ご家族でも面会できないことが多い一方、弁護士は面会（接見）できます。"),
        ("送致・勾留請求", "最大24時間",
         "検察官が、引き続き身柄を拘束する必要があるかを判断し、裁判官に勾留を請求します。逮捕からここまでが最大72時間です。"),
        ("勾留", "10日間",
         "裁判官が勾留を認めると、原則10日間、警察署などで身柄を拘束されます。"),
        ("勾留延長", "最大10日間",
         "捜査が続く場合、さらに最大10日間延長されることがあります。"),
        ("起訴・不起訴", "逮捕から最長23日",
         "検察官が起訴するかどうかを決めます。不起訴になれば釈放されます。罰金で終わる略式手続になることもあります。起訴されると裁判になり、身柄拘束が続くことがあります。"),
        ("裁判（公判）", "起訴から約1〜2か月",
         "第1回の裁判が開かれます。事件によっては、より長い期間がかかります。判決で刑罰（拘禁刑・罰金、執行猶予の有無など）が決まります。"),
    ],

    "cases_eyebrow": "Common cases",
    "cases_h2":      "旅行者に多い事件",
    "cases_lead":    "旅行中の事件には、日本の法律が母国と違うことがきっかけになるものも少なくありません。",
    "cases": [
        ("万引き・窃盗",
         "ドラッグストアや量販店での万引きが典型です。被害弁償や示談が進めば、不起訴や早期の釈放につながることがあります。"),
        ("暴行・傷害",
         "繁華街での飲酒後のけんかなど。被害者との示談が、処分に大きく影響します。"),
        ("大麻・THC製品などの薬物",
         "母国で合法でも、日本では違法です。CBD製品などにTHCが含まれていると処罰の対象になり、2024年12月からは大麻の使用も処罰されます。空港での持込み（個人使用目的）も含みます。将来の入国への影響が特に大きい類型です。"),
        ("盗撮・痴漢",
         "駅や電車内、商業施設などでの事件です。性的姿態撮影処罰法や、各都道府県の迷惑防止条例が適用されます。"),
        ("器物損壊・建造物侵入",
         "落書き、寺社や文化財の損壊、立入禁止区域への立入りなど。文化財の場合は、より重く処罰されることがあります。"),
        ("無免許運転・交通事故",
         "国際運転免許証の種類や発行国によっては日本で運転できず、無免許運転になります。レンタカーでの事故にも対応します。"),
        ("刃物の携帯",
         "刃体の長さが6cmを超える刃物を、正当な理由なく持ち歩くと銃刀法違反になります。購入した包丁などは、梱包したまま持ち運んでください。"),
    ],

    "can_eyebrow": "What we do",
    "can_h2":      "弁護士ができること",
    "can_items": [
        ("接見（面会）", "警察署などで本人と面会し、取調べへの対応や今後の流れを説明します。通訳人の手配にも対応します。"),
        ("準抗告", "勾留の決定に対して不服を申し立て、釈放を求めます。"),
        ("勾留取消請求", "勾留の理由や必要性がなくなった場合に、勾留の取消しを求めます。"),
        ("保釈請求", "起訴された後、保釈金を納めることを条件に釈放を求めます。起訴前には保釈の制度はありません。"),
        ("接見禁止の一部解除", "ご家族との面会や手紙のやりとりが禁止されている場合に、その一部解除を求めます。"),
        ("勾留理由開示", "法廷で勾留の理由を明らかにするよう求めます。ご家族が本人の姿を確認できる機会にもなります。"),
        ("示談交渉", "被害者のいる事件では、弁護士が被害者側と示談交渉を行います。示談は、不起訴や早期の釈放に大きく影響します。"),
        ("差入れ", "衣類・書籍・日用品などを、施設の規則の範囲内でお届けします。ご家族が面会できない場合も、弁護士を通じてお届けできることがあります。"),
    ],

    "need_eyebrow": "For release",
    "need_h2":      "釈放・保釈のために必要なこと",
    "need_lead":    "旅行者の方は日本に住所や身近な知人がいないことが多く、帰国のおそれを理由に、釈放や保釈が認められにくい傾向があります。次の点を早めに整えることが重要です。",
    "need_items": [
        ("滞在先の確保（制限住居）", "釈放後に滞在する日本国内のホテルなどの住所です。保釈の条件として、滞在先が指定されます。"),
        ("身元引受人", "釈放後の生活を監督し、裁判への出頭を支える方です。来日できるご家族や、日本に住む知人などが考えられます。"),
        ("パスポートの保管", "帰国しないことを示すため、保釈の条件としてパスポートを弁護人が預かることがあります。"),
        ("滞在期限と帰国便", "身柄拘束中や保釈中に短期滞在の期限が来る場合は、入管での手続が必要です。帰国便の変更も早めに検討します。"),
    ],

    "imm_eyebrow": "Returning home",
    "imm_h2":      "帰国・再来日への影響",
    "imm_lead":    "旅行者の方にとって、刑事手続の結果は、予定どおりの帰国や将来の来日に直結します。早い段階から弁護士が関わり、手続を短く終わらせる道筋を探ることが重要です。",
    "imm_list": [
        "身柄拘束中に短期滞在の期限が切れると、釈放後に入管の手続が必要になることがあります。",
        "保釈中はパスポートを預けるため、裁判が終わるまで出国できません。",
        "不起訴になれば前科はつきません。略式手続で罰金を納めて手続が終わる場合もありますが、罰金も前科になります。",
        "有罪判決の内容によっては、将来日本への入国を拒否されることがあります。薬物事件で有罪となった場合は、特に影響が大きくなります。",
    ],
    "imm_note": "※ どのような影響があるかは、事件の内容や判決によって異なります。個別にご相談ください。",

    "rights_eyebrow": "Your rights",
    "rights_h2":      "逮捕された方の権利",
    "rights_items": [
        ("黙秘権", "取調べで、言いたくないことは言わなくてかまいません。"),
        ("弁護人を依頼する権利", "弁護士を依頼できます。国籍にかかわらず、一定の場合は国選弁護人を利用できます。"),
        ("通訳", "日本語が分からない場合、取調べや裁判は通訳人を介して行われます。"),
        ("領事館への通報", "自国の領事館に、逮捕されたことを知らせるよう求めることができます。"),
        ("署名を拒む権利", "内容が正しくない、または理解できない供述調書には、署名・押印を拒むことができます。"),
    ],

    "sup_eyebrow": "Our support",
    "sup_h2":      "First72の対応",
    "sup_items": [
        ("通訳人の手配", "接見や打合せには、通訳人の手配に対応します。"),
        ("全国対応", "大阪を拠点に、全国の警察署・拘置所へ伺います（交通費・日当は別途、日程は調整のうえ）。"),
        ("母国語でのご連絡", "メールは母国語でお送りいただいてもかまいません。"),
        ("海外のご家族からのご相談", "日本国外にお住まいのご家族からのご相談も、メールで承ります。"),
        ("費用のお支払い", "ご依頼の前にお見積りをお示しし、海外送金でお支払いいただきます。"),
        ("ホテル・旅行会社の方へ", "宿泊されている方やツアー参加者が逮捕された場合のご連絡も承ります。"),
    ],

    "contact_eyebrow": "Contact",
    "contact_h2":      "まずはメールでご相談ください",
    "contact_lead":    "ご連絡はメールをおすすめします。お名前、逮捕された方との関係、逮捕された場所（警察署名）、帰国予定日、分かっている事情をお書きください。",
    "f_name": "お名前", "f_email": "メールアドレス", "f_phone": "電話番号（任意）",
    "f_msg": "ご相談内容", "f_submit": "送信する",
    "contact_note": "※ お急ぎの場合はお電話もご利用ください。逮捕直後は時間が結果を左右します。",

    "final_eyebrow": "訪日旅行者の刑事弁護",
    "final_h2":      "最初の72時間から。",
    "final_p":       "逮捕のご連絡は、時間との勝負です。まずはメールでご相談ください。",

    "lawyer":       "弁護士 岩佐 拳伍（大阪弁護士会所属）",
    "tel_domestic": "日本国内から",
    "main_site":    "First72 総合サイト（日本語）",
    "disclaimer":   "本ページは日本の刑事手続に関する一般的な情報の提供を目的とするもので、特定の結果を保証するものではありません。翻訳版と日本語版の内容に相違がある場合は、日本語版が優先します。",
},

# =============================================================
# English
# =============================================================
"en": {
    "meta_title": "Arrested While Traveling in Japan? Criminal Defense for Visitors | First72",
    "meta_desc":  "For foreign visitors arrested in Japan and their families: the timeline from arrest to trial, the impact on returning home and future visits, and common cases such as shoplifting, assault, cannabis, voyeurism and unlicensed driving. Interpreters can be arranged. Nationwide.",
    "sub":        "Criminal Defense for Visitors to Japan",
    "hdr_mail":   "Email",

    "tag":   "For visitors to Japan and their families",
    "h1":    "Arrested while traveling in Japan?<br>The <em>first 72 hours</em> matter most.",
    "lead":  "In Japan, a suspect can be held in custody for up to 23 days between arrest and the decision whether to prosecute. Will you make your flight home? Will you be able to visit Japan again? Involving a lawyer early can affect when you are released, how the case ends, and your future travel to Japan.",
    "cta_mail": "Contact us by email",
    "cta_tel":  "Call",
    "note":  "Interpreters can be arranged / Nationwide (travel costs separate; schedule by arrangement) / Fees are payable by international bank transfer",

    "tl_eyebrow": "Procedure",
    "tl_h2":      "From arrest to trial",
    "big1_u": "hours", "big1_label": "From arrest to the detention request",
    "big2_u": "days",  "big2_label": "Maximum from arrest to the charging decision",
    "tl_lead":    "After an arrest, the procedure moves forward under strict time limits. During the first 72 hours, family visits are often not allowed, which makes this a critical period in which a lawyer can meet the arrested person.",
    "steps": [
        ("Arrest", "Up to 48 hours",
         "The police question the arrested person and send the case to a public prosecutor. Family visits are often not allowed, but a lawyer can meet the person."),
        ("Referral and detention request", "Up to 24 hours",
         "The prosecutor decides whether continued custody is necessary and asks a judge to order detention. This is up to 72 hours in total from the arrest."),
        ("Detention", "10 days",
         "If the judge approves, the person is held, usually at a police station, for 10 days."),
        ("Extension", "Up to 10 more days",
         "If the investigation continues, detention may be extended by up to 10 days."),
        ("Charging decision", "Within 23 days of arrest",
         "The prosecutor decides whether to indict. If not indicted, the person is released. Some cases end with a fine through a summary procedure. If indicted, the case goes to trial and custody may continue."),
        ("Trial", "About 1–2 months after indictment",
         "The first hearing is held. Some cases take longer. The judgment determines the sentence, such as imprisonment or a fine, and whether it is suspended."),
    ],

    "cases_eyebrow": "Common cases",
    "cases_h2":      "Cases common among visitors",
    "cases_lead":    "Many cases involving visitors start because Japanese law differs from the law at home.",
    "cases": [
        ("Shoplifting and theft",
         "Shoplifting at drugstores and large discount stores is typical. Compensating the store and reaching a settlement can lead to non-prosecution or early release."),
        ("Assault and injury",
         "Fights after drinking in nightlife districts, for example. A settlement with the victim strongly affects the outcome."),
        ("Cannabis, THC products and other drugs",
         "Legal at home does not mean legal in Japan. CBD and other products containing THC can be punished, and since December 2024 using cannabis is also a crime. This includes bringing drugs through the airport for personal use. Drug cases have a particularly serious effect on future entry to Japan."),
        ("Voyeurism and groping",
         "Cases at stations, on trains and in shopping facilities. The Act on Punishment of Sexual Image Recording and prefectural nuisance ordinances apply."),
        ("Property damage and trespassing",
         "Graffiti, damage to shrines, temples or cultural properties, and entering restricted areas. Damage to cultural properties can be punished more severely."),
        ("Unlicensed driving and traffic accidents",
         "Depending on the type of international driving permit and the issuing country, you may not be allowed to drive in Japan, and driving becomes unlicensed driving. We also handle rental car accidents."),
        ("Carrying knives",
         "Carrying a knife with a blade longer than 6 cm without a legitimate reason violates the Firearms and Swords Control Act. Keep knives you have bought packed as sold while carrying them."),
    ],

    "can_eyebrow": "What we do",
    "can_h2":      "What a lawyer can do",
    "can_items": [
        ("Visits (sekken)", "We meet the arrested person at the police station or detention facility, explain the process, and advise on how to handle questioning. Interpreters can be arranged."),
        ("Appeal against detention (junkōkoku)", "We challenge the detention order and seek release."),
        ("Request to cancel detention", "If the grounds or need for detention no longer exist, we ask the court to cancel it."),
        ("Bail", "After indictment, we apply for release on bail. Japan has no bail before indictment."),
        ("Partial lifting of a no-contact order", "If visits or letters with family are prohibited, we ask the court to lift the ban in part."),
        ("Disclosure of detention grounds", "We ask the court to state the reasons for detention in open court. This can also give family a chance to see the arrested person."),
        ("Settlement negotiations", "In cases with a victim, we negotiate a settlement with the victim's side. A settlement strongly affects non-prosecution and early release."),
        ("Delivering items (sashiire)", "We can deliver clothing, books and daily necessities within the facility's rules. In some cases this is possible even when family cannot visit."),
    ],

    "need_eyebrow": "For release",
    "need_h2":      "What is needed for release or bail",
    "need_lead":    "Visitors often have no address or close contacts in Japan and are considered likely to leave the country, which can make release or bail harder to obtain. It is important to prepare the following early.",
    "need_items": [
        ("A place to stay (designated address)", "An address in Japan, such as a hotel, where the person will stay after release. Bail conditions specify where the person must stay."),
        ("Guarantor (mimoto hikiukenin)", "A person who supervises life after release and helps ensure attendance at court, such as a family member who can travel to Japan or an acquaintance living in Japan."),
        ("Passport kept by the lawyer", "As a bail condition, the lawyer may be asked to keep the passport to show the person will not leave Japan."),
        ("Period of stay and return flight", "If the short-term stay period expires during custody or while on bail, an immigration procedure is needed. We also consider changing the return flight early."),
    ],

    "imm_eyebrow": "Returning home",
    "imm_h2":      "Returning home and visiting Japan again",
    "imm_lead":    "For visitors, the outcome of a criminal case directly affects whether you can go home as planned and whether you can visit Japan in the future. Involving a lawyer early and looking for ways to end the case quickly is important.",
    "imm_list": [
        "If the short-term stay period expires during custody, an immigration procedure may be needed after release.",
        "While on bail, the passport is kept, so you cannot leave Japan until the trial ends.",
        "Non-prosecution leaves no criminal record. Some cases end by paying a fine through a summary procedure, but a fine is also a criminal record.",
        "Depending on the judgment, you may be refused entry to Japan in the future. A drug conviction has a particularly serious effect.",
    ],
    "imm_note": "The effect depends on the facts of the case and the judgment. Please consult us about your specific case.",

    "rights_eyebrow": "Your rights",
    "rights_h2":      "Rights after arrest",
    "rights_items": [
        ("Right to remain silent", "You do not have to say anything you do not wish to say during questioning."),
        ("Right to a lawyer", "You may appoint a lawyer. Regardless of nationality, a court-appointed lawyer is available in certain cases."),
        ("Interpretation", "If you do not understand Japanese, questioning and trial are conducted through an interpreter."),
        ("Consular notification", "You may ask that your country's consulate be informed of your arrest."),
        ("Right to refuse to sign", "You may refuse to sign or seal a written statement that is incorrect or that you do not understand."),
    ],

    "sup_eyebrow": "Our support",
    "sup_h2":      "How First72 supports you",
    "sup_items": [
        ("Interpreters", "Interpreters can be arranged for visits and meetings."),
        ("Nationwide", "Based in Osaka, we visit police stations and detention facilities across Japan (travel costs separate; schedule by arrangement)."),
        ("Your own language", "You may write to us by email in your own language."),
        ("Families abroad", "Families living outside Japan can also consult us by email."),
        ("Payment", "We provide a fee estimate before you engage us. Fees are payable by international bank transfer."),
        ("Hotels and travel agencies", "We also accept contact from hotels and travel agencies when a guest or tour member has been arrested."),
    ],

    "contact_eyebrow": "Contact",
    "contact_h2":      "Contact us by email first",
    "contact_lead":    "Email is the best way to reach us. Please include your name, your relationship to the arrested person, where they were arrested (the police station), the planned return date, and what you know so far.",
    "f_name": "Name", "f_email": "Email", "f_phone": "Phone (optional)",
    "f_msg": "Message", "f_submit": "Send",
    "contact_note": "If it is urgent, please also call us. Time matters in the first days after an arrest.",

    "final_eyebrow": "Criminal Defense for Visitors to Japan",
    "final_h2":      "From the first 72 hours.",
    "final_p":       "After an arrest, time is critical. Please contact us by email first.",

    "lawyer":       "Kengo Iwasa, Attorney at Law (Osaka Bar Association)",
    "tel_domestic": "from within Japan",
    "main_site":    "First72 main site (Japanese)",
    "disclaimer":   "This page provides general information about criminal procedure in Japan and does not guarantee any particular outcome. If the translated version differs from the Japanese version, the Japanese version prevails.",
},
}
