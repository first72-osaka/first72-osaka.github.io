#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
First72 サイトビルダー
---------------------------------------------
共通のヘッダー・フッター・CSS・連絡先を1か所で管理し、
各ページの本文を流し込んで HTML を生成する。

使い方:
    python3 build.py
出力:
    ./index.html
    ./crimes/chikan.html
"""

import os

# =============================================================
# サイト共通設定（変更はここだけ）
# =============================================================
SITE = {
    "brand":        "First72",
    "tagline":      "大阪の刑事弁護",
    "catch":        "最初の72時間から",
    "base_url":     "https://first72-osaka.github.io",
    "benfit_url":   "https://benfit-osaka.github.io",

    # 連絡先（法人名・住所・代表番号は掲載しない方針）
    "lawyer":       "岩佐 拳伍",
    "lawyer_kana":  "いわさ けんご",
    "bar":          "大阪弁護士会所属",
    "tel":          "06-6202-8789",
    "tel_link":     "0662028789",
    "tel_note":     "直通",
    "email":        "kengo-iwasa@yglpc.com",
    "line_url":     "https://works.do/GkiX4R8",
    "form_action":  "https://formspree.io/f/xrepwjpg",
    "form_subject": "【First72】お問い合わせがありました",

    "year":         "2026",
}

# =============================================================
# デザイントークン
# =============================================================
CSS = """
:root{
  --navy:#0E2A47; --navy-deep:#0A2038; --paper:#F7F8FA; --white:#fff;
  --ink:#1A1A1A; --slate:#5A6672; --line:#E2E6EC;
  --amber:#E8892B; --amber-dark:#CE7620; --amber-ink:#14213A;
  --maxw:1080px;
}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{margin:0;font-family:"Noto Sans JP",system-ui,sans-serif;color:var(--ink);
  background:var(--paper);line-height:1.85;font-size:16px;-webkit-font-smoothing:antialiased;padding-bottom:72px;}
a{color:inherit;}
img{max-width:100%;}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 20px;}
.eyebrow{font-family:"Barlow Condensed",sans-serif;text-transform:uppercase;letter-spacing:.14em;
  font-weight:600;font-size:.82rem;color:var(--amber);}
h2{font-size:1.5rem;line-height:1.5;font-weight:700;margin:.4em 0 .8em;}
@media(min-width:720px){h2{font-size:1.9rem;}}
h3{font-size:1.12rem;font-weight:700;margin:1.6em 0 .5em;}

/* header */
.hdr{position:sticky;top:0;z-index:50;background:rgba(14,42,71,.96);
  backdrop-filter:saturate(140%) blur(6px);border-bottom:1px solid rgba(255,255,255,.08);}
.hdr-in{display:flex;align-items:center;justify-content:space-between;height:60px;}
.brand{display:flex;align-items:baseline;gap:.5em;color:#fff;text-decoration:none;}
.brand .mark{font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:1.5rem;}
.brand .mark b{color:var(--amber);}
.brand .sub{font-size:.72rem;color:#B9C6D6;letter-spacing:.04em;}
@media(max-width:520px){.brand .sub{display:none;}}
.hdr-call{font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:1.05rem;color:#fff;
  text-decoration:none;display:flex;align-items:center;gap:.4em;}
.hdr-call svg{width:18px;height:18px;fill:var(--amber);}

/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.5em;font-weight:700;
  text-decoration:none;border-radius:10px;padding:15px 22px;font-size:1.02rem;line-height:1.2;
  transition:transform .12s ease,background .12s ease;border:none;cursor:pointer;font-family:inherit;}
.btn svg{width:20px;height:20px;flex:none;}
.btn-call{background:var(--amber);color:var(--amber-ink);box-shadow:0 6px 18px rgba(232,137,43,.32);}
.btn-call svg{fill:var(--amber-ink);}
.btn-call:hover{background:var(--amber-dark);transform:translateY(-1px);}
.btn-line{background:#06C755;color:#fff;} .btn-line svg{fill:#fff;}
.btn-line:hover{transform:translateY(-1px);}
.btn-ghost{background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,.4);}
.btn-ghost:hover{border-color:#fff;}

/* hero */
.hero{background:var(--navy);color:#fff;padding:54px 0 46px;}
.hero .tag{display:inline-block;font-size:.8rem;color:#B9C6D6;border:1px solid rgba(255,255,255,.2);
  border-radius:999px;padding:5px 13px;margin-bottom:20px;}
.hero h1{font-size:1.72rem;line-height:1.5;font-weight:700;margin:0 0 16px;}
.hero h1 em{font-style:normal;color:var(--amber);}
@media(min-width:720px){.hero h1{font-size:2.5rem;line-height:1.45;}}
.hero p.lead{color:#D5DEE8;font-size:1.05rem;margin:0 0 26px;max-width:34em;}
.hero-cta{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:14px;}
.hero-note{font-size:.82rem;color:#9DB0C4;}

/* 72h rail */
.clock{background:var(--navy-deep);color:#fff;padding:40px 0 48px;border-top:1px solid rgba(255,255,255,.06);}
.clock h2{color:#fff;}
.clock .big{font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:5.2rem;line-height:.9;color:#fff;}
.clock .big span{color:var(--amber);}
.clock .cap{color:#B9C6D6;font-size:.95rem;max-width:38em;margin:.2em 0 30px;}
.rail{display:grid;gap:18px;}
@media(min-width:760px){.rail{grid-template-columns:repeat(3,1fr);gap:22px;}}
.step{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:18px;}
.step .t{font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:1.15rem;color:var(--amber);letter-spacing:.05em;}
.step .h{font-weight:700;font-size:1.02rem;margin:4px 0 6px;}
.step .d{font-size:.9rem;color:#C6D2DF;line-height:1.7;}
.step.key{border-color:rgba(232,137,43,.55);background:rgba(232,137,43,.08);}

/* sections */
.sec{padding:52px 0;}
.sec-alt{background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line);}
.lead-txt{font-size:1.05rem;max-width:40em;}
.cap-note{font-size:.8rem;color:var(--slate);margin-top:14px;}

/* crime grid */
.crimes{display:grid;gap:14px;margin-top:6px;}
@media(min-width:720px){.crimes{grid-template-columns:repeat(2,1fr);}}
.crime{display:block;background:var(--white);border:1px solid var(--line);border-radius:12px;
  padding:20px;text-decoration:none;transition:transform .12s ease,box-shadow .12s ease;}
.crime:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(14,42,71,.09);}
.crime b{display:block;font-size:1.08rem;margin-bottom:4px;}
.crime span{font-size:.9rem;color:var(--slate);}
.crime .go{color:var(--amber);font-weight:700;font-size:.88rem;margin-top:10px;display:inline-block;}
.crime.soon{opacity:.55;pointer-events:none;}

/* summary cards */
.cards{display:grid;gap:20px;margin-top:8px;}
@media(min-width:760px){.cards{grid-template-columns:1fr 1fr;}}
.card{background:var(--white);border:1px solid var(--line);border-radius:14px;overflow:hidden;
  box-shadow:0 8px 24px rgba(14,42,71,.05);}
.card h3{margin:0;padding:16px 20px;font-size:1.02rem;background:var(--navy);color:#fff;font-weight:700;}
.card h3.alt{background:#3B4A5E;}
.rows{padding:6px 20px 4px;}
.row{display:flex;justify-content:space-between;gap:14px;padding:9px 0;border-bottom:1px solid var(--line);font-size:.95rem;}
.row:last-child{border-bottom:none;}
.row .k{color:var(--slate);} .row .v{font-weight:700;text-align:right;}
.row .v.good{color:#1E7A46;} .row .v.warn{color:#C0392B;}
.card .foot{display:flex;gap:.5em;align-items:flex-start;background:var(--navy);color:#fff;
  padding:13px 20px;font-size:.9rem;font-weight:700;}
.card .foot::before{content:"\\25B6";color:var(--amber);}
.card .foot.alt{background:#3B4A5E;}

/* stats */
.stats{display:grid;gap:18px;margin-top:10px;}
@media(min-width:720px){.stats{grid-template-columns:repeat(3,1fr);}}
.stat{background:var(--white);border:1px solid var(--line);border-radius:12px;padding:20px;}
.stat .n{font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:2.6rem;line-height:1;color:var(--navy);}
.stat .n small{font-size:1.1rem;color:var(--amber);margin-left:.1em;}
.stat .l{font-size:.9rem;color:var(--slate);margin-top:6px;line-height:1.6;}

/* accent block */
.accent{border-left:4px solid var(--amber);padding-left:18px;font-weight:500;}

/* do list */
ul.do{display:grid;gap:14px;margin-top:6px;padding:0;}
@media(min-width:720px){ul.do{grid-template-columns:1fr 1fr;}}
ul.do li{list-style:none;display:flex;gap:12px;background:var(--white);border:1px solid var(--line);
  border-radius:12px;padding:16px 18px;}
ul.do li svg{width:22px;height:22px;fill:var(--amber);flex:none;margin-top:2px;}
ul.do li b{display:block;margin-bottom:2px;}
ul.do li span{font-size:.92rem;color:var(--slate);}

.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px;}
.chip{background:var(--white);border:1px solid var(--line);border-radius:999px;padding:8px 16px;font-size:.9rem;}

/* cases */
.cases{display:grid;gap:16px;margin-top:6px;}
@media(min-width:760px){.cases{grid-template-columns:1fr 1fr;}}
.case{background:var(--white);border:1px solid var(--line);border-radius:12px;padding:20px;}
.case .badge{display:inline-block;font-size:.78rem;font-weight:700;color:#1E7A46;background:#E7F3EC;
  border-radius:6px;padding:3px 10px;margin-bottom:10px;}
.case p{margin:0;font-size:.93rem;color:#33404F;}

/* table */
.fee-tbl{width:100%;border-collapse:collapse;margin-top:6px;background:var(--white);
  border:1px solid var(--line);border-radius:12px;overflow:hidden;}
.fee-tbl th,.fee-tbl td{text-align:left;padding:14px 18px;border-bottom:1px solid var(--line);font-size:.95rem;}
.fee-tbl th{background:var(--navy);color:#fff;font-weight:700;}
.fee-tbl tr:last-child td{border-bottom:none;}
.fee-tbl td.amt{font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:1.15rem;}

/* faq */
.faq{max-width:760px;}
.qa{background:var(--white);border:1px solid var(--line);border-radius:12px;margin-top:12px;overflow:hidden;}
.qa button{width:100%;text-align:left;background:none;border:none;cursor:pointer;font-family:inherit;
  font-size:1rem;font-weight:700;color:var(--ink);padding:16px 18px;display:flex;justify-content:space-between;
  align-items:center;gap:14px;line-height:1.6;border-radius:0;}
.qa button .ic{flex:none;width:22px;height:22px;border-radius:50%;background:var(--navy);color:#fff;
  display:grid;place-items:center;transition:transform .2s ease;font-size:1rem;}
.qa.open button .ic{transform:rotate(45deg);background:var(--amber);color:var(--amber-ink);}
.qa .ans{max-height:0;overflow:hidden;transition:max-height .28s ease;}
.qa .ans p{margin:0;padding:0 18px 18px;color:#33404F;font-size:.94rem;}

/* contact form */
.form{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:24px;max-width:640px;margin-top:18px;}
.fg{margin-bottom:16px;}
.fg label{display:block;font-size:.9rem;font-weight:700;margin-bottom:6px;}
.fg .req{color:var(--amber);margin-left:.3em;}
.fg input,.fg textarea{width:100%;padding:12px 14px;border:1px solid var(--line);border-radius:8px;
  font-family:inherit;font-size:1rem;background:var(--paper);}
.fg textarea{min-height:130px;resize:vertical;}

/* final */
.final{background:var(--navy);color:#fff;padding:56px 0;text-align:center;}
.final h2{color:#fff;font-size:1.8rem;}
@media(min-width:720px){.final h2{font-size:2.3rem;}}
.final p{color:#C6D2DF;max-width:32em;margin:0 auto 26px;}
.final .hero-cta{justify-content:center;}

/* footer */
footer{background:var(--navy-deep);color:#9DB0C4;padding:34px 0 40px;font-size:.84rem;line-height:1.85;}
footer .brand{margin-bottom:10px;display:inline-flex;}
footer .brand .mark{font-size:1.25rem;}
footer .brand .sub{display:inline;}
footer strong{color:#D5DEE8;}
footer a.x{color:#B9C6D6;}
footer .disc{margin-top:16px;border-top:1px solid rgba(255,255,255,.1);padding-top:16px;
  font-size:.78rem;color:#7E90A4;}

/* sticky */
.sticky{position:fixed;left:0;right:0;bottom:0;z-index:60;display:grid;grid-template-columns:1fr 1fr;
  gap:10px;background:rgba(14,42,71,.98);padding:10px 12px;border-top:1px solid rgba(255,255,255,.1);}
.sticky .btn{padding:13px 10px;font-size:.98rem;}
@media(min-width:820px){.sticky{display:none;} body{padding-bottom:0;}}

:focus-visible{outline:3px solid var(--amber);outline-offset:2px;border-radius:4px;}
@media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important;}}
"""

# =============================================================
# 部品
# =============================================================
ICON_TEL = ('<svg viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 '
            '1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 '
            '0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.4 0 .8-.2 1l-2.3 2.2z"/></svg>')
ICON_LINE = ('<svg viewBox="0 0 24 24"><path d="M12 3C6.5 3 2 6.6 2 11c0 4 3.6 7.3 8.5 7.9.3.1.8.2.9.5.1.3.1.7 '
             '0 1l-.1.9c-.1.3-.3 1.1 1 .6 1.3-.5 6.9-4.1 9.4-7C23.2 13.2 24 12 24 11c0-4.4-4.5-8-12-8z"/></svg>')
ICON_CHECK = '<svg viewBox="0 0 24 24"><path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg>'


def cta_pair(ghost=False, prefix=""):
    """電話＋LINE のボタン対"""
    line_cls = "btn-ghost" if ghost else "btn-line"
    line_icon = "" if ghost else ICON_LINE
    return f"""<div class="hero-cta">
      <a class="btn btn-call" href="tel:{SITE['tel_link']}">{ICON_TEL}今すぐ電話（24時間受付）</a>
      <a class="btn {line_cls}" href="{SITE['line_url']}" target="_blank" rel="noopener">{line_icon}LINEで相談</a>
    </div>"""


def header(prefix=""):
    return f"""<header class="hdr"><div class="wrap hdr-in">
  <a class="brand" href="{prefix}index.html">
    <span class="mark">First<b>72</b></span><span class="sub">{SITE['tagline']}</span>
  </a>
  <a class="hdr-call" href="tel:{SITE['tel_link']}">{ICON_TEL}今すぐ電話</a>
</div></header>"""


def footer(prefix=""):
    return f"""<footer><div class="wrap">
  <a class="brand" href="{prefix}index.html">
    <span class="mark">First<b>72</b></span><span class="sub">{SITE['tagline']}</span>
  </a>
  <div><strong>弁護士 {SITE['lawyer']}（{SITE['lawyer_kana']}）</strong>／{SITE['bar']}</div>
  <div>TEL {SITE['tel']}（{SITE['tel_note']}）／MAIL <a class="x" href="mailto:{SITE['email']}">{SITE['email']}</a></div>
  <div style="margin-top:10px;">同じ弁護士が運営するフィットネス業界向け法務サイト
    <a class="x" href="{SITE['benfit_url']}" target="_blank" rel="noopener"><strong>BenFit</strong></a></div>
  <div class="disc">
    本サイトは刑事弁護に関する一般的な情報を提供するものであり、特定の結果を保証するものではありません。
    掲載の統計は「地方公共団体条例違反」等を母集団とする参考値を含み、痴漢のみの数値ではありません
    （出典：令和6年版犯罪白書、検察統計）。個別事案の見通しは弁護士へ直接ご相談ください。<br>
    &copy; {SITE['year']} {SITE['brand']}
  </div>
</div></footer>"""


def sticky():
    return f"""<div class="sticky">
  <a class="btn btn-call" href="tel:{SITE['tel_link']}">{ICON_TEL}今すぐ電話</a>
  <a class="btn btn-line" href="{SITE['line_url']}" target="_blank" rel="noopener">{ICON_LINE}LINE相談</a>
</div>"""


SCRIPT = """<script>
document.querySelectorAll('.qa button').forEach(function(b){
  b.addEventListener('click',function(){
    var qa=b.closest('.qa'), ans=qa.querySelector('.ans');
    var open=qa.classList.toggle('open');
    b.setAttribute('aria-expanded',open?'true':'false');
    ans.style.maxHeight=open?(ans.scrollHeight+'px'):'0px';
  });
});
</script>"""


def page(title, description, body, prefix="", canonical=""):
    """共通シェルに本文を流し込んで完成HTMLを返す"""
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE['base_url']}/{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{header(prefix)}
{body}
{footer(prefix)}
{sticky()}
{SCRIPT}
</body>
</html>"""


# =============================================================
# 共通セクション
# =============================================================
def clock_section():
    return f"""<section class="clock"><div class="wrap">
  <span class="eyebrow">The first 72 hours</span>
  <div class="big"><span>72</span>時間</div>
  <p class="cap">逮捕から、勾留するかどうかを検察官・裁判官が判断するまでが、およそ72時間。
    この間は家族でも面会できず、<strong style="color:#fff">弁護士だけが本人に会えます。</strong>
    ここでどれだけ早く動けるかが、示談と不起訴の可能性を大きく左右します。</p>
  <div class="rail">
    <div class="step"><div class="t">0 — 48h</div><div class="h">逮捕・警察の捜査</div>
      <div class="d">本人は外部と連絡できず、ご家族は状況をつかめません。弁護士は即日接見が可能です。</div></div>
    <div class="step key"><div class="t">〜 72h</div><div class="h">勾留するかの判断（分岐点）</div>
      <div class="d">検察官の勾留請求、裁判官の勾留質問。弁護士が勾留阻止・準抗告に動けば、勾留されず釈放となる例もあります。</div></div>
    <div class="step"><div class="t">72h 〜</div><div class="h">起訴／不起訴へ</div>
      <div class="d">示談が成立すれば起訴猶予（不起訴）の可能性が高まります。不起訴なら前科はつきません。</div></div>
  </div>
</div></section>"""


def contact_section():
    return f"""<section class="sec sec-alt" id="contact"><div class="wrap">
  <span class="eyebrow">お問い合わせ</span>
  <h2>まずはご相談ください</h2>
  <p class="lead-txt">お電話・LINE・フォームのいずれでも承ります。ご家族からのご相談も可能です。</p>
  {cta_pair()}
  <form class="form" action="{SITE['form_action']}" method="POST">
    <input type="hidden" name="_subject" value="{SITE['form_subject']}">
    <div class="fg"><label for="name">お名前<span class="req">*</span></label>
      <input type="text" id="name" name="name" required></div>
    <div class="fg"><label for="email">メールアドレス<span class="req">*</span></label>
      <input type="email" id="email" name="email" required></div>
    <div class="fg"><label for="phone">電話番号（任意）</label>
      <input type="tel" id="phone" name="phone"></div>
    <div class="fg"><label for="message">ご相談内容<span class="req">*</span></label>
      <textarea id="message" name="message" required></textarea></div>
    <button type="submit" class="btn btn-call">送信する</button>
  </form>
  <p class="cap-note">※ お急ぎの場合はお電話ください。逮捕直後は時間が結果を左右します。</p>
</div></section>"""


def final_cta():
    return f"""<section class="final"><div class="wrap">
  <span class="eyebrow">{SITE['tagline']}</span>
  <h2>{SITE['catch']}。</h2>
  <p>逮捕・呼び出しのご連絡は、時間との勝負です。24時間受付。まずはお電話ください。</p>
  {cta_pair(ghost=True)}
</div></section>"""


# =============================================================
# トップページ
# =============================================================
def build_index():
    body = f"""<section class="hero" id="top"><div class="wrap">
  <span class="tag">大阪の刑事事件・刑事弁護</span>
  <h1>逮捕・呼び出しなら、<br><em>最初の72時間</em>で動きます。</h1>
  <p class="lead">示談交渉に強い弁護士が、前科を回避するために最短で動く。
    大阪地裁・大阪拘置所・府内各警察署へ即日接見します。</p>
  {cta_pair()}
  <p class="hero-note">弁護士 {SITE['lawyer']}（{SITE['bar']}）／ご家族からのご相談も承ります</p>
</div></section>

{clock_section()}

<section class="sec"><div class="wrap">
  <span class="eyebrow">取扱い事件</span>
  <h2>犯罪類型ごとの見通しと量刑相場</h2>
  <p class="lead-txt">事件の種類によって、身柄拘束の見通しも、不起訴を取るための道筋も変わります。
    統計と実務に基づいた見通しを、類型ごとに整理しています。</p>
  <div class="crimes">
    <a class="crime" href="crimes/chikan.html">
      <b>痴漢（大阪府迷惑防止条例）</b>
      <span>初犯・示談成立なら不起訴の可能性。示談の早さが結果を分けます。</span>
      <span class="go">量刑相場を見る →</span>
    </a>
    <div class="crime soon"><b>不同意わいせつ・不同意性交等</b>
      <span>準備中</span></div>
    <div class="crime soon"><b>薬物事件（覚醒剤・大麻）</b>
      <span>準備中</span></div>
    <div class="crime soon"><b>窃盗・万引き</b>
      <span>準備中</span></div>
    <div class="crime soon"><b>暴行・傷害</b>
      <span>準備中</span></div>
    <div class="crime soon"><b>詐欺</b>
      <span>準備中</span></div>
  </div>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <span class="eyebrow">First72 ができること</span>
  <h2>逮捕直後から、やるべきことを同時に進めます</h2>
  <ul class="do">
    <li>{ICON_CHECK}<div><b>即日接見・身柄解放</b><span>逮捕直後の接見、勾留阻止・準抗告で早期釈放を目指します。</span></div></li>
    <li>{ICON_CHECK}<div><b>被害者との示談交渉</b><span>本人・ご家族では着手が難しい交渉を、弁護士が代理します。</span></div></li>
    <li>{ICON_CHECK}<div><b>不起訴に向けた働きかけ</b><span>検察官への意見書提出など、処分に向けた活動を行います。</span></div></li>
    <li>{ICON_CHECK}<div><b>起訴後の情状弁護</b><span>再犯防止策の構築を含め、量刑を軽くするための弁護を行います。</span></div></li>
  </ul>
</div></section>

<section class="sec"><div class="wrap">
  <span class="eyebrow">大阪に特化</span>
  <h2>大阪の刑事事件に、地元で対応します</h2>
  <p class="lead-txt">大阪府迷惑防止条例をはじめ、大阪で発生した刑事事件に対応します。
    逮捕の一報を受けたら、即日で接見に向かいます。</p>
  <div class="chips">
    <span class="chip">大阪地方裁判所</span><span class="chip">大阪拘置所</span>
    <span class="chip">府内各警察署へ即日接見</span><span class="chip">大阪弁護士会所属</span>
  </div>
</div></section>

{contact_section()}
{final_cta()}"""
    return page(
        title="大阪の刑事事件・刑事弁護｜First72 ― 最初の72時間から",
        description="大阪の刑事弁護。示談交渉に強い弁護士が、逮捕直後から前科回避のために動きます。犯罪類型ごとの量刑相場を掲載。24時間受付・即日接見。",
        body=body, prefix="", canonical="index.html")


# =============================================================
# 痴漢ページ
# =============================================================
def build_chikan():
    body = f"""<section class="hero" id="top"><div class="wrap">
  <span class="tag">大阪府迷惑防止条例｜痴漢事件</span>
  <h1>大阪で痴漢事件。<br>逮捕・呼び出しなら、<em>最初の72時間</em>で動きます。</h1>
  <p class="lead">示談交渉に強い弁護士が、前科を回避するために最短で動く。
    大阪地裁・大阪拘置所・府内各警察署へ即日接見します。</p>
  {cta_pair()}
  <p class="hero-note">弁護士 {SITE['lawyer']}（{SITE['bar']}）／ご家族からのご相談も承ります</p>
</div></section>

{clock_section()}

<section class="sec sec-alt"><div class="wrap">
  <span class="eyebrow">こんな状況ではありませんか</span>
  <h2>「家族が痴漢で逮捕された」<br>「後日、警察から呼び出しの連絡が来た」</h2>
  <p class="lead-txt">今いちばん大事なのは時間です。逮捕された直後も、後日呼び出しの在宅事件でも、
    起訴・不起訴が決まる前の初動が結果を左右します。特に示談は、着手が早いほど成立しやすくなります。</p>
</div></section>

<section class="sec"><div class="wrap">
  <span class="eyebrow">量刑の見通し</span>
  <h2>痴漢事件の相場と見通し</h2>
  <div class="cards">
    <div class="card">
      <h3>痴漢（大阪府迷惑防止条例）｜初犯</h3>
      <div class="rows">
        <div class="row"><span class="k">逮捕される可能性</span><span class="v">中（現行犯が多い）</span></div>
        <div class="row"><span class="k">勾留される可能性</span><span class="v">低〜中</span></div>
        <div class="row"><span class="k">不起訴の可能性</span><span class="v good">高 ※示談成立が条件</span></div>
        <div class="row"><span class="k">起訴された場合</span><span class="v">略式罰金が中心</span></div>
        <div class="row"><span class="k">量刑（法定刑）</span><span class="v">6月以下の拘禁刑<br>又は50万円以下の罰金</span></div>
        <div class="row"><span class="k">前科がつくか</span><span class="v good">不起訴なら前科なし</span></div>
      </div>
      <div class="foot">結果を分ける最大要因：示談の成否と早さ（相場10〜50万円）</div>
    </div>
    <div class="card">
      <h3 class="alt">痴漢（大阪府迷惑防止条例）｜前科あり・常習</h3>
      <div class="rows">
        <div class="row"><span class="k">逮捕・勾留の可能性</span><span class="v warn">高</span></div>
        <div class="row"><span class="k">不起訴の可能性</span><span class="v">低〜中（示談でも起訴されうる）</span></div>
        <div class="row"><span class="k">起訴された場合</span><span class="v">公判請求が増える</span></div>
        <div class="row"><span class="k">量刑（法定刑）</span><span class="v">常習は1年以下の拘禁刑<br>又は100万円以下の罰金</span></div>
        <div class="row"><span class="k">争点</span><span class="v">執行猶予か、実刑か</span></div>
      </div>
      <div class="foot alt">前科累積・執行猶予中の犯行では実刑リスク。示談＋再犯防止策が鍵</div>
    </div>
  </div>

  <div class="stats">
    <div class="stat"><div class="n">52.1<small>%</small></div>
      <div class="l">地方公共団体条例違反（痴漢を含む）の起訴率。裏返せば約半数は不起訴で終わっています。</div></div>
    <div class="stat"><div class="n">33.7<small>%</small></div>
      <div class="l">不同意わいせつ（下着の中に手を入れる等）の起訴率。罰金刑がなく、起訴されれば公判です。</div></div>
    <div class="stat"><div class="n">10–50<small>万円</small></div>
      <div class="l">痴漢事件の示談金の一般的な相場。事案により100万円規模となることもあります。</div></div>
  </div>
  <p class="cap-note">※ 痴漢のみを抽出した統計は公表されていません。上記は「地方公共団体条例違反」等を母集団とする
    参考値で、盗撮・つきまとい等も含みます（出典：令和6年版犯罪白書＝令和5年、検察統計）。
    初犯かつ示談が成立した場合の不起訴率はこれより高くなる傾向がありますが、個別事案で結果は異なります。</p>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <span class="eyebrow">適用される法律</span>
  <h2>痴漢はどの法律で処罰されるのか</h2>
  <p class="lead-txt">衣服の上から触れるなどの行為は<strong>大阪府迷惑防止条例</strong>
    （正式名称：大阪府公衆に著しく迷惑をかける暴力的不良行為等の防止に関する条例）違反となり、
    下着の中に手を入れるなど悪質性が高い行為は<strong>刑法の不同意わいせつ罪</strong>が適用され、
    法定刑も量刑相場も大きく重くなります。</p>
  <ul class="do">
    <li>{ICON_CHECK}<div><b>大阪府迷惑防止条例違反</b><span>6月以下の拘禁刑又は50万円以下の罰金／常習は1年以下の拘禁刑又は100万円以下の罰金</span></div></li>
    <li>{ICON_CHECK}<div><b>不同意わいせつ罪（刑法176条）</b><span>6月以上10年以下の拘禁刑。罰金刑がなく、起訴されれば正式裁判です。</span></div></li>
  </ul>
  <p class="cap-note">※ 2025年6月1日施行の改正刑法により、従来の「懲役・禁錮」は「拘禁刑」に一本化されました。</p>
</div></section>

<section class="sec"><div class="wrap">
  <span class="eyebrow">前科を避ける鍵</span>
  <h2>痴漢事件は、示談で結果が決まります</h2>
  <p class="lead-txt">痴漢で前科を避けられるかは、被害者との示談が成立するかにほぼかかっています。
    検察官は被害感情が示談で収まっているかを重視するため、示談が成立すれば起訴猶予（不起訴）となる
    可能性が高まります。不起訴なら前科はつきません。</p>
  <p class="lead-txt accent">ただし被害者は加害者側との直接接触を拒むのが通常で、示談は弁護士が入らなければ
    着手すら困難です。しかも起訴・不起訴が決まる前の限られた期間内にまとめる必要があります。
    だから「誰が」「どれだけ早く」入るかが、そのまま結果を分けます。</p>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <span class="eyebrow">First72 ができること</span>
  <h2>逮捕直後から、やるべきことを同時に進めます</h2>
  <ul class="do">
    <li>{ICON_CHECK}<div><b>即日接見・身柄解放</b><span>逮捕直後の接見、勾留阻止・準抗告で早期釈放を目指します。</span></div></li>
    <li>{ICON_CHECK}<div><b>被害者との示談交渉</b><span>本人・ご家族では着手が難しい交渉を、弁護士が代理します。</span></div></li>
    <li>{ICON_CHECK}<div><b>不起訴に向けた働きかけ</b><span>検察官への意見書提出など、処分に向けた活動を行います。</span></div></li>
    <li>{ICON_CHECK}<div><b>起訴後の情状弁護</b><span>再犯防止策の構築を含め、量刑を軽くするための弁護を行います。</span></div></li>
  </ul>
</div></section>

<section class="sec"><div class="wrap">
  <span class="eyebrow">解決事例</span>
  <h2>解決事例</h2>
  <div class="cases">
    <div class="case"><span class="badge">不起訴・前科回避</span>
      <p>〔会社員・初犯。受任当日に示談交渉に着手し、勾留請求が却下されて早期釈放。その後示談が成立し、
        不起訴で前科を回避した事例 ― 実際の事例に差し替え〕</p></div>
    <div class="case"><span class="badge">早期釈放</span>
      <p>〔後日呼び出しの在宅事件。示談成立により略式罰金にとどめ、公判を回避した事例 ― 実際の事例に差し替え〕</p></div>
  </div>
  <p class="cap-note">※ 守秘義務およびプライバシー保護のため、内容は特定を避けて記載しています。
    結果を保証するものではありません。</p>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <span class="eyebrow">費用</span>
  <h2>明朗な料金体系</h2>
  <table class="fee-tbl">
    <tr><th>項目</th><th>費用（税込）</th></tr>
    <tr><td>初回相談</td><td class="amt">〔無料 ※要件〕</td></tr>
    <tr><td>着手金（起訴前弁護）</td><td class="amt">〔◯◯万円〜〕</td></tr>
    <tr><td>報酬金（不起訴・示談成立）</td><td class="amt">〔◯◯万円〜〕</td></tr>
    <tr><td>接見のみのご依頼</td><td class="amt">〔◯万円〜〕</td></tr>
  </table>
  <p class="cap-note">※ 事案により費用は異なります。ご依頼前に総額の見積りを明示します。</p>
</div></section>

<section class="sec"><div class="wrap faq">
  <span class="eyebrow">よくある質問</span>
  <h2>よくある質問</h2>
  <div class="qa"><button aria-expanded="false"><span>会社や家族に知られますか？</span><span class="ic">+</span></button>
    <div class="ans"><p>事案の状況によりますが、早期に弁護士が対応することで、身柄拘束の長期化や
      公判に至るリスクを下げられる場合があります。まずは個別の状況をお聞かせください。</p></div></div>
  <div class="qa"><button aria-expanded="false"><span>逮捕されず後日呼び出しでも、弁護士は必要ですか？</span><span class="ic">+</span></button>
    <div class="ans"><p>在宅事件でも、起訴・不起訴は決まります。呼び出し段階から示談や検察官への働きかけを
      進めることで、不起訴を目指せます。早い相談ほど選択肢が広がります。</p></div></div>
  <div class="qa"><button aria-expanded="false"><span>被害者の連絡先が分からなくても示談できますか？</span><span class="ic">+</span></button>
    <div class="ans"><p>弁護士は、捜査機関を通じて被害者側に連絡を取り、示談交渉を進めることができます。
      本人やご家族が直接連絡することは通常できないため、弁護士が代理します。</p></div></div>
  <div class="qa"><button aria-expanded="false"><span>費用はどのくらいかかりますか？</span><span class="ic">+</span></button>
    <div class="ans"><p>事案により異なります。ご依頼前に総額の見積りを明示し、ご納得いただいたうえで契約します。</p></div></div>
</div></section>

{contact_section()}
{final_cta()}"""
    return page(
        title="大阪の痴漢事件・刑事弁護｜First72 ― 迷惑防止条例違反の量刑相場",
        description="大阪で痴漢事件（迷惑防止条例違反）に強い刑事弁護。示談交渉により前科回避を目指します。初犯・前科ありの量刑相場と不起訴の見通しを統計に基づき解説。",
        body=body, prefix="../", canonical="crimes/chikan.html")


# =============================================================
# 実行
# =============================================================
def main():
    root = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(root, "crimes"), exist_ok=True)

    pages = {
        "index.html": build_index(),
        os.path.join("crimes", "chikan.html"): build_chikan(),
    }
    for path, html in pages.items():
        full = os.path.join(root, path)
        with open(full, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"built: {path}  ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
