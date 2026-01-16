# さらなる理論

[← 前へ](02-scrum-basics.md) | [目次](../README.md) | [次へ →](04-roles.md)

---

<!--
このコンテンツは、Scrum Guide Expansion Pack (https://scrumexpansion.org) から取得したものです。

著者: Ralph Jocham、John Coleman、Jeff Sutherland
翻訳: 内山遼子、川口恭伸、長沢智治、山本尊人、和田圭介
ライセンス: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
出典: https://github.com/ScrumGuides/ScrumGuide-ExpansionPack

詳細は NOTICE.md を参照してください。
-->


<!-- ### Product Thinking -->

### プロダクト思考

<!-- People consume Products (including services), not projects. A Product is the conduit to deliver value, balancing the short- and long-term. This is why Scrum has a Product Owner and not a Project Owner. Products are long-term and need to be taken care of for their entire existence, whereas a project is timeboxed and often leaves an orphaned Product behind once the project is completed. -->

人々が実際に使うのはプロジェクトではなく、プロダクト（サービスを含む）である。プロダクトは、ユーザーに価値を届けるためのものであり、短期的な成果と長期的な視点の両方が求められる。そのため、スクラムでは「プロジェクトオーナー」ではなく「プロダクトオーナー」の役割が設けられている。プロダクトは長期間にわたって継続的に管理・改善していく必要があるが、プロジェクトはタイムボックスが決まっており、プロジェクトが完了するとプロダクトが十分にサポートされず放置されてしまうことがよくある。

<!-- Product thinking (86-88) deals with the tension (111) that Products often need to _Focus_ on growth in the short-term but also need to address long-term concerns, e.g., gaining traction with early adopters, 'crossing the chasm' (5), expanding, updating Product versions, continuous change, customer lifetime value and total cost of ownership. -->

プロダクト思考(86-88)とは、プロダクトが短期的な成長に _集中_ する必要がある一方で、長期的な課題にも対応しなければならないという葛藤(111)を扱う考え方である。たとえば、短期的には、アーリーアダプターを獲得し勢いを得ながら、プロダクトの利用を広げることが重要である。一方で、長期的には「キャズム（普及の壁）を超え」(5)、プロダクトを拡張し、バージョンアップや継続的な改善を行いながら、顧客のライフタイムバリュー（生涯価値）や総所有コストといった観点にも目を向ける必要がある。

<!-- To 'cross the chasm,' a strategy shift is needed from targeting savvy, risk-taking customers to winning over more pragmatic, risk-averse buyers, decision-makers, users, or other Stakeholders by focusing on a specific market area or target and delivering a complete, reliable solution that solves real problems. This step is crucial for a Product's transition from niche success to widespread adoption, as it moves from appealing to early adopters to attracting the early majority. The early majority often requires clear evidence of the Product's reliability and problem-solving capabilities within a specific context. By focusing on a niche and providing a complete solution, a company can build credibility, create reference customers, and establish a strong market position, effectively bridging the 'chasm' between early adopters and the mainstream market. -->

「キャズムを超える」には、新しいもの好きでリスクをいとわない顧客をターゲットにする戦略から、より現実的でリスク回避傾向が強い購入者や意思決定者、ユーザー、または他のステークホルダーを獲得するための戦略へとシフトする必要がある。そのためには、特定の市場やターゲット層に焦点を当て、実際の課題を解決できる、信頼性の高い完成度のあるソリューションを提供することが重要である。このステップは、一部のアーリーアダプターから、アーリーマジョリティに広く使われるようになるための分岐点となる。アーリーマジョリティは、特定の状況や用途でそのプロダクトが本当に信頼でき、問題解決に役立つという明確なエビデンスを求める傾向がある。ニッチな市場に集中し、完成度の高いソリューションを提供することで、企業は信頼を築き、他の顧客に紹介できる実績ある顧客（リファレンス顧客）を作り、市場での強固なポジションを確立できる。こうすることで、アーリーアダプターとメインストリームの市場の間にある「キャズム」を効果的に乗り越えることができる。

<!-- Product Owners need to master the handling of trade-offs between the _here_ and _now_ and the anticipated future (the _there_ and _then_) (148) through courage, humility, consultation, collaboration, healthy conflict, etc. -->

プロダクトオーナーは、勇気や謙虚さを持ち、周囲と相談したり協力したり、ときには建設的な意見のぶつかり合いを通じて、ここ（_Here_）と今（_Now_）と、予想される未来（そこ（_There_）とその時（_Then_））(148)の間のトレードオフを上手く扱う力が求められる。

<!-- Suppose the people involved are purely short-term thinkers. In that case, they will likely experience long-term side effects such as technical debt, low Scrum Team morale, busyness, output focus, etc. For that reason, mitigating factors would need to be put in place to support the long-term. -->

もし関係者が短期的な視点でのみ行動してしまうと、技術的負債がたまったり、スクラムチームの士気が下がったり、常に忙しくなったり、アウトプットばかりを重視してしまうなど、長期的にさまざまな副作用を経験する可能性がある。そのため、長期的な視点を持つための工夫や対策をあらかじめ用意しておく必要がある。

<!--
Technical debt is the extra work
    that builds up
        – consciously or unconsciously –
    when you take shortcuts
        in implementation or design
    to deliver something faster.
Over time,
    it slows you down, just like real debt
        —with interest—
    because it makes future changes
        harder and riskier.
Professionals strive to minimize
    technical debt and sloppiness
    as much as possible.
If they decide to incur debt,
    it should be transparent,
    and if possible,
    an emergent mitigation plan should be in place.
-->

技術的負債とは、
何かをより早く提供するために、
実装や設計で近道をした際に
（意識的にしても無意識でも）
積み重なっていく追加作業のことである。
時間が経つにつれて、
実際の借金のように
（利子付きで）
開発のスピードを落としてしまう。
なぜなら、今後の変更を
余計に難しく、リスクの高いものにするからである。
プロフェッショナルならば、
技術的負債・ずさんな作業を
できるだけ最小限に抑えるよう努める。
もし負債を負うことを決めたとしたら、
それは透明性を持つべきであり、
可能な限り、
後から柔軟に対応できるような緩和策を用意しておくべきである。

<!-- For Products, Scrum supports feasibility, usability, desirability, value, and viability within ethical (57) boundaries through: -->

プロダクトに対して、スクラムは倫理的(57)な枠組みの中で、実現可能性、使いやすさ、魅力、価値、そして実行可能性を、以下を通じて支援する。

<!-- - Product design -->
<!-- - Product management -->
<!-- - Intentional consideration of the cohesive interplay of Stakeholders, research, goals, discovery, design, delivery, and continuous value realization -->
<!-- - In the specific case of technology Products, through Product engineering. -->

- プロダクト設計
- プロダクトマネジメント
- ステークホルダー、研究、ゴール、ディスカバリー、設計、デリバリー、継続的な価値実現といった要素が密接に連携し合うことを意識的に考慮すること
- 技術系プロダクトの場合は、プロダクトエンジニアリングを通じて

<!-- Scrum favors a healthy balance of the short-term and the long-term. Goal orientation enables potential outcomes through an emphasis on value and risk reduction. The Sprint Goal _(here_ and _now)_ should be a step toward the Product Goal _(there_ and _then)_, which enables pathways to the long-term. The Product Goal often supports the Product strategy and Product Vision. -->

スクラムは、短期と長期の健全なバランスを大切にする。ゴール指向で進めることで、価値の創出やリスク低減に重点を置き、潜在的なアウトカムを実現しやすくする。スプリントゴール（ここ（_Here_）と今（_Now_））は、プロダクトゴール（そこ（_There_）とその時（_Then_））に向かうための一歩であり、これが長期的な成長への道筋となる。プロダクトゴールは、プロダクト戦略やプロダクトビジョンを支える役割も果たす。

<!-- ### Systems Thinking -->

### システム思考

<!-- Systems thinking (55) acknowledges the interconnectedness of elements within organizational and social contexts, recognizing that actions in one area ripple in ways that aren't always predictable or linear. Theory-informed experiments, feedback loops, and follow-up data analysis help surface valuable and actionable insights. Systems Thinking provides valuable tools and ideas and facilitates insights. -->

システム思考（55）は、組織や社会の文脈において様々な要素が相互に結びついていることに着目し、ある領域での行動が必ずしも予測可能ではなく、また線形ではない方法で波及していくことを重視する考え方である。理論に基づく実験、フィードバックループ、追跡的なデータ分析を通じて、価値ある実践的な知見が得られる。システム思考は有用なツールとアイデアを提供し、洞察を促進する。

<!-- For an organization to become adaptive (80), it is necessary to avoid local sub-optimizations such as reducing unit costs while increasing long-term costs, eroding quality goals only to lose customer trust, or improving a Scrum Team, workflow, or process that should not exist. For complex work (30-35), it's not always possible to link cause and effect, except in hindsight. It's helpful, nevertheless, to consider possible and actual upstream, cross-stream, and downstream effects of interventions. -->

適応力(80)のある組織になるためには、個々のコストを削減しながら長期コストを増加させる、品質目標を犠牲にして顧客信頼を失う、そもそも存在すべきでないスクラムチーム、ワークフロー、プロセスを改善するなどの局所的な部分最適化を避けることが必要である。複雑な作業(30-35)では、原因と結果を結びつけることは必ずしもできず、多くの場合、事後に初めて理解できるものである。それでもなお、アクションや施策がもたらす前工程や関連領域、後工程に対する実際的もしくは潜在的な影響を考慮することは有用である。

<!-- ### Discovery -->

### ディスカバリー

<!-- Discovery (50-51) often starts with understanding people's expectations, needs, and wants through observation, analysis, conversations, and synthesis toward a desired outcome. Once a Scrum Team has gathered insights, it frames the problem or opportunity and orders them by potential value. The Scrum Team crowdsources possible solutions without judging them too quickly. If the potential value is high but there is a lack of evidence that the value can be realized, the Scrum Team should do research, assumption testing, or build simple prototypes they can test with real customers, decision-makers, or users. Discovery is never over; consider regular interviews or observations of customers, decision-makers, or users. -->

ディスカバリー(50-51)は、多くの場合、観察・分析・対話・統合を通じて人々の期待やニーズ、要望を把握し、望ましい成果を明確にすることから始まる。スクラムチームが十分な洞察を得たら、問題や機会を整理し、それらに潜在的な価値の大きさで優先順位を付ける。チームは急いで結論を出すことはせず、可能性のあるソリューションについて広くアイデアを集める。もし潜在的な価値が高いにもかかわらず、その価値が本当に実現できるというエビデンスが足りない場合は、追加の調査や仮説検証をする、あるいは実際の顧客・意思決定者・ユーザーに試せるシンプルなプロトタイプをつくるべきである。ディスカバリーは終わりのない活動であり、顧客や意思決定者、ユーザーへの定期的なインタビューや観察を続けることが推奨される。

<!-- Discovery is about learning toward a desired outcome through prioritizing, doing, avoiding, or constantly improving ideas informed by user observation, feedback, or other learnings. Discovery emphasizes collaboration, creativity, and not being afraid to fail and try again. Discovery frames work as problems or opportunities and helps the Scrum Team to create, prioritize, and test solution options that balance what people desire, what's technically possible, and what makes business sense—all while having fun. -->

ディスカバリーとは、ユーザー観察やフィードバック、その他の学びをもとに、アイデアの優先順位付け、実行、不要なものの見送り、そして継続的な改善を通じて、望ましい成果に向かって学び続ける活動である。ディスカバリーは、チームのコラボレーションや創造性を大切にし、失敗を恐れずに何度でも挑戦する姿勢を重視する。また、ディスカバリーによって、チームは作業を問題や機会として捉え直し、人々が望むもの・技術的に実現可能なこと・ビジネスとして意味があることのバランスを取りながら、さまざまな解決策の選択肢を生み出し、優先順位をつけて試すことができるようになる。そして、こうした活動全般をチームは楽しみながら行う。

<!-- If discovery is needed, it should (insofar as it is possible) be included in a manner that is consistent with Scrum. For example, discovery work is made transparent in the Product Backlog and Sprint Backlog, Scrum Team members practice discovery and other skills, learnings are discussed during the Sprint and at the Scrum events, and at least one Increment is produced (and ideally released) every Sprint, regardless of how much discovery is done. There is a balance to be struck: discovery can help avoid building the wrong thing, but it can be overdone, and, in the end, the result feedback matters the most. -->

ディスカバリーが必要な場合は、可能な限りスクラムと整合した形で取り入れるべきである。たとえば、ディスカバリーの作業はプロダクトバックログやスプリントバックログで可視化され、スクラムチームのメンバーはディスカバリーやその他のスキルを実践し、学びはスプリント中やスクラムイベントで議論される。そして、どれだけディスカバリーを行ったかに関わらず、毎スプリントで少なくとも一つのインクリメントが必ず作り出され（理想的にはリリースされ）るべきである。バランスを取ることが重要であり、ディスカバリーは間違ったものを作ることを防ぐのに役立つが、やりすぎることもあり得る。最終的には、結果からのフィードバック（結果フィードバック）が最も重要である。

<!-- ### Leadership -->

### リーダーシップ

<!-- Leadership is the ability to influence, guide, and inspire a group of people to achieve a common goal while avoiding demotivation. It inspires thoughts, actions, and passion and fosters clear strategic directions. It embraces purposeful and intentional Go See, Listen, and Understand, collecting facts and observations to inform decisions, better known as Genchi Genbutsu (84). -->

リーダーシップとは、共通のゴールを達成するために、人々の意欲を低下させずに良い影響を与え、導き、鼓舞する能力である。それは思考、行動、情熱を刺激して、明確な戦略的方向性を育む。それは目的意識と意図を持って、現場を見る、聞く、理解するということを実践し、事実と観察結果を収集して意思決定に反映させるプロセスであり、現地現物(84)として知られている。

<!-- Leadership is a dynamic social process involving responsibility, relationship building, and empowerment. Successful leadership results in co-creating a direction of travel, effective alignment of resources and people needed, and mutual _Commitment_ among group members. -->

リーダーシップは、責任・人間関係構築・エンパワーメントを含んだ、動的で社会的なプロセスである。効果的なリーダーシップにより、進むべき方向の共創・必要なリソースと人材の効果的な配置・グループメンバー間の相互の _コミットメント_ が実現される。

<!-- Scrum strives for a particular leadership, that is, leadership for resilience, a set of qualities, not a management position. Thus, leadership needs to include but not be limited to cultivating the environment for self-managing Scrum Teams, clarity, trust, transparency, emergence (71) in a direction, fulfillment at work, embracing uncertainty (72) and failures, gathering evidence for better decisions, proactively managing risk, and removing organizational inefficiencies. -->

スクラムにおけるリーダーシップとはすなわち、レジリエンスを重視するリーダーシップであり、管理職の地位ではなく一連の資質を指す。したがって、リーダーシップには、自己管理型スクラムチームの育成、明確さ、信頼、透明性、方向性における創発(71)、仕事における充実感、不確実性(72)と失敗の受け入れ、より良い意思決定のためのエビデンスの収集、積極的なリスク管理、組織の非効率性の除去などが含まれるが、これらに限定されない。

<!-- Leadership happens from all angles, should be at all levels, and fosters reflection at the right times. Leadership should drive ruthlessly for value, yet be compassionate and ethical. Leadership requires persistent agency to change workflows, processes, systems, and the work environment; this includes (but is not limited to) HR, finance, and vendor management. A leader is someone who demonstrates leadership. -->

リーダーシップはあらゆる方向から生まれ、すべてのレベルで存在すべきものであり、適切なタイミングで自らを振り返る契機ともなる。真のリーダーシップとは、価値の実現に向けて徹底的に取り組む姿勢を持ちつつも、常に思いやりと倫理観を忘れないことが求められる。リーダーシップには、ワークフロー、プロセス、システム、そして職場環境をより良くするための持続的な主体性が求められる。その取り組みは、人事、財務、ベンダー管理も含まれる（ただしこれらに限定されない）。
つまり、リーダーとは、こうした姿勢をもってリーダーシップを発揮する人のことを指す。

<!-- Product Owners and Scrum Masters balance leadership, authority, and subtle control by providing clear intent, fostering initiative, and reinforcing accountability. They guide rather than micromanage, ensuring the Scrum Team understands the vision and goals, has the autonomy to execute, and remains accountable for outcomes. When intervention is needed, they step in decisively while preserving the Scrum Team's ownership of their accountabilities. Product Developers demonstrate leadership with their self-managing team orientation, professionalism, and goal orientation; self-management comes with responsibilities. Supporters demonstrate leadership by supporting short- and long-term impediment removal, improving the coherence of management processes with Scrum, and supporting emergent change in a powerful direction when requested. -->

プロダクトオーナーとスクラムマスターは、明確な意図を示し、自主性を促進し、責任感を高めることで、リーダーシップ・権威・そして微妙なコントロールのバランスを取る。彼らはマイクロマネジメントに陥ることなく、スクラムチームがビジョンとゴールを理解し、それを自律的に実行しながらアウトカムに対する説明責任を持ち続けるよう導く。介入が必要な場合は、スクラムチームのオーナーシップを保持させた上で、断固とした対応をとる。開発者は、自己管理チーム指向、専門性、そしてゴール指向を通じてリーダーシップを発揮する。自己管理には責任が伴う。サポーターは、短期と長期の障害物除去の支援、スクラムとの整合性を高める管理プロセスの改善、要求に応じて明確な方向性に基づいた創発的な変化を後押しすることで、リーダーシップを発揮する。

<!-- ### First Principles Thinking -->

### 第一原理思考

<!-- First principles thinking is a method of problem-solving that involves breaking down challenges into their most fundamental truths and discovering solutions from the ground up. Instead of relying on analogy or established conventions, this approach asks, _'What do we know for certain?'_ and reconstructs understanding and solutions from those basic elements. Examples could include but are not limited to: -->

第一原理思考は、課題をその最も基本的な真実に分解し、根本から解決策を導き出す問題解決方法である。類推や確立された慣例に依存する代わりに、このアプローチは「確実に知っていることは何か？」と問い、それらの基本要素から理解と解決策を再構築する。例には以下が含まれるがこれらに限定されない：

<!-- - Encouraging the Scrum Team to _Focus_ on the core drivers of effectiveness, adaptiveness (80), and timeliness \-such as autonomy, transparency, and adaptation- rather than blindly following processes or copying what others have done. -->

- スクラムチームが盲目的にプロセスに従ったり、他チームの前例を模倣するよりも、自律性、透明性、適応といった効果性、適応性(80)、適時性を高める中核的要因に _集中_ することを促進する。

<!-- - Questioning every assumption and reconstructing solutions based on facts and essential principles, which can enable breakthroughs. -->

- あらゆる前提に疑問を持ち、事実と基本原理に基づいて解決策を再構築することで、ブレークスルーを可能にする。

<!-- - Advocating original thinking, continuous improvement, and the _Courage_ to challenge the status quo-unlocking creativity and enabling transformative results. -->

- 独創的な思考、継続的改善、現状に挑戦する _勇気_ を奨励し、創造性を解放し、変革を実現可能とする。

<!-- ### People and Change -->

### 人と変化

<!--
The level of difficulty in adopting Scrum
    should not be underestimated.
Scrum
    offers some guiding principles
    through its elements.
It offers an approach
    to go back to first principles.
-->

スクラム適用の難しさを
過小評価すべきではない。
スクラムは
各構成要素を通じて
いくつかの道しるべとなる原則（guiding principles）を提供する。
第一原理に立ち返るための
アプローチを提供している。

<!-- Scrum is not about adopting tools, short term delivery that sacrifices long term value. Often, incorrectly, Scrum practitioners only focus on short term impediment removal. Scrum requires change agency that balances the short term with the long term. -->

スクラムは、ツールの導入や長期的な価値を犠牲にした短期的なデリバリーの追求を目的とするものではない。スクラム実践者は、短期的な障害物の除去だけに終始してしまうことがよくある。しかしスクラムに必要なのは、短期と長期のバランスを取る変革推進力である。

<!-- スクラムとは、
    単なるツールの導入ではない。
障害物の除去だけに終始するものでもない。
スクラムにおける障害物とは、
    進捗を阻害または遅延させるあらゆる要因を指す。 -->
<!-- A work related problem in Scrum could be anything that blocks or slows down progress, often addressed by self-managment of the Product Onwer and Product Developers. An impediment is a type of problem in Scrum and is anything that blocks or slows down progress and cannot be solved by the Developers & Product Owner.  -->

スクラムにおける仕事上の問題とは、進捗を阻害または遅延させるあらゆるものを指し。多くの場合、プロダクトオーナーやプロダクト開発者による自己管理によって対処されるものである。障害物とはスクラムにおけるスクラムにおける問題の一種であり、進捗を阻害または遅延させるものであり、開発者やプロダクトオーナーだけでは解決できないものを指す。

<!-- It is crucial to be
    intentional, unrelenting, and tenacious
    about people, change, and communications.
The change often includes
    people development, designs, workflows,
    processes, systems, attitudes, behaviors,
    language, habits, and the work climate.
Culture is an emerging result.
-->

人・変化・コミュニケーションについて、
意図的に、手を緩めず、粘り強く
取り組むことが必要不可欠である。
変化には様々な要素が含まれる。
人材開発、設計、ワークフロー、
プロセス、システム、態度、行動、
言語、習慣、職場環境などである。
文化とは、
そうした変化の創発的な結果である。

<!--
An effective Scrum adoption
    uses an emergent approach,
    has effective change agents,
    and engages enthusiastic support
        from those affected by it or affecting it.
Intentionality and daily progress
    with the adoption
    are crucial;
    the adoption work should not be the last thing
        that is worked on
        after everything else is finished.
-->
<!-- 効果的なスクラムの適用には、
    創発的なアプローチの活用や
    効果的なチェンジエージェントの存在、
    そして、スクラムの影響を受ける人や影響を与える人たちの
        熱心な協力を得ることが必要である。
スクラムの導入においては、
    意図的な取り組みと日々の進捗が重要であり、
    他のすべての作業が終わった後に
        最後に取りかかるものとしてはならない。 -->

<!-- An effective Scrum adoption uses an emergent approach, has effective change agents (including Supporters and other Leaders), and engages enthusiastic support from those affected by it or affecting it. Intentionality and daily progress with the adoption are crucial; the adoption work should not be the last thing that is worked on after everything else is finished. -->

効果的なスクラムの適用は、創発的なアプローチの活用や効果的なチェンジエージェント（サポーターや他のリーダーを含む）の存在、そして、スクラムの影響を受ける人や影響を与える人たちの熱心な協力を得ることが必要である。スクラムの導入においては、意図的な取り組みと日々の進捗が重要であり、他のすべての作業が終わった後に最後に取りかかるものとしてはならない。

<!--
Start with disciplined emergent change
    in a direction.
Strive to make emergent change so normal
    that it eventually becomes
    part of the scheduled work.
A Scrum adoption has direction
    but not a predefined destination.
The change is emergent
    and therefore not predictable.
Curiosity enables a pattern of
    sense, listen, learn, and adapt
    in a direction.
It's important to
    foster relationships and
    understand perspectives,
    and to listen to
        what is not being said and
        what is not happening.
Change is hard work,
    yet fulfilling.
-->
<!-- 方向性を持ち、
    規律ある創発的変化から始めよう。
創発的変化を当たり前にして、
    最終的に定常的な仕事の一部になるまで
    進めることを目指す。
スクラムの適用には方向性があるが、
    事前に定められた目的地はない。
変化とは創発的なものであり、
    それゆえ予測できない。
好奇心は、
    方向性を持った上で、
    感じる・聴く・学ぶ・適応する
    というパターンを可能にする。
関係性を育み、
    多様な視点を理解し、
    語られていないことや
    起こっていないことに
    耳を傾けることが重要である。
変化は困難だが、
    やりがいのある作業である。 -->

<!-- Start with disciplined emergent change in a direction. Strive to make emergent change a normality; eventually it becomes part of the scheduled work. A Scrum adoption has a direction but not a predefined destination. The change is emergent and therefore not predictable; a north star lights the path but is not a fixed destination. Curiosity enables a pattern of sense, listen, learn, and adapt in a direction. It’s important to foster relationships and understand perspectives, and to listen to what is not being said and what is not happening. Change is hard work, yet fulfilling. -->

方向性を持ち、規律ある創発的変化から始めよう。創発的な変化を当たり前にして、やがてそれは定常的な仕事の一部になる。スクラムの適用には方向性はあるが、事前に定められた目的地はない。変化とは創発的なものであり、それゆえ予測できない。北極星が道を照らすことはあっても、それ自体が決まった目的地ではない。好奇心は、方向性を持った上で、感じる・聴く・学ぶ・適応するというパターンを可能にする。関係性を育み、多様な視点を理解し、語られていないことや起こっていないことに耳を傾けることが重要である。変化は困難だが、やりがいのある作業である。

<!-- Scrum Practioners and Supporters try not to be victims and do not rely on others to change. They try to make continual marginal changes within their grasp and create continual positive momentum.
Ideally they are change catalysts and they radiate realistic positivity and possibilities. -->

スクラムの実践者とサポーターは、受け身の姿勢に甘んじず、他者の変化に依存しないように努める。自らの手の届く範囲で継続的に小さな変化を積み重ねることで、持続的な前向きな機運を生み出そうとする。
理想的には、彼らは変化の推進役となり、実現可能な前向きさを広める存在である。

<!-- ## The Scrum Roles in the Expansion Pack -->

## 拡張パックにおけるスクラムの役割


---

[← 前へ](02-scrum-basics.md) | [目次](../README.md) | [次へ →](04-roles.md)
