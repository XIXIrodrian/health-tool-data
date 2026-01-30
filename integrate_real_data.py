"""数据整合脚本 - 将爬取的真实数据整合到现有数据库"""
import json
import os

def integrate_real_data():
    """整合真实数据到现有数据库"""
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"
    fetched_file = r"D:\Users\86198\WeChatProjects\数据库\fetched_real_data.json"

    print("\n" + "="*70)
    print("第十四轮数据扩充 - 整合真实爬取数据")
    print("="*70)

    # 读取爬取的数据
    print("\n读取爬取的真实数据...")
    with open(fetched_file, 'r', encoding='utf-8') as f:
        fetched_data = json.load(f)

    print(f"   已读取 {len(fetched_data)} 条新数据")

    # 按类别分类
    food_data = []
    furniture_data = []
    textile_data = []

    for item in fetched_data:
        category = item.get('category', '')
        if category in ['谷物类', '肉类', '蛋类', '未分类']:
            food_data.append(item)
        elif category == '衣料纺织品':
            textile_data.append(item)
        else:
            furniture_data.append(item)

    print(f"   食物数据: {len(food_data)} 条")
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
    print("第十四轮数据扩充完成!")
    print("="*70)
    print(f"\n新增真实数据: {len(fetched_data)} 条")
    print("  - 食物: {len(food_data)} 条（来自USDA FoodData Central API）")
    print(f"  - 建材: {len(furniture_data)} 条")
    print(f"  - 纺织品: {len(textile_data)} 条")
    print("\n数据来源:")
    print("  - USDA FoodData Central API (美国农业部食物数据中心)")
    print("  - 国家建材标准数据库")
    print("  - 纺织品标准数据库")
    print("\n版本: v14.0")
    print("="*70)

if __name__ == "__main__":
    integrate_real_data()
