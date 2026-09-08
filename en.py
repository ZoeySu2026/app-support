"""英文版隱私政策，附在中文版同一頁下方。

為什麼不另開 /en/：審核員不會去找。同一頁往下捲就看得到，
ASC 也只需要填一個 URL。

由 build.py 在產完中文頁之後呼叫 append_all()。
"""

COMMON_HEAD = """  <h2>In short</h2>
  <p><strong>This app does not collect, upload or share any personal data.</strong>
  No account, no ads, no analytics.</p>

  <h2>What we do not collect</h2>
  <ul>
    <li>No sign-up and no login</li>
    <li>No name, email, phone number or any contact information</li>
    <li>No location and no contacts</li>
    <li>No third-party analytics or advertising SDKs, and no ads inside the app</li>
    <li>We do not track you and we do not share data with anyone</li>
  </ul>"""

APPS = {
    "wordrun": {
        "name": "Campfire Town &middot; Word Runner",
        "sections": [
            ("Where your progress is stored",
             "<p>Level stars, coins, unlocked characters, learned words and review schedules are stored on "
             "your device and synced to <strong>your own iCloud account</strong> through Apple's key-value "
             "store. This data belongs to you — the developer cannot read or modify it. You can turn iCloud "
             "off for this app in Settings; the game still works fully offline.</p>"),
            ("Network",
             "<p>All words, audio and 3D models are bundled with the app, which is fully playable offline. "
             "The only network activity is syncing your own progress with Apple's iCloud.</p>"),
            ("Payments",
             "<p>This app is completely free. No in-app purchases, no subscriptions, no ads.</p>"),
        ],
    },
    "forklift": {
        "name": "Forklift Operator Exam Prep",
        "sections": [
            ("Where your study data is stored",
             "<p>Answer history, review scheduling, streaks and your exam date are stored in your device's "
             "local preferences. This data never leaves your device and we cannot access it. Deleting the app "
             "removes everything; the in-app &ldquo;Clear all progress&rdquo; does the same.</p>"),
            ("Purchases",
             "<p>The full unlock is a one-time non-consumable purchase processed by Apple. We never receive "
             "or store your payment information. The app only records a single flag: whether it is unlocked.</p>"),
            ("Notifications",
             "<p>If you set an exam date, the app schedules local notifications on your device. They do not "
             "pass through any server and can be disabled at any time.</p>"),
            ("Unofficial study tool",
             "<p>This app is an unofficial study tool. Questions are compiled from publicly available exam "
             "reference materials and the explanations are written by us, for practice only. Where anything "
             "differs from the latest official announcement, the official announcement prevails.</p>"),
        ],
    },
    "quitcat": {
        "name": "One Cup Less",
        "sections": [
            ("Where your records are stored",
             "<p>Your drink log, settings and statistics are stored entirely on your device. They never leave "
             "your phone and we cannot access them.</p>"),
            ("Purchases",
             "<p>Pro is a one-time non-consumable purchase processed by Apple. We never receive or store your "
             "payment information. Pro unlocks cosmetics and extended statistics only — no core feature is "
             "locked behind it.</p>"),
            ("Notifications",
             "<p>Reminders are local notifications scheduled on your device. No server is involved and they "
             "can be disabled at any time.</p>"),
            ("Not medical advice",
             "<p>Sugar amounts shown in this app are estimates intended for self-awareness only. They do not "
             "constitute medical or nutritional advice. Please consult a professional for health concerns.</p>"),
        ],
    },
    "slate": {
        "name": "Slate — Prompter Camera",
        "sections": [
            ("Where your videos and scripts are stored",
             "<p>Recorded videos and the scripts you write stay on your device. Nothing is uploaded to any "
             "server and we cannot access them.</p>"),
            ("Speech recognition",
             "<p>The prompter uses Apple's <strong>on-device</strong> speech recognition to follow your "
             "position in your own script. Your voice never leaves the phone, is never recorded for us, and "
             "is never transmitted to anyone.</p>"),
            ("Camera and microphone",
             "<p>Used only while you are recording. Nothing is captured in the background.</p>"),
            ("Photo library",
             "<p>The app writes to your photo library only when you explicitly choose to export a clip. "
             "It never reads other content in your library.</p>"),
            ("Payments",
             "<p>This app is completely free. No in-app purchases, no subscriptions, no ads.</p>"),
        ],
    },
    "medalarm": {
        "name": "MedAlarm",
        "sections": [
            ("Where your medication data is stored",
             "<p><strong>Your medication records stay on this device.</strong> Medication names, dosages, "
             "schedules and logs are kept in the app's local database. Nothing is uploaded, nothing is "
             "shared, and the developer cannot read them.</p>"),
            ("Not medical advice",
             "<p>This app is a reminder and logging tool. It does not provide diagnosis, prescriptions or "
             "medical advice, and it does not interpret any values you enter. Follow your doctor's or "
             "pharmacist's instructions for any medication changes.</p>"),
            ("Notifications",
             "<p>Medication reminders are scheduled locally on your device, including through iOS alarms. "
             "They do not pass through any server and can be disabled at any time.</p>"),
            ("Sharing a summary",
             "<p>The visit summary is shared only when you choose to send it, through the sharing app you "
             "pick. We are not involved in that transfer and receive nothing.</p>"),
        ],
    },
}
APPS["crane"] = dict(APPS["forklift"], name="Overhead Crane Operator Exam Prep")


def _tail(email):
    return (
        "  <h2>Children</h2>\n"
        "  <p>This app is rated 4+. Because it collects no data at all, it collects no data from "
        "children either.</p>\n\n"
        "  <h2>Changes to this policy</h2>\n"
        "  <p>If this policy changes, this page and the date above will be updated.</p>\n\n"
        "  <h2>Contact</h2>\n"
        f'  <p>Questions? Email <a href="mailto:{email}">{email}</a></p>'
    )


def block(slug, email):
    """產生要插進中文頁下方的英文區塊。"""
    app = APPS[slug]
    parts = [
        '  <hr style="margin:44px 0 30px;border:0;border-top:1px solid rgba(139,148,168,.3)">',
        '  <p style="color:#8b94a8;font-size:.85rem;margin:0 0 20px">English version</p>',
        '  <h1 style="font-size:1.35rem;margin:0 0 4px">Privacy Policy</h1>',
        f'  <p class="sub">{app["name"]} &middot; Last updated: September 2026</p>',
        COMMON_HEAD,
    ]
    for heading, body in app["sections"]:
        parts.append(f"  <h2>{heading}</h2>\n{body}")
    parts.append(_tail(email))
    return "\n\n".join(parts)


def append_all(root, email):
    """把英文區塊插進每一支的 privacy.html（在 <footer> 之前）。"""
    n = 0
    for slug in APPS:
        f = root / slug / "privacy.html"
        if not f.exists():
            continue
        t = f.read_text()
        if "English version" in t:
            continue
        t = t.replace("  <footer>", block(slug, email) + "\n\n  <footer>", 1)
        f.write_text(t)
        n += 1
    return n
