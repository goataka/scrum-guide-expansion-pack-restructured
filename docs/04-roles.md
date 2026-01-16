# スクラムの役割

[← 前へ](03-theory.md) | [目次](../README.md) | [次へ →](05-artifacts.md)

---

<!--
このコンテンツは、Scrum Guide Expansion Pack (https://scrumexpansion.org) から取得したものです。

著者: Ralph Jocham、John Coleman、Jeff Sutherland
翻訳: 内山遼子、川口恭伸、長沢智治、山本尊人、和田圭介
ライセンス: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
出典: https://github.com/ScrumGuides/ScrumGuide-ExpansionPack

詳細は NOTICE.md を参照してください。
-->


<!-- [2020 Scrum Guide: 'The entire Scrum Team is accountable for creating a valuable, useful Increment every Sprint. Scrum defines three specific accountabilities within the Scrum Team: the Developers, the Product Owner, and the Scrum Master.' An accountability is a list of expectations that one is accountable for, e.g., the Product Owner accountable for value, the Scrum Master for the Scrum Team’s effectiveness, and Developers for creating the usable Increment. A role does not necessarily have accountabilities.] -->

[2020年版スクラムガイド: 「**スクラムチーム全体が、スプリントごとに価値のある有⽤なインクリメントを作成する責任を持つ**。スクラムはスクラムチームにおいて、**開発者、プロダクトオーナー、スクラムマスターという 3 つの明確な責任を定義する**。」**責任（説明責任）**とは、それぞれが説明責任を負うことになる**期待事項のリスト**である。例えば、**プロダクトオーナーは価値に対して説明責任を持ち**、**スクラムマスターはスクラムチームの効果性に対して説明責任を持ち**、**開発者は有用なインクリメントの作成に対して説明責任を持つ**。**役割が必ずしも説明責任を伴うとは限らない**。]

<!-- Not all roles have accountabilities, i.e. Stakeholder. The four Scrum roles are Product Owner, Product Developer, Scrum Master, and Stakeholder. They give, reward, and earn trust and enable coherent leadership. Only the three accountabilities, Product Owner, Product Developer, and Scrum Master, are in the Scrum Team. -->

- **すべての役割が説明責任を持つわけではなく**、その一例がステークホルダーである
- **スクラムの4つの役割**とは、**プロダクトオーナー・プロダクト開発者・スクラムマスター・ステークホルダー**
- これらは**信頼を与え、信頼に報い、信頼を獲得し、一貫したリーダーシップを可能にする**

<!-- A person can hold more than one Scrum role. By taking on more than one role, one must be careful not to overstep. The Scrum roles are designed to keep check and balances in place. -->

- **1人が複数のスクラムの役割を担うことができる**
- **複数の役割を担う場合、越権行為をしないよう注意しなければならない**
- **スクラムの役割は、チェック・アンド・バランスを保つよう設計されている**

> スクラムには4つの役割（プロダクトオーナー、プロダクト開発者、スクラムマスター、ステークホルダー）が存在し、そのうち3つが説明責任を持つ。役割と説明責任は異なる概念であり、すべての役割が説明責任を伴うわけではない。1人が複数の役割を担うことは可能だが、適切なチェック・アンド・バランスを維持するために越権行為に注意が必要である。これらの役割は信頼関係を構築し、一貫したリーダーシップを実現する。

<!-- A Scrum Team is a team that practices Scrum, addresses three Scrum _accountabilities,_ namely, Scrum Master, Product Owner, and Product Developers, deals with Stakeholder (including but not limited to customer or user) problems or opportunities, and delivers useful, usable, and potentially valuable Increments from the perspectives of the Scrum Team and Stakeholders toward the Product Goal. For complex (30-35) work, a Scrum Team should be small, cognitively diverse, and self-managing, where human Scrum Team members, often assisted by technology, care about each other's work and learn how to do each other's work. -->

#### スクラムチームの特性 📝

```
スクラムチームは機能横断型で階層がなく、ディスカバリー、デリバリー、価値検証に必要なすべてのスキルを保持する。サポーターの支援を受けながら、プロダクトゴールに向けて問題や機会に共同で取り組み、自己管理によって誰が何をいつどのように行うかを決定する。価値検証とは、期待される結果が達成されたかを確認するプロセスであり、スクラムチームの中核的な活動である。
```

- **スクラムチーム**は、スクラムを実践し、**スクラムマスター、プロダクトオーナー、プロダクト開発者**というスクラムの**3つの _説明責任_** を担い、**ステークホルダー**（顧客やユーザーを含むがこれらに限定されない）の**問題や機会に対応**し、スクラムチームとステークホルダーの視点から、**プロダクトゴールに向けて有用で利用可能かつ潜在的に価値のあるインクリメントをデリバリーする**チーム
- **複雑な(30-35)作業**においては、スクラムチームは**小規模で認知的多様性を持ち、自己管理型であるべき**
- 人間のスクラムチームメンバーは、技術的な支援を受けながら、**お互いの作業を気にかけ、お互いの作業のやり方を学ぶ**

<!-- The Scrum Team should be cross-functional, which means it is multidisciplinary, including technical and business domain skills. There is no explicit hierarchy within the Scrum Team. The Scrum Team should have all the skills and support needed to: -->

- スクラムチームは**機能横断型であるべき**で、これは**技術とビジネスドメインのスキルを含む多分野にわたる**ことを意味する
- **スクラムチーム内に明示的な階層は存在しない**
- スクラムチームは以下に必要な**すべてのスキルとサポートを備えるべき**である：

<!-- - Discover (including research and design) as needed, -->

- 必要に応じて**ディスカバー**する（調査と設計を含む）
<!-- - Deliver (including engineering when appropriate); and, -->
- **デリバリー**する（適切な場合はエンジニアリングを含む）；そして
<!-- - Validate value realization (and additionally usability, desirability, and viability within ethical (57) boundaries). -->
- **価値実現**（および**使いやすさ・魅力・倫理的な(57)境界内での実現可能性**）を**検証する**。

<!-- The Scrum Team, supported by the Supporters, collectively takes care of the problem or opportunity domain, Product discovery, delivery, verification and built-in quality, go-to-market, and value validation toward the Product Goal. The Scrum Team strives for net improvements; being self-managing (49), they decide _who_ does _what_, _how_, _when,_ and _where_. -->

- スクラムチームは、**サポーターの支援**を受けながら、**問題や機会の領域、プロダクトのディスカバリー、デリバリー、検証、作り込み品質、市場投入、そしてプロダクトゴールに向けた価値検証**に共同で取り組む
- このチームは**実質的な改善**を目指し、**自己管理(49)**をしているため、**_誰が_、_何を_、_どのように_、_いつ_、_どこで_、行うのかを自ら決定する**

<!--
Value validation
    is the confirmation (or disconfirmation)
    within given boundaries
    that the expected outcome(s) has been achieved.
-->

**価値検証**とは、
与えられた範囲内で、
**期待される結果が達成されたかどうかを
確認（または棄却）すること**である。



<!-- The Scrum Team delivers an Increment(s) every Sprint, continuously self-manages (49) to find and fix problems, synchronizes continuously, and releases frequently. The Scrum Team is small enough to remain nimble and large enough to complete significant work within a Sprint. Often, smaller Scrum Teams communicate better and are more productive. -->

#### スクラムチームの作業パターン 📝

```
スクラムチームは毎スプリントでインクリメントを提供し、継続的に自己管理して同期・リリースを行う。チームは小規模で俊敏性を保ちつつ、重要な作業を完了できる規模を持つ。自律性は存在するがスクラムの枠組みによって境界が設けられ、意図的な相互作用とリーダーの支援が成功に不可欠である。集中はプロダクトゴールの効果的な達成と価値あるアウトカムの提供に向けられるべきである。
```

- スクラムチームは**毎スプリントでインクリメントを提供**し、問題を発見して修正するために**継続的に自己管理し(49)**、**継続的に同期**し、**頻繁にリリースする**
- スクラムチームは、**俊敏性を保つのに十分な小ささ**と、**スプリント内で重要な作業を完了するのに十分な大きさ**を持つ
- 多くの場合、**より小さなスクラムチームの方がよりよくコミュニケーションを取り、より生産的**

<!-- Scrum is built on self-managing Scrum Teams (49) within a defined organizational or Product structure. Autonomy exists, but it is bounded by Scrum events, accountabilities, artifacts, commitments, pillars, values, and organizational needs. -->

- スクラムは、定義された組織またはプロダクト構造内の**自己管理スクラムチーム(49)**に基づいて構築されている
- **自律性は存在する**が、**スクラムイベント・説明責任・作成物・コミットメント・三本柱・価値基準・組織のニーズによって境界が設けられている**

<!-- Scrum engages groups of people who collectively have or acquire all the skills and expertise to do the work and share such skills as needed. Intentional interactions, supported by leaders, are needed to help improve the chances of successful outcomes. -->

- スクラムは、**作業に必要なすべてのスキルと専門知識を集合的に保有または習得**し、必要に応じてそれらのスキルを共有する人々のグループを関与させる
- 成功につながるアウトカムの可能性を高めるために、**リーダーによって支援された意図的な相互作用が必要**

<!-- The _Focus_ should remain on achieving the Product Goal in the most effective way, with the right amount of investment, while delivering valuable outcomes. -->

**_集中_** は、**価値あるアウトカムを提供しながら、適切な投資量で最も効果的な方法でプロダクトゴールを達成すること**に向けられるべきである。



<!-- Scrum fosters collaborative teamwork by encouraging continuous interaction and shared accountability rather than sequential, siloed work. This approach enables the Scrum Team and Stakeholders to embrace uncertainty (72), allowing for quicker adjustments informed by ongoing learning and feedback. The overlapping nature of discovery, development, and value validation ensures a more adaptive (80), value-driven approach to Product development. -->

#### 協調的チームワークと適応性 📝

```
スクラムは継続的な相互作用と共有説明責任により協調的チームワークを促進し、不確実性を受け入れて迅速に適応する。発見・開発・価値検証の重複により価値駆動型のアプローチが可能となり、重複する作業が説明責任の共有とエンゲージメントを高める。スクラムチームはあらゆるプロダクト関連活動を担い品質を作り込む。学習内容は予測不可能で、確実性を高めることも不確実性を増すこともある。
```

- スクラムは、**逐次的でサイロ化された作業ではなく**、**継続的な相互作用と共有説明責任を奨励**することで、**協調的なチームワークを促進する**
- このアプローチにより、スクラムチームとステークホルダーは**不確実性(72)を受け入れる**ことができ、**継続的な学習とフィードバックに基づくより迅速な調整**が可能になる
- **発見、開発、価値検証の重複する性質**は、**より適応的(80)で価値駆動型のプロダクト開発アプローチ**を保証する

<!-- Overlapping work fosters shared accountability among the Scrum Team, enhancing engagement and commitment. The Scrum Team directs attention to addressing challenges and opportunities, encourages proactive behavior, cultivates a diverse skill set, and increases awareness of market dynamics among all participants. -->

- **重複する作業**は、スクラムチーム内における**説明責任の共有を促進**し、**エンゲージメントとコミットメントを高める**
- スクラムチームは、**課題や機会への対応に意識を向け**、**自発的な行動を促し**、**多様なスキルセットを育成**し、すべての関係者に**市場動向への意識を高める**

<!-- The Scrum Team addresses all Product-related activities, from Stakeholder collaboration to value validation, including verification, maintenance, operation, experimentation, research and development, and anything else that might be required. The Scrum Team instills quality. Supporters ensure the organization structures the climate and the work environment and empowers the Scrum Team to self-manage (49). Working in Sprints at a sustainable pace improves _Focus_ and consistency. -->

- スクラムチームは、**ステークホルダーとの連携から価値検証に至るまで**、検証、保守、運用、実験、研究開発、その他必要とされる**あらゆるプロダクト関連の活動**を行う
- スクラムチームは**品質を作り込む**
- **サポーター**は、組織が適切な環境と作業環境を整備し、スクラムチームが**自己管理(49)できるように支援する**
- **持続可能なペースでスプリントで作業する**ことは、**_集中_ と一貫性を向上させる**

<!-- The Scrum Team and Stakeholders don't know what they will learn. Some learning provides greater certainty, and some creates more uncertainty (72). Some things could emerge, fade away, drop out, or become less of a priority. -->

- スクラムチームとステークホルダーは、**何を学ぶことになるかを事前には知り得ない**
- ある学びは**確実性を高める**一方で、ある学びは**さらなる不確実性(72)を生み出す**こともある
- いくつかのことは**出現し、消え去り、脱落したり、優先度が低下したりする**可能性がある



<!-- A Scrum Team has aligned autonomy. Aligned autonomy means the Scrum Team has the freedom to decide how to solve problems while staying focused on shared goals and outcomes, enabling both innovation and organizational coherence. Fostering a cognitively diverse Scrum Team is essential. Cross-pollination is more likely when the Scrum Team members collaborate, trust each other, and can self-reflect. -->

#### 整合性の取れた自律性と多様性 📝

```
スクラムチームは整合性の取れた自律性を持ち、共通目標に集中しながら解決方法を自ら決定してイノベーションと組織の一貫性を両立させる。認知的多様性の育成が不可欠で、協働・信頼・自己内省により他家受粉が促進される。成功のためにはアンラーンする意欲と間違いを許容する風土が必要であり、批判はアイデアに向け、全員が同じフィールドで責任を共有する。
```

- スクラムチームは、**整合性の取れた自律性**を有している
- **整合性の取れた自律性**とは、スクラムチームが**共通の目標とアウトカムに集中しながらも**、**課題の解決方法を自ら決定できる自由を持つ**状態を指し、**イノベーションと組織としての一貫性の両立**を可能にするもの
- **認知的多様性を持つスクラムチームを育成することは不可欠**
- スクラムチームのメンバーが**互いに協働し、信頼し合い、自己を内省できる**とき、**他家受粉がより促進される**

<!-- For successful outcomes, the Scrum Team and Supporters should cultivate a willingness to unlearn outdated principles. Inspection and Adaptation require a climate that anticipates and tolerates mistakes. It is essential to _Focus_ criticism on ideas rather than individuals. All Scrum Team members 'play on the same field' with coherently overlapping work, and are all accountable for success. -->

- 成功につながるアウトカムのためには、スクラムチームおよびサポーターが**時代遅れの原則を手放す姿勢、すなわちアンラーンする意欲を育む**ことが求められる
- **検査と適応**を実現するには、**間違いを予期し許容する風土**が不可欠
- 批判は**個人ではなく、アイデアに対して**向けることに **_集中_** する必要がある
- スクラムチームのすべてのメンバーは**「同じフィールドでプレーする」存在**であり、作業は**一貫性をもって重なり合い**、**成功に対して全員が責任を負う**



<!-- ### Stakeholder -->

### ステークホルダー

<!-- Stakeholder is a role. A Stakeholder is an entity, individual, or group interested in, affected by, or impacting inputs, activities, and outcomes. Stakeholders have a direct or indirect interest inside or outside the organization, its Products, or services. -->

- **ステークホルダーは役割の一つ**
- ステークホルダーとは、**インプット・活動・アウトカムに関心を持ち**、そこから**影響を受けたり影響を与える存在・個人・グループ**
- ステークホルダーは、**組織・プロダクト・サービスの内外に直接的・間接的な利害関係を持つ**

<!-- Examples of Stakeholders include (but are not limited to) customers, decision-makers, users, vendors, influencers, managers, colleagues, leaders, legislators, financial sponsors, subject matter experts, and governance oversight. Inanimate, non-human Stakeholders such as the law or AI should not be ignored. Some Stakeholders have more impact or are more impacted than others, and each can favor different factors. Each Stakeholder has a different degree of power or influence. -->

- ステークホルダーには、**顧客、意思決定者、ユーザー、ベンダー、インフルエンサー、マネージャー、同僚、リーダー、立法者、資金提供者、特定分野のエキスパート、ガバナンス監督者**が含まれるが、これらに限定されない
- **法律やAIなどの無機物で人間ではないステークホルダー**も無視すべきではない
- ステークホルダーは、**他のステークホルダーよりも影響力が強かったり、影響を受けたりする**場合があり、**優先する要素がそれぞれ異なる**
- **ステークホルダーごとに権力や影響力の程度が異なる**

<!-- A customer is any Stakeholder who receives value from the Product by purchasing and/or selecting it. Customers may include buyers (those who pay for or acquire the Product), decision-makers (those who approve or authorize its adoption), and end users (those who interact directly with the Product). Sometimes, the customer is not the same as the end-customer, e.g., in B2B2C (79) or B2B2B (78). -->

#### 顧客 📝

- **顧客**とは、プロダクトを**購入や選択することにより価値を受け取る**ステークホルダーの一種
- 顧客には、**購入者**（プロダクトを購入または取得する人）、**意思決定者**（プロダクトの採用を承認または決定する人）、**エンドユーザー**（プロダクトを直接利用し、相互作用する人）が含まれる
- **B2B2C(79)やB2B2B(78)**などのように、**顧客と最終顧客が異なることがある**

<!-- For a successful Scrum adoption, it's crucial to have regular intentional interactions between Stakeholders (including but not limited to customers and users) and the Scrum Team. -->

**スクラムの適用を成功させるためには**、ステークホルダー（顧客とユーザーを含むがこれらに限定されない）とスクラムチームとの間で**相互作用を生むやり取りを意図的かつ定期的に持つこと**が重要である。

<!-- A user is a Stakeholder who directly interacts with the Product to achieve specific goals or solve problems. Users experience the Product firsthand, whether it is a service, platform, or experience, and their feedback and satisfaction are crucial for ongoing Product improvement. Users may or may not have a say in purchasing decisions, but their adoption and engagement are essential for the Product's continued success. Sometimes, the user is not the same as the end-user, e.g., in B2B2C or B2B2B. For a successful Scrum adoption, it's crucial to have regular intentional interactions between users (and possibly end-users) and the Scrum Team. -->

#### ユーザー 📝

- **ユーザー**とは、**特定の目標を達成するまたは課題を解決するため**にプロダクトと**直接相互作用する**ステークホルダーの一種
- ユーザーはサービス、プラットフォーム、体験などのプロダクトを**実際に利用**し、その**フィードバックや満足度はプロダクトの継続的改善に不可欠**
- ユーザーは**購入決定に発言権を持つ場合もあれば持たない場合もある**が、ユーザーによる**プロダクトの利用とエンゲージメントはプロダクトの成功にとって重要**
- B2B2CやB2B2Bなどのように、**ユーザーとエンドユーザーが異なる場合**もある
- **スクラムの適用を成功させるためには**、ユーザー（必要に応じてエンドユーザーも）とスクラムチームとの間で**相互作用を生むやり取りを意図的かつ定期的に持つこと**が重要

<!-- A decision-maker (called a 'chooser' by Jeff Patton) (82) is a Stakeholder with the authority to approve, select, or authorize the adoption or purchase of the Product. The decision-maker is responsible for evaluating options and making the final call, often considering the needs of both users and the broader organization. Decision-makers may or may not use the Product themselves, but their choices directly impact which Products are adopted and how value is delivered to other Stakeholders. For a successful Scrum adoption, it's often better to proceed with imperfect information, and capture emerging result feedback. -->

#### 意思決定者 📝

- **意思決定者(82)**は、プロダクトの**採用や購入を承認、選択、または決定する権限を持つ**ステークホルダーの一種。**Jeff Pattonは「チューザー（選択者）」と呼んでいる**
- 意思決定者は**選択肢を評価し、最終判断を下す責任**を負い、多くの場合、**ユーザーや組織全体のニーズを考慮する**
- 意思決定者自身が**プロダクトを使用する場合もしない場合もある**が、彼らの選択は**どのプロダクトが採用され、他のステークホルダーにどのように価値が提供されるかに直接影響する**
- **スクラムの適用を成功させるためには**、**不完全な情報でも行動**し、**創発的な結果からのフィードバック（結果フィードバック）を捉えていくことが効果的**

<!-- Legislators (plus, for the purpose of this document, external or internal policy makers) establish rules, policies, and boundaries for a Product's operation. They define legal, regulatory, or organizational frameworks that shape the Product's value delivery to Stakeholders and professionalism standards. They ensure the Product aligns with external or internal mandates, guiding its evolution and sustainability. For a successful Scrum adoption, it's crucial not to exaggerate or underestimate legal requirements. -->

#### 立法者 📝

- **立法者**（加えて、この文書の目的に向けた外部または内部のポリシー立案者）は、プロダクトの運用に関する**ルール、ポリシー、境界を策定する**
- 立法者はステークホルダーへのプロダクトの価値提供やプロフェッショナリズムの基準を形成する**法的、規制的、または組織内の枠組みを定義する**
- 立法者はプロダクトが**外部や内部の要件に沿って進化し持続可能であるように導く**
- **スクラムの適用を成功させるためには**、**法的要件を過大評価も過小評価もせず、適切に対応すること**が重要

<!-- Financial sponsors provide funding and resources for Product development, launch, and improvement. They assess the Product's viability, value, and feasibility, investing informed by its potential to deliver continuous value to Stakeholders. Financial sponsors influence the Product vision, strategy, and goals to ensure alignment with return on investment and long-term sustainability. For a successful Scrum adoption, it's crucial to have a flexible attitude and flexible funding as new information comes to light. -->

#### 資金提供者 📝

- **資金提供者**は、プロダクト開発、リリース、改善のために**資金やリソースを提供する**
- 資金提供者はプロダクトの**実現可能性、価値、実行可能性を評価**し、ステークホルダーに**継続的に価値を提供できる可能性**を見極めて投資を行う
- 資金提供者は**投資回収や長期的な持続性との整合**を確かなものとするため、プロダクトの**ビジョン、戦略、目標に影響を与える**
- **スクラムの適用を成功させるためには**、新しい情報が明らかになるにつれて、**柔軟に姿勢や資金運用を変えること**が求められる

<!-- Subject matter experts contribute deep knowledge or unique skills essential to Product creation, evolution, and maintenance. Whether focused on technology, design, compliance, or a specific domain, subject matter experts support the Product's usability, feasibility, professionalism, and extendability but do not get in the way of self-managing Scrum Teams (49). They can help address satisfaction gaps and contribute to the Product's ability to adapt and identify, represent, or measure emergence (71). For a successful Scrum adoption, it's crucial to foster regular transfer of learning from subject matter experts to and across the Scrum Team. -->

#### 特定分野のエキスパート 📝

- **特定分野のエキスパート**は、プロダクトの作成、進化、保守に不可欠な**深い知識や独自のスキルを提供する**
- 技術、設計、コンプライアンス、特定ドメインなどの分野で、特定分野のエキスパートはプロダクトの**使いやすさ、実現可能性、プロフェッショナリズム、拡張性を支援する**が、**自己管理スクラムチーム(49)を妨げてはならない**
- 特定分野のエキスパートは**満足度ギャップを解消**し、プロダクトが適応しやすくなるよう支援し、**創発(71)を特定、表現、評価する**役割を担う
- **スクラムの適用を成功させるために**、特定分野のエキスパートからスクラムチームへ、そしてスクラムチーム全体への**定期的な学びの移転を促進すること**が重要

<!-- The term satisfaction gap means the difference between what Stakeholders experience now and what they wish their experience was. In other words, it's the gap between how satisfied Stakeholders are with a Product today and how satisfied they could be. -->

- **満足度ギャップ**とは、ステークホルダーが**現在体験していることと彼らが体験したいと望むこととの差**を指す
- 言い換えれば、ステークホルダーが**現在のプロダクトにどれだけ満足しているか**と、**ここからどれだけ満足させられるか**との間のギャップ

<!-- Governance refers to structures, standards, regulations, norms, processes, and practices that consciously constrain and guide a Product's direction, decision-making, and accountability. Governance fosters transparency and guides adherence to standards of value, viability, and professionalism. It provides mechanisms for managing risks and adapting the Product to changing needs or environments, supporting its long-lived and evolutionary nature. For a successful Scrum adoption, it's crucial that governance is coherent with Scrum, e.g., a single point of contact per governance area, who has intentional interactions around quality and compliance with the Scrum Team, regular Inspection and Adaptation of the governance, and no surprises. -->

#### ガバナンス 📝

```
ステークホルダーはインプット・活動・アウトカムに関心を持つ存在で、顧客・ユーザー・意思決定者・立法者・資金提供者・特定分野のエキスパートなど多様な形態がある。各ステークホルダーは異なる権力・影響力・優先事項を持ち、法律やAIなど非人間のステークホルダーも存在する。スクラム成功にはステークホルダーとの意図的で定期的な相互作用が不可欠であり、ガバナンスはスクラムと一貫性を持ちながら透明性と基準遵守を促進すべきである。
```

- **ガバナンス**とは、プロダクトの**方向性、意思決定、説明責任を意図的に制約**する**構造、標準、規制、規範、プロセス、プラクティス**を指す
- ガバナンスは**透明性を促進**し、**価値、実現可能性、プロフェッショナリズムの基準への遵守を促進**させる
- ガバナンスは**リスク管理を支援**し、**変化するニーズや環境に合わせてプロダクトを適応させるメカニズム**を提供し、プロダクトを**長期的に成長させ続ける土台**を提供する
- **スクラムの適用を成功させるために**、**ガバナンスがスクラムと一貫性を持つこと**が重要
- たとえば、**ガバナンス領域ごとに単一の連絡窓口を設定**し、**品質やコンプライアンスに関する意図的な対話をスクラムチームと行い**、**ガバナンス自体を定期的に検査・適応**し、**予期せぬ事象が生じないようにすること**が重要



<!-- ### Supporter -->

### サポーター

```
サポーターは特定のステークホルダータイプであり、チェンジエージェントとして強力な指導連合の一部を形成する。スクラムチームの繁栄を支援し、組織の仕組みをスクラム適用と一貫させるよう影響を与える。真のサポーターはスクラムチームをエンパワーメントし、経営層はサポーターが機能する環境を育成する。価値創造には他ステークホルダーとの効果的なコラボレーションが必要であり、サポーターはスクラムチームが評価するリーダーシップを示すべきである。
```

<!-- Supporter is a specific Stakeholder type. Supporters are supporting Stakeholders and change agents. Supporters are often part of a powerful guiding coalition (83), who inspire and remove demotivating factors. Supporters support the Scrum Team to thrive and influence the organization's workflows, processes, systems, Products, services, and work environment to become coherent with a Scrum adoption and emergence (71). Supporters should participate when and where needed or as requested. Value creation often requires effective and constructive collaboration with other Stakeholders. -->

- **サポーターは特定のステークホルダータイプ**。サポーターは**支援するステークホルダーでありチェンジエージェント**
- サポーターはしばしば**強力な指導連合(83)の一部**であり、**インスピレーションを与え、やる気をそぐ要因を取り除く**
- サポーターは、**スクラムチームが繁栄することを支援**し、組織のワークフロー・プロセス・システム・プロダクト・サービス・作業環境が**スクラム適用と創発(71)と一貫するよう影響を与える**
- サポーターは**必要な時と場所で、または要求に応じて参加すべき**
- **価値創造**はしばしば**他のステークホルダーとの効果的で建設的なコラボレーションを必要とする**

<!-- Depending on the size of the organization, examples of Supporters include (but are not limited to) colleagues, decision-makers, financial sponsors, governance oversight, managers, subject matter experts, marketing, HR, finance, procurement, and early adopters. Supporters who do not empower Scrum Teams to do what is recommended in this document are not really Supporters. Executives and board members have a crucial role in fostering a climate where Supporters support. Supporters should demonstrate leadership that the Scrum Team appreciates. -->

- 組織の規模に応じて、サポーターの例には、**同僚、意思決定者、資金提供者、ガバナンス監督、マネージャー、特定分野のエキスパート、マーケティング、HR、財務、調達、スクラム導入経験者**が含まれる（ただしこれらに限定されない）
- **この文書で推奨されることをスクラムチームができるようにエンパワーメントしないサポーターは、サポーターとはいえない**
- **経営層と役員**は、**サポーターが支援できる環境を育むうえで、重要な役割を持つ**
- サポーターは、**スクラムチームにとって価値のあるリーダーシップを発揮すべき**



<!-- ### Artificial Intelligence -->

### 人工知能

<!-- Artificial Intelligence (AI) is increasingly part of the work environment and may significantly expand a Scrum Team's capabilities in discovery, decision-making, Product development, and value realization. -->

**人工知能（AI）**はますます作業環境の一部となり、**ディスカバリー、意思決定、プロダクト開発、価値実現におけるスクラムチームの能力を大幅に拡張する**可能性がある。

<!-- AI may enhance Scrum through: -->

#### AIによるスクラムの強化 📝

AIは以下を通じてスクラムを強化する可能性がある：

<!--
- Empirical Process Control (64-66): AI-driven analytics improve transparency, inspection, and adaptation.
- Cognitive Augmentation: AI allows human Scrum Team members to focus on strategic, creative, and ethical considerations.
- Continuous Value Adaptation: AI could update and reprioritize Product Backlog Items informed by live user feedback and trends.
- Systems Insight: AI identifies hidden interdependencies, improving data-informed decision-making.
-->

- **経験的プロセス制御(64-66)**：**AI駆動の分析**により、**透明性・検査・適応が改善される**。
- **認知的拡張**：AIにより、人間のスクラムチームメンバーは**戦略的・創造的・倫理的な検討に集中できる**。
- **継続的な価値適応**：AIは、**リアルタイムのユーザーフィードバックとトレンドに基づき**、プロダクトバックログアイテムの**更新と再優先順位付けを行うことができる**。
- **システム洞察**：AIは**隠れた相互依存関係を特定**し、**データに基づいた意思決定を改善する**。

<!-- The possibilities are endless. Scrum Teams could leverage AI to: -->

#### AIの活用可能性 📝

```
AIはスクラムチームの能力を拡張し、経験的プロセス制御・認知的拡張・継続的な価値適応・システム洞察を通じてスクラムを強化する。テキストの曖昧さ発見、モデル適応、透明性促進、エージェント作成、既存思考への挑戦など無限の可能性がある。AIにより人間は戦略的・創造的・倫理的検討に集中でき、リアルタイムフィードバックに基づいた優先順位付けと隠れた相互依存関係の特定が可能となる。
```

**可能性は無限である**。スクラムチームは以下のためにAIを活用できる：

<!--
- Discover ambiguities in text and continuously inspect its own recommendations and results for bias, errors, and unintended consequences.
- Regularly validate and adapt models and applications.
- Foster transparency in Product Backlog ordering (sequencing).
- Create agents as AI team members.
- AI can be helpful to deliberately test and challenge the existing thinking.
-->

- **テキスト内の曖昧さを見つけ出し**、自らの推奨や結果に**偏り、誤り、意図しない結果が含まれていないかを継続的に検査する**。
- **モデルとアプリケーションを定期的に検証し適応させる**。
- プロダクトバックログの順序付け（シーケンス化）における**透明性を促進する**。
- **AIチームメンバーとしてエージェントを作成する**。
- AIは**既存の思考を意図的にテストし挑戦するのに役立つ**。



<!--
The dangers are also endless.
Maintain clear human accountability for all outcomes (guided by the accountabilities from Scrum),
   using AI as a powerful but supervised decision-making partner.
This is known as keeping the 'human in the loop.'
While AI can enhance innovation and effectiveness at the lowest costs,
   it does not replace human accountability.
AI should support—not override—Scrum's empirical process control (64-66) and ethical (57) decision-making.
The Scrum Team remains accountable for delivering valuable outcomes,
   assessing evidence, and upholding professionalism.
-->

#### AIの危険性と人間の説明責任 📝

**危険もまた、無限にあるものだ**。
すべてのアウトカムに対して、**人間に説明責任があることを明確に維持した上で**（スクラムにおける説明責任に従う）、
**強力だが監督された意思決定パートナーとしてAIを使う**。
これは**「ヒューマン・イン・ザ・ループ」として知られている**。
AIによって、**最小のコストでイノベーションと効果性を高めることができる**。
しかし、**人間の説明責任を置き換えることはできない**。
AIは**スクラムにおける経験的プロセス制御(64-66)と倫理的(57)意思決定を支援すべき**であり、
**上書きしてしまってはならないのだ**。
**スクラムチームは**、
**価値あるアウトカムの提供・エビデンスの評価・プロフェッショナリズムを守ることに対して**、
**引き続き説明責任を負う**。

<!--
AI can be a supporting tool if used with good intent.
AI tools should be evaluated
  like any other contributor
    to psychological flow (70) and learning:
Do they improve feedback loops?
Do they help validate assumptions faster?
Do they act,
   and when they do,
   is it ethical (57) action?
-->

#### AIの評価基準 📝

```
AIは無限の可能性と危険を持つ。人間の説明責任を明確に維持し「ヒューマン・イン・ザ・ループ」として監督された意思決定パートナーとしてAIを使用すべきである。AIは経験的プロセス制御と倫理的意思決定を支援するが上書きしてはならず、スクラムチームは価値提供・エビデンス評価・プロフェッショナリズムの説明責任を負う。AIツールは心理学的フローと学習への貢献で評価され、焦点は人間の力学に留まりAIは支援として位置付けられる。
```

AIは**善意に基づいて使用されれば、人を支援するツール**になりうる。
AIツールは、
**他の貢献者を評価する際と同様に
心理学的フロー(70)や学習において、評価されるべき**である。
**フィードバックループを改善するだろうか**？
**仮説をより迅速に検証するのに役立つだろうか**？
**行動するだろうか**？
行動するならば、
**倫理的(57)な行動といえるだろうか**？

<!-- Psychological flow (70) is a state of complete absorption and enjoyment in an activity, where action and awareness merge, and time seems to pass differently. -->

**心理学的フロー(70)**は、**活動への完全な没頭と楽しみの状態**であり、**行動と認識が融合**し、**時間が異なって過ぎるように見える**。

<!-- Scrum encourages the Scrum Team to experiment with AI responsibly using small, sometimes reversible trials. Adaptation and inspection apply not only to the Product but also to how AI is integrated into delivery. -->

スクラムは、スクラムチームが**小さく、時には可逆的な試行を使用してAIを責任を持って実験すること**を奨励する。**適応と検査は、プロダクトだけでなく、AIが提供にどのように統合されるかにも適用される**。

<!-- The focus should remain on the human dynamics of teamwork and collaboration, with AI positioned as a potential aid. -->

**焦点は、チームワークとコラボレーションの人間の力学に留まるべき**であり、**AIは潜在的な支援として位置付けられる**。



<!-- ### Product Developer -->

### プロダクト開発者

<!-- 'Product Developer' is a role and an accountability. All Product Developers together should possess all the skills needed to create Increments. The combined skill set is often referred to as cross-functional. -->

- **「プロダクト開発者」は役割および説明責任の一つ**
- すべてのプロダクト開発者は**インクリメントを作成するために必要な一通りのスキルを合わせ持つべき**
- これらのスキルセットは**機能横断型とよく呼ばれる**

<!-- A Product Developer may be human or automated. Human Product Developers are _Committed_ to creating, researching, inspecting, and adapting any aspect of a releasable Increment each Sprint. Their primary _Focus_ is on the current Sprint. Some capacity is often invested into future-looking refinement and examining result feedback, side effects, or other learning. -->

- プロダクト開発者は**人間でも自動化された存在でもよい**
- **人間のプロダクト開発者**は、**リリース可能なインクリメントのあらゆる側面をスプリント毎に作成、調査、検査、適応すること**を **_確約_** している
- 彼らの**主な _集中_ は現在のスプリントにある**
- ただし、プロダクト開発者の**一部のキャパシティは将来に向けたリファインメント**や、**結果からのフィードバック（結果フィードバック）、副次的影響、その他の学習の検査に投資される**ことが多い

<!-- Product Developers adhere to the Definition of Output Done and strive for net improvement. The Product Developers achieve the best results if they _Focus_ solely on one Product. If, at a given point in time, the Product Owner or Scrum Master actively works on items in the Sprint Backlog, they perform that work as Product Developers. -->

- プロダクト開発者は**アウトプット完成の定義を遵守**し、**実質的な改善を目指す**
- プロダクト開発者は、**1つのプロダクトに _集中_ することで最良の結果を達成する**
- ある時点でプロダクトオーナーまたはスクラムマスターがスプリントバックログのアイテムに対する作業に取り組む場合、その作業は**プロダクト開発者として実行する**

<!-- The Product Developers should adopt appropriate behaviors depending on the situation; these include (but are not limited to) collaborator, creator, and a champion of technical quality, discovery, delivery, and value validation. -->

- プロダクト開発者は**状況に応じて適切な行動を取る**必要がある
- 例えば、**協力者、クリエイター、技術的品質、探索、デリバリー、価値検証の推進者**として行動するなどがあるが、これらに限定されない

<!-- _At least one Product Developer should be human._ Multiple human Product Developers often improve cognitive diversity, helpful for addressing complexity. -->

**_少なくとも1人のプロダクト開発者は人間であるべきである。_** **複数の人間のプロダクト開発者**は多くの場合に**認知的多様性を向上させ**、**複雑性への対応に役立つ**。

<!-- Product Developers are always collectively accountable for: -->

#### プロダクト開発者の説明責任 📝

```
プロダクト開発者は役割かつ説明責任であり、機能横断型のスキルセットを持ち人間または自動化された存在である。少なくとも1人は人間であるべきで、複数の人間開発者が認知的多様性を高める。リリース可能なインクリメントの作成・検査・適応に確約し、現スプリントに集中しつつ将来のリファインメントにもキャパシティを投資する。説明責任には創発的計画作成・品質作り込み・使用可能なインクリメント作成・学習・日次適応・プロフェッショナルとしての相互責任・実質的改善が含まれる。
```

プロダクト開発者は**常に以下に対して説明責任を負う**：

<!-- - Creating an emergent plan in the Sprint Backlog for achieving the Sprint Goal; -->

- **スプリントゴール達成のための創発的な計画をスプリントバックログ内で作成する**
<!-- - Instilling quality by adhering to and improving the Definition of Output Done; -->
- **アウトプット完成の定義を遵守し改善することで品質を作り込む**
<!-- - Creating at least one usable Increment every Sprint; -->
- **毎スプリント少なくとも1つの使用可能なインクリメントを作成する**
<!-- - Learning, often through data that is guided by the Definition of Outcome Done; -->
- **アウトカム完成の定義により導かれるデータなどを通じて学習する**
<!-- - Adapting their plan each day toward the Sprint Goal; -->
- **スプリントゴールに向けて日々計画を適応させる**
<!-- - Holding each other accountable as professionals; and, -->
- **プロフェッショナルとしてお互いに責任を負う**
<!-- - Net improvement. -->
- **実質的な改善**

<!-- Context matters, it is crucial to consider the specific circumstances. But as a rule of thumb, a Product Developer who is neither willing nor ready nor able to be a professional should step down as a Product Developer. -->

- **文脈は重要**であり、その場で起きている**特定の状況を考慮することが重要**
- しかし**経験則として**、**プロフェッショナルとしての意志、準備、能力がないプロダクト開発者は、その役割から退くべき**



<!-- ### Product Owner -->

### プロダクトオーナー

<!-- Product Owner is a role and an accountability. The Product Owner must be human. To be effective, the Product Owner should be a leader for the Product. The Product Owner maximizes long-term value and needs to know where the value is and when it is needed. The Product Owner is expected to work at all levels and across all relevant business areas. The Product Owner collaborates with Stakeholders, the Scrum Master, and the Product Developers to create value. -->

- **プロダクトオーナーは役割および説明責任の一つ**。**プロダクトオーナーは人間でなければならない**
- 効果的であるために、プロダクトオーナーは**プロダクトのリーダーであるべき**
- プロダクトオーナーは**長期価値を最大化**し、**価値がどこにあり、いつ必要かを知る**必要がある
- プロダクトオーナーは、**すべてのレベルおよび関連するすべてのビジネス領域において業務を行うこと**が求められる
- プロダクトオーナーは、**ステークホルダー・スクラムマスター・プロダクト開発者と協働して価値を創出する**

<!-- The Product Owner uses the Product Backlog to define what gets built and in what approximate order. The Product Owner always keeps the Product Goal in mind; their primary _Focus_ is to maximize long-term value at every step. -->

- プロダクトオーナーは、**プロダクトバックログを用いて**、**何を構築するか、そしておおよそどの順序で構築するかを定義する**
- プロダクトオーナーは**常にプロダクトゴールを念頭に置いて**おり、**主要な _集中_ は、あらゆる段階で長期的な価値を最大化すること**

<!--
The Product Owner is not defined by analyzing and writing detailed Product Backlog Items.
Every minute spent not trusting the Product Developers is a missed chance
    to think more strategically, work more with Stakeholders, or create more value.
The Product Owner should adopt appropriate behaviors depending on the situation;
    these include (but are not limited to)
    being a visionary, customer representative, collaborator, influencer,
    experimenter, decision maker,
    and champion of Stakeholder engagement, clarity, Product quality, and value realization.
-->

#### プロダクトオーナーの本質 📝

プロダクトオーナーは、**詳細なプロダクトバックログアイテムの分析と記述によって定義されるものではない**。
プロダクト開発者を信頼せずに細かく管理・監督することに費やす分だけ、
**より戦略的に思考し、よりステークホルダーと連携し、
より価値を生み出すための機会が奪われる**のである。
プロダクトオーナーは**状況に応じて適切な行動を取るべき**であり、
それには以下が含まれる（ただしこれらに限定されない）。
**ビジョナリー、顧客代表、協力者、影響者、
実験者、意思決定者、
そしてステークホルダーエンゲージメント・明確性・プロダクト品質・価値実現の推進者**など。

<!-- The Product Owner is always accountable for: -->

#### プロダクトオーナーの説明責任 📝

プロダクトオーナーは**常に以下に対して説明責任を負う**：

<!-- - Stakeholder engagement, understanding Stakeholders, their power, expectations, needs, and wants; -->
<!-- - Continuously sensing, listening, learning, and adapting as needed; -->
<!-- - Continuously balancing trade-offs, including but not limited to: -->
<!--   - Quality, speed, capability, risk reduction, value, simplicity (149); -->
<!--   - Stakeholders and their multiplicity of often competing expectations and limits; -->
<!--   - Value, work climate, potential customers; -->
<!-- - Developing and explicitly communicating the Product Goal; -->
<!-- - Developing and effectively communicating a coherent Product narrative; -->
<!-- - Creating and clearly communicating Product Backlog Items; -->
<!-- - Ordering Product Backlog Items; -->
<!-- - Ensuring that the Product Backlog is transparent and understood; -->
<!-- - Effectively communicating outcomes supported by measures in the Definition of Outcome Done; -->
<!-- - Having the final say on the Definition of Outcome Done; -->
<!-- - Fostering the high-quality creation, discovery, delivery, and validation of value; and, -->
<!-- - Other Product management activities as required. -->

- **ステークホルダーエンゲージメント**・ステークホルダーとその**権力・期待・ニーズ・要望の理解**。
- 必要に応じた**継続的な感知・傾聴・学習・適応**。
- 以下の事項（ただしこれらに限定されない）において**トレードオフのバランスを取り続けること**：
  - **品質・速度・ケイパビリティ・リスク削減・価値・シンプルさ(149)**。
  - **ステークホルダー**・しばしば相反する**複数の期待と制約**。
  - **価値・作業風土・潜在顧客**。
- **プロダクトゴールを策定**し、それを**明確に伝えること**。
- **一貫性のあるプロダクトのナラティブを構築**し、それを**効果的に伝えること**。
- **プロダクトバックログアイテムの作成と明確なコミュニケーション**。
- **プロダクトバックログアイテムの並び替え**。
- プロダクトバックログの**透明性が高く、関係者に正しく理解されることの保証**。
- **アウトカム完成の定義において、計測指標に基づくアウトカムを効果的に伝えること**。
- **アウトカム完成の定義に対する最終決定権**。
- **高品質な価値の創造・ディスカバリー・デリバリー・検証の促進**。
- 必要に応じた**他のプロダクトマネジメント活動**。

<!-- The Product Owner may do the above work or collaborate with the Scrum Team to mutually agree on responsibilities for doing the above work. Regardless, the Product Owner remains accountable. -->

- プロダクトオーナーは、上記の作業を**自ら実施することもできる**し、**スクラムチームと協力してその作業に関する責任を相互に合意することもできる**
- いずれにしても、**プロダクトオーナーが説明責任を負う**

<!-- For Product Owners to succeed, all Stakeholders and Supporters should _Respect_ their decisions. These decisions are visible in the content and ordering of the Product Backlog and through the inspectable Increment at the Sprint Review. The Product Owner has delegated authority from the organization. -->

- プロダクトオーナーが成功するためには、すべてのステークホルダー・サポーターは、その**意思決定を _尊敬_ すべき**
- これらの意思決定は、**プロダクトバックログの内容・順序**・**スプリントレビューで検査可能なインクリメント**...を通じて**可視化される**
- プロダクトオーナーは**組織から権限を委譲されている**

<!-- Product Ownership requires strong Product management skills and domain skills. A Product Owner lacking these skills may need support and guidance until they develop the necessary expertise. Context matters. But as a rule of thumb, a Product Owner who is neither willing, ready, nor able to gain Product management skills should step down as Product Owner. A domain subject matter expert is not necessarily the best choice for a Product Owner as Product management skills and leadership are needed; for example, the Product Developer accountability is often more appropriate. -->

#### プロダクトオーナーに求められるスキル 📝

```
プロダクトオーナーは役割かつ説明責任で必ず人間であり、プロダクトのリーダーとして長期価値を最大化する。詳細な分析や記述ではなく戦略的思考・ステークホルダー連携・価値創出に集中すべきである。説明責任にはステークホルダーエンゲージメント・トレードオフバランス・プロダクトゴール策定・ナラティブ構築・バックログ管理・アウトカム伝達・価値検証促進が含まれる。プロダクトマネジメントスキルとリーダーシップが必要で一人の人間として意思決定に責任を負う。
```

- **プロダクトオーナーシップ**には、**優れたプロダクトマネジメントスキルおよびドメインに関するスキル**が求められる
- これらのスキルを欠くプロダクトオーナーは、**必要な専門性を身につけるまでの間、支援とガイダンスを受ける**必要がある
- **文脈は重要**。しかし**経験則として**、**プロダクトマネジメントスキルを身につける意思・準備・能力のいずれも持たないプロダクトオーナーは、その職務を辞するべき**
- **特定分野のエキスパートが、必ずしもプロダクトオーナーに最適であるとは限らない**。なぜなら、**プロダクトマネジメントスキルとリーダーシップ**が求められるため。例えば、**プロダクト開発者の方が適切である場合も多い**

<!-- If the Scrum Team inadvisably works on multiple Products, platforms, or projects, each Product, platform, or project manager should be a Stakeholder (and Supporter) of the Product Owner and collaborate to maximize long-term value. Scrum encourages the Scrum Team to stay _Focused_ and _Committed_, helping it deliver valuable outcomes and avoid the pitfalls associated with operating as a 'feature-factory.' -->

- スクラムチームが不適切に**複数の製品、プラットフォーム、またはプロジェクトに取り組む場合**、各プロダクト、プラットフォーム、またはプロジェクトのマネージャーは**プロダクトオーナーのステークホルダー（およびサポーター）**となり、**長期的な価値を最大化するために協力する**必要がある
- スクラムはスクラムチームが **_集中_ と _確約_** を維持することを奨励し、**価値あるアウトカムを届け**、**「フィーチャーファクトリー」として運営するリスクを回避することを支援する**

<!-- The Product Owner is one person, not a committee or technology. Those wanting to change the Product Backlog need to convince the Product Owner. The Product Owner maximizes long-term value and often makes trade-offs in doing so. -->

- **プロダクトオーナーは一人の人間**であり、**委員会やテクノロジーではない**
- **プロダクトバックログを変更したい人は、プロダクトオーナーを説得する必要がある**
- プロダクトオーナーは**長期的な価値を最大化**し、その過程で**しばしばトレードオフを行う**



<!-- ### Scrum Master -->

### スクラムマスター

<!-- The Scrum Master is a role and an accountability. The Scrum Master must be human. The Scrum Master is a change agent who works at all organizational levels and across business areas. The Scrum Master leads by example and guides the effectiveness of the Product Owner, Scrum Team, Stakeholders, and Supporters in their adoption of Scrum. The Scrum Master understands complexity (30-35) and is skillful in enabling the next right thing. -->

- **スクラムマスターは役割および説明責任の一つ**。**スクラムマスターは人間でなければならない**
- スクラムマスターは**チェンジエージェント**であり、**組織全体のあらゆるレベルや事業領域で活動する**
- スクラムマスターは**模範を示してリード**し、プロダクトオーナー、スクラムチーム、ステークホルダー、サポーターが**スクラムを適用する際の効果性を高めるよう導く**
- スクラムマスターは**複雑性(30-35)を理解**し、**次の正しい行動を可能にするスキル**を備える

<!-- The Scrum Master should adopt appropriate behaviors depending on the situation; these include (but are not limited to) being a guide, coach, mentor, teacher, observer, impediment remover, agent of change, effectiveness facilitator, and continuous improvement champion. The Scrum Master is neither a team administrator, status manager, taskmaster, rule-dictator, meeting-room booker, report dashboard administrator, chairperson, hero, coordinator, nor an in absentia Scrum Master, leaving everything to 'self-management.' -->

#### スクラムマスターの役割と非役割 📝

- スクラムマスターは**状況に応じて適切に振る舞う**必要がある
- これには**ガイド、コーチ、メンター、教師、観察者、障害物除去者、チェンジエージェント、効果性のファシリテーター、継続的改善の推進者**などが含まれるが、これらに限定されない
- 一方でスクラムマスターは**チーム管理者、進捗管理者、タスク指示者、ルール決定者、会議室予約係、レポートやダッシュボードの管理者、議長、ヒーロー、調整役ではなく**、すべてをチームの**「自己管理」に任せて不在のスクラムマスターでもない**

<!-- The Scrum Master is accountable for the effectiveness of the Scrum Team, Stakeholders, Supporters, and the affected people in embracing empiricism (67), self-management, and Scrum adoption as described in this document. The Scrum Master addresses whatever impedes or slows a Scrum Team's progress and cannot be resolved by the Scrum Team. -->

- スクラムマスターは、スクラムチーム・ステークホルダー・サポーター・影響を受ける人々が、本文書で説明されている**経験主義(67)・自己管理・スクラム適用の効果性を高めること**に**説明責任を負う**
- スクラムマスターは**スクラムチームが解決できない、進捗を阻害したり遅らせたりするあらゆる障害物の除去**に取り組む

<!-- The Scrum Master supports the Scrum Team, Product Owner, and Supporters in several ways, including: -->

#### スクラムマスターの支援活動 📝

スクラムマスターは、さまざまな形で**スクラムチーム、プロダクトオーナー、サポーター**を支援する：

<!-- - Helping everyone understand Scrum theory and practice, educating or coaching when needed; -->

- **全員がスクラムの理論と実践を理解できるよう支援する**。そのために必要に応じて**教育やコーチング**を行う
<!-- - Enabling the Scrum Team and Supporters to improve in a variety of ways continuously; -->
- スクラムチームとサポーターが**様々な方法で継続的に改善できるよう支援する**
<!-- - Fostering timely, purposeful, and intentional interactions; -->
- **タイムリーで意図的な目的を持った相互作用を促進する**
<!-- - Ensures the Scrum Team has a suitable Definition of Output Done; -->
- スクラムチームが**適切なアウトプット完成の定義を持てるよう努める**
<!-- - Ensuring that all Scrum events take place and are constructive, productive, and kept within the timebox; -->
- **すべてのスクラムイベントが実施され**、**建設的かつ生産的**であり、**タイムボックス内で完了するようにする**
<!-- - Causing the removal of impediments to Product-related work and to effective Scrum adoption; -->
- プロダクトに関連する作業や効果的なスクラム適用を**阻害する障害物を取り除く**
<!-- - Coaching toward self-management (49) and cross-functionality; -->
- **自己管理（49）と機能横断な行動に向けたコーチング**
<!-- - Helping the Scrum Team, Stakeholders, and Supporters understand their importance in supporting high-value Increments that meet the Definition of Output Done toward the Product Goal and Definition of Outcome Done; -->
- プロダクトゴールおよびアウトカム完成の定義の実現に向かうために、**アウトプット完成の定義を満たす価値の高いインクリメントの作成**をスクラムチーム、ステークホルダー、サポーターがサポートすることの**重要性を理解できるように支援する**
<!-- - Improving adaptiveness (80) and optimizing the flow of value; -->
- **適応性(80)を改善し**、**フロー（価値の流れ）を最適化する**
<!-- - Fostering evidence-informed confidence but being compassionate and timely to avoid overconfidence; -->
- **エビデンスに基づく自信を育みながらも**、**過信を避けるために相手の気持ちに共感しタイムリー**であろうとする
<!-- - Fostering change agency and general agency by the Scrum Team and Supporters; -->
- スクラムチームやサポーターが**チェンジエージェントとして振る舞い、あらゆることに主体的に行動するよう促す**
<!-- - Encouraging helpful behaviors within the Scrum Team that are aligned with the Scrum Values to foster trust, collaboration, and high performance; and, -->
- **信頼、コラボレーション、高パフォーマンスを促進する**スクラムの価値基準に沿ってスクラムチームが**効果的に行動することを支援する**
<!-- - Fostering the Scrum Team to deliver valuable work, get feedback, and do rework as needed, quickly and often. -->
- スクラムチームが**価値ある作業を提供し、フィードバックを得て、必要に応じて迅速かつ頻繁に再作業をできるようにする**

<!-- The Scrum Master supports the Scrum Team in several ways, including: -->

スクラムマスターは、さまざまな形でスクラムチームを支援する：

<!-- - Supporting the Scrum Team in its formation, upskilling, and continuous improvement; -->

- スクラムチームの立ち上げ、スキル向上、継続的改善を支援する
<!-- - Helping the Scrum Team understand the need for clear and concise Product Backlog Items that deliver value; and, -->
- 価値を提供する明確で簡潔なプロダクトバックログアイテムの必要性についてスクラムチームに理解してもらう
<!-- - Being vigilant that the entire Scrum Team is collaborating purposefully and intentionally with each other and Stakeholders, honoring the Definition of Output Done, and focused on creating high-value Increments according to the Definition of Outcome Done. -->
- スクラムチーム全体が互いに、そしてステークホルダーと意図的かつ目的を持って協力し、アウトプット完成の定義を尊重し、アウトカム完成の定義に沿って価値の高いインクリメントを作成することに集中できるよう常に意識を向ける。

<!-- The Scrum Master supports the Product Owner in several ways, including: -->

スクラムマスターは、さまざまな形でプロダクトオーナーを支援する：

<!-- - Helping find techniques for effective Product Goal definition and Product Backlog management; -->

- 効果的なプロダクトゴールの定義とプロダクトバックログ管理の⽅法を探すことを支援する
<!-- - Helping establish emergent Product planning for a complex (30-35) environment; -->
- 複雑な(30-35)環境における創発的なプロダクト計画の策定を支援する
<!-- - Helping the Product Owner to express outcomes as measures through the Definition of Outcome Done; -->
- アウトカム完成の定義に沿って計測されたアウトカムをプロダクトオーナーが表現できるようにする
<!-- - Helping the Product Owner understand the need for clear and concise Product Backlog Items that deliver value; and, -->
- 価値を提供する明確で簡潔なプロダクトバックログアイテムの必要性についてプロダクトオーナーに理解してもらう
<!-- - Helping the Product Owner to _Focus_ on value realization. -->
- プロダクトオーナーが価値実現に _集中_ できるよう支援する

<!-- The Scrum Master supports the Stakeholders in several ways, including: -->

スクラムマスターは、さまざまな形でステークホルダーを支援する：

<!-- - When more than expertise is needed, helping affected people and Stakeholders understand and adopt: -->
<!--   - An empirical approach for complex (30-35) work where cause and effect are only coherent in retrospect, -->
<!--   - Going beyond empirical process control, e.g., running multiple parallel safe-to-fail experiments, seeking fresh thinking, exaptation, or testing educated hunches. Exaptation means taking something that was made or used for one purpose and using it for a different purpose, especially when facing new or unclear situations. -->
<!-- - Fostering actions that support the mantra 'Stop putting items in progress; start finishing items;' -->
<!-- - Facilitating Stakeholder collaboration as requested or needed; -->
<!-- - Helping Stakeholders understand the need for clear and concise Product Backlog Items that deliver value; and, -->
<!-- - Helping the Stakeholders to _Focus_ primarily on value realization. -->

- 専門知識を超える取り組みが必要なとき、影響を受ける人やステークホルダーが以下を理解し採用することを手助けする：
  - 後から振り返ってはじめて因果関係が明らかになるような、複雑な(30-35)仕事における経験主義的アプローチ
  - 経験的プロセス制御の枠を超えたアプローチ。例えば、安全に失敗できる実験の複数並行した実行、新たな思考の追求、外適応、経験的な直感の試行。外適応（exaptation）とは、ある目的のために作成または使用されたものを、新たな状況や不透明な状況において、異なる目的に使用すること
- 「アイテムを仕掛中にするのはやめ、完成させる活動を始めよう」というモットーに沿う行動を促進する
- 要求・必要に応じて、ステークホルダーのコラボレーションを促進する
- 価値を提供する、明確で簡潔なプロダクトバックログアイテムの必要性についてステークホルダーの理解を手助けする
- ステークホルダーが価値実現に最も _集中_ できるよう手助けする

<!-- The Scrum Master works with the Supporters in several ways, including: -->

スクラムマスターは、さまざまな形でサポーターと協働する：

<!-- - Leading, training, and coaching the Supporters in the Scrum adoption; -->
<!-- - Clarifying what is getting in the way of an effective Scrum adoption; -->
<!-- - Facilitating disciplined emergent change in a direction to support the Scrum adoption; and, -->
<!-- - Fostering organizational changes toward ease of delivery vs ease of management. -->

- スクラム適用においてサポーターに対し指導・トレーニング・コーチする
- 効果的なスクラムの適用を阻害している要因を明確にする
- スクラム適用を支援する方向への規律ある創発的変化を促進する
- 管理の容易さからデリバリーの容易さを重視する組織への変革を促進する

<!-- The Scrum Master works with the organization in several ways, including: -->

スクラムマスターは、さまざまな形で組織と協働する：

<!-- - Leading, training, and coaching the organization in its Scrum adoption(s); -->
<!-- - Planning and advising Scrum adoptions within the organization; -->
<!-- - Working with related departments in how they could support the Scrum adoption; and, -->
<!-- - Removing barriers to the Scrum adoptions. -->

- 組織へのスクラム適用を指導・トレーニング・コーチする
- 組織内のスクラム適用計画を策定し助言する
- 関連部署とスクラム適用を支援する方法について協議する
- スクラムの適用を妨げる障害物を取り除く

<!-- Scrum Masters can team up with other Scrum Masters or Supporters to support the whole organization; they can also collaborate with other change agents or leaders when needed. The Scrum Master, as a change agent, is accountable for the quality of the Scrum adoption and should collaborate with other change agents to improve it. -->

- スクラムマスターは**組織全体を支援するために他のスクラムマスターやサポーターとチームを組むことができる**
- 必要に応じて**他のチェンジエージェントやリーダーと協力することもできる**
- スクラムマスターは**チェンジエージェントとしてスクラム適用の品質に説明責任を負い**、その品質を改善するために**他のチェンジエージェントと協力して進めるべき**

<!-- The Scrum Master is one person, not a committee or technology, and serves the Product Owner, Scrum Team, Stakeholders, and the larger organization. Being a change agent and leader, the Scrum Master should generally invite people to participate in the change. It is helpful if the Scrum Master has an understanding of the flow of value (68,69), lean (63), complexity theory (30-35), and other supporting and complementary theory in this document, as well as assisting people with the _how_. It is also helpful if the Scrum Master is unrelenting and has an insatiable appetite for learning and change. -->

#### スクラムマスターの資質 📝

```
スクラムマスターは役割かつ説明責任で必ず人間であり、チェンジエージェントとして組織全体で活動する。ガイド・コーチ・メンター等の役割を持つが管理者ではない。経験主義・自己管理・スクラム適用の効果性に説明責任を負い、障害物除去に取り組む。スクラムチーム・プロダクトオーナー・ステークホルダー・サポーター・組織を支援し、理論理解・継続改善・イベント促進・適応性向上・価値フロー最適化を実現する。価値の流れ・リーン・複雑性理論を理解し、他者の成功を支援し、功績を譲り責任を取る。
```

- **スクラムマスターは1人の人間**であり、**委員会や技術ではない**
- スクラムマスターは**プロダクトオーナー、スクラムチーム、ステークホルダー、より大きな組織に奉仕する**
- **チェンジエージェントかつリーダー**であり、一般的に**人々を変革へ参加するよう招待すべき**
- スクラムマスターが**価値の流れ(68,69）、リーン(63)、複雑性理論(30-35)**、そしてこの文書に記載されたその他の**支援的・補完的理論を理解**し、**どのように（_How_）行動すべきかを人々に示すこと**が望ましい
- **粘り強く**、**学びと変化への飽くなき欲求を持っている**こともスクラムマスターに求められる素養

<!-- Being a Scrum Master is a calling where helping others succeed is reward enough. A Scrum Master doesn't seek the spotlight. Like any good leader, they give credit to others and take responsibility when things go wrong. Staying in the role for a longer time helps guide the Scrum Team toward its full potential, but only if the Product Developers collectively develop self-management. Parent-style Scrum Master behavior does not foster a self-managing Scrum Team. Context matters. But as a rule of thumb, a Scrum Master who is neither willing, ready, nor able to be an agent of change should step down as a Scrum Master. -->

- スクラムマスターは、**他者の成功に貢献することを大きなやりがいとする役割**。スクラムマスターは**目立とうとはしない**
- 優れたリーダーと同様に、**功績を他者に譲り**、**物事がうまくいかない時には責任を取る**
- **長期的にスクラムマスターを務めることで**スクラムチームの**潜在能力を最大限引き出すことができる**が、それは**プロダクト開発者がチームとして自己管理を身につけた場合に限る**
- **親のようなスクラムマスターの振る舞いは自己管理スクラムチームの成長を妨げる**
- **文脈は重要**だが、**経験則として**、**変革の担い手となる意志、準備、能力がないスクラムマスターはその役割から退くべき**



<!-- ## The Scrum Artifacts in the Expansion Pack -->

## 拡張パックにおけるスクラムの作成物


---

[← 前へ](03-theory.md) | [目次](../README.md) | [次へ →](05-artifacts.md)
