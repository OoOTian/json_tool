import json
from flask import Flask, render_template, request, jsonify
from json_repair import repair_json  # 假设此函数能修复坏掉的JSON

app = Flask(__name__, template_folder='../templates')

def highlight_changes(original, modified):
    highlighted = ""
    i, j = 0, 0
    while i < len(original) and j < len(modified):
        if original[i] != modified[j]:
            highlighted += '<span class="highlight">'
            while j < len(modified) and (i >= len(original) or original[i] != modified[j]):
                highlighted += modified[j]
                j += 1
            highlighted += '</span>'
        else:
            highlighted += modified[j]
            i += 1
            j += 1
    if j < len(modified):
        highlighted += '<span class="highlight">' + modified[j:] + '</span>'
    return highlighted

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        json_input = request.form['json_input']
        try:
            # 使用 repair_json 修复 JSON
            repaired_json = repair_json(json_input)

            # 将修复后的 JSON 格式化为漂亮的字符串
            parsed_json = json.loads(repaired_json)
            pretty_json = json.dumps(parsed_json, indent=4)
            
            # 高亮显示变化部分
            highlighted_json = highlight_changes(json_input, pretty_json)

            return jsonify({'success': True, 'repaired_json': highlighted_json})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    return render_template('frontend/index.html')

if __name__ == '__main__':
    app.run(debug=True)