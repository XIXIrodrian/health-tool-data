"""整合批次16的真实数据"""
import json
import os

def integrate_batch16():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"
    fetched_file = r"D:\Users\86198\WeChatProjects\数据库\fetched_real_data_batch16.json"

    print("\n" + "="*70)
    print("批次16数据整合 - 整合USDA API和标准数据")
    print("="*70)

    # 读取爬取的数据
    print("\n读取批次16数据...")
    with open(fetched_file, 'r', encoding='utf-8') as f:
        fetched_data = json.load(f)

    print(f"   已读取 {len(fetched_data)} 条新数据")

    # 按类别分类
    food_data = []
    furniture_data = []
    textile_data = []

    for item in fetched_data:
        category = item.get('category', '')
        if category in ['谷物类', '蔬菜类', '水果类', '肉类', '海鲜类', '乳制品', '豆类', '坚果类']:
            food_data.append(item)
        elif category == '衣料纺织品':
            textile_data.append(item)
        else:
            furniture_data.append(item)

    print(f"\n   食物数据: {len(food_data)} 条")
    print(f"   建材数据: {len(furniture_data)} 条")
    print(f"   纺织品数据: {len(textile_data)} 条")

    # 整合到food.json
    if food_data:
        print("\n整合食物数据...")
        food_file = os.path.join(base_dir, "food.json")
        with open(food_file, 'r', encoding='utf-8') as f:
            existing_food = json.load(f)

        all_food = existing_food + food_data

        with open(food_file, 'w', encoding='utf-8') as f:
            json.dump(all_food, f, ensure_ascii=False, indent=2)

        print(f"   {len(existing_food)} -> {len(all_food)} (+{len(food_data)})")

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
    print("批次16数据整合完成!")
    print("="*70)
    print(f"\n新增真实数据: {len(fetched_data)} 条")
    print(f"  - 食物: {len(food_data)} 条 (USDA API)")
    print(f"  - 建材: {len(furniture_data)} 条 (GB国家标准)")
    print(f"  - 纺织品: {len(textile_data)} 条 (GB/FZ标准)")
    print("\n数据来源:")
    print("  - USDA FoodData Central API")
    print("  - GB 18582-2020 (内墙涂料标准)")
    print("  - GB/T 5849-2016 (细木工板标准)")
    print("  - GB/T 18102-2020 (强化复合地板标准)")
    print("  - GB 18583-2008 (胶粘剂标准)")
    print("  - GB/T 9775-2008 (石膏板标准)")
    print("  - GB 18401 (纺织品安全标准)")
    print("  - OEKO-TEX Standard 100")
    print("\n版本: v16.0")
    print("="*70)

if __name__ == "__main__":
    integrate_batch16()
