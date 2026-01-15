# 背景と目的

[← 前へ](../README.md) | [目次](../README.md) | [次へ →](02-scrum-basics.md)

---

<!--
このコンテンツは、Scrum Guide Expansion Pack (https://scrumexpansion.org) から取得したものです。

著者: Ralph Jocham、John Coleman、Jeff Sutherland
翻訳: 内山遼子、川口恭伸、長沢智治、山本尊人、和田圭介
ライセンス: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
出典: https://github.com/ScrumGuides/ScrumGuide-ExpansionPack

詳細は NOTICE.md を参照してください。
-->

## 背景 {#背景}

<!-- Ken Schwaber and Jeff Sutherland led the development of the Scrum framework. The [2020 Scrum Guide](https://scrumguides.org/) (40) describes the Scrum Essentials. Tobias Mayer's [A Simple Guide to Scrum](https://scrum.academy/guide/) (58) is a shortened, edited version of the official Scrum Guide by Ken Schwaber and Jeff Sutherland. The [Scrum Hexis](https://thecynefin.co/product/hexi-scrumorg/?srsltid=AfmBOorcohLYeVy0qBsQFI6mK_bZtJA_uGC6hPL2BdptiTwNmMwpKTQv%20) (52) elaborate on the 2020 Scrum Guide (40) from a 2025 perspective. For mass adoption, the Scrum Guide (40) needed to be simple. -->

Ken SchwaberとJeff Sutherlandがスクラムフレームワークの開発を主導した。[2020年版スクラムガイド](https://scrumguides.org/)(40)はスクラムの本質を説明している。Tobias Mayerの[A Simple Guide to Scrum](https://scrum.academy/guide/)(58)は、Ken SchwaberとJeff Sutherlandによる公式スクラムガイドの短縮編集版である。[スクラム ヘキシス](https://thecynefin.co/product/hexi-scrumorg/?srsltid=AfmBOorcohLYeVy0qBsQFI6mK_bZtJA_uGC6hPL2BdptiTwNmMwpKTQv%20)(52)は2025年の視点から2020年版スクラムガイド(40)を詳述している。スクラムが広い範囲で採用されるために、スクラムガイド(40)はシンプルである必要があった。

<!-- ## Purpose of the Scrum Guide Expansion Pack {#purpose-of-the-scrum-guide-expansion-pack} -->

## スクラムガイド拡張パックの目的 {#スクラムガイド拡張パックの目的}

<!-- For a more successful adoption, this Expansion Pack offers additional guidance for current times, based on the 2020 Scrum Guide by Ken Schwaber and Jeff Sutherland (40). Ralph Jocham's contribution (89) to the 2020 Scrum Guide provided additional depth in bringing the original ideas of the 2020 Scrum Guide (40) into this expansion pack. -->

スクラムの導入をより成功させるため、この拡張パックは、Ken SchwaberとJeff Sutherlandによる2020年版スクラムガイド(40)を基に、現在の状況に合わせた追加のガイダンスを提供する。Ralph Jochamの2020年版スクラムガイド(40)への貢献(89)により、2020年版スクラムガイド(40)のオリジナルなアイデアをさらに深掘りした内容がこの拡張パックに追加された。

<!-- This Scrum Guide Expansion Pack explains the _what_ and _why_ of each element of Scrum through a future-looking lens. Each element serves a specific purpose and contributes to the overall value and results realized with Scrum. This Expansion Pack will evolve regularly. The reader is expected to read the document sequentially, at least the first time. -->

このスクラムガイド拡張パックは、未来を見通すレンズを通じてスクラムの各要素の _何_ と _なぜ_ を説明する。各要素は特定の目的を担い、スクラムで実現される全体的な価値と結果に貢献する。この拡張パックは継続的に進化していく予定だ。読者には前から順に読んでいくことを期待している。少なくとも一度目はそうしてほしい。

<!-- This document assumes some fluency with Scrum and its related language. It could be helpful to read the 2020 Scrum Guide first before reading this document. References are included for attribution purposes. The appendix and references provide an opportunity for the reader to explore, research and learn to gain a broader and deeper understanding. -->

本書は、スクラムおよび関連用語について、ある程度理解している読者を想定している。この文書を読む前に、2020年版スクラムガイドを読んでおくと役立つだろう。出典明示のため、参考文献を記載している。付録と参考文献は、読者がより広く深い理解を得るために探求し、研究し、学習する機会を提供する。

<!-- Practitioners and stakeholders should adopt Scrum when appropriate, with agency, urgency, courage, transparency, inspection, adaptation, rhythm, and resilience, and continually improve to support goals for the product and the organization. It is hoped that Scrum adoptions will surpass the guidance presented here—across theory, roles, artifacts, events, scaling, and every other facet addressed in this document—and, in doing so, inspire a lasting curiosity to explore, question, and continually improve. -->

実践者とステークホルダーは、以下を満たす場合にスクラムを採用すべきである。すなわち、主体性・緊急性・勇気・透明性・検査・適応・リズム・回復力を持って、プロダクトと組織の目標を支援すべく継続的に改善している場合である。スクラムを適用することで、この文書で提示されたガイダンスを超越することを期待している。すなわち、理論・役割・作成物・イベント・スケーリング・その他のすべての面である。持続的な好奇心を持って、探求・問い・継続的な改善へと繋げてほしい。

<!-- This Expansion Pack is designed to support all aspects of product delivery by a self-managing team (49) driven by stakeholder needs or wants in response to a problem or opportunity. This includes (but is not limited to) product discovery, development, delivery, and value realization. While originally rooted in software product development, Scrum has been widely adopted across various domains, enabling the delivery of value through complex (30-35) work. As its use expands, professionals such as engineers, programmers, researchers, analysts, lawyers, marketers, and scientists increasingly apply Scrum successfully to their fields. -->

この拡張パックは、自己管理チーム(49)によるプロダクトデリバリーのすべての側面を支援するよう設計されている。そうしたチームは、問題や機会に対するステークホルダーのニーズや要望を原動力としている。これにはプロダクト発見・開発・デリバリー・価値実現が含まれる（ただしこれらに限定されない）。もともとソフトウェアプロダクト開発から始まったスクラムは、現在は多様な領域で幅広く採用され、複雑な(30-35)仕事を通じた価値の提供を可能にしている。利用が拡大するにつれ、エンジニア・プログラマー・研究者・アナリスト・弁護士・マーケター・科学者などの専門家が、それぞれの分野でスクラムを効果的に適用する例が増えている。

<!-- Stakeholder value refers to any perceived need that a stakeholder (including but not limited to customers, decision-makers, and users) considers important and that a team delivers. However, stakeholders may not always be aware of what could be valuable to them. Observation or evidence could intentionally or unintentionally surface value and influence priorities. As new information arises, potentially valuable items should be identified, inspected, refined, and adapted. Value remains an assumption until confirmed by evidence, such as observation or measured outcomes. -->

ステークホルダー価値とは、ステークホルダーが重要と考え、チームが提供する、あらゆるニーズである（ステークホルダーには顧客、意思決定者、ユーザーを含むがこれらに限定されない）。ただしステークホルダー自身が、自分たちにとって価値あるものが何であるかを、かならずしも認識しているわけではない。観察やエビデンスを通じて、意図的もしくは意図しないところで価値が顕在化し、それが優先順位に影響を与えることがある。新しい情報が出てきたら、潜在的に価値のあるアイテムを特定し、検査し、リファインし、適応させるべきである。価値とは、観察や計測されたアウトカムなどのエビデンスによって確認されるまでは、あくまで仮説にすぎない。

<!-- ## Scrum in a Nutshell {#scrum-in-a-nutshell} -->

## スクラム早わかり {#スクラム早わかり}

<!-- Scrum is a framework for complex (30-35) Product delivery, where expertise is valuable but more than expertise is needed, and cause and effect are only coherent in retrospect. Scrum addresses the full Product lifecycle, which includes (but is not limited to) creating, replacing, sustaining, adapting, continuously changing, maintaining, and retiring Products or features. Scrum helps individuals, teams, and organizations become and stay flexible and create value by adapting to change. -->

スクラムは、複雑な(30-35)プロダクトデリバリーのためのフレームワークである。専門性の価値を認めつつも、専門性を超えたものが必要であり、原因と結果の関係は、後から振り返ってこそ見えてくるものである。スクラムは、プロダクトライフサイクル全体をカバーする。そこには、プロダクトや機能の作成・置換・維持・適応・継続的変更・保守・廃止が含まれる(ただしこれらに限定されない)。スクラムは、個人・チーム・組織が変化に適応し、柔軟性を保ちながら価値を創造するのを支援する。

<!-- Scrum fosters a setting for understanding and coherently responding to Stakeholder needs. Scrum's iterative and incremental approach reduces risk and fosters continuous improvement. Scrum helps a team to strike a balance between exploring problems, discovering Stakeholder (including but not limited to customer) needs, delivering solutions, proactively managing risk, and validating value. -->

スクラムはステークホルダーのニーズを理解し、一貫して対応するための環境を育む。スクラムのイテレーティブ（反復的）でインクリメンタル（漸進的）なアプローチはリスクを削減し、継続的改善を促進する。スクラムはチームが問題の探求、ステークホルダー（顧客を含むがこれに限定されない）のニーズの発見、ソリューションの提供、積極的なリスク管理、価値の検証のバランスを取ることを支援する。

<!--
A risk is any factor that could result in a future adverse consequence.
Since risk exposure remains unpredictable even as time elapses,
    anticipation is key.
Risk exposure can include (but is not limited to)
    market risk, problem-solution fit, Product-market fit,
    technology, signal detection, responsiveness, compliance,
    remediation, poor trade-off decisions, etc.
Scrum supports proactive risk management and opportunity discovery.
-->

リスクとは、今後不利な結果をもたらしうる何らかの要因のことである。
時間が経過してもリスクエクスポージャー（リスクの影響度）は予測不可能であり、
あらゆる状況を見越した備え（anticipation）が鍵になる。
リスクエクスポージャーには、次のものが含まれる（ただしこれらに限定されない）。
市場リスク、プロブレム-ソリューションフィット、プロダクト-マーケットフィット、
技術、シグナル検出、応答性、コンプライアンス、
修復・再発防止、不適切なトレードオフ判断など。
スクラムは積極的なリスク管理と機会発見を支援する。

<!-- Scrum encourages a reduction in the existing separation between Stakeholders who present problems or opportunities and the people solving them. -->

スクラムは、問題や機会を提示するステークホルダーとそれらを解決する人々の間にある距離を縮めることを奨励する。

<!-- In a nutshell, Scrum is based on an environment where: -->

一言で言うと、スクラムは以下のような環境に基づいている：

<!-- 1. Supporting Stakeholders, hereafter referred to as Supporters, doing what is requested to proactively support and enhance the adoption of Scrum, guided and supported by the Scrum Master. -->
<!-- 2. A Product Owner sets the Product Goal, instrumental in fulfilling Stakeholder value. -->
<!-- 3. The self-managing Scrum Team (49) defines, refines, and turns the selection of work into valuable outcomes. -->
<!-- 4. The Scrum Team and Stakeholders inspect the results during the Sprint and adapt. -->
<!-- 5. Supporters help the Scrum Team to thrive. -->
<!-- 6. _Repeat._ -->

1. サポートステークホルダー（以下、サポーター）は、スクラムマスターの指導と支援のもと、要求されたことを実行し、スクラムの採用を積極的に支援し、促進する。
2. プロダクトオーナーがプロダクトゴールを設定し、ステークホルダー価値の実現に貢献する。
3. 自己管理スクラムチーム(49)が、選択された作業を定義し、リファインメントし、価値あるアウトカムに変える。
4. スクラムチームとステークホルダーがスプリント中に結果を検査し、適応する。
5. サポーターがスクラムチームの成長と発展を支援する。
6. _繰り返し。_

<!-- A release is the process of making a new or updated version of a Product available to Stakeholders (including but not limited to customers, decision-makers, and end users). It marks an inflection point in the development cycle and represents the transition of the Product from development to availability for use and the potential realization of Stakeholder value. -->

リリースとは、プロダクトの新バージョンや更新版をステークホルダーが利用できるようにするプロセスである（ステークホルダーには顧客・意思決定者・エンドユーザーを含むが、これらに限定されない）。これは開発サイクルにおける転換点となる。プロダクトが開発段階から実際に使用可能な状態に移行し、ステークホルダー価値の可能性を具現化する。

<!-- Scrum is intentionally incomplete. Instead of prescribing detailed processes, it provides a framework that guides relationships and purposeful interactions. Various processes, techniques, and methods can complement Scrum, but their application depends on the context and varies across different uses of Scrum. -->

スクラムは意図的に不完全である。詳細なプロセスを規定する代わりに、関係性および意図的な相互作用を導くフレームワークを提供する。様々なプロセス・技術・手法によってスクラムを補完することができる。しかし、そうしたものの適用は文脈に依存し、スクラムの用途ごとに異なるものになる。

<!-- Scrum integrates with existing practices or, in some cases, makes them unnecessary or obsolete. By transparently assessing the effectiveness of the Scrum Team, Supporters, current management, work environment, and techniques, Scrum enables continuous improvement. -->

スクラムは既存の他のプラクティスと融合するが、場合によってはそれらを不要にしたり、置き換えることもある。スクラムチーム・サポーター・現在のマネジメント・作業環境・技術の効果性を、透明性高く評価することによって、スクラムは継続的な改善を可能にする。

<!-- In the context of knowledge work, the term Scrum, borrowed from the game of rugby, was coined by Takeuchi and Nonaka (29) to describe teams that worked this way and where knowledge was spread rapidly throughout an enterprise to deliver outstanding Products. -->

知識労働の文脈において、スクラムという用語は、竹内弘高と野中郁次郎(29)がラグビーというゲームから借用して考案したものである。これまでに述べたような働き方をし、優れたプロダクトを提供するため、企業全体に知識を急速に広めるチームを説明するために用いられている。

<!-- ## Supporting and Complementary Theory {#supporting-and-complementary-theory} -->

## 支援・補完理論 {#支援・補完理論}


---

[← 前へ](../README.md) | [目次](../README.md) | [次へ →](02-scrum-basics.md)
