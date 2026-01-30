"""分析数据来源"""
import json
import os

def analyze_sources():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"

    print("\n" + "="*70)
    print("数据来源分析")
    print("="*70)

    # 分析建材数据
    print("\n1. 建材数据来源:")
    furniture_file = os.path.join(base_dir, "furniture.json")
    with open(furniture_file, 'r', encoding='utf-8') as f:
        furniture_data = json.load(f)

    furniture_sources = {}
    for item in furniture_data:
        source = item.get('source', '未知')
        furniture_sources[source] = furniture_sources.get(source, 0) + 1

    for source, count in sorted(furniture_sources.items()):
        print(f"   {source}: {count}条")

    # 分析纺织品数据
    print("\n2. 纺织品数据来源:")
    textile_file = os.path.join(base_dir, "textile.json")
    with open(textile_file, 'r', encoding='utf-8') as f:
        textile_data = json.load(f)

    textile_sources = {}
    for item in textile_data:
        source = item.get('source', '未知')
        textile_sources[source] = textile_sources.get(source, 0) + 1

    for source, count in sorted(textile_sources.items()):
        print(f"   {source}: {count}条")

    # 分析食物数据
    print("\n3. 食物数据来源:")
    food_file = os.path.join(base_dir, "food.json")
    with open(food_file, 'r', encoding='utf-8') as f:
        food_data = json.load(f)

    food_sources = {}
    for item in food_data:
        source = item.get('source', '未知')
        food_sources[source] = food_sources.get(source, 0) + 1

    for source, count in sorted(food_sources.items()):
        print(f"   {source}: {count}条")

    # 识别需要删除的数据(自己编写的)
    print("\n" + "="*70)
    print("需要删除的自编数据识别:")
    print("="*70)

    manual_sources = [
        "第三轮数据扩充",
        "第四轮数据扩充-食物",
        "第五轮数据扩充-衣物用品",
        "第六轮数据扩充",
        "第七轮数据扩充-冬季保暖通风",
        "第八轮数据扩充-服装专用",
        "第九轮数据扩充-纺织",
        "第十轮数据扩充-智能家居园林卫浴",
        "第十一轮数据扩充-肉类坚果豆制品菌菇中药",
        "第十二轮数据扩充-铁艺家具材料"
    ]

    # 统计需要删除的数量
    furniture_delete_count = sum(furniture_sources.get(s, 0) for s in manual_sources)
    textile_delete_count = sum(textile_sources.get(s, 0) for s in manual_sources)
    food_delete_count = sum(food_sources.get(s, 0) for s in manual_sources)

    print(f"\n建材: 需删除 {furniture_delete_count} 条自编数据")
    print(f"纺织品: 需删除 {textile_delete_count} 条自编数据")
    print(f"食物: 需删除 {food_delete_count} 条自编数据")
    print(f"\n总计需删除: {furniture_delete_count + textile_delete_count + food_delete_count} 条自编数据")

    # 统计保留的真实数据
    real_sources = [
        "USDA FoodData Central API",
        "国家建材标准数据库",
        "纺织品标准数据库",
        "ECHA SCIP Database",
        "OEKO-TEX Standard 100",
        "中国食物成分表",
        "食物数据库",
        "基础数据",
        "初始数据",
        "第一轮数据扩充",
        "第二轮数据扩充"
    ]

    furniture_keep_count = sum(furniture_sources.get(s, 0) for s in real_sources)
    textile_keep_count = sum(textile_sources.get(s, 0) for s in real_sources)
    food_keep_count = sum(food_sources.get(s, 0) for s in real_sources)

    print("\n保留的真实数据:")
    print(f"建材: {furniture_keep_count} 条")
    print(f"纺织品: {textile_keep_count} 条")
    print(f"食物: {food_keep_count} 条")
    print(f"总计保留: {furniture_keep_count + textile_keep_count + food_keep_count} 条真实数据")

    print("\n" + "="*70)

    # 保存分析结果到文件
    with open('source_analysis.txt', 'w', encoding='utf-8') as f:
        f.write("\n" + "="*70 + "\n")
        f.write("数据来源分析\n")
        f.write("="*70 + "\n")

        f.write("\n1. 建材数据来源:\n")
        for source, count in sorted(furniture_sources.items()):
            f.write(f"   {source}: {count}条\n")

        f.write("\n2. 纺织品数据来源:\n")
        for source, count in sorted(textile_sources.items()):
            f.write(f"   {source}: {count}条\n")

        f.write("\n3. 食物数据来源:\n")
        for source, count in sorted(food_sources.items()):
            f.write(f"   {source}: {count}条\n")

        f.write("\n" + "="*70 + "\n")
        f.write("需要删除的自编数据识别:\n")
        f.write("="*70 + "\n")

        f.write(f"\n建材: 需删除 {furniture_delete_count} 条自编数据\n")
        f.write(f"纺织品: 需删除 {textile_delete_count} 条自编数据\n")
        f.write(f"食物: 需删除 {food_delete_count} 条自编数据\n")
        f.write(f"\n总计需删除: {furniture_delete_count + textile_delete_count + food_delete_count} 条自编数据\n")

        f.write("\n保留的真实数据:\n")
        f.write(f"建材: {furniture_keep_count} 条\n")
        f.write(f"纺织品: {textile_keep_count} 条\n")
        f.write(f"食物: {food_keep_count} 条\n")
        f.write(f"总计保留: {furniture_keep_count + textile_keep_count + food_keep_count} 条真实数据\n")

        f.write("\n" + "="*70 + "\n")

    print("\n分析结果已保存到 source_analysis.txt")

if __name__ == "__main__":
    analyze_sources()
