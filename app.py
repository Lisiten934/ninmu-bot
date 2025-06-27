from flask import Flask, render_template_string, request

app = Flask(__name__)

# 任務データ（簡易版）
missions = [
    "10分でCS60体以上取れ！",
    "ピンクワードを2個以上置け！",
    "ロームでキルアシスト1回せよ！",
    "15分間死なずにプレイせよ！"
]

# 任務表示ページ
@app.route('/')
def index():
    mission_list_html = "<ul>" + "".join(f"<li>{m}</li>" for m in missions) + "</ul>"
    return render_template_string(f"""
        <h1>任務リスト</h1>
        {mission_list_html}
        <form action="/submit" method="POST">
            <input type="text" name="player" placeholder="プレイヤー名" required><br>
            <textarea name="report" placeholder="任務報告を書いてね" required></textarea><br>
            <button type="submit">任務提出</button>
        </form>
    """)

# 任務提出受け取り（POST）
@app.route('/submit', methods=['POST'])
def submit():
    player = request.form.get('player')
    report = request.form.get('report')
    # ここでDBやファイルに保存する処理を入れる想定
    return f"<h2>{player}さん、任務提出ありがとう！</h2><p>報告内容:<br>{report}</p><a href='/'>戻る</a>"

if __name__ == '__main__':
    app.run(debug=True)
