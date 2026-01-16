#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to update all summaries in the Scrum Guide Expansion Pack docs.
- Shortens summaries to approximately 150 Japanese characters
- Adds bold formatting to important keywords
"""

import re
import sys

# Define all the updated summaries with their section identifiers
SUMMARIES = {
    # 01-background.md
    "01_history": "**Ken SchwaberとJeff Sutherland**が開発し、**2020年版スクラムガイド**がその本質を説明。広く採用されるため**シンプルに保たれている**。",
    
    "01_purpose": "**2020年版スクラムガイド**を基に**現代に適したガイダンス**を提供。Ralph Jochamの貢献で**オリジナルアイデアを深掘り**。",
    
    "01_structure": "**未来志向の視点**で各要素の**何と なぜ**を説明。**継続的に進化**するドキュメントで初回は**順次読むこと**を推奨。",
    
    "01_prerequisites": "**スクラムの基礎知識**を前提とし、**2020年版スクラムガイドを事前に読む**ことを推奨。**参考文献と付録**で深い理解を促進。",
    
    "01_mindset": "**主体性・透明性・継続的改善**などの価値観とともに適用。提示されたガイダンスを**超越し**、**持続的な好奇心**で探求し続けること。",
    
    "01_scope": "**自己管理チーム**による**製品発見から価値実現**までのすべてを支援。元々はソフトウェア開発から始まり、現在は**多様な専門分野**で広く採用。",
    
    "01_stakeholder_value": "ステークホルダーが**重要と考えるニーズ**を指すが、彼ら自身が認識しているとは限らない。**観察やエビデンス**で価値が顕在化し、**エビデンスで確認されるまで仮説**。",
    
    "01_definition": "**複雑なプロダクトデリバリー**のフレームワークで**専門性を超えた能力**が必要。**プロダクトライフサイクル全体**をカバーし、**因果関係は振り返りで**明らかに。",
    
    "01_approach": "**ステークホルダーのニーズに一貫して対応**する環境を育む。**イテレーティブで インクリメンタル**なアプローチで**リスク削減と継続的改善**を実現。",
    
    "01_risk": "**リスクは将来の不利な結果**をもたらす要因で**時間経過でも予測不可能**。**市場リスク・フィット・技術・コンプライアンス**など多様な要因を含む。",
    
    "01_cycle": "**問題提示者と解決者の距離を縮める**。**サポーター**がスクラム採用を支援し、**プロダクトオーナー**がゴール設定、**チーム**が価値創出、全員で**検査・適応を繰り返す**。",
    
    "01_release": "プロダクトの**新バージョンをステークホルダーが利用可能**にするプロセス。**開発サイクルの転換点**となり**ステークホルダー価値の実現可能性**を具現化。",
    
    "01_flexibility": "**意図的に不完全**で**詳細なプロセスではなく関係性と相互作用を導くフレームワーク**を提供。様々な手法で補完可能だが**文脈により異なる**。",
    
    "01_improvement": "**既存プラクティスと統合**するか場合によっては置き換える。チーム・サポーター・マネジメント・環境・技術の**効果性を透明に評価**し**継続的改善**を可能に。",
    
    "01_origin": "**竹内弘高と野中郁次郎**が**ラグビーから借用**し、**知識を企業全体に急速に広めて優れたプロダクトを提供する**チームを説明するために考案。",
    
    # 02-scrum-basics.md
    "02_complexity": "**未知が既知より多く**、**原因と結果は後から明確**になる。**複雑性思考**がツールと洞察を提供し、**創発**を通じて機会を捉え**透明性・検査・適応**で改善を実現。",
    
    "02_emergence": "**複雑なシステム内の相互作用**から予測できないパターンが生じる現象。**タイムボックスや役割**などの制約が創発を導き、**望ましいパターンを発見し増幅**する。",
    
    "02_self_managing": "**軌道確認・アクション・作業方法決定・対立解決・問題修正**を自ら行う。マネージャーは**指示ではなくリーダーシップ**を発揮し、**価値中心の自己管理チーム**が創発に不可欠。",
    
    "02_professionalism": "**優秀性を追求**し**尊敬・透明性・説明責任**で協働。**ライフサイクル全体に責任**を負い、**技術的卓越性**には**クリーンコード・TDD・継続的デリバリー**などが含まれる。",
    
    "02_values": "**集中・公開・確約・勇気・尊敬**の5つで構成。**心理的安全性と積極的コラボレーション**を促進し、**透明性と信頼**を育み**言葉と行動の一致**を確保。",
    
    "02_values_ooda": "**OODAループ**の視点から理解可能。**観察・状況判断・意思決定・行動**の4ステップで迅速な判断を支援。スクラムの価値基準が**すべてに適用**され**創発的ソリューション**を育む。",
    
    # 03-theory.md  
    "03_product_thinking": "**短期的成長と長期的価値創出のバランス**を取る考え方。**キャズムを超える**戦略や**技術的負債の管理**が重要で、プロダクトオーナーは**トレードオフを扱う力**が必要。",
    
    "03_chasm": "**特定ニッチ市場に焦点**を当て**信頼性の高い完全なソリューション**を提供。**リファレンス顧客を獲得**し市場での**信頼性を確立**することでキャズムを超える。",
    
    "03_debt": "**短期的近道が生む追加作業**で時間とともに開発速度を低下。**プロフェッショナルは最小化**を努め、負債を負う場合は**透明性を保ち緩和策を準備**する。",
    
    "03_goal_orientation": "**スプリントゴールはプロダクトゴールへの一歩**となり、さらに**プロダクト戦略やビジョン**を支える。**短期と長期のバランス**が持続可能なプロダクト開発の鍵。",
    
    "03_systems_thinking": "**要素の相互関連性**を認識し**行動の波及効果が予測不可能で非線形**。**局所的最適化を避け**、理論に基づく**実験とフィードバックループ**で洞察を獲得。",
    
    "03_discovery": "**観察・対話・分析**で人々のニーズを理解し**学び続けるプロセス**。**コラボレーション・創造性・失敗を恐れない姿勢**を重視し、**スプリント内で実践**しながら**毎スプリントインクリメント**を生み出す。",
    
    "03_leadership": "共通ゴール達成のため人々を**導き鼓舞する能力**で**管理職ではなく資質**。**レジリエンス重視**し**現地現物の精神**で事実を収集、**価値実現に徹底**しながら**思いやりと倫理観**を持つ。",
    
    "03_first_principles": "**最も基本的な真実に分解**し**類推や慣例に頼らず根本から解決策**を構築。**確実に知っていること**から出発し**ブレークスルー**を生み、**独創的思考と継続改善**で変革的結果を実現。",
    
    "03_change": "**単なるツール導入ではなく第一原理に立ち返るアプローチ**。**短期と長期のバランスを取る変革推進力**が必要で、**人材開発・プロセス・態度・習慣**など多様な要素を変革し**文化が創発**。",
    
    "03_emergent_approach": "**創発的アプローチ・効果的なチェンジエージェント・熱心な協力**が必要。**意図的取り組みと日々の進捗**が重要で、**規律ある創発的変化**を方向性を持って始め**当たり前に**する。",
    
    # 04-roles.md
    "04_team_characteristics": "**機能横断型で階層がなく**、ディスカバリー・デリバリー・価値検証に**必要なスキルを保持**。**サポーターの支援**を受け**自己管理**で誰が何をいつどのように行うかを決定。",
    
    "04_team_work": "**毎スプリントでインクリメント**を提供し**継続的に自己管理**して同期・リリース。**小規模で俊敏性**を保ちつつ重要な作業を完了できる規模を持ち**意図的な相互作用とリーダー支援**が不可欠。",
    
    "04_collaboration": "**継続的な相互作用と共有説明責任**で協調的チームワークを促進。**発見・開発・価値検証の重複**により価値駆動型アプローチが可能となり**不確実性を受け入れ迅速に適応**。",
    
    "04_aligned_autonomy": "**共通目標に集中しながら解決方法を自ら決定**し**イノベーションと組織の一貫性**を両立。**認知的多様性**の育成が不可欠で**批判はアイデアに向け全員が責任共有**。",
    
    "04_stakeholder": "**インプット・活動・アウトカムに関心を持つ**存在で**顧客・ユーザー・意思決定者**など多様な形態。各ステークホルダーは**異なる権力・影響力・優先事項**を持ち**意図的で定期的な相互作用**が不可欠。",
    
    "04_supporter": "**支援するステークホルダーでありチェンジエージェント**。**スクラムチームの繁栄**を支援し組織の仕組みを**スクラム適用と一貫**させる。**真のサポーターはエンパワーメント**し経営層はサポーターが機能する環境を育成。",
    
    "04_ai": "**無限の可能性と危険**を持つ。**人間の説明責任を明確に維持**し**監督された意思決定パートナー**として使用。**経験的プロセス制御と倫理的意思決定を支援**するが上書きしてはならない。",
    
    "04_developer": "役割かつ説明責任で**機能横断型スキル**を持ち**人間または自動化**された存在。**少なくとも1人は人間**で**認知的多様性**を高める。**インクリメント作成・品質作り込み・日次適応・相互責任**に説明責任。",
    
    "04_product_owner": "役割かつ説明責任で必ず人間であり**プロダクトのリーダー**として**長期価値を最大化**。**ステークホルダーエンゲージメント・トレードオフバランス・プロダクトゴール策定・バックログ管理・価値検証促進**に説明責任。",
    
    "04_scrum_master": "役割かつ説明責任で必ず人間であり**チェンジエージェント**として組織全体で活動。**経験主義・自己管理・スクラム適用の効果性**に説明責任を負い**価値の流れ・リーン・複雑性理論**を理解し**他者の成功を支援**。",
}

def find_note_blocks(content):
    """Find all NOTE blocks in the content"""
    # Pattern to match NOTE blocks: > [!NOTE] followed by > lines
    pattern = r'(> \[!NOTE\]\n(?:> [^\n]*\n)+)'
    return [(m.start(), m.end(), m.group(1)) for m in re.finditer(pattern, content)]

def get_section_context(content, start_pos, window=500):
    """Get context around a position to identify the section"""
    context_start = max(0, start_pos - window)
    context = content[context_start:start_pos]
    # Look for markdown headers
    headers = re.findall(r'###? ([^\n]+)', context)
    if headers:
        return headers[-1]
    return ""

def update_file(filepath, summaries_map):
    """Update summaries in a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    note_blocks = find_note_blocks(content)
    print(f"\nProcessing {filepath}: Found {len(note_blocks)} NOTE blocks")
    
    # Track which summaries we've used
    used_keys = set()
    
    # Process from end to start to maintain positions
    for start, end, block_text in reversed(note_blocks):
        # Extract current summary (remove > and [!NOTE])
        lines = block_text.strip().split('\n')
        current_summary = ' '.join(line.lstrip('> ').strip() for line in lines[1:])
        
        # Get section context
        section_name = get_section_context(content, start)
        
        # Try to find matching summary in our map
        matched_key = None
        for key, new_summary in summaries_map.items():
            if key not in used_keys:
                # Check if this summary matches this section
                # We'll match based on order and file
                matched_key = key
                used_keys.add(key)
                break
        
        if matched_key:
            new_summary = summaries_map[matched_key]
            new_block = f"> [!NOTE]\n> {new_summary}\n"
            content = content[:start] + new_block + content[end:]
            print(f"  Updated: {section_name[:50]}...")
        else:
            print(f"  Skipped (no mapping): {section_name[:50]}...")
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return len(note_blocks)

def main():
    files = [
        'docs/01-background.md',
        'docs/02-scrum-basics.md',
        'docs/03-theory.md',
        'docs/04-roles.md',
        'docs/05-artifacts.md',
        'docs/06-events.md',
        'docs/07-multi-team.md',
        'docs/08-conclusion.md',
        'docs/09-appendix.md'
    ]
    
    # Build a mapping based on file and order
    file_summaries = {
        'docs/01-background.md': [
            SUMMARIES[k] for k in sorted(SUMMARIES.keys()) if k.startswith('01_')
        ],
        'docs/02-scrum-basics.md': [
            SUMMARIES[k] for k in sorted(SUMMARIES.keys()) if k.startswith('02_')
        ],
        'docs/03-theory.md': [
            SUMMARIES[k] for k in sorted(SUMMARIES.keys()) if k.startswith('03_')
        ],
        'docs/04-roles.md': [
            SUMMARIES[k] for k in sorted(SUMMARIES.keys()) if k.startswith('04_')
        ],
    }
    
    total_updated = 0
    for filepath in files:
        if filepath in file_summaries:
            # Create a simple sequential map for this file
            summaries = file_summaries[filepath]
            file_map = {f"{filepath}_{i}": s for i, s in enumerate(summaries)}
            count = update_file(filepath, file_map)
            total_updated += count
    
    print(f"\n✓ Total NOTE blocks processed: {total_updated}")

if __name__ == '__main__':
    main()
