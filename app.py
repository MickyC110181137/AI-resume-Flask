from flask import Flask, request, jsonify
from flask_cors import CORS
import json

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
# llm = AutoModelForCausalLM.from_pretrained(
#     "TheBloke/Chinese-Alpaca-2-13B-GGUF",
#       model_file="chinese-alpaca-2-13b.q5_K_M.gguf", 
#       model_type="alpaca"
#     )

# 讀取 JSON 檔案
def load_users():
    with open("./json/users.json", "r", encoding="utf-8") as file:
        return json.load(file)
def load_resumeData():
    with open("./json/resumeData.json", "r", encoding="utf-8") as file:
        return json.load(file)
def load_AIspeak():
    with open("./json/AIspeak.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_users(users):
    with open("./json/users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)
def save_resumeData(data_storage):
    with open("./json/resumeData.json", "w", encoding="utf-8") as file:
        json.dump(data_storage, file, ensure_ascii=False, indent=4)
def save_AIspeak(AIspeak):
    with open("./json/AIspeak.json", "w", encoding="utf-8") as file:
        json.dump(AIspeak, file, ensure_ascii=False, indent=4)

# 加載JSON檔
users = load_users()
data_storage = load_resumeData()
AIspeak = load_AIspeak()
app = Flask(__name__)
CORS(app)

# ------------------Kevin前端JSON 欄位資料------------------------------
@app.route("/resumeData", methods=["GET"])
def get_resumeData():
    if request.method == 'GET':
        return jsonify(data_storage), 200
    else:
        return jsonify({"message": "No data available"}), 404

@app.route("/resumeData", methods=["POST"])
def add_resume():
    new_data = request.json
    # 確保有數據可以填充
    if request.method == 'POST':
        # 填充數據到第一個resumeData結構中
        resume = data_storage[0]["resumeData"][0]
        # 使用字典更新現有字段
        resume.update({key: new_data.get(key, resume.get(key)) for key in resume})
        # 保存數據
        save_resumeData(data_storage)
        return jsonify({"message": "Data updated successfully"}), 200
    else:
        return jsonify({"message": "No data structure available to update"}), 404
    

# ----------------------------面試官JSON ------------------------------
@app.route("/AIspeak", methods=["GET"])
def get_AIspeak():
    if request.method == 'GET':
        return jsonify(AIspeak), 200
    else:
        return jsonify({"message": "No data available"}), 404

@app.route("/AIspeak/aiQuestion", methods=["POST"])
def add_aiQuestiion():
    if request.method == 'POST':
        data = request.json  # 獲取POST請求中的JSON數據
        # 更新 aiQuestion
        question = AIspeak[0]["aiQuestion"][0]
        question.update({key: data.get(key, question.get(key)) for key in question})
        save_AIspeak(AIspeak)
        return jsonify({"message": "Data updated successfully"}), 200
    else:
        return jsonify({"message": "No data available"}), 404

@app.route("/AIspeak/userAnswer", methods=["POST"])
def add_userAnswser():
    if request.method == 'POST':
        data = request.json  # 獲取POST請求中的JSON數據
        # 更新 aiQuestion
        answer = AIspeak[0]["userAnswer"][0]
        answer.update({key: data.get(key, answer.get(key)) for key in answer})
        save_AIspeak(AIspeak)
        return jsonify({"message": "Data updated successfully"}), 200
    else:
        return jsonify({"message": "No data available"}), 404

# --------------------初版-----------------------------------------------
# 獲取所有用戶的信息
@app.route("/resume", methods=["GET"])
def get_user():
    return jsonify({"users": users})

# 創建新的用戶
@app.route("/resume", methods=["POST"])
def create_user():
    request_data = request.get_json()
    new_user = {"name": request_data["name"], "message": [], "llm_anwser": []}
    users.append(new_user)
    save_users(users)  # 保存到 JSON 檔案
    return jsonify(new_user), 201

# 在指定用戶中添加訊息
@app.route("/resume/<string:name>/message", methods=["POST"])
def add_message_to_user(name):
    request_data = request.get_json()
    for user in users:
        if user["name"] == name:
            new_message = request_data["message"]
            user["message"].append(new_message)
            save_users(users)  # 保存到 JSON 檔案
            return jsonify({"message": f"Course {new_message} added to user {name}"}), 201
    return jsonify({"message": "usesr not found"}), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)