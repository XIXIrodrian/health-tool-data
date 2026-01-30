"""清理自编数据，保留真实数据"""
import json
import os
from datetime import datetime

def clean_manual_data():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"

    print("\n" + "="*70)
    print("数据清理 - 删除自编数据，保留真实数据")
    print("="*70)

    # 定义需要删除的手动编写数据来源
    manual_sources = [
        "第三轮数据扩充",
        "第四轮数据扩充-房屋建材",
        "第五轮数据扩充-更多房屋建材",
        "第六轮数据扩充-厨卫照明暖通",
        "第七轮数据扩充-衣料",
        "第七轮数据扩充-食物",
        "第八轮数据扩充-衣料专项",
        "第九轮数据扩充-羊毛环保运动时尚",
        "第十轮数据扩充-智能家居园林卫浴五金",
        "第十一轮数据扩充-肉类坚果豆制品菌菇中药",
        "第十二轮数据扩充-铁艺家具材料"
    ]

    # 清理建材数据
    print("\n1. 清理建材数据...")
    furniture_file = os.path.join(base_dir, "furniture.json")
    with open(furniture_file, 'r', encoding='utf-8') as f:
        furniture_data = json.load(f)

    original_furniture_count = len(furniture_data)
    cleaned_furniture = [item for item in furniture_data if item.get('source') not in manual_sources]
    deleted_furniture = original_furniture_count - len(cleaned_furniture)

    with open(furniture_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_furniture, f, ensure_ascii=False, indent=2)

    print(f"   原有: {original_furniture_count} 条")
    print(f"   删除: {deleted_furniture} 条自编数据")
    print(f"   保留: {len(cleaned_furniture)} 条真实数据")

    # 清理纺织品数据
    print("\n2. 清理纺织品数据...")
    textile_file = os.path.join(base_dir, "textile.json")
    with open(textile_file, 'r', encoding='utf-8') as f:
        textile_data = json.load(f)

    original_textile_count = len(textile_data)
    cleaned_textile = [item for item in textile_data if item.get('source') not in manual_sources]
    deleted_textile = original_textile_count - len(cleaned_textile)

    with open(textile_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_textile, f, ensure_ascii=False, indent=2)

    print(f"   原有: {original_textile_count} 条")
    print(f"   删除: {deleted_textile} 条自编数据")
    print(f"   保留: {len(cleaned_textile)} 条真实数据")

    # 清理食物数据
    print("\n3. 清理食物数据...")
    food_file = os.path.join(base_dir, "food.json")
    with open(food_file, 'r', encoding='utf-8') as f:
        food_data = json.load(f)

    original_food_count = len(food_data)
    cleaned_food = [item for item in food_data if item.get('source') not in manual_sources]
    deleted_food = original_food_count - len(cleaned_food)

    with open(food_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_food, f, ensure_ascii=False, indent=2)

    print(f"   原有: {original_food_count} 条")
    print(f"   删除: {deleted_food} 条自编数据")
    print(f"   保留: {len(cleaned_food)} 条真实数据")

    # 总结
    print("\n" + "="*70)
    print("数据清理完成!")
    print("="*70)
    print(f"\n总计删除: {deleted_furniture + deleted_textile + deleted_food} 条自编数据")
    print(f"  - 建材: -{deleted_furniture} 条")
    print(f"  - 纺织品: -{deleted_textile} 条")
    print(f"  - 食物: -{deleted_food} 条")

    print(f"\n总计保留: {len(cleaned_furniture) + len(cleaned_textile) + len(cleaned_food)} 条真实数据")
    print(f"  - 建材: {len(cleaned_furniture)} 条")
    print(f"  - 纺织品: {len(cleaned_textile)} 条")
    print(f"  - 食物: {len(cleaned_food)} 条")

    print("\n保留的数据来源:")
    print("  - USDA FoodData Central API (美国农业部食物数据)")
    print("  - 国家建材标准数据库")
    print("  - 纺织品标准数据库")
    print("  - ECHA SCIP Database (欧洲化学品数据库)")
    print("  - OEKO-TEX Standard 100 (纺织品环保认证)")
    print("  - 中国食物成分表")
    print("  - 早期基础数据 (第一、二轮)")

    print("\n数据库版本: v15.0 (清理自编数据)")
    print("清理时间: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("="*70)

if __name__ == "__main__":
    clean_manual_data()
