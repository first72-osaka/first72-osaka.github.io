# -*- coding: utf-8 -*-
"""
First72 外国籍の方向けページ 翻訳辞書
---------------------------------------------
言語を追加するときは FOREIGN に同じキー構成で1ブロック足す。
LANG_META に載っていても FOREIGN に無い言語は生成・表示されない。
"""

LANG_META = {
    "ja": {"label": "日本語",      "dir": "foreign", "html_lang": "ja"},
    "en": {"label": "English",     "dir": "en",      "html_lang": "en"},
    "zh": {"label": "简体中文",    "dir": "zh",      "html_lang": "zh-Hans"},
    "ko": {"label": "한국어",      "dir": "ko",      "html_lang": "ko"},
    "vi": {"label": "Tiếng Việt",  "dir": "vi",      "html_lang": "vi"},
}

FOREIGN = {
# =============================================================
# 日本語（マスター）
# =============================================================
"ja": {
    "meta_title": "外国籍の方の刑事事件・刑事弁護｜First72 ― 日本での逮捕・勾留に対応",
    "meta_desc":  "日本で逮捕された外国籍の方とご家族へ。逮捕から勾留・起訴までの流れ、保釈・勾留取消などの弁護活動、在留資格への影響を解説。通訳人の手配に対応。全国対応。",
    "sub":        "外国籍の方の刑事弁護",
    "hdr_mail":   "メール",

    "tag":   "外国籍の方・ご家族の方へ",
    "h1":    "日本で逮捕されたら、<br><em>最初の72時間</em>が重要です。",
    "lead":  "日本の刑事手続では、逮捕から起訴・不起訴の判断まで、最長23日間身柄を拘束されることがあります。言葉も制度も分からない中で、早い段階から弁護士が関わることが、釈放・処分・在留資格のすべてに影響します。",
    "cta_mail": "メールで相談する",
    "cta_tel":  "電話",
    "note":  "通訳人の手配に対応／全国対応（交通費・日当は別途、日程は調整のうえ）",

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
         "検察官が起訴するかどうかを決めます。不起訴になれば釈放されます。起訴されると裁判になり、身柄拘束が続くことがあります。"),
        ("裁判（公判）", "起訴から約1〜2か月",
         "第1回の裁判が開かれます。事件によっては、より長い期間がかかります。判決で刑罰（拘禁刑・罰金、執行猶予の有無など）が決まります。"),
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
        ("差入れ", "衣類・書籍・日用品などを、施設の規則の範囲内でお届けします。ご家族が面会できない場合も、弁護士を通じてお届けできることがあります。"),
    ],

    "need_eyebrow": "For release",
    "need_h2":      "釈放・保釈のために必要なこと",
    "need_lead":    "外国籍の方は、帰国や所在不明のおそれを理由に、釈放や保釈が認められにくい傾向があります。次の条件を早めに整えることが重要です。",
    "need_items": [
        ("身元引受人", "釈放後の生活を監督し、裁判への出頭を支える方です。日本に住むご家族・勤務先・知人などが考えられます。"),
        ("制限住居の確保", "釈放後に住む日本国内の住所です。保釈の条件として、住む場所が指定されます。"),
        ("パスポートの保管", "帰国しないことを示すため、保釈の条件としてパスポートを弁護人が預かることがあります。"),
        ("在留期間の管理", "身柄拘束中や保釈中に在留期限が来る場合は、更新の手続が必要です。期限が切れたまま釈放されると、入管の施設に収容されることがあります。"),
    ],

    "imm_eyebrow": "Residence status",
    "imm_h2":      "在留資格への影響にご注意ください",
    "imm_lead":    "刑事事件の結果によっては、在留資格を失い、退去強制（国外退去）の対象となることがあります。刑事手続と入管手続を分けずに考え、在留への影響を踏まえて弁護方針を立てることが重要です。",
    "imm_list": [
        "1年を超える拘禁刑の実刑判決を受けた場合",
        "薬物事件で有罪となった場合（執行猶予付きでも対象）",
        "在留資格の種類によっては、窃盗・詐欺などで有罪となった場合（執行猶予付きでも対象になりうる）",
    ],
    "imm_note": "※ 該当するかどうかは、罪名・判決内容・在留資格によって異なります。個別にご相談ください。",

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
    ],

    "contact_eyebrow": "Contact",
    "contact_h2":      "まずはメールでご相談ください",
    "contact_lead":    "ご連絡はメールをおすすめします。お名前、逮捕された方との関係、逮捕された場所（警察署名）、分かっている事情をお書きください。",
    "f_name": "お名前", "f_email": "メールアドレス", "f_phone": "電話番号（任意）",
    "f_msg": "ご相談内容", "f_submit": "送信する",
    "contact_note": "※ お急ぎの場合はお電話もご利用ください。逮捕直後は時間が結果を左右します。",

    "final_eyebrow": "外国籍の方の刑事弁護",
    "final_h2":      "最初の72時間から。",
    "final_p":       "逮捕のご連絡は、時間との勝負です。まずはメールでご相談ください。",

    "lawyer":       "弁護士 岩佐 拳伍（大阪弁護士会所属）",
    "tel_domestic": "日本国内から",
    "main_site":    "First72 総合サイト（日本語）",
    "disclaimer":   "本ページは刑事手続に関する一般的な情報の提供を目的とするもので、特定の結果を保証するものではありません。翻訳版と日本語版の内容に相違がある場合は、日本語版が優先します。",
},

# =============================================================
# English
# =============================================================
"en": {
    "meta_title": "Criminal Defense for Foreign Nationals in Japan | First72",
    "meta_desc":  "Arrested in Japan? Guidance for foreign nationals and their families: the timeline from arrest to trial, release and bail options, and the impact on your residence status. Interpreters can be arranged. Nationwide.",
    "sub":        "Criminal Defense in Japan",
    "hdr_mail":   "Email",

    "tag":   "For foreign nationals and their families",
    "h1":    "Arrested in Japan?<br>The <em>first 72 hours</em> matter most.",
    "lead":  "In Japan, a suspect can be held in custody for up to 23 days between arrest and the decision whether to prosecute. When the language and the system are unfamiliar, involving a lawyer early can affect release, the outcome of the case, and your residence status.",
    "cta_mail": "Contact us by email",
    "cta_tel":  "Call",
    "note":  "Interpreters can be arranged / Nationwide (travel costs separate; schedule by arrangement)",

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
        ("Indictment or release", "Within 23 days of arrest",
         "The prosecutor decides whether to indict. If not indicted, the person is released. If indicted, the case goes to trial and custody may continue."),
        ("Trial", "About 1–2 months after indictment",
         "The first hearing is held. Some cases take longer. The judgment determines the sentence, such as imprisonment or a fine, and whether it is suspended."),
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
        ("Delivering items (sashiire)", "We can deliver clothing, books and daily necessities within the facility's rules. In some cases this is possible even when family cannot visit."),
    ],

    "need_eyebrow": "For release",
    "need_h2":      "What is needed for release or bail",
    "need_lead":    "Foreign nationals are often considered a flight risk, which can make release or bail harder to obtain. It is important to prepare the following early.",
    "need_items": [
        ("Guarantor (mimoto hikiukenin)", "A person who supervises life after release and helps ensure attendance at court, such as family, an employer or a friend living in Japan."),
        ("A fixed address in Japan", "Bail conditions require the person to live at a designated address in Japan."),
        ("Passport kept by the lawyer", "As a bail condition, the lawyer may be asked to keep the passport to show the person will not leave Japan."),
        ("Managing the period of stay", "If the period of stay expires during custody or while on bail, it must be renewed. A person released with an expired status may be transferred to an immigration detention facility."),
    ],

    "imm_eyebrow": "Residence status",
    "imm_h2":      "A criminal case can affect your visa",
    "imm_lead":    "Depending on the outcome, a person may lose their residence status and face deportation. Defense strategy should take immigration consequences into account from the start, rather than treating the criminal case and immigration separately.",
    "imm_list": [
        "An unsuspended prison sentence of more than one year",
        "A conviction for a drug offense (even with a suspended sentence)",
        "For certain types of residence status, a conviction for theft, fraud or similar offenses (possibly even with a suspended sentence)",
    ],
    "imm_note": "Whether this applies depends on the offense, the judgment and the residence status. Please consult us about your specific case.",

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
    ],

    "contact_eyebrow": "Contact",
    "contact_h2":      "Contact us by email first",
    "contact_lead":    "Email is the best way to reach us. Please include your name, your relationship to the arrested person, where they were arrested (the police station), and what you know so far.",
    "f_name": "Name", "f_email": "Email", "f_phone": "Phone (optional)",
    "f_msg": "Message", "f_submit": "Send",
    "contact_note": "If it is urgent, please also call us. Time matters in the first days after an arrest.",

    "final_eyebrow": "Criminal Defense in Japan",
    "final_h2":      "From the first 72 hours.",
    "final_p":       "After an arrest, time is critical. Please contact us by email first.",

    "lawyer":       "Kengo Iwasa, Attorney at Law (Osaka Bar Association)",
    "tel_domestic": "from within Japan",
    "main_site":    "First72 main site (Japanese)",
    "disclaimer":   "This page provides general information about criminal procedure in Japan and does not guarantee any particular outcome. If the translated version differs from the Japanese version, the Japanese version prevails.",
},
}
