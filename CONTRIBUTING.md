# 改善に参加する

再現できる相談例、動いた環境、うまくいかなかった点をIssuesやPull Requestで共有してください。

## 問題を報告するとき

- Codex版かChat版か
- GameMakerのIDE・Runtimeの版、出力先
- 日本語で頼んだ内容と、対象オブジェクト・イベント
- 必要な範囲のコード、エラー全文、再現操作
- 期待した結果と実際の結果

## 共通ルールを直すとき

`.agents/skills/gml-gamemaker/references/gml-rules.md` を編集し、次を実行してChat用の指示文を更新します。利用者が通常使うだけならPythonは不要です。

```text
python tools/build_chat_prompt.py
python tools/build_chat_prompt.py --check
```

Codex固有の作業手順はSKILL.md、Chat固有の説明は `chat/chat-mode.md` に置きます。
新しい指示は、実際に起きた問題と、指示が改善する範囲を説明してください。一度の失敗からすべての作業に重い制約を追加しないようにします。

## サンプルを追加するとき

対象版、必要なオブジェクト・イベント・資産、導入手順、操作と期待結果を添えます。
ソースの点検、ビルド、実行、操作確認を分け、実際に行った確認だけを記録します。
第三者コードやマニュアル本文を転載する場合は、先に配布条件と帰属表示を確認してください。
