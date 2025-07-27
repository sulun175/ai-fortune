from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

# 确保模板自动重新加载
app.config['TEMPLATES_AUTO_RELOAD'] = True

# 运势模板库
FORTUNE_TEMPLATES = {
    'love': [
        "❤️ 今日红鸾星动，会有意外邂逅",
        "🌸 主动表达会收获惊喜"
    ],
    'career': [
        "💼 提出的方案将被领导采纳",
        "📈 项目进展比预期快30%"
    ],
    'health': [
        "🍎 多吃红色食物能增强运势",
        "💤 早睡1小时效率翻倍"
    ]
}

@app.route("/")
def home():
    """首页路由"""
    return render_template("index.html")

@app.route("/fortune", methods=['POST'])
def get_fortune():
    """运势生成路由"""
    try:
        name = request.form.get('name', '亲爱的朋友').strip()
        if not name:
            return render_template("index.html", error="请输入名字")
        
        # 生成运势内容
        fortune = {
            'love': random.choice(FORTUNE_TEMPLATES['love']),
            'career': random.choice(FORTUNE_TEMPLATES['career']),
            'health': random.choice(FORTUNE_TEMPLATES['health']),
            'lucky_num': random.randint(1, 100),
            'name': name
        }
        
        return render_template("result.html", fortune=fortune)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return render_template("index.html", error="系统繁忙，请稍后再试")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)