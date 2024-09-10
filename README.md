09/06
我們目前只有本地可以使用，所以要測試只能clone下來  
然後會需要你按照 指令.txt 裝個python的虛擬環境，我是用conda  
![image](https://github.com/MickyC110181137/AI-resume-Flask/blob/main/txt/%E6%8C%87%E4%BB%A4.png)  
環境弄好之後運行app.py，之後就可以測試API了，  
本地的網址是http://127.0.0.1:8080   
使用POST會回傳一個uuid.json, 再用uuid.json, 去get JSON  
![image](https://github.com/MickyC110181137/AI-resume-Flask/blob/main/txt/postman.png)  

GET http://127.0.0.1:8080/AIspeak/get_Json/檔名.json 

DELETE http://127.0.0.1:8080//AIspeak/delete_Json/檔名.json  

這個是我用來改面試官的問題  
POST http://127.0.0.1:8080/AIspeak/aiQuestion  
{  
    "q1": "44444444444444444444 you good?",  
    "q2": "333333333333333",  
    "q3": "22222222222222",  
    "q4": "11111111111111",  
    "q5": "hhhhhhhh3333333333333333hhhhhhhh"  
}  

這個是賴你用來傳資料給我  
POST http://127.0.0.1:8080/AIspeak/resumeData  
{  
    "resumeName":"Kevin",  
    "resumeField1":"javascript, react",  
    "resumeField2":"man",  
    "resumeField3":"talent, handsome",  
    "resumeAutobiography":"dskljfkdsjfkdsjfdskfsadfsdfsdafewfewr"  
}  