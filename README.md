# aws_ec2_startstop

## 概要
pythonで作成したawsのec2インスタンスを停止しているものは起動、起動しているものは停止するバッチです。  
boto3を利用しています。  
[boto3詳細（公式）](https://boto3.readthedocs.io/en/latest/)  
python2系で動きます

## 環境
環境：AmazonLinux(pipインストール済み)  
python: 2.7.10（最初から入っているもの）

## セットアップ
awscli インストール
```
sudo pip install awscli
aws configure
#作成した適切なIAMの各種情報を設定
```
boto3 インストール
```
sudo pip install boto3
```

## 実行
aws_ec2_startstop.pyを任意の場所に設置し実行
```
python aws_ec2_startstop.py インスタンスid インスタンスid ...
```
※引数にインスタンスidを指定すればそのインスタンスを停止、起動します（複数可）  
※cronに設置すれば開発サーバなどを深夜止めて経費節約などに利用できます
