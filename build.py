#!/usr/bin/env python3
"""產生所有 App 的支援頁與隱私政策。

為什麼用腳本而不是手寫 HTML：六支 App × 兩頁，樣式要一致、
聯絡信箱與免責條款要能一次改完。改 APPS 裡的資料然後重跑就好。
    python3 build.py && git add -A && git commit -m "..." && git push
"""
import pathlib, html

EMAIL = "zoey.meala@gmail.com"

CSS = """
  :root{color-scheme:light dark}
  body{margin:0;background:#f5f7fb;color:#141821;
       font:16px/1.75 "Noto Sans TC","PingFang TC",-apple-system,sans-serif}
  @media (prefers-color-scheme:dark){body{background:#0f1420;color:#eef1f7}}
  main{max-width:44rem;margin:0 auto;padding:52px 20px 80px}
  h1{font-size:1.45rem;letter-spacing:-.02em;margin:0 0 4px}
  .sub{color:#8b94a8;margin:0 0 34px;font-size:.9rem}
  h2{font-size:1.02rem;margin:30px 0 6px;font-weight:700}
  p,li{margin:0 0 10px}
  ul{padding-left:1.2rem}
  a{color:#0a66c2}
  @media (prefers-color-scheme:dark){a{color:#7cc0ff}}
  strong{font-weight:700}
  footer{margin-top:52px;padding-top:18px;border-top:1px solid rgba(139,148,168,.3);
         font-size:.85rem;color:#8b94a8}
  footer a{margin-right:14px}
"""

def page(title, subtitle, body, footer_links):
    links = " ".join(f'<a href="{h}">{t}</a>' for t, h in footer_links)
    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<main>
  <h1>{html.escape(title.split(' — ')[0])}</h1>
  <p class="sub">{subtitle}</p>
{body}
  <footer>{links}</footer>
</main>
</body>
</html>
"""

# ── 每支 App 的差異都在這裡；共通的段落由 privacy_common() 補
APPS = {
    "wordrun": {
        "name": "篝火町・單字快跑",
        "short": "單字快跑",
        "tagline": "邊跑邊背單字的 3D 跑酷",
        "faq": [
            ("進度不見了",
             "<p>遊戲進度會自動同步到你的 iCloud。換手機或重裝之後，用<strong>同一個 Apple ID</strong> 打開就會回來。"
             "沒有回來的話，先確認「設定 → 你的名字 → iCloud」有開啟，再重開一次 App。</p>"
             "<p>沒有登入 iCloud 也能玩，只是進度只存在這台手機上。</p>"),
            ("沒有聲音",
             "<p>iOS 規定要先有觸碰才能播放聲音，所以第一次進遊戲點過畫面之後聲音才會出來。"
             "還是沒聲音的話，檢查手機側邊的靜音開關，以及遊戲內「設定」裡的音樂／音效／語音三個滑桿。</p>"),
            ("「篝火町」是什麼？",
             "<p>白天在島上跑關卡撿字，夜裡回營地把今天撿到的字添進火裡。"
             "火越旺，越多動物被暖意吸引來過夜，早上推開帳篷就看得到誰來了。</p>"),
            ("怎麼換角色",
             "<p>大廳右下角「換角色」。角色用遊戲中賺到的金幣解鎖，不需要付費。</p>"),
            ("字太難／太簡單",
             "<p>大廳的「1 分鐘分級測驗」會依你的程度直接開放對應的島。可以重測，只會往上調不會往下收。</p>"),
            ("睡著的燈籠是什麼？",
             "<p>你學過但一陣子沒複習的字會「睡著」。<strong>每次只會叫醒三盞</strong>——"
             "所以放一週假回來也不會堆成一大疊複習卡，接著跑就好。</p>"),
        ],
        "privacy_extra": [
            ("遊戲進度存在哪裡",
             "<p>關卡星數、金幣、解鎖的角色、學過的單字與複習排程，都存在你的裝置上，"
             "並透過 <strong>Apple 的 iCloud 鍵值儲存</strong>同步到你自己的 iCloud 帳戶。</p>"
             "<p>這份資料屬於你、存在你的 iCloud 裡，開發者無法讀取也無法修改。"
             "不想同步的話，關閉系統設定裡本 App 的 iCloud 權限即可，遊戲仍可正常遊玩。</p>"),
            ("網路連線",
             "<p>單字、語音與 3D 模型全部內建，遊戲完全離線可玩。唯一的連線是與 Apple 的 iCloud 同步進度。</p>"),
            ("付費", "<p>本 App 完全免費，沒有 App 內購買、沒有訂閱、沒有廣告。</p>"),
        ],
    },
    "forklift": {
        "name": "堆高機特訓",
        "short": "堆高機特訓",
        "tagline": "堆高機操作單一級技術士學科練習",
        "faq": [
            ("題庫依據什麼？",
             "<p>整理自公開之學科測試參考資料。解析為自製內容，說明「為什麼這個對、你選的那個錯在哪」。</p>"
             "<p>本 App 為<strong>非官方</strong>學習工具，如與主管機關最新公告不符，一律以官方公告為準。</p>"),
            ("要付費嗎？",
             "<p>不用。全部題目、全部解析與無限次模擬考都免費，沒有 App 內購買、沒有訂閱、沒有廣告。</p>"),
            ("換手機之後進度不見了",
             "<p>學習紀錄只存在裝置本機，重裝或換機不會轉移，這也是它不需要帳號的代價。</p>"),
            ("有術科教學嗎？",
             "<p>沒有。本 App 只處理學科測試。術科需要實機操作與場地練習，請依受訓單位安排。</p>"),
            ("怎麼設定考試提醒？",
             "<p>「我的 → 考試日」開啟並選日期，會在考前 7 天、3 天與當天早上各提醒一次，"
             "並依剩餘天數算出每天建議做幾題。</p>"),
            ("字太小看不清楚",
             "<p>題目與解析會跟著系統字級調整。到「設定 → 螢幕顯示與亮度 → 文字大小」調大即可。</p>"),
        ],
        "privacy_extra": [
            ("學習紀錄存在哪裡",
             "<p>作答紀錄、複習排程、連續天數與考試日期，全部以裝置內建的偏好設定儲存在你的 iPhone 上。"
             "這些資料不會離開你的裝置，我們也無從讀取。</p>"
             "<p>刪除 App 即刪除全部紀錄；App 內的「清除所有學習進度」也會將其歸零。</p>"),
            ("付費", "<p>本 App 完全免費，沒有 App 內購買、沒有訂閱、沒有廣告。</p>"),
            ("通知",
             "<p>若你設定了考試日期，App 會在你的裝置上排定本地通知。這些通知不經過任何伺服器，"
             "可隨時在系統設定中關閉。</p>"),
        ],
        "disclaimer": True,
    },
    "quitcat": {
        "name": "少一杯",
        "short": "少一杯",
        "tagline": "手搖飲少一杯，先看見自己喝了多少",
        "faq": [
            ("方糖數怎麼算的？",
             "<p>依你選的品項、糖度與容量估算含糖量，再換算成方糖顆數（一顆方糖約 5 公克糖）。"
             "這是<strong>估計值</strong>，實際含糖量各店家配方不同，數字用來建立感覺，不是營養標示。</p>"),
            ("紀錄不見了",
             "<p>紀錄存在裝置本機。刪除 App 會一併刪除，重裝不會恢復。</p>"),
            ("沒有收到提醒",
             "<p>到「設定 → 通知 → 少一杯」確認允許通知。App 內也要在設定頁開啟提醒。</p>"),
            ("Pro 買了沒解鎖",
             "<p>到 App 內的 Pro 頁面點「還原購買」。仍未恢復請來信並附購買收據。</p>"),
            ("我不想戒，只想知道自己喝多少",
             "<p>那也很好。這支 App 沒有任何強制目標，不記錄也不會被扣分。</p>"),
        ],
        "privacy_extra": [
            ("紀錄存在哪裡",
             "<p>你的飲料紀錄、設定與統計全部存在裝置本機（偏好設定），不會離開你的手機，我們也無從讀取。</p>"),
            ("購買",
             "<p>Pro 為一次性買斷，透過 Apple 的 App 內購買機制完成，交易由 Apple 處理。"
             "我們不會收到也不會儲存你的付款資訊。</p>"),
            ("通知", "<p>提醒為裝置上的本地通知，不經過任何伺服器，可隨時關閉。</p>"),
            ("這不是醫療建議",
             "<p>本 App 呈現的糖量為估算值，僅供自我覺察參考，不構成任何醫療或營養建議。"
             "有健康疑慮請諮詢專業人員。</p>"),
        ],
    },
    "slate": {
        "name": "開拍 Slate",
        "short": "開拍",
        "tagline": "會跟著你唸稿的提詞器相機",
        "faq": [
            ("提詞器跟不上我",
             "<p>語音追蹤靠裝置上的語音辨識，環境太吵或講話太小聲會影響判斷。"
             "可以先在安靜環境試一次；真的不順時切換成等速捲動（可調 0.8–1.5×）。</p>"),
            ("辨識支援哪些語言？",
             "<p>中英自動偵測，全程在你的手機上運行，語音不會上傳。</p>"),
            ("講稿怎麼分段？",
             "<p>在講稿中用單獨一行的 <code>---</code> 分段。拍攝時可以直接跳到任一段，也可以點某一行跳到那個位置。</p>"),
            ("錄好的影片在哪？",
             "<p>存在 App 內的片段清單，可從那裡存到相簿。存到相簿需要相簿權限。</p>"),
            ("4K 60fps 錄不了",
             "<p>不是所有機型都支援 4K60。App 會自動搜尋可用格式，找不到時會退回你機型支援的最高規格。"
             "長時間 4K 錄影手機會發熱，App 有過熱監測會提醒你。</p>"),
            ("為什麼要相機、麥克風、語音辨識權限？",
             "<p>相機與麥克風用來拍攝與收音；語音辨識用來讓提詞器跟上你唸到哪。"
             "三者都只在你按下錄影或開啟提詞器時使用。</p>"),
        ],
        "privacy_extra": [
            ("影片與講稿存在哪裡",
             "<p>拍攝的影片與你寫的講稿全部存在裝置本機，不會上傳到任何伺服器，我們也無從讀取。</p>"),
            ("語音辨識",
             "<p>提詞器的語音追蹤使用 Apple 的<strong>裝置端</strong>語音辨識，"
             "你的聲音不會離開手機、不會被錄下來、也不會被傳送給任何人。</p>"),
            ("相簿",
             "<p>只有在你主動選擇「存到相簿」時才會寫入相簿，App 不會讀取你相簿裡的其他內容。</p>"),
            ("付費", "<p>本 App 完全免費，沒有 App 內購買、沒有訂閱、沒有廣告。</p>"),
        ],
    },
    "medalarm": {
        "name": "藥定 MedAlarm",
        "short": "藥定",
        "tagline": "吃藥提醒與回診前的一頁摘要",
        "faq": [
            ("提醒沒有響",
             "<p>先確認「設定 → 通知 → 藥定」允許通知，並允許「重要提醒」。"
             "另外檢查專注模式（勿擾）是否擋掉了提醒。</p>"),
            ("可以幫家人設定嗎？",
             "<p>可以。App 內有長輩端的大字模式，字級與按鈕都放大，適合直接交給長輩使用。</p>"),
            ("藥吃完了要怎麼標記？",
             "<p>在提醒上標記已服用，紀錄會累積成回診時可以直接給醫師看的摘要。</p>"),
            ("資料會不會傳出去？",
             "<p>不會。用藥紀錄全部存在你的手機裡，我們讀不到，也沒有任何伺服器會收到。</p>"),
        ],
        "privacy_extra": [
            ("用藥資料存在哪裡",
             "<p><strong>你的用藥紀錄只存在這台裝置上。</strong>藥名、劑量、服藥時間與紀錄"
             "都存在 App 自己的本機資料庫，不會上傳、不會分享、開發者無法讀取。</p>"),
            ("這不是醫療建議",
             "<p>本 App 是提醒與紀錄工具，不提供診斷、處方或醫療建議。"
             "任何用藥調整請依醫師或藥師指示，不要以本 App 的內容取代專業判斷。</p>"),
            ("通知",
             "<p>吃藥提醒為裝置上的本地通知（含 iOS 的提醒功能），不經過任何伺服器，可隨時關閉。</p>"),
        ],
        "disclaimer_med": True,
    },
}
APPS["crane"] = dict(APPS["forklift"],
                     name="起重機特訓", short="起重機特訓",
                     tagline="固定式起重機操作單一級技術士學科練習")

def privacy_common(app):
    parts = ["""  <h2>一句話版本</h2>
  <p><strong>本 App 不收集、不上傳、不分享任何個人資料。</strong>沒有帳號、沒有廣告、沒有分析工具。</p>

  <h2>我們不收集什麼</h2>
  <ul>
    <li>不需要註冊，也沒有登入功能</li>
    <li>不收集姓名、電子郵件、電話或任何聯絡資訊</li>
    <li>不收集位置或通訊錄</li>
    <li>不使用第三方分析或廣告 SDK，App 內沒有任何廣告</li>
    <li>不追蹤你，也不會把資料提供給其他公司</li>
  </ul>"""]
    for h2, body in app["privacy_extra"]:
        parts.append(f"  <h2>{h2}</h2>\n{body}")
    parts.append("""  <h2>兒童</h2>
  <p>本 App 分級為 4+。因為不收集任何資料，自然也不會收集兒童的個人資料。</p>

  <h2>政策變更</h2>
  <p>若日後有變更，會更新本頁並修改上方的更新日期。</p>""")
    parts.append(f"""  <h2>聯絡我們</h2>
  <p>有任何疑問請來信：<a href="mailto:{EMAIL}">{EMAIL}</a></p>""")
    return "\n\n".join(parts)

root = pathlib.Path(__file__).parent
for slug, app in APPS.items():
    d = root / slug
    d.mkdir(exist_ok=True)

    faq = "\n\n".join(f"  <h2>{h}</h2>\n{b}" for h, b in app["faq"])
    faq += f"""\n\n  <h2>還是沒解決</h2>
  <p>來信：<a href="mailto:{EMAIL}">{EMAIL}</a>，通常一到兩個工作天回覆。</p>"""
    if app.get("disclaimer"):
        faq += """\n\n  <p style="margin-top:28px;color:#8b94a8;font-size:.85rem">
  本 App 為非官方學習工具。題庫整理自公開之學科測試參考資料，解析內容為自製，僅供練習參考；
  如與主管機關最新公告不符，一律以官方公告為準。</p>"""
    if app.get("disclaimer_med"):
        faq += """\n\n  <p style="margin-top:28px;color:#8b94a8;font-size:.85rem">
  本 App 為提醒與紀錄工具，不提供診斷、處方或醫療建議。用藥請依醫師或藥師指示。</p>"""

    (d / "index.html").write_text(page(
        f"支援 — {app['short']}", f"{app['name']} — 支援與常見問題",
        faq, [("隱私政策", "privacy.html"), ("其他 App", "../")]))

    (d / "privacy.html").write_text(page(
        f"隱私政策 — {app['short']}", f"{app['name']} · 最後更新：2026 年 9 月",
        privacy_common(app), [("支援與常見問題", "index.html"), ("其他 App", "../")]))
    print(f"  ✓ {slug}/  {app['name']}")

cards = "\n".join(
    f'  <a class="card" href="{slug}/"><b>{a["name"]}</b><span>{a["tagline"]}</span></a>'
    for slug, a in APPS.items())
(root / "index.html").write_text(f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>App 支援</title>
<style>{CSS}
  a.card{{display:block;padding:15px 17px;margin-bottom:9px;text-decoration:none;
         border:1px solid rgba(139,148,168,.3);border-radius:8px;color:inherit}}
  a.card:hover{{border-color:#8b94a8}}
  a.card b{{display:block;font-size:1.02rem;margin-bottom:2px}}
  a.card span{{font-size:.85rem;color:#8b94a8}}
</style>
</head>
<body>
<main>
  <h1>App 支援</h1>
  <p class="sub">有問題歡迎來信 <a href="mailto:{EMAIL}">{EMAIL}</a></p>
{cards}
</main>
</body>
</html>
""")
print("  ✓ index.html（總覽）")

# 英文版隱私政策接在中文版同一頁下方
# （審核員不會去找 /en/，ASC 也只能填一個 URL）
import en
print(f"  ✓ 英文版隱私政策 {en.append_all(root, EMAIL)} 支")
