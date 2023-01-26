# dwg-to-dxf

dwg ファイルを dxf に変換する

# ビルド

```sh
docker build --rm -t dwg-to-dxf .
```

# 利用方法

1. 変換したいファイルを input ディレクトリに配置する。
2. 下記のコマンドを実行する。

```sh
docker run --rm -it -v $(pwd):/app dwg-to-dxf
```

3. output ディレクトリに出力される。
