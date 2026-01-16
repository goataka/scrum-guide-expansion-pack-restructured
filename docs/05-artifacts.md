# スクラムの作成物

[← 前へ](04-roles.md) | [目次](../README.md) | [次へ →](06-events.md)

---

<!--
このコンテンツは、Scrum Guide Expansion Pack (https://scrumexpansion.org) から取得したものです。

著者: Ralph Jocham、John Coleman、Jeff Sutherland
翻訳: 内山遼子、川口恭伸、長沢智治、山本尊人、和田圭介
ライセンス: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
出典: https://github.com/ScrumGuides/ScrumGuide-ExpansionPack

詳細は NOTICE.md を参照してください。
-->


<!-- Scrum's artifacts provide Transparency about what the Scrum Team and Stakeholders believe will deliver value. Thus, everyone can have the same basis for Inspection and Adaptation. -->

- スクラムの作成物は、スクラムチームとステークホルダーが価値を生み出すと信じている内容について、透明性をもたらす
- これにより、誰もが同じ基準で作業内容を検査し、必要に応じて適応できるようになる

<!-- Each artifact contains a commitment: -->

- また、各作成物には「確約（コミットメント）」が含まれている

<!-- - For the Product serving the Stakeholders, it is the Definition of Outcome Done. -->

- ステークホルダーに提供するプロダクトについては、アウトカム完成の定義
<!-- - For the Increment that is a candidate update for the Product, it is the Definition of Output Done. -->
- プロダクトのアップデート予定であるインクリメントについては、アウトプット完成の定義
<!-- - For the Product Backlog, it is the Product Goal. -->
- プロダクトバックログについては、プロダクトゴール
<!-- - For the Sprint Backlog, it is the Sprint Goal. -->
- スプリントバックログについては、スプリントゴール

<!-- Upon release of the Increment (output), the Product is what creates value (outcomes). Value is the measurable or observable fulfillment or creation of expectations, needs, or wants from the Stakeholders' perspective. -->

- インクリメント（アウトプット）がリリースされることで、プロダクトが価値（アウトカム）を生み出すことになる
- ここでいう価値とは、計測可能または観察可能な形で、ステークホルダーの視点から見た、期待やニーズ、要望が満たされたり、新たに生み出されたりすること

<!-- These commitments reinforce the pillars of Transparency, Inspection, and Adaptation, enabling empirical process control (64-66). The Product Goal is fixed for as long as no contrary evidence or observations emerge in the observed Product's Definition of Outcome Done. The Definition of Output Done is not weakened during the Sprint. So what could be diminished or changed instead? It could be the Acceptance Criteria for a specific Product Backlog Item, the implementation or fidelity of a specific feature, or even alternative Product Backlog Items for achieving the Sprint Goal, etc. -->

- これらのコミットメントは、透明性・検査・適応というスクラムの三本柱を強化し、経験的なプロセス制御を可能にする(64-66）
- プロダクトゴールは、プロダクトのアウトカム完成の定義において反対のエビデンスや観察が現れない限り、固定される
- アウトプット完成の定義はスプリント中に妥協されることはない
- では、代わりに何が見直されたり変更されたりするのかというと、例えば、特定のプロダクトバックログアイテムの受け入れ基準や、特定の機能の実装内容や精度、あるいはスプリントゴール達成のための代替となるプロダクトバックログアイテムなどが挙げられる

<!-- If the Product Goal shifts often, it could indicate that something is off, perhaps due to a lack of _Focus_ on what matters. _Focus_ is about being professional and deciding what to work on but also what not to work on. -->

- もしプロダクトゴールが頻繁に変わるようであれば、それは何かがうまくいっていない兆候を示しており、重要なことに _集中_ できていない可能性がある
- _集中_ とは、プロフェッショナルとして何に取り組むかだけでなく、何に取り組まないかを決めること

<!-- ### Product -->

### プロダクト

<!-- The Product is an artifact. A Product can be a holistic experience or a platform. It can also be a service, physical, digital, or hybrid, delivering continuous value to Stakeholders (including but not limited to users). -->

- プロダクトは作成物の一つである
- プロダクトは包括的な体験またはプラットフォームとなることができる
- また、サービス、物理的、デジタル、またはハイブリッドであり、ステークホルダー（ユーザーを含むがこれに限定されない）に継続的な価値を提供する

<!-- An experience is a specific solution designed to meet the needs of Stakeholders, including the user, ideally external to the organization. It provides a direct interaction that delivers value. It is typically focused on solving a particular problem or opportunity, or a set of them for Stakeholders, including but not limited to customers, decision-makers, and users. -->

- 体験とは、理想的には組織外のユーザーを含むステークホルダーのニーズを満たすように設計された特定のソリューション
- それは価値を提供する直接的な相互作用を提供する
- ステークホルダーの特定の課題や機会、またはそれらの組み合わせを解決することに焦点を当てている。対象となるステークホルダーには、顧客、意思決定者、ユーザーなどが含まれるがそれらに限定されない

<!-- A platform is an architectural device, foundational infrastructure, or set of tools that enables developers to build Products in order to provide an experience. Platforms provide a base for multiple Products to be developed upon, focusing on scalability, reliability, and flexibility for engineers rather than direct user interaction. -->

- プラットフォームとは、体験を提供するためのプロダクトを開発者が構築することを可能にするアーキテクチャデバイス、基盤となるインフラストラクチャ、またはツールセット
- プラットフォームは複数のプロダクトを構築するための基盤を提供し、直接的なユーザーとの相互作用よりもエンジニアのためのスケーラビリティ、信頼性、柔軟性に重点を置く

<!-- The Scrum Team and Stakeholders need to have a clear understanding at all times of what the Product is, who the customers, users, or decision-makers are, and the type of Product it is —like one for end-users, employees, or Scrum Teams—has different Stakeholders and ways it creates value. A Product is evolutionary and often long-lived. The Product needs a single Product Backlog to increase Transparency and maximize value. -->

- スクラムチームとステークホルダーはこのプロダクトが何であるか、顧客、ユーザー、または意思決定者が誰であるか、そしてどのようなタイプのプロダクトなのか（エンドユーザー向け、従業員向け、スクラムチーム向けなど）を常に明確な理解を持つ必要がある
- プロダクトのタイプにより異なるステークホルダーが存在し、価値創出の方法も異なることを理解する必要がある
- プロダクトは進化的であり、しばしば長期にわたり存続する。透明性を高め、価値を最大化するために、プロダクトには単一のプロダクトバックログが必要

<!-- Context matters. But as a rule of thumb, for a Product to create and maintain traction, it helps if the Product: -->

- 文脈は重要である
- しかし、経験則として、プロダクトが牽引力を生み出し、それを維持するためには、以下の条件を満たすことが有効：

<!-- - Sufficiently addresses satisfaction gaps; -->

- 満足度のギャップに十分に対処している
<!-- - Is valuable, desirable, viable, usable, feasible, safe, and secure; -->
- 価値があり、望ましく、実行可能で、使用可能で、実現可能で、安全で、セキュアである
<!-- - Has professionalism built-in; -->
- プロフェッショナリズムが組み込まれている
<!-- - Has a compelling, clear, and outcome-metric-oriented Product Vision, Product strategy, and Product Goal, often including intent, rationale, and anti-goals; -->
- 明確で説得力があり、成果指標に基づくプロダクトビジョン、プロダクト戦略、プロダクトゴールを備えている。その中には意図、根拠、避けるべきゴールが含まれる事が多い
<!-- - Adapts and improves to identify, represent, or measure emergence (71); and, -->
- 創発(71)を特定、表現、評価するために適応し改善する
<!-- - Is extendable and maintainable. -->
- 拡張可能であり、保守可能である

<!-- The Product is the manifestation of _why_ we do _what_ we do. -->

- プロダクトは、我々が何のために仕事をしているのかを表現したもの

<!-- #### Commitment: Definition of Outcome Done -->

#### コミットメント：アウトカム完成の定義

<!-- The Definition of Outcome Done is a commitment. It describes the observable evidence measures (quantitative or qualitative) required to demonstrate realized benefits, often referred to as value validation. It could be for the overall Product or a specific goal. It's often best to define the measures for value validation before realization starts, as this avoids biases and mistaken interpretations. -->

- アウトカム完成の定義はコミットメントの一つである
- これは、実現された価値を示すために必要な観察可能なエビデンスの計測基準（定量的または定性的）を記述し、しばしば価値検証と呼ばれる
- これはプロダクト全体、または特定のゴールに対して設定される。バイアスや誤った解釈を避けるため、実装を開始する前に価値検証のための計測基準を定義しておくことが最善であることが多い

<!-- Outcomes and related interpretations inform future adaptations, ideally confirming the intended Stakeholder impact(including but not limited to business or user impact)—measuring whether the output fulfills the anticipated outcome(s) and delivers real value. It could be for a specific goal, such as a larger feature or several features, and be validated through Product telemetry (the Product can measure its own usage). Alternatively, it could be for the overall Product, where it is often about the strategic impact and the validation of the efficacy of the implemented strategic deployment (120-124). Or a combination of both. -->

- アウトカムとそれに関連する解釈は、将来の適応のための情報として役立ち、理想的には意図したステークホルダーへの影響（ビジネスやユーザーの影響を含むがそれに限定されない）を確認することを目的とする
- つまり、アウトプットが期待されたアウトカムを実現し、真の価値を提供したかどうかを計測する
- これは、特定の大きな機能や複数の機能などに向けて設定された特定のゴールを対象とし、プロダクトのテレメトリ（プロダクト自身がその利用状況を計測する）によって検証される。あるいは、プロダクト全体を対象とし、戦略的影響や実施された戦略展開(120-124)の有効性の検証に関するもの。またはこれら両方の組み合わせ

<!-- Favor direct evidence over circumstantial evidence. For example: -->

- アウトカム完成の定義は状況証拠よりも直接的な証拠（エビデンス）を優先する。例えば以下のようなもの：

<!-- - Customer outcomes could Focus on delivering measurable value to customers, such as increased customer satisfaction, customer long-term cost reduction, or the number of customer jobs addressed. -->

- 顧客のアウトカムは顧客満足度の向上、顧客の長期コスト削減、対応した顧客の案件数など、計測可能な顧客価値の提供に集中することができる
<!-- - User outcomes could address specific changes in user behavior that solve problems and improve experiences, like completing tasks more efficiently or engaging with new features. -->
- ユーザーのアウトカムはタスクをより効率的に完了することや新機能の利用など、問題を解決し体験を改善するユーザー行動の具体的な変化に対処することができる
<!-- - Product Stakeholder outcomes could connect these behavioral changes to Product performance metrics, e.g., trends in Product customer, decision-maker/user metrics, Product time to release, time to learn, time to pivot, etc. -->
- プロダクトステークホルダーのアウトカムは、これらの行動変化をプロダクトのパフォーマンス指標に結び付けることができる。例えば、顧客、意思決定者/ユーザー指標のトレンド、プロダクトとしてのリリースまでの時間、学習までの時間、ピボットまでの時間など
<!-- - Business Stakeholder outcomes, e.g., compliance, business long-term cost reduction, business results, trends in market share, customer satisfaction across all Products, organizational time to release, time to learn, time to pivot, etc. -->
- ビジネスステークホルダーのアウトカム。例えば、コンプライアンス、長期的なコスト削減、ビジネス成果、市場シェアの傾向、すべてのプロダクトにわたる顧客満足度、組織としてのリリースまでの時間、学習までの時間、ピボットまでの時間など
<!-- - Scrum Team outcomes such as improved technical capability (psychological flow (70), frequency of release, tooling, skills, technical debt, UX or CX debt, capacity), climate/culture for net improvement and innovation. -->
- スクラムチームのアウトカム。技術的能力の向上（心理学的フロー状態(70)、リリース頻度、ツール、スキル、技術的負債、UXまたはCX負債、開発能力）、実質的な改善やイノベーションのための風土や文化など

<!-- User eXperience (UX) or Customer eXperience (CX) debt is the sum of design and implementation choices—intentional or not—that make a Product or service less usable, enjoyable, or effective for users or customers. Recognizing, tracking, and addressing this debt is essential for delivering Products that truly meet user needs and expectations. -->

- ユーザーエクスペリエンス（UX）負債やカスタマーエクスペリエンス（CX）負債とは、意図的であるか否かに関わらず、プロダクトやサービスをユーザーや顧客にとって使いにくく、楽しめず、効果的でないものとする設計および実装上の選択の総和
- この負債を認識し、追跡し、対処することは、真にユーザーのニーズと期待に応えるプロダクトを提供するために不可欠

<!-- Measures over time make Product, market, and Stakeholder trends (including but not limited to customer or user) transparent; these can be reviewed at any time during the Sprint, including the Sprint Review. -->

- 時間の経過に伴い計測することで、プロダクト、市場、ステークホルダーのトレンド（顧客やユーザーを含むがこれらに限定されない）が透明化される
- これらはスプリントレビューを含めスプリントの期間中のいつでも参照可能

<!-- ### Increment -->

### インクリメント

<!-- The Increment is an artifact. It is the integration of the work completed to the standard of the Definition of Output Done. The Increment is an output and a Product candidate. -->

- インクリメントは作成物の一つである
- これはアウトプット完成の定義の標準まで基準に従って完了した作業を統合したもの
- インクリメントはアウトプットでありプロダクトの候補

<!-- Multiple Increments may be created within a Sprint through the completion of Product Backlog Items. Each Increment is thoroughly verified, usable, and integrated with all previous Increments. The resulting aggregated Increment is inspected as soon as possible, at the latest at the Sprint Review. The Increment must be usable and useful to enable result feedback. An Increment is central to Scrum as it enables ongoing value validation. -->

- プロダクトバックログアイテムの完了により、スプリントでは複数のインクリメントを作成可能
- 各インクリメントは徹底的に検証され、利用可能であり、すべての以前のインクリメントと統合されている
- 結果として得られる集約されたインクリメントは、可能な限り早く、遅くともスプリントレビューで検査される。インクリメントは結果からのフィードバック（結果フィードバック）を可能にするために利用可能かつ有用でなければならない。インクリメントは継続的な価値検証を可能にするため、スクラムの中心的な存在

<!-- An Increment-candidate does not qualify as an Increment until it meets the quality standard of the Definition of Output Done. Only an Increment can be released. An Increment should be a concrete stepping stone toward the Product Goal. Increments may be delivered to Stakeholders or released prior to the Sprint Review. _The best value validation is attained through result feedback._ -->

- インクリメント候補は、アウトプット完成の定義の品質基準を満たすまでインクリメントとして認められない
- リリース可能なのはインクリメントのみ
- インクリメントはプロダクトゴールに向けた具体的な踏み⽯となるべき。スプリントレビューより前にインクリメントをステークホルダーにデリバリーしたり、リリースされたりする可能性がある。_最良の価値検証は結果からのフィードバック（結果フィードバック）を通じて実現される_

<!-- #### Commitment: Definition of Output Done -->

#### コミットメント：アウトプット完成の定義

<!-- The Definition of Output Done is a commitment. It formally describes the quality measures that express due diligence for the Increment so that it could be delivered to Stakeholders. -->

- アウトプット完成の定義はコミットメントの一つである
- これはステークホルダーにインクリメントを提供可能とするために適正に評価をしていること（デューデリジェンス）を表す品質基準を正式に記述したもの

<!-- The Definition of Output Done typically includes (but is not limited to) both technical standards and Product qualities. The Scrum Team creates it if not provided by the organization as a minimum. If there are multiple Scrum Teams on the same Product, they share the same Definition of Output Done as the common foundation but may improve upon it. -->

- アウトプット完成の定義は通常、技術的標準とプロダクト品質の両方を含む（ただしこれらに限定されない）
- 組織から最低限の基準としてアウトプット完成の定義を提供していない場合は、スクラムチームが作成する
- プロダクトに関わるスクラムチームが複数ある場合、共通の基盤として同じアウトプット完成の定義を共有するが、それを改善することもできる

<!-- The Scrum Team is duty-bound to conform to the Definition of Output Done and continuously improve it. The Increment is cumulative. The Definition of Output Done is for the good of the Product and its Stakeholders. The Definition of Output Done is the overall quality standard for the whole Increment, not the specific standard for each item (e.g., Acceptance Criteria). -->

- スクラムチームはアウトプット完成の定義を遵守し、継続的に改善する義務を負う
- インクリメントは累積的なもの
- アウトプット完成の定義はプロダクトとそのステークホルダーの利益のために存在する。これはインクリメント全体に対する総合的な品質基準であり、個々のアイテムの基準（例：受け入れ基準）ではない

<!-- A released Increment enables result feedback for Definition of Outcome Done value validation. -->

- リリースされたインクリメントは、アウトカム完成の定義による価値検証のための結果からのフィードバック（結果フィードバック）を可能にする

<!-- ### Product Backlog -->

### プロダクトバックログ

<!-- The Product Backlog is an artifact. It is the emergent, ordered (sequenced) list of Product Backlog Items needed to attain the Product Goal. The Product Backlog provides Transparency (work clarity) and is the single source of work for the Scrum Team in order to achieve the Product Goal. The Product Owner, always keeping value in mind, guides the ordering of the Product Backlog Items in the Product Backlog. A smaller Product Backlog often provides more Transparency. -->

- プロダクトバックログは作成物の一つである
- これは創発的かつ順番に並べられた、プロダクトゴールの達成に必要なプロダクトバックログアイテムの一覧
- プロダクトバックログは透明性（作業の明確さ）を提供し、スクラムチームにとってプロダクトゴールを達成するために必要な作業の唯一の情報源。プロダクトオーナーは常に価値を意識し、プロダクトバックログ内のプロダクトバックログアイテムの順序付けを行う。プロダクトバックログが小さいほど、透明性はより高める

<!-- #### Product Backlog Item -->

#### プロダクトバックログアイテム

<!-- A Product Backlog Item is a potentially valuable item in the Product Backlog. It is not necessarily in any specific format. It is intended to deal with a problem or opportunity. It can include Acceptance Criteria that can tell when work is completed, in addition to the Definition of Output Done. One might deliver exactly what was requested but still not deliver sufficient outcomes. So, a Product Backlog Item can also include clearly defined Outcome Criteria that can tell when sufficient value is delivered, in addition to what is already in the Definition of Outcome Done. -->

- プロダクトバックログアイテムは、プロダクトバックログ内にある潜在的に価値のあるアイテム
- これは必ずしも特定の形式である必要はない。プロダクトバックログアイテムは問題や機会に対処することを目的としている
- アウトプット完成の定義に加えて、作業が完了したことを判断するための受け入れ基準を含むことができる。要求された内容を正確に提供したとしても、十分なアウトカムが得られない場合がある。そのため、アウトカム完成の定義に含まれているものに加えて、十分な価値が提供されたかどうかを示すための明確なアウトカム基準をプロダクトバックログアイテムに含むことができる

<!-- A Product Backlog Item is a single piece of work that discovers or delivers value. A Product Backlog Item can evolve anytime, even while Product Developers work on it. During refinement, it is broken down into smaller, more understandable (mostly to the Scrum Team) Product Backlog Items that could deliver value. Occasionally, an item in the Product Backlog might not be related to the Product Goal; if this happens often, it's worth examining if the _Focus_ level might not be where it needs to be. The Scrum Team and Stakeholders should _Focus_ on outcomes over outputs, keep the trade-off balance right, and not let the Scrum Team become a 'feature-factory' or 'discovery-factory.' -->

- プロダクトバックログアイテムは価値を発見または提供するための単一の作業単位
- プロダクトバックログアイテムは、プロダクト開発者が作業している間であっても、いつでも進化する可能性がある
- リファインメントの過程で、価値を提供をでき、より小さく、スクラムチームにとってより理解しやすいプロダクトバックログアイテムに分割される。時にはプロダクトバックログ内のアイテムがプロダクトゴールと無関係である場合もある。そのような状況が頻繁に起きるのであれば、 _集中_ のレベルが適切に保たれているか検査する価値がある。スクラムチームおよびステークホルダーは、アウトプットよりもアウトカムに _集中_ し、トレードオフのバランスを保ち、スクラムチーム が「機能工場」や「発見工場」にならないようにする必要がある

<!-- #### Acceptance Criteria -->

#### 受け入れ基準

<!-- Acceptance Criteria, if they exist, describe when an output for a specific Product Backlog Item is complete, in addition to the Definition of Output Done. Acceptance Criteria in refined items should provide unambiguous clarity on _what_ is requested. Acceptance Criteria include criteria specific to a Product Backlog Item not already addressed in the Definition of Output Done; they can be functional or non-functional. Acceptance Criteria can evolve anytime, even while Product Developers work on them. -->

- 受け入れ基準が存在する場合、アウトプット完成の定義の記述に加えて、特定のプロダクトバックログアイテムのアウトプットがいつ完了するかを記述する
- リファインメントされたアイテムの受け入れ基準は、_何_ が要求されているかについて曖昧さのない明確な基準を示す必要がある
- 受け入れ基準は、アウトプット完成の定義でまだ扱われていないプロダクトバックログアイテム固有の機能的・非機能的な基準を含む。受け入れ基準は、プロダクト開発者が作業している間であっても、いつでも進化する可能性がある

<!-- #### Outcome Criteria -->

#### 成果基準

<!-- Outcome criteria, if they exist, describe the intention of the Product Backlog Item; it is the _why_ behind the _what_. The fulfillment of Outcome Criteria often complements the Definition of Outcome Done for the Product. They can include criteria specific to a Product Backlog Item not already addressed in the Definition of Outcome Done. If questions arise, the Outcome Criteria provide direction; they can be in the form of a narrative or measures, ideally, the latter. Outcome Criteria can evolve anytime, even while Product Developers work on them. -->

- 成果基準が存在する場合、プロダクトバックログアイテムの意図を記述する。つまり、何（_What_）の背後にあるなぜ（_Why_）を記述するもの
- 成果基準の達成は、しばしばプロダクトのアウトカム完成の定義を補完する
- 成果基準は、アウトカム完成の定義でまだ扱われていないプロダクトバックログアイテム固有の基準を含むことがある。疑問が生じた場合、成果基準は方向性を示す。それは、ナラティブ形式または計測可能な指標の形式を取るが、理想的には後者。成果基準は、プロダクト開発者が作業している間であっても、いつでも進化する可能性がある

<!-- #### Refinement -->

#### リファインメント

<!-- Refinement is an activity. It may be formal (an additional event) or informal. Refinement is an ongoing emergent process that fosters clarity and reduces risk; it builds enough understanding and confidence that the selected or upcoming Product Backlog Items are ready (can be completed in accordance with the Definition of Output Done within a small number of days, or shorter). Various types of dependencies are considered. -->

- リファインメントは活動の一つであり、正式な場合（追加イベント）もあれば、非公式な場合もある
- リファインメントは明確さを育み、リスクを軽減する継続的な創発プロセス
- これは選択された、または直近で対応予定のプロダクトバックログアイテムが準備完了（アウトプット完成の定義に従って数日以内に完了できる）であるために必要な十分な理解と確信をチームに形成する。様々な種類の依存関係が考慮される

<!-- Refinement involves breaking down Product Backlog Items into smaller, more understandable (mostly to the Scrum Team) Product Backlog Items. It can add more details such as description, Acceptance Criteria, Outcome Criteria, order, and size. Attributes vary but should be meaningful to the Scrum Team. Refinement can involve research, including but not limited to, problem or opportunity validation, user or customer experience, solution validation. The Product Developers, and nobody else, are responsible for sizing the Product Backlog Items. The Product Owner may influence the Product Developers by helping them understand and select potential trade-offs. -->

- リファインメントは、プロダクトバックログアイテムをより小さく、（主にスクラムチームにとって）より理解しやすく分解することを含む
- 説明、受け入れ基準、成果基準、並び順、サイズなどの詳細を追加することができる。属性はさまざまあるが、スクラムチームにとって意味のあるものでなければならない
- リファインメントには、問題や機会の検証、ユーザーや顧客の体験、ソリューションの検証などの調査活動が含まれるがこれに限定されない。プロダクト開発者のみがプロダクトバックログアイテムのサイズを決定する責任を負う。プロダクトオーナーは、潜在的なトレードオフを理解し、選択できるよう支援することでプロダクト開発者に影響を与えることができる

<!-- Participants often include Stakeholders and members of the Scrum Team; it is not uncommon for Product Developers to work directly with Stakeholders. Refinement is often supported or facilitated by the Product Owner. The Product Owner can _Focus_ more on Product ownership if the Product Developers have a broad understanding of the Product. Generally speaking, it is a forward-looking activity that offers clarity, direction, and potential _Focus_ for upcoming Sprints. -->

- リファインメントの参加者には、多くの場合ステークホルダーやスクラムチームのメンバーが含まれる
- プロダクト開発者がステークホルダーと直接作業することも珍しいことではない。リファインメントは、通常プロダクトオーナーにより支援またはファシリテートされる
- プロダクト開発者がプロダクトに対する幅広い理解を持っている場合、プロダクトオーナーはプロダクトオーナーシップの発揮により _集中_ できる。一般に、リファインメントは今後のスプリントに向けて明確さ、方向性、潜在的な _集中_ を提供する将来を見据える活動

<!-- #### Commitment: Product Goal -->

#### コミットメント：プロダクトゴール

<!-- The Product Goal is a commitment. It is represented through the Product Backlog, which is owned by the Product Owner. It is the current single, more strategic, ambitious objective (the _why_). It gives direction for the Product and enables _Focus_ for the Product Developers working on the Product. It improves Transparency by providing a clear, valuable direction for the Product Developers to work toward, using a more tactical Sprint Goal (the _why_ for the Sprint). -->

- プロダクトゴールはコミットメントの一つである
- これはプロダクトオーナーがオーナーであるプロダクトバックログを通じて表現される。プロダクトゴールは現時点における単一かつより戦略的で野心的な目標（なぜ（_Why_））
- プロダクトに方向性を示し、プロダクト開発者がプロダクトに取り組むための _集中_ の源となる。プロダクトゴールはより戦術的な目標であるスプリントゴール（スプリントのなぜ（_Why_））を通じて、プロダクト開発者が向かうべき明確で価値のある方向性を提供し、透明性を高める

<!-- A Product Goal is the medium-term objective for the Scrum Team and the Stakeholders (and Supporters). The Scrum Team should fulfill (or abandon) one Product Goal before taking on the next. -->

- プロダクトゴールはスクラムチームとステークホルダー（および サポーター）の中期的な目標
- 次のプロダクトゴールに移る前に、スクラムチームはひとつのプロダクトゴールを達成（または放棄）しなければならない

<!-- A Product Goal is usually an as-yet-unproven assertion about value. It can be expressed as one of many things, including a set of hypotheses about closing or lessening satisfaction gaps. It gets the balance right by focusing on a subset of the multiplicity of Stakeholders (including but not limited to customers or users) expectations and limits. Through Inspection and Adaptation, it's essential to embrace uncertainty (72), result feedback, side effects, and other learnings. -->

- プロダクトゴールは通常、価値に関する未証明の仮説
- 満足度ギャップを埋めるもしくは大きくするための仮説のセットを含む、様々なものひとつとして表現される。それは、多様なステークホルダー（顧客やユーザーを含むがそれに限定されない）の期待や制約の中から、焦点を絞り適切なバランスを取るもの
- 検査と適応を通じて、不確実性(72）、結果からのフィードバック（結果フィードバック）、副作用、その他の学習を受け入れることが不可欠

<!-- #### What about a Product Vision? -->

#### プロダクトビジョンについては？

<!-- Many organizations work with a Product Vision, which helps visualize a potential future. The Scrum Team can use a Vision as input for considering a Product Goal. A Product Vision is a meaningful, long-term set of valuable desired outcomes. The medium-term Product Goal is often a stepping stone toward a long-term Product Vision. -->

- 多くの組織では、未来の可能性を見える化するためにプロダクトビジョンを活用する
- スクラムチームは、プロダクトゴールを検討するためのインプットとしてビジョンを用いることができる
- プロダクトビジョンは、意味のある長期的な価値のある望ましいアウトカムのまとまり。中期的なプロダクトゴールは、多くの場合、長期的なプロダクトビジョンに向けた踏み石となる

<!-- As the Scrum Team and Stakeholders inspect and adapt toward the Product Goal, they need to be _open_ to the idea that the Product Vision or Product Goal might also need to adapt. Often, several Product Goals are sequentially achieved while working toward a vision. -->

- スクラムチームとステークホルダーがプロダクトゴールに向けての検査と適応を行う際、プロダクトビジョンやプロダクトゴールも適応が必要な場合があるという考えに公開（_Open_）である必要がある
- 多くの場合、ビジョンに向かって進む中で、複数のプロダクトゴールを一つずつ達成していく

<!-- The key thing to note is that a Product Vision is often a work of fiction; none of it may be true. Forming hypotheses and running experiments in a direction is essential, and is where Scrum can add the most value. -->

- 重要な点は、プロダクトビジョンは創作作品であることであり、必ずしも真実とは限らない
- 仮説を立てて、方向性を持って実験を重ねることが不可欠であり、そこでスクラムが最も価値を発揮する

<!-- A Product Vision is often inspiring but can be overwhelming. The Product Goal reduces overwhelm by acting as a more tangible vertical slice of a Product Vision or as an enabler for a Product Vision. -->

- プロダクトビジョンは多くの場合、刺激的であるが、規模が大きすぎて負担に感じることもある
- プロダクトゴールは、プロダクトビジョンのより具体的な垂直スライスや、またはプロダクトビジョン実現のきっかけとなることで、負担感を軽減する

<!-- ### Sprint Backlog -->

### スプリントバックログ

<!-- The Sprint Backlog is an artifact. It is composed of the Sprint Goal (the _why_ for the Sprint), the set of Product Backlog Items selected (the _what_, also known as the forecast) for the Sprint, and often has an actionable plan for delivering the Increment (the _how_). It provides Transparency (work clarity) throughout the Sprint. -->

- スプリントバックログは作成物の一つである
- スプリントゴール（スプリントのなぜ（_Why_））、スプリントのために選んだプロダクトバックログアイテムのセット（何（_What_）をやるのか、つまり予測）、そして、多くの場合、インクリメントを提供するための実行可能な計画（どのように（_How_））で構成される
- これにより、スプリント全体を通じた透明性（作業の明確性）が高まる

<!-- The Sprint Backlog is a plan by and for the Product Developers. It is the Product Developers' viewpoint of the understood work to achieve the Sprint Goal (the why for the Sprint). Suppose a suboptimal scenario where most items in the Sprint Backlog are continually unrelated to the Product Goal. In that case, the _Focus_ and _Commitment_ Scrum Values are not being upheld. -->

- スプリントバックログは、開発者による開発者のための計画
- これはスプリントゴール（スプリントのなぜ（Why））を達成するために、どんな作業が必要かを開発者の視点でまとめている
- もしスプリントバックログのほとんどのアイテムがプロダクトゴールと関係ない状況が続いてしまうと、スクラムの _集中_ と _確約_ の価値基準が守られなくなる

<!-- Within the context of the Sprint Goal, the Product Developers update their plan, even the forecast, throughout the Sprint as more is learned. The Sprint Backlog should have enough work to get started, e.g., start with one or two Product Backlog Items toward the Sprint Goal. The Product Developers inspect their progress toward the Sprint Goal in the Daily Scrum or more often. Product Developers learn to adapt and respond to uncertainty (72). -->

- スプリントゴールの文脈の中においても、プロダクト開発者がより多くのことを学ぶにつれ、スプリント全体を通じた、予測すら含めた計画を更新する
- スプリントバックログには、まず始めるのに十分な作業が入っていればよい。例えば、最初は、スプリントゴールに向けた1つまたは2つのプロダクトバックログアイテムで十分
- プロダクト開発者はデイリースクラムにて、またはより頻繁に、スプリントゴールに向けた進捗を検査し、不確実性に適応し対応することを学ぶ(72）

<!-- #### Commitment: Sprint Goal -->

#### コミットメント：スプリントゴール

<!-- [2020 Scrum Guide: '... the Sprint Goal is a commitment by the Developers ...']  -->

- [2020年版スクラムガイド: 「スプリントゴールは開発者が確約するものだが...」]

<!-- The Sprint Goal is a commitment created and owned by the Scrum Team. The Sprint Goal is the single unifying objective of the Sprint (the _why_) for the Product Developers, created in Sprint Planning. Delivery of the Sprint Goal is a commitment by the Product Developers. The Sprint Backlog (including the _why_, the _what,_ and, often, the _how_) provides _Focus_ and flexibility regarding the evolving work, thus improving Transparency. -->

- スプリントゴールはスクラムチームによって作成され、所有されるコミットメントの一つ
- スプリントゴールはプロダクト開発者にとってのスプリントの唯一のかつ統一された目的（なぜ（_Why_））であり、スプリントプランニングで作成される。スプリントゴールの達成はプロダクト開発者による確約
- スプリントバックログ（なぜ（_why_）、なに（_what_）、そして多くの場合どのように（_how_）を含む）は進化する作業に対して _集中_ と柔軟性をもたらし、透明性を向上させる

<!-- The Sprint Goal encourages the Scrum Team to work together rather than on separate initiatives. If the work turns out to be different from what the Product Developers expected, the Product Developers collaborate with the Product Owner to negotiate possibilities within the Sprint without affecting the Sprint Goal. No one tells the Product Developers how to size or do their work. -->

- スプリントゴールはスクラムチームが個別に作業するのではなく、協力して作業することを促進する
- もし作業がプロダクト開発者の予想と異なることが判明した場合は、スプリントゴールに影響を与えることがないように、プロダクト開発者はプロダクトオーナーと協力してスプリント内で対応する可能性を調整する
- 誰もプロダクト開発者に作業の見積りや進め方を指示することはない

<!-- If there are multiple objectives, as long as they are coherent with the Product Goal it might be ok. Be careful. Consider the trade off of context switching and focus. The Scrum Team should strive to attain balance over time –– balancing current team capabilities and climate, current stakeholder value, potential stakeholder value and time to value. -->

- 複数のゴールがある場合でも、それらがプロダクトゴールと整合性がとれている限りは問題はないかもしれない。ただし、注意が必要
- コンテキスト切り替えと集中のトレードオフを考慮すること
- スクラムチームは、時間をかけてバランスをとるよう努めるべきであり、そのバランスとは現在のチームの能力と風土、現在のステークホルダーへの価値、潜在的なステークホルダーへの価値、そして価値を届けるまでの時間との間で成り立つもの

<!-- ## The Scrum Events in the Expansion Pack -->

## 拡張パックにおけるスクラムイベント


---

[← 前へ](04-roles.md) | [目次](../README.md) | [次へ →](06-events.md)
