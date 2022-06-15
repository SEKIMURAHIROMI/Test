from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'myapp/index.html',{'data':['Hello', 'new', 'world']})

                  # render関数は3つの引数が必要（request, <表示したいhtmlを指定>,{<htmlに渡したいデータ>}）
                  # 第１引数 ここは必須（index.htmlからリクエストがあった場合データが来る）
                  # 第２引数 ここも必須、表示させたいhtmlを指定する
                  # 第３引数 ここはデータがない場合{}だけでOK,主にhtmlに送るデータ(データベースから引っ張ったりなど