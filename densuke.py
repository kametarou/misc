# 入力：yyyy m

import calendar
import sys

SUNDAY=6
youbi={0:'(月)', 1:'(火)',2:'(水)',3:'(木)',4:'(金)',5:'(土)',6:'(日)'}

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python densuke.py yyyy m")
    cal=calendar.Calendar(SUNDAY) # 日曜始まりのカレンダーを生成
    year=sys.argv[1]
    month=sys.argv[2]
    cal_thismonth=cal.itermonthdays2(int(year),int(month))
    print("イベント名: 研究室に行く予定("+year+"年"+month+"月)\n")
    print("イベント説明文: 行く気満々の場合には'○'を、もしかしたら行くかも〜という場合には'△'をつけてください\n")
    for day in cal_thismonth:
        if(day[0]>0): # 前月分は無視する
            print(month+'月'+str(day[0])+'日'+youbi[day[1]]+'-12時')
            print(month+'月'+str(day[0])+'日'+youbi[day[1]]+'12時-17時')
            print(month+'月'+str(day[0])+'日'+youbi[day[1]]+'17時-')
