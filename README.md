# issue-webdriber-chromium-119

chromium=119 の環境で chromedriver-binary=118 が動かなかったので再現

普段はバージョンが変わると`This version of ChromeDriver only supports Chrome version XX Current browser version is YY`というメッセージとともにエラー終了するが、今回は実行されるまでエラーにならなかった。

## 再現方法

1. devcontainer で立ち上げ
2. chromium=119をinstall
  a. `apt-get install chromium=119` みたいな方法は使えない？ひとまず`apt-get install chromium`で119をinstall
3. `pip install -r requirements.txt`
4. `python main.py`を実行すると`selenium.common.exceptions.WebDriverException: Message: unknown error: result.webdriverValue.value list is missing or empty in Runtime.callFunctionOn response`
