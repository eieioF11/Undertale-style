# Undertale-style
Undertale風のゲーム作成用リポジトリ
# 環境構築
pythonバージョン:3.7.8
## pygameインストール
```bash
pip install pygame
```
## 上のコマンドでインストールできない場合
pygameディレクトリに移動もしくは[このページ](https://pypi.org/project/pygame/#files)で使用しているpythonバージョンのwhlファイル
をダウンロードし,以下のようなコマンドを入力してインストールする(installのあとのファイル名はダウンロードしてきたものに替える)\
以下はpythonバージョン3.8.5の64bit環境の例
```bash
 python -m pip install .\pygame-2.0.2-cp38-cp38-win_amd64.whl
```
pythonのパスが通っていない場合は以下のようにpython.exeの場所のパスを指定する
```bash
 & C:/ProgramData/Anaconda3/python.exe -m pip install .\pygame-2.0.2-cp38-cp38-win_amd64.whl
```

# pygame参考
[図形表示](https://shizenkarasuzon.hatenablog.com/entry/2018/12/29/213355)\
[キー入力](https://shizenkarasuzon.hatenablog.com/entry/2019/02/08/184932)\
[画像入力](https://shizenkarasuzon.hatenablog.com/entry/2019/02/23/151418)
