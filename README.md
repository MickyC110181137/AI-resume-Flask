09/06
我們目前只有本地可以使用，所以要測試只能clone下來  
然後會需要你按照 指令.txt 裝個python的虛擬環境，我是用conda  

環境弄好之後運行app.py，之後就可以測試API了，本地的網址是http://127.0.0.1:8080
然後你的語音需要的題目與答案是http://127.0.0.1:8080/AIspeak  
你可以看到JSON檔
然後POST的話你會回傳給我使用者的答案所以就用postman去測http://127.0.0.1:8080/AIspeak/userAnswer  
下面是資料的格式

增加  
get http://127.0.0.1:8080/AIspeak

post http://127.0.0.1:8080/AIspeak/aiQuestion  
{  
    "q1": "44444444444444444444 you good?",  
    "q2": "333333333333333",  
    "q3": "22222222222222",  
    "q4": "11111111111111",  
    "q5": "hhhhhhhh3333333333333333hhhhhhhh"  
}  
post http://127.0.0.1:8080/AIspeak/userAnswer  
{  
    "a1": "ffffffffffffffff you good?",  
    "a2": "sssssssssssssssss",  
    "a3": "ddddddddddddd",  
    "a4": "eeeeeeeeeeeeee",  
    "a5": "jujjjjjjjjjjjjjjjjjjjjjjj"  
}  
