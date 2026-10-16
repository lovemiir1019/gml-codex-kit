# 既存ツールを調べて、重複する実装を避ける

調査日: 2026年10月16日。公開リポジトリの説明とライセンス表示を確認しました。
下表は作者側の説明を整理したものです。本キットで各ツールをインストール・実行して互換性を検証した結果ではありません。

| 候補 | 役割 | 本キットでの位置づけ |
| --- | --- | --- |
| [YoYoGames/gm-cli](https://github.com/YoYoGames/gm-cli) | 公式CLI。編集、ビルド、実行、ResourceToolのMCP連携。Apache-2.0 | 環境を拡張する場合の第一候補 |
| [Ampersand-Game-Studios/gms-mcp](https://github.com/Ampersand-Game-Studios/gms-mcp) | 非公式。Codex等からの資産操作、診断、ビルド、任意の実行中ゲーム連携。MIT | 公式機能で足りない用途を検討するときの候補 |
| [leihaht/gamemaker-skills](https://github.com/leihaht/gamemaker-skills) | Claude Code向けのGMLスキルと参照資料。MIT | 既存のGMLスキルがあることを確認。対象クライアントや指示の妥当性は導入前に検討 |
| [Petah/gamemaker-mcp](https://github.com/Petah/gamemaker-mcp) | GMLマニュアルの検索・関数参照 | 版の鮮度と文書の配布条件を確認した上で検討 |
| [GameMakerDiscord/gml-tools-langserver](https://github.com/GameMakerDiscord/gml-tools-langserver) | GMS2向けの診断、補完、定義参照 | エディター支援。日本語からコードを作るAIそのものではない |
| [nutt-y/seams](https://github.com/nutt-y/seams) | 開発途中のGML言語サーバー | エディター支援の別候補 |

## このキットで追加する範囲

日本語の要望からコードへ進む導線、CodexとChatで共有するGMLルール、手動で適用する手順、切り替え時の引き継ぎをまとめます。
GMLのコンパイラー、言語サーバー、GameMaker資産管理、独自MCPサーバーは新規実装しません。
基本機能には追加のMCPを必須にしません。通常のChatでは、ローカルのMCP接続がある前提を置きません。

## 採用を決めるとき

対応するGameMakerの版、保守状況、依存関係、ライセンス、設定の変更範囲を確認します。
ツール自体のライセンスが無償でも、接続するAIサービスやゲームの配布条件まで無償になるとは限りません。
本キットには第三者コードとマニュアル本文をコピーせず、公式資料や元リポジトリへのリンクを載せています。
