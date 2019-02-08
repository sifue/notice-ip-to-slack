ボット名のメンションを飛ばすと `ip addr` の結果を教えてくれるSlackbotのPython3のデーモン

# 前提

python3の環境を用意して、

```
sudo pip3 install slackbot
```

でslackbotをインストールしておく。

# 使い方

```
cp slackbot_settings_template.py slackbot_settings.py
vi slackbot_settings.py
```

にて Slack のボットトークンを設定。

```
# -*- coding: utf-8 -*-

API_TOKEN = "xoxb-yourbottoken"

default_reply = "notice-ip-to-slack running."
```

以上のように設定の後、

```
python3 run.py
```

以上で動作確認。ボットに @ボット名 でメンションを送ることで、ip addr の結果を返してくれる。

# デーモン化

```
vi noticeiptoslack.service
```

ExecStartのパスだけを`run.py`への正しいパスに変更。

```
[Unit]
Description=NoticeIpToSlack

[Service]
ExecStart=/home/pi/workspace/notice-ip-to-slack/run.py
Restart=always
Type=forking
PIDFile=/var/run/notice-ip-to-slack.pid

[Install]
WantedBy=multi-user.target
```

その後デーモン化、

```
sudo chmod 755 -R .
cp noticeiptoslack.service /usr/lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start noticeiptoslack.service
```

これでデーモンとして起動できる。

```
sudo systemctl status noticeiptoslack.service
```

でステータス確認。

```
sudo systemctl stop noticeiptoslack.service
```

以上で終了。


なお、起動時に自動的に起動するには、

```
sudo systemctl enable noticeiptoslack.service
```

自動起動解除、するには


```
sudo systemctl disable noticeiptoslack.service
```

となり、自動起動するサービス一覧は、

```
sudo systemctl list-unit-files  -t service
```

で確認できる。

これで自動起動しておくと、Raspberry PI などを起動して、ネットワークに繋いだ後、
Slack上でボットアカウントがアクティブになるので @ボット名 でメンションを飛ばすと
そのIPがわかるようになる。


