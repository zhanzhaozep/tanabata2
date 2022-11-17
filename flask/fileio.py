# ファイルを作成する; 書き込み(w)モード
#  open('ファイル名', 'w')			w => write （書く）
file = open('aloha.txt', 'w')

# ファイルに書き込む
file.write('ALOHA!')

# ファイルを閉じる（保存する）
file.close()

# ファイルを開く （古いデータも、保存する = 消さない）
file = open('aloha.txt', 'a')

# 新しいデータを書く
file.write('hello')

# ファイルを保存する
file.close()