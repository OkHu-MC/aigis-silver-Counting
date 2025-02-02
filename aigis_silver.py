import tkinter as tk
from functools import partial as ftpl

d = ["ソルジャー","ヘビーアーマー","ワルキューレ","ローグ","バンデッド","天使","竜兵","侍","神官戦士","アーチャー","メイジ","ヒーラー","ウィッチ","パイレーツ","ヴァンパイアハンター","砲術士","ビショップ"]
import os
import webbrowser as wb
from urllib.parse import quote
import time
def string_to_data_uri(data, mime_type="text/plain;charset=utf-8"):
  """
  文字列をData URIに変換する関数

  Args:
    data: 変換する文字列
    mime_type: Data URIのMIMEタイプ (デフォルト: text/plain;charset=utf-8)

  Returns:
    Data URI文字列
  """
  encoded_data = quote(data.encode("utf-8"))
  return f"data:{mime_type},{encoded_data}"

class main_window:
    def __init__(self,a):
        self.root =tk.Tk()
        self.root.title("アイギスのCC銀必要数確認用")
        self.root.geometry("440x300")
        self.w =[]
        self.val =[]
        self.fr =[]
        self.l=[]
        for i,val in enumerate(a):  #a=range(17)
            print(i)
            fr = tk.Frame(self.root,width=100)
            print(i) #0~16まで表示される
            self.w.append(tk.Button(fr,text=f"{'0'.zfill(3)}",command=ftpl(self.add,i)))
            self.l.append( tk.Label(fr,text=f"{val}",anchor="n"))
            self.val.append(0)
            self.fr.append(fr)
            
            self.l[-1].pack()#(x=0,y=30)
            self.w[-1].pack()#(x=0,y=0)
            #20
            self.fr[-1].place(x=(i%5)*75+20,y=(i//5)*70+5)
        self.b =tk.Button(self.root,text="出力",font=("",20),command=self.dump,anchor="sw")
        self.b.place(x=300,y=200)
    def add(self,k):
        self.val[k]+=1
        self.w[k]["text"]=str(self.val[k]).zfill(3)
        print(k)    #常に16になる
    def dump(self):
       # fn =  filedialog.asksaveasfilename(initialdir =os.getcwd(),title = "名前を付けて保存",filetypes =  [("text file","*.txt")],initialfile="aigis.txt")
        #print(fn)
        #if fn=="":
         #   return
        #with open(fn, 'w',encoding="utf-8") as f:
        st ='<h3>このhtmlは一時ファイルとして既に削除されています。保存したい場合はctrl+sを押してください</h3>\n<br><table>\n  <caption>アイギスCC銀消費数</caption>\n     <thead><tr><th scope="col">クラス名</th><th scope="col">使用数</th></tr></thead>\n  <tbody>'
        for j,fv in  enumerate(d):
            st +=f'<th scope="row">{fv}</th>\n'
            st +=f'<td>{self.val[j]}</td><tr>\n'
    
        st +="</tbody></table>"
       # fn =filedialog.asksaveasfilename(initialdir =os.getcwd(),title = "名前を付けて保存",filetypes =  [("html file","*.html")],initialfile="aigis.html")
        fn =os.getcwd()+"\\aigis-銀ユニット必要数.html"
        with open(fn,"w",encoding="utf-8") as f:
            f.write(st)
        wb.open(f"file://{fn}")
        time.sleep(1)
        os.remove(fn)
        #wb.open(f"data:text/html,{base64.b64encode(st.encode())}")
      #  wb.open(string_to_data_uri(st,"text/html;charset=utf-8"))
if __name__=="__main__":
    main = main_window(d)
    main.root.mainloop()