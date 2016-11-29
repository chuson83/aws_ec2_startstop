#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import boto3

# 引数で指定されたインスタンスidを取得
instanceIds = sys.argv
if len(instanceIds) < 2:
        print '引数にEC2インスタンスidを指定してください'
        sys.exit()

del instanceIds[0]      # 最初の引数は実行ファイル名なので削除する

# ec2オブジェクト生成
ec2 = boto3.resource('ec2')

# インスタンスIDを回す
for instanceId in instanceIds:
        instance = ec2.Instance(instanceId)

        #ステータスを見て起動してたら停止、停止してたら起動をする
        status = instance.state
        if status['Code'] == 16:
                #起動しているので停止
                instance.stop()
        elif status['Code'] == 80:
                #停止しているので起動
                instance.start()

sys.exit()