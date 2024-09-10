from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
import uuid

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
# llm = AutoModelForCausalLM.from_pretrained(
#     "TheBloke/Chinese-Alpaca-2-13B-GGUF",
#       model_file="chinese-alpaca-2-13b.q5_K_M.gguf", 
#       model_type="alpaca"
#     )

# 讀取 JSON 檔案
# def load_users():
#     with open("./json/users.json", "r", encoding="utf-8") as file:
#         return json.load(file)

# def save_users(users):
#     with open("./json/users.json", "w", encoding="utf-8") as file:
#         json.dump(users, file, ensure_ascii=False, indent=4)

# # 加載JSON檔
# users = load_users()


app = Flask(__name__)
CORS(app)


# ------------------Kevin前端JSON 欄位資料------------------------------
@app.route("/AIspeak/resumeData", methods=["POST"])
def add_resume():
    if request.method == 'POST':
        data = request.get_json()
        save_directory = './json'
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        filename = f"{uuid.uuid4()}.json"
        filepath = os.path.join(save_directory, filename)
        
        formatted_data = [
            {
                "resumeData": [
                    {
                        "resumeName": data.get("resumeName", ""),
                        "resumeField1": data.get("resumeField1", ""),
                        "resumeField2": data.get("resumeField2", ""),
                        "resumeField3": data.get("resumeField3, handsome", ""),
                        "resumeAutobiography": data.get("resumeAutobiography", "")
                    }
                ]
            }
        ]

        # 保存數據
        with open(filepath, 'w') as json_file:
            json.dump(formatted_data, json_file)
        
        return jsonify({"message": "JSON file created", "filename": filename}), 201
        
    else:
        return jsonify({"message": "No data structure available to update"}), 404
    

# ----------------------------面試官JSON ------------------------------
@app.route("/AIspeak/aiQuestion", methods=["POST"])
def add_aiQuestiion():
    if request.method == 'POST':
        data = request.get_json()
        save_directory = './json'
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        filename = f"{uuid.uuid4()}.json"
        filepath = os.path.join(save_directory, filename)
        
        formatted_data = [
            {
                "aiQuestion": [
                    {
                        "q1": data.get("q1", ""),
                        "q2": data.get("q2", ""),
                        "q3": data.get("q3", ""),
                        "q4": data.get("q4", ""),
                        "q5": data.get("q5", "")
                    }
                ]
            }
        ]

        # 保存數據
        with open(filepath, 'w') as json_file:
            json.dump(formatted_data, json_file)
        
        return jsonify({"message": "JSON file created", "filename": filename}), 201
        
    else:
        return jsonify({"message": "No data structure available to update"}), 404
    
@app.route('/AIspeak/get_Json/<filename>', methods=['GET'])
def get_json(filename):
    directory = './json'
    try:
        return send_from_directory(directory, filename)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    
@app.route('/AIspeak/delete_Json/<filename>', methods=['DELETE'])
def delete_json(filename):
    directory = './json'
    file_path = os.path.join(directory, filename)
    try:
        os.remove(file_path)
        return jsonify({"message": "File deleted successfully"}), 200
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --------------------初版-----------------------------------------------
# 獲取所有用戶的信息
# @app.route("/resume", methods=["GET"])
# def get_user():
#     return jsonify({"users": users})

# # 創建新的用戶
# @app.route("/resume", methods=["POST"])
# def create_user():
#     request_data = request.get_json()
#     new_user = {"name": request_data["name"], "message": [], "llm_anwser": []}
#     users.append(new_user)
#     save_users(users)  # 保存到 JSON 檔案
#     return jsonify(new_user), 201

# # 在指定用戶中添加訊息
# @app.route("/resume/<string:name>/message", methods=["POST"])
# def add_message_to_user(name):
#     request_data = request.get_json()
#     for user in users:
#         if user["name"] == name:
#             new_message = request_data["message"]
#             user["message"].append(new_message)
#             save_users(users)  # 保存到 JSON 檔案
#             return jsonify({"message": f"Course {new_message} added to user {name}"}), 201
#     return jsonify({"message": "usesr not found"}), 404

# ---------------------------------------------------------------------



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)