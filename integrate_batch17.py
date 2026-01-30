"""整合批次17数据"""
import json
import os

def integrate_batch17():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"
    fetched_file = r"D:\Users\86198\WeChatProjects\数据库\fetched_real_data_batch17.json"

    print("\n" + "="*70)
    print("批次17数据整合 - GB标准建材和纺织品")
    print("="*70)

    # 读取爬取的数据
    print("\n读取批次17数据...")
    with open(fetched_file, 'r', encoding='utf-8') as f:
        fetched_data = json.load(f)

    print(f"   已读取 {len(fetched_data)} 条新数据")

    # 按类别分类
    furniture_data = []
    textile_data = []

    for item in fetched_data:
        category = item.get('category', '')
        if category == '衣料纺织品':
            textile_data.append(item)
        else:
            furniture_data.append(item)

    print(f"\n   建材数据: {len(furniture_data)} 条")
    print(f"   纺织品数据: {len(textile_data)} 条")

    # 整合到furniture.json
    if furniture_data:
        print("\n整合建材数据...")
        furniture_file = os.path.join(base_dir, "furniture.json")
        with open(furniture_file, 'r', encoding='utf-8') as f:
            existing_furniture = json.load(f)

        all_furniture = existing_furniture + furniture_data

        with open(furniture_file, 'w', encoding='utf-8') as f:
            json.dump(all_furniture, f, ensure_ascii=False, indent=2)

        print(f"   {len(existing_furniture)} -> {len(all_furniture)} (+{len(furniture_data)})")

    # 整合到textile.json
    if textile_data:
        print("\n整合纺织品数据...")
        textile_file = os.path.join(base_dir, "textile.json")
        with open(textile_file, 'r', encoding='utf-8') as f:
            existing_textile = json.load(f)

        all_textile = existing_textile + textile_data

        with open(textile_file, 'w', encoding='utf-8') as f:
            json.dump(all_textile, f, ensure_ascii=False, indent=2)

        print(f"   {len(existing_textile)} -> {len(all_textile)} (+{len(textile_data)})")

    # 总结
    print("\n" + "="*70)
    print("批次17数据整合完成!")
    print("="*70)
    print(f"\n新增真实数据: {len(fetched_data)} 条")
    print(f"  - 建材: {len(furniture_data)} 条")
    print(f"  - 纺织品: {len(textile_data)} 条")

    print("\n新增类别:")
    print("  建材:")
    print("    - 防水材料: 聚氨酯防水涂料、SBS改性沥青防水卷材")
    print("    - 保温材料: 岩棉板、挤塑聚苯板(XPS)")
    print("    - 门窗材料: 断桥铝合金型材")
    print("    - 管道材料: PPR给水管、UPVC排水管")
    print("    - 吊顶材料: 铝扣板")
    print("  纺织品:")
    print("    - 高档面料: 真丝绸缎、天丝、莫代尔")
    print("    - 功能面料: 速干布、抗菌银离子布、防紫外线布、阻燃防护布")

    print("\n版本: v17.0")
    print("="*70)

if __name__ == "__main__":
    integrate_batch17()
