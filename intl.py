"""日本語・한국어（＋英文 FAQ）區塊，附在中文頁同一頁下方（同 en.py 的理由：ASC 只填一個 URL）。

目前只有介面有日韓文的 App（Posté）。由 build.py 在 en.append_all() 之後呼叫 append_all()。
"""

HR = '  <hr style="margin:44px 0 30px;border:0;border-top:1px solid rgba(139,148,168,.3)">'
LABEL = '  <p style="color:#8b94a8;font-size:.85rem;margin:0 0 20px">{}</p>'

POSTE = {
    "faq": {
        "en": ("English", "Support", [
            ("Are my photos uploaded?",
             "<p>No. All glass, print and paper effects are computed on your phone. No account, no servers.</p>"),
            ("What is a recipe?",
             "<p>A recipe is a ready-made glass look (e.g. “Half Sunset”, “A Rainy Window”, “Pressed Floral Glass”). "
             "Tap a card in the Recipes tab and pick a photo — it opens with the look applied. Long-press a card for details "
             "or to try it on a sample photo.</p>"),
            ("How do I move or rotate the Half Glass line?",
             "<p>In the Range tab, drag the line on the photo to move it and rotate with two fingers (it snaps near 0°, 15°, 45°, 90°). "
             "Tap “Flip” to put the glass on the other side. “Reeded Sky” and “Rippled Sea” find the horizon for you — "
             "if they miss, just drag the line.</p>"),
            ("Why does the app ask whether to save when I leave the editor?",
             "<p>Not every try is worth keeping. “Save Draft” keeps it in Works so you can come back; “Don’t Save” discards it.</p>"),
            ("Is it free?",
             "<p>Yes. Everything is free — no watermark, no in-app purchases, no subscriptions, no ads.</p>"),
        ]),
        "ja": ("日本語", "サポート", [
            ("写真はアップロードされますか？",
             "<p>いいえ。ガラス・印刷・紙の処理はすべてお使いのスマートフォン上で行います。アカウントもサーバーもありません。</p>"),
            ("レシピとは？",
             "<p>あらかじめ調整されたガラスの効果です（「半分だけの夕焼け」「雨の窓辺」「海棠ガラス」など）。"
             "「レシピ」タブでカードをタップして写真を選ぶと、効果がかかった状態で編集画面が開きます。"
             "カードを長押しすると説明が見られ、サンプル写真で試すこともできます。</p>"),
            ("ハーフガラスの境界線を動かすには？",
             "<p>「範囲」タブで写真上の線をドラッグして移動、2本指で回転します（0°・15°・45°・90° 付近で吸着）。"
             "「反対側」でガラスの側を入れ替えます。「空のモール」「水面の波紋」は地平線を自動で探します。ずれた場合は線をドラッグしてください。</p>"),
            ("編集画面を閉じるときに保存を聞かれるのはなぜ？",
             "<p>すべての作品を残したいとは限らないためです。「下書きに保存」で「作品」タブに残り、あとから続きを編集できます。"
             "「保存しない」を選ぶと残りません。</p>"),
            ("写真への保存について",
             "<p>初めて保存するとき「写真の追加」のみを許可するよう求めます。Posté がアルバム全体を読み取ることはありません。</p>"),
            ("料金は？",
             "<p>すべての機能が無料です。透かしなし、App 内課金・サブスクリプション・広告もありません。</p>"),
        ]),
        "ko": ("한국어", "지원", [
            ("사진이 업로드되나요?",
             "<p>아니요. 유리·인쇄·종이 효과는 모두 휴대폰 안에서 처리돼요. 계정도 서버도 없어요.</p>"),
            ("레시피가 뭔가요?",
             "<p>미리 조정된 유리 효과예요(‘노을, 반만 유리로’, ‘비 오는 창가’, ‘꽃무늬 유리’ 등). "
             "‘레시피’ 탭에서 카드를 누르고 사진을 고르면 효과가 적용된 채로 편집 화면이 열려요. "
             "카드를 길게 누르면 설명을 보거나 샘플 사진으로 먼저 써 볼 수 있어요.</p>"),
            ("반쪽 유리의 경계선은 어떻게 옮기나요?",
             "<p>‘영역’ 탭에서 사진 위의 선을 드래그해 옮기고, 두 손가락으로 돌려 각도를 바꿔요(0°·15°·45°·90° 근처에서 자석처럼 맞춰져요). "
             "‘방향 전환’으로 유리 쪽을 바꿀 수 있어요. 하늘·수면 레시피는 수평선을 자동으로 찾고, 틀리면 선을 직접 옮기면 돼요.</p>"),
            ("편집 화면을 나갈 때 저장할지 묻는 이유는?",
             "<p>모든 시도를 남기고 싶지는 않으니까요. ‘초안으로 저장’을 누르면 ‘작품’ 탭에 남아 나중에 이어서 편집할 수 있고, "
             "‘저장 안 함’을 누르면 남지 않아요.</p>"),
            ("사진 앱 저장 권한",
             "<p>처음 저장할 때 ‘사진 추가’ 권한만 요청해요. Posté는 앨범 전체를 읽지 않아요.</p>"),
            ("유료인가요?",
             "<p>모든 기능이 무료예요. 워터마크, 인앱 결제, 구독, 광고가 없어요.</p>"),
        ]),
    },
    "privacy": {
        "ja": ("日本語", "プライバシーポリシー", "最終更新：2026年10月", [
            ("概要", "<p><strong>このアプリは個人データを収集・アップロード・共有しません。</strong>アカウント、広告、解析ツールはありません。</p>"),
            ("写真ライブラリ", "<p>システムの写真ピッカーで<strong>あなたが選んだ</strong>写真・動画だけを読み込みます。保存時は「写真の追加」のみを求め、アルバム全体を読み取ることはありません。</p>"),
            ("写真の日付と位置情報（EXIF）", "<p>作品の地名・日付・時刻を自動入力するために使います。座標は iOS の機能である <strong>Apple のジオコーディングサービス</strong>で地名に変換されます。Posté は独自のサーバーを持たず、座標を保存・送信しません。</p>"),
            ("モーションセンサー", "<p>スマートフォンの傾きでガラスの光を動かすために端末上でのみ使用し、保存しません。</p>"),
            ("端末に保存されるデータ", "<p>下書き・作品・切手・設定はアプリ内に保存されます。アプリを削除するとすべて削除されます。</p>"),
            ("お子さまについて", "<p>本アプリは 4+ です。データを一切収集しないため、お子さまのデータも収集しません。</p>"),
            ("お問い合わせ", '<p><a href="mailto:{email}">{email}</a></p>'),
        ]),
        "ko": ("한국어", "개인정보 처리방침", "최종 업데이트: 2026년 10월", [
            ("요약", "<p><strong>이 앱은 개인정보를 수집·업로드·공유하지 않아요.</strong> 계정, 광고, 분석 도구가 없어요.</p>"),
            ("사진 보관함", "<p>시스템 사진 선택기로 <strong>직접 고른</strong> 사진과 동영상만 읽어요. 저장할 때는 ‘사진 추가’ 권한만 요청하고, 앨범 전체를 읽지 않아요.</p>"),
            ("사진의 날짜와 위치(EXIF)", "<p>작품의 장소·날짜·시간을 자동으로 채우는 데 써요. 좌표는 iOS 기능인 <strong>Apple 지오코딩 서비스</strong>로 장소 이름으로 바뀌며, Posté는 자체 서버가 없고 좌표를 저장하거나 전송하지 않아요.</p>"),
            ("모션 센서", "<p>휴대폰 기울기로 유리의 빛을 움직이는 데 기기 안에서만 쓰고, 저장하지 않아요.</p>"),
            ("기기에 저장되는 데이터", "<p>초안·작품·우표·설정은 앱 안에 저장돼요. 앱을 삭제하면 모두 삭제돼요.</p>"),
            ("어린이", "<p>이 앱은 4+ 등급이에요. 어떤 데이터도 수집하지 않으므로 어린이의 데이터도 수집하지 않아요.</p>"),
            ("문의", '<p><a href="mailto:{email}">{email}</a></p>'),
        ]),
    },
}


def _faq_block(lang):
    label, title, items = POSTE["faq"][lang]
    parts = [HR, LABEL.format(label), f'  <h1 style="font-size:1.35rem;margin:0 0 4px" lang="{lang}">Posté — {title}</h1>']
    parts += [f'  <h2 lang="{lang}">{h}</h2>\n{b}' for h, b in items]
    return "\n\n".join(parts)


def _privacy_block(lang, email):
    label, title, updated, items = POSTE["privacy"][lang]
    parts = [HR, LABEL.format(label), f'  <h1 style="font-size:1.35rem;margin:0 0 4px" lang="{lang}">{title}</h1>',
             f'  <p class="sub">Posté &middot; {updated}</p>']
    parts += [f'  <h2 lang="{lang}">{h}</h2>\n{b.format(email=email)}' for h, b in items]
    return "\n\n".join(parts)


def append_all(root, email):
    n = 0
    idx, pri = root / "poste" / "index.html", root / "poste" / "privacy.html"
    if idx.exists():
        t = idx.read_text()
        if 'lang="ja"' not in t:
            blocks = "\n\n".join(_faq_block(l) for l in ("en", "ja", "ko"))
            idx.write_text(t.replace("  <footer>", blocks + "\n\n  <footer>", 1)); n += 1
    if pri.exists():
        t = pri.read_text()
        if 'lang="ja"' not in t:
            blocks = "\n\n".join(_privacy_block(l, email) for l in ("ja", "ko"))
            pri.write_text(t.replace("  <footer>", blocks + "\n\n  <footer>", 1)); n += 1
    return n
