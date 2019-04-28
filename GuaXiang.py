# -*- encoding: utf-8 -*-
import base64
import re
import os

permutation_table = {
    '乾'  :'A',
    '坤'  :'B',
    '屯'  :'C',
    '蒙'  :'D',
    '需'  :'E',
    '讼'  :'F',
    '师'  :'G',
    '比'  :'H',
    '小畜':'I',
    '履'  :'J',
    '泰'  :'K',
    '否'  :'L',
    '同人':'M',
    '大有':'N',
    '谦'  :'O',
    '豫'  :'P',
    '随'  :'Q',
    '蛊'  :'R',
    '临'  :'S',
    '观'  :'T',
    '噬咳':'U',
    '贲'  :'V',
    '剥'  :'W',
    '复'  :'X',
    '无妄':'Y',
    '大畜':'Z',
    '颐'  :'a',
    '大过':'b',
    '坎'  :'c',
    '离'  :'d',
    '咸'  :'e',
    '恒'  :'f',
    '遁'  :'g',
    '大壮':'h',
    '晋'  :'i',
    '明夷':'j',
    '家人':'k',
    '睽'  :'l',
    '蹇'  :'m',
    '解'  :'n',
    '损'  :'o',
    '益'  :'p',
    '夬'  :'q',
    '姤'  :'r',
    '萃'  :'s',
    '升'  :'t',
    '困'  :'u',
    '井'  :'v',
    '革'  :'w',
    '鼎'  :'x',
    '震'  :'y',
    '根'  :'z',
    '渐'  :'0',
    '归妹':'1',
    '丰'  :'2',
    '旅'  :'3',
    '巽'  :'4',
    '兑'  :'5',
    '涣'  :'6',
    '节'  :'7',
    '中孚':'8',
    '小过':'9',
    '既济':'+',
    '未济':'/',
}

def coding():
    os.system("cls")
    source = input("请输入磁力链接：")
    pattern = re.compile('.{1,1}')
    source = ('\x00'.join(pattern.findall(source)))
    sou_base = str(base64.b64encode(source.encode('utf-8')))[2:-1].replace('=','A')
    for (k,v) in permutation_table.items():
        sou_base = sou_base.replace(v,k)
    print(sou_base)
    os.system("pause")

def decoding():
    os.system("cls")
    cipher = input("请输入加密卦象：")
    for (k,v) in permutation_table.items():
        cipher = cipher.replace(k,v)
    source = str(base64.b64decode(cipher))[2:-1].replace('\\x00','')
    print(source)
    os.system("pause")

def main():
    while True:
        os.system("cls")
        choose = int(input("（1、加密/2、解密/0、退出）\n选择磁力链接编解码："))
        
        if choose == 1:
            coding()
        elif choose == 2:
            decoding()
        elif choose == 0:
            exit()
        else:
            print("ERROR!Please Reinput the number!")

main()