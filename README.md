# スクラムガイド拡張パック 2025.6（日本語版）

本リポジトリは、[Scrum Guide Expansion Pack](https://scrumexpansion.org/ja/scrum-guide-expansion-pack/2025.6/)の内容を読みやすい形に再構成したものです。

## 📖 目次

1. [背景と目的](docs/01-background.md)
   - [背景](docs/01-background.md#背景)
   - [スクラムガイド拡張パックの目的](docs/01-background.md#スクラムガイド拡張パックの目的)
   - [スクラム早わかり](docs/01-background.md#スクラム早わかり)

2. [支援・補完理論](docs/02-scrum-basics.md)
   - [複雑性-スクラムである理由](docs/02-scrum-basics.md#複雑性-スクラムである理由)
   - [創発](docs/02-scrum-basics.md#創発)
   - [自己管理スクラムチーム](docs/02-scrum-basics.md#自己管理スクラムチーム)
   - [プロフェッショナリズム](docs/02-scrum-basics.md#プロフェッショナリズム)
   - [リーン思考](docs/02-scrum-basics.md#リーン思考)
   - [経験主義](docs/02-scrum-basics.md#経験主義)
   - [ケイデンス](docs/02-scrum-basics.md#ケイデンス)
   - [スクラムの経験的プロセス制御の三本柱](docs/02-scrum-basics.md#スクラムの経験的プロセス制御の三本柱)
     - [透明性](docs/02-scrum-basics.md#透明性)
     - [検査](docs/02-scrum-basics.md#検査)
     - [適応](docs/02-scrum-basics.md#適応)
   - [スクラムの価値基準](docs/02-scrum-basics.md#スクラムの価値基準)

3. [さらなる支援・補完理論](docs/03-theory.md)
   - [プロダクト思考](docs/03-theory.md#プロダクト思考)
   - [システム思考](docs/03-theory.md#システム思考)
   - [ディスカバリー](docs/03-theory.md#ディスカバリー)
   - [リーダーシップ](docs/03-theory.md#リーダーシップ)
   - [第一原理思考](docs/03-theory.md#第一原理思考)
   - [人と変化](docs/03-theory.md#人と変化)

4. [拡張パックにおけるスクラムの役割](docs/04-roles.md)
   - [ステークホルダー](docs/04-roles.md#ステークホルダー)
   - [サポーター](docs/04-roles.md#サポーター)
   - [人工知能](docs/04-roles.md#人工知能)
   - [プロダクト開発者](docs/04-roles.md#プロダクト開発者)
   - [プロダクトオーナー](docs/04-roles.md#プロダクトオーナー)
   - [スクラムマスター](docs/04-roles.md#スクラムマスター)

5. [拡張パックにおけるスクラムの作成物](docs/05-artifacts.md)
   - [プロダクト](docs/05-artifacts.md#プロダクト)
   - [インクリメント](docs/05-artifacts.md#インクリメント)
   - [プロダクトバックログ](docs/05-artifacts.md#プロダクトバックログ)
   - [スプリントバックログ](docs/05-artifacts.md#スプリントバックログ)

6. [拡張パックにおけるスクラムイベント](docs/06-events.md)
   - [スプリント](docs/06-events.md#スプリント)
   - [スプリントプランニング](docs/06-events.md#スプリントプランニング)
   - [デイリースクラム](docs/06-events.md#デイリースクラム)
   - [スプリントレビュー](docs/06-events.md#スプリントレビュー)
   - [スプリントレトロスペクティブ](docs/06-events.md#スプリントレトロスペクティブ)

7. [複数スクラムチームプロダクト](docs/07-multi-team.md)
   - [複数スクラムチームプロダクト](docs/07-multi-team.md#複数スクラムチームプロダクト)

8. [最後に](docs/08-conclusion.md)
   - [最後に](docs/08-conclusion.md#最後に)
   - [スクラム拡張版 1ページ要約](docs/08-conclusion.md#スクラム-拡張版-1ページ要約)
   - [拡張ログ](docs/08-conclusion.md#拡張ログ)

9. [付録](docs/09-appendix.md)
   - [付録（詳細なガイダンス）](docs/09-appendix.md#付録)
   - [帰属情報](docs/09-appendix.md#スクラムガイド拡張パックにおける収録資料の帰属情報)
   - [翻訳について](docs/09-appendix.md#翻訳について)
   - [参考文献](docs/09-appendix.md#参考文献)
   - [用語集](docs/09-appendix.md#スクラムガイド拡張パック用語集)

## 📄 原文

- 日本語版: https://scrumexpansion.org/ja/scrum-guide-expansion-pack/2025.6/
- 英語版: https://scrumexpansion.org/scrum-guide-expansion-pack/2025.6/

## ⚖️ ライセンスと帰属

**重要**: 著者、翻訳者、ライセンス、著作権の詳細については、[NOTICE.md](NOTICE.md)を必ずお読みください。

### 本リポジトリのライセンス

このリポジトリの構造化、README、ナビゲーション要素は、MIT Licenseの下で提供されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

### コンテンツのライセンス

`docs/`ディレクトリに含まれるスクラムガイド拡張パックのコンテンツは、Creative Commons Attribution-ShareAlike 4.0 International ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/))ライセンスで提供されています。詳細は[NOTICE.md](NOTICE.md)を参照してください。

## 📝 使用上の注意

- 本リポジトリは、学習・参照を容易にするための構造化を行ったものです
- コンテンツの内容に関する質問や貢献は、[オリジナルリポジトリ](https://github.com/ScrumGuides/ScrumGuide-ExpansionPack)へお願いします
- コンテンツの再配布や改変を行う場合は、CC BY-SA 4.0ライセンスの条件に従ってください

## 🔗 関連リンク

- [スクラムガイド公式サイト](https://scrumguides.org/)
- [Scrum Guide Expansion Pack 公式サイト](https://scrumexpansion.org/)
- [オリジナルリポジトリ](https://github.com/ScrumGuides/ScrumGuide-ExpansionPack)