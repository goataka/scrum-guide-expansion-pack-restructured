# 複数チーム

[← 前へ](06-events.md) | [目次](../README.md) | [次へ →](08-conclusion.md)

---

<!--
このコンテンツは、Scrum Guide Expansion Pack (https://scrumexpansion.org) から取得したものです。

著者: Ralph Jocham、John Coleman、Jeff Sutherland
翻訳: 内山遼子、川口恭伸、長沢智治、山本尊人、和田圭介
ライセンス: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
出典: https://github.com/ScrumGuides/ScrumGuide-ExpansionPack

詳細は NOTICE.md を参照してください。
-->


<!-- If a Scrum Team becomes too large, it should consider reorganizing into multiple cohesive Scrum Teams, each focused on the same Product. Multiple Scrum Teams on the same Product should share the same Product Goal, Product Backlog, Product Owner, baseline Definition of Outcome Done, and baseline Definition of Output Done. -->

- スクラムチームが**大きくなりすぎた場合**、同じプロダクトに集中する、**複数の結束したスクラムチーム**に再編成することを検討すべき。同じプロダクトに複数のスクラムチームが存在する場合、それらのチームは**共通の**プロダクトゴール**、**プロダクトバックログ**、**プロダクトオーナー**、基準となる**アウトカム完成の定義**およびアウトプット完成の定義**を共有する必要がある。

<!-- Be careful with blind assumptions that more value is produced from more Scrum Teams. Scale only when the benefits clearly outweigh the additional overhead. Before you scale, the single Scrum Team setup has to be able to reliably produce an Increment every Sprint. But if you must scale, use an approach that is coherent with this document. Often fewer teams result in more outcomes. -->

- スクラムチームの数が増えればより多くの価値が生み出されるという盲目的な思い込みには注意が必要。スケーリングを行うのは、追加される負荷を上回る明確な利点がある場合に限る。スケーリングを行う前に、単一のスクラムチームが毎スプリント確実に**インクリメント**を提供できる状態にあることが必要。
- スケーリングが避けられない場合には、本書の内容と整合性のあるアプローチを使用するとよい。多くの場合、チームが少ない方がより多くのアウトカムを生み出す。

> 複数のスクラムチームでプロダクトを開発する場合、共通の**プロダクトゴール**、**プロダクトバックログ**、**プロダクトオーナー**、基準となる完成の定義を共有する必要がある。しかし、スクラムチームの数が増えれば価値が増すという盲目的な思い込みには注意が必要である。スケーリングは追加される負荷を上回る明確な利点がある場合に限り実施すべきであり、単一のスクラムチームが毎スプリント確実に**インクリメント**を提供できる状態を確立してから行うべきである。多くの場合、チームが少ない方がより多くのアウトカムを生み出す。

<!-- In a multi-Scrum-Team context, Scrum Teams may reduce inter-Scrum-Team dependencies by becoming more cross-functional through collaboration, cross-pollination, transfer of learning, and intentional interactions. The specific skills needed are often broad and will vary with the domain of work. In a multi-Scrum-Team setting, purposeful and intentional interactions and professionalism (including continuous integration) become even more important. -->

- 複数のスクラムチームの文脈においては、コラボレーション、他家受粉、学習の移転、意図的な相互作用を通じて、より機能横断になることでチーム間の依存関係を減らすことができる。必要なスキルは多岐にわたることが多く、業務領域によって異なる。こうした状況下では、意図的で目的のある相互作用やプロフェッショナリズム（継続的インテグレーションを含む）が一層重要となる。

<!-- In a one Product Owner and one Scrum Team setup, the Product Owner could be a Product manager, marketing director, technology director, etc. In a multi-Scrum-Team setup for a Product, the ideal is still only one Product Owner, who should be a leader for the Product. To allow the Product Owner to handle multiple Scrum Teams on the same Product, the Product Owner often becomes more strategic and delegates problems to solve and opportunities to the Product Developers, including, for example, aspects of Product design or Product management. -->

- 1人の**プロダクトオーナー**と1つのスクラムチームという構成では、**プロダクトオーナー**はプロダクトマネージャー、マーケティングディレクター、技術部門責任者などを担うこともある。プロダクトに対して複数のスクラムチームが存在する構成では、理想としては依然として**プロダクトオーナー**は1人のみであり、プロダクトに対するリーダーであるべき。複数のスクラムチームに対応するため、**プロダクトオーナー**はより戦略的な役割を担い、問題の解決や機会の実現を**プロダクト開発者**に委任することが多くなる。
- たとえば、プロダクトの設計やプロダクトマネジメントの側面などが該当する。

> 複数スクラムチームの環境では、コラボレーション、他家受粉、学習の移転、意図的な相互作用を通じて、チーム間の依存関係を減らすことが重要である。**プロダクトオーナー**は理想的には1人であり、複数のチームに対応するためにより戦略的な役割を担い、問題の解決や機会の実現を**プロダクト開発者**に委任する。**プロダクトバックログ**は透明性を高めるためのツールであり、プロダクトあたりのバックログが少ないほど、サイロが減少し、透明性が高まり、価値の明確さが増す。

<!-- The Product Backlog is a tool for increasing transparency. -->

- **プロダクトバックログ**は透明性を高めるためのツール。

<!-- Generally, the fewer Product Backlogs per Product, implicit (like a filter of a Product Backlog) or explicit: -->

一般的に、暗黙的（**プロダクトバックログ**のフィルターのように）にしろ明示的にしろ、プロダクトあたりの**プロダクトバックログ**が少ないほど良い：

<!-- - The fewer the silos in the Product and the greater the transparency across the entire Product; -->

- プロダクト内のサイロが減少し、プロダクト全体の透明性が高まる。
<!-- - The more transparent the overall progress tracking across the entire Product; -->
- プロダクト全体における進捗の追跡がより透明になる。
<!-- - The better the big-picture value clarity across the entire Product; -->
- プロダクト全体のビッグピクチャーとしての価値の明確さが増す。
<!-- - The more likely a Scrum Team would know it's working on low-value items from a Product perspective; -->
- スクラムチームがプロダクトの観点から低い価値のアイテムに取り組んでいることに気づきやすくなる。
<!-- - The more likely one is to observe improvement in the attainment of value; and, -->
- 価値の達成における改善が見られやすくなる。
<!-- - The more strategic the Product Owner becomes by delegating cross-Product work to the Product Developers. -->
- **プロダクトオーナー**は、プロダクトを横断する作業を**プロダクト開発者**に委任することで、より戦略的な役割を担うようになる。

> プロダクトあたりの**プロダクトバックログ**が少ないほど、プロダクト内のサイロが減少し、全体の透明性が高まり、ビッグピクチャーとしての価値の明確さが増す。また、低い価値のアイテムに取り組んでいることに気づきやすくなり、価値の達成における改善が見られやすくなる。**プロダクトオーナー**はプロダクトを横断する作業を**プロダクト開発者**に委任することで、より戦略的な役割を担うようになる。**プロダクトバックログ**が少ないほど適応性は高まるが、権限委譲されたオーナーシップ、整合性のある管理範囲、**ステークホルダー**との直接的な接点がなければギャップが生じる。

<!-- Fewer Product Backlogs per Product are better for adaptiveness (80), but without empowered ownership, a coherent span of control, or direct contact with relevant Stakeholders, gaps will arise. Scrum fosters a climate for happenstance and multi-learning as various people and Scrum Teams collaborate, discoveries and insights can be shared and leveraged. This is unlikely to happen in an environment where each component has a Product Backlog in isolation. -->

- プロダクトあたりの**プロダクトバックログ**が少ないほど、適応性(80)は高まる。しかし、権限委譲されたオーナーシップ、整合性のある管理範囲、または関連する**ステークホルダー**との直接的な接点がない場合には、ギャップが生じる。スクラムにより様々な人々やスクラムチームがコラボレーションし、発見や洞察が共有され活用されるように、スクラムは偶発性と多重学習のための土壌を育む。
- これは、各コンポーネントが孤立した**プロダクトバックログ**を持つ環境では起こりにくい。

<!-- Happenstance in the context of 'The New New Product Development Game' (29) means that sometimes useful ideas or solutions come about by chance, not by careful planning. When Scrum Teams work closely together and share information, they might discover new approaches or answers simply because they are open to unexpected events or accidental findings. -->

- 「The New New Product Development Game」（29）の文脈における偶然性とは、有用なアイデアや解決策が、綿密な計画ではなく偶然によって生まれることを意味する。スクラムチームが密接に連携し、情報を共有していると、予期せぬ出来事や偶然の発見によって新しいアプローチや答えを見出すことがある。

<!-- Multi-learning means that team members learn in many different ways at the same time. They pick up new skills and knowledge not only in their own area but also in other areas, and they learn as individuals, as a group, and as part of the whole company. This helps the team become more flexible and able to solve a wide range of problems quickly, because everyone is learning from each other and from their experiences as they work together. -->

- マルチラーニングとは、チームメンバーが同時に様々な方法で学習することを意味する。メンバーは自分の専門領域だけでなく、他の分野においてもスキルや知識を習得し、個人として、グループとして、そして会社全体の一員として学習していく。これにより、チームは柔軟性を持ち、幅広い課題を迅速に解決できるようになる。
- なぜなら、全員が互いから学び、共に働く中での経験から学び続けているから。

> スクラムは偶発性と多重学習のための土壌を育み、様々な人々やスクラムチームがコラボレーションし、発見や洞察が共有され活用される環境を醸成する。偶発性とは、有用なアイデアや解決策が綿密な計画ではなく偶然によって生まれることを意味し、マルチラーニングとは、チームメンバーが自分の専門領域だけでなく他の分野においてもスキルや知識を習得し、個人として、グループとして、会社全体の一員として学習していくことを意味する。適切なバランスを見つけることはジレンマだが、良い経験則として、**プロダクトバックログ**は少ない方が良く、それはマルチラーニングと組織的な学習の移転によって実現される。

<!-- Finding the right balance is a dilemma. There are always trade-offs to consider. However, a good heuristic is: The fewer Product Backlogs, implicit or explicit, the better, enabled through multi-learning and the organizational transfer of learning across Scrum Teams, departments, and Products. -->

- 適切なバランスを見つけることはジレンマ。常に考慮すべきトレードオフがある。しかし、良い経験則として、プロダクトごとの**プロダクトバックログ**は暗黙的か明示的かを問わず少ない方が良い。
- それは、マルチラーニングとスクラムチーム、部門、プロダクトを横断した組織的な学習の移転によって実現される。

<!-- Organizational transfer of learning, as described in 'The New New Product Development Game' (29), is the process by which knowledge and insights gained in one new Product development area are regularly shared and applied to subsequent areas or other divisions within the organization. -->

- 「The New New Product Development Game」（29）で説明されている組織的な学習の移転とは、ある新製品開発の領域で得られた知識や洞察が、後続の領域や他の部門にも継続的に共有され適用されるプロセスを指す。

> 組織は往々にして成果を出すための容易さよりも、管理するための容易さを優先して設計される。価値を届けるために、いくつのスクラムチームがその課題や機会に関与するかを自問し、その数を少なくすることが重要である。チームを指揮統制から解き放ち、調整された自律性を重視し、目的のある意図的な相互作用を育む。最小限でありながら十分なマネジメントのプロセス、足場、境界のある働く環境を醸成し、単なるデリバリーではなく、方向性のある変革推進力と継続的改善をケイデンスの中に組み込むことが重要である。

<!-- Organizations are often designed for ease of management over ease of outcomes. Ask yourself how many Scrum Teams a problem or opportunity touches to deliver value; generally, the lower that number, the better. -->

- 組織は往々にして、成果を出すための容易さよりも、管理するための容易さを優先して設計される。価値を届けるために、いくつのスクラムチームがその課題や機会に関与するかを自問してみてほしい。一般的には、その数が少ないほど良い。

<!-- Free teams from command and control. Err on the side of aligned autonomy. Foster purposeful, intentional interactions within and between self-managing Scrum Teams (49). Foster a work climate with minimal but sufficient management processes, scaffolding, and boundaries. Balance and nurture Stakeholder expectations and limits. Build change agency and continual improvement in a direction, not just delivery, into a cadence. -->

- チームを指揮統制から解き放つ。調整された自律性を重視する。自己管理スクラムチーム(49)の中およびその間で、目的のある意図的な相互作用を育む。
- 最小限でありながら十分なマネジメントのプロセス、足場、境界のある働く環境を醸成する。**ステークホルダー**の期待と制約のバランスをとり、育成する。単なるデリバリーではなく、方向性のある変革推進力と継続的改善をケイデンスの中に組み込む。

<!-- When in doubt, study the New New Product Development Game (29), embrace the good of what's new in the present, but abandon any notions of an industrial complex (30-35) where only the brave people have the agency to do anything. -->

- 判断に迷ったときには「The New New Product Development Game」（29）を研究し、現代における新しいものの良さを受け入れつつ、勇敢な人だけが行動力を持つような産業複合体（30-35）の思考は捨てるべき。

<!-- ## End Note -->

## 最後に 📝



> 判断に迷ったときには「The New New Product Development Game」を研究し、現代における新しいものの良さを受け入れつつ、勇敢な人だけが行動力を持つような産業複合体の思考は捨てるべきである。戦術、戦略、手法、フレームワークを活用するかしないかに関わらず、まずはトップ層として両利き性、人間的な効果性、適応性、タイムリーさを支える精神を受け入れることが重要である。そうでなければ、組織内の変革ごっこや、タイムリーさ、人間性、効果性のある作業の寄せ集めを監督し続けることになる。

---

[← 前へ](06-events.md) | [目次](../README.md) | [次へ →](08-conclusion.md)
