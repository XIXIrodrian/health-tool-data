"""数据结构迁移脚本 - 统一为详细版铁艺格式"""
import json
import os
from datetime import datetime

def migrate_furniture_data(item):
    """迁移家具建材数据"""
    data = item.get('data', {})

    # 确保category在data中
    if 'category' not in data:
        data['category'] = item.get('category', '未分类')

    # 添加扩展字段（如果不存在）
    if 'advantages' not in data:
        data['advantages'] = [
            "符合国家环保标准",
            "性能稳定",
            "适用范围广"
        ]

    if 'disadvantages' not in data:
        data['disadvantages'] = [
            "需要定期维护",
            "价格因材质而异"
        ]

    if 'maintenance_tips' not in data:
        data['maintenance_tips'] = [
            "定期清洁",
            "避免潮湿环境",
            "注意通风"
        ]

    if 'health_recommendations' not in data:
        data['health_recommendations'] = [
            "选择符合环保标准的产品",
            "新品需通风散味",
            "定期检查材料状态"
        ]

    if 'physical_properties' not in data:
        data['physical_properties'] = {
            "硬度": "根据材质",
            "重量": "根据材质",
            "耐用性": "良好"
        }

    if 'application_scenarios' not in data:
        data['application_scenarios'] = ["室内", "家居"]

    item['data'] = data
    item['last_updated'] = datetime.now().isoformat()
    item['version'] = "13.0"

    return item

def migrate_textile_data(item):
    """迁移纺织品数据"""
    data = item.get('data', {})

    # 添加category到data中
    if 'category' not in data:
        data['category'] = item.get('category', '衣料纺织品')

    # 从health_benefits和health_risks提取优缺点
    if 'advantages' not in data:
        data['advantages'] = data.get('health_benefits', ["舒适透气", "亲肤柔软"])

    if 'disadvantages' not in data:
        # 从health_risks提取
        risks = data.get('health_risks', [])
        disadvantages = []
        for risk in risks:
            if isinstance(risk, dict):
                disadvantages.append(risk.get('description', risk.get('type', '')))
        data['disadvantages'] = disadvantages if disadvantages else ["需要适当护理", "不同材质特性不同"]

    if 'maintenance_tips' not in data:
        # 从care_instructions提取
        care = data.get('care_instructions', {})
        tips = []
        if isinstance(care, dict):
            if care.get('washing'):
                tips.append(f"清洗方式: {care['washing']}")
            if care.get('drying'):
                tips.append(f"晾干方式: {care['drying']}")
            if care.get('ironing'):
                tips.append(f"熨烫方式: {care['ironing']}")
        data['maintenance_tips'] = tips if tips else ["按洗涤标签说明护理", "避免暴晒"]

    if 'health_recommendations' not in data:
        data['health_recommendations'] = [
            "选择有认证的产品",
            "新品清洗后再穿",
            "注意材质过敏"
        ]

    if 'physical_properties' not in data:
        data['physical_properties'] = {
            "手感": "根据面料",
            "透气性": "根据面料",
            "弹性": "根据面料"
        }

    if 'application_scenarios' not in data:
        data['application_scenarios'] = ["日常穿着", "服装制作"]

    item['data'] = data
    item['last_updated'] = datetime.now().isoformat()
    item['version'] = "13.0"

    return item

def migrate_food_data(item):
    """迁移食物数据"""
    data = item.get('data', {})

    # 确保category在data中
    if 'category' not in data:
        data['category'] = item.get('category', '未分类')

    # 从health_benefits提取优点
    if 'advantages' not in data:
        benefits = data.get('health_benefits', [])
        data['advantages'] = benefits if benefits else ["提供营养", "天然健康"]

    # 从contraindications提取缺点/注意事项
    if 'disadvantages' not in data:
        contra = data.get('contraindications', [])
        data['disadvantages'] = contra if contra else ["适量食用", "注意食用禁忌"]

    if 'maintenance_tips' not in data:
        data['maintenance_tips'] = [
            "妥善储存",
            "注意保质期",
            "避免交叉污染"
        ]

    if 'health_recommendations' not in data:
        intake = data.get('recommended_intake', {})
        recommendations = []
        if isinstance(intake, dict):
            for key, value in intake.items():
                recommendations.append(f"{key}建议摄入量: {value}")
        if not recommendations:
            recommendations = ["均衡饮食", "适量食用", "注意个人体质"]
        data['health_recommendations'] = recommendations

    if 'physical_properties' not in data:
        nutrients = data.get('nutrients', {})
        props = {}
        if isinstance(nutrients, dict):
            for key, value in nutrients.items():
                if isinstance(value, dict) and 'value' in value:
                    props[key] = f"{value['value']}{value.get('unit', '')}" if value['value'] else "适量"
        data['physical_properties'] = props if props else {"营养成分": "丰富"}

    if 'application_scenarios' not in data:
        data['application_scenarios'] = ["日常饮食", "营养补充"]

    item['data'] = data
    item['last_updated'] = datetime.now().isoformat()
    item['version'] = "13.0"

    return item

def main():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"

    print("\n" + "="*70)
    print("数据结构迁移开始 - 统一为详细版铁艺格式")
    print("="*70)

    # 迁移家具建材数据
    print("\n1. 迁移家具建材数据...")
    furniture_file = os.path.join(base_dir, "furniture.json")
    with open(furniture_file, 'r', encoding='utf-8') as f:
        furniture_data = json.load(f)

    migrated_furniture = [migrate_furniture_data(item) for item in furniture_data]

    with open(furniture_file, 'w', encoding='utf-8') as f:
        json.dump(migrated_furniture, f, ensure_ascii=False, indent=2)

    print(f"   家具建材数据迁移完成: {len(migrated_furniture)} 条")

    # 迁移纺织品数据
    print("\n2. 迁移纺织品数据...")
    textile_file = os.path.join(base_dir, "textile.json")
    with open(textile_file, 'r', encoding='utf-8') as f:
        textile_data = json.load(f)

    migrated_textile = [migrate_textile_data(item) for item in textile_data]

    with open(textile_file, 'w', encoding='utf-8') as f:
        json.dump(migrated_textile, f, ensure_ascii=False, indent=2)

    print(f"   纺织品数据迁移完成: {len(migrated_textile)} 条")

    # 迁移食物数据
    print("\n3. 迁移食物数据...")
    food_file = os.path.join(base_dir, "food.json")
    with open(food_file, 'r', encoding='utf-8') as f:
        food_data = json.load(f)

    migrated_food = [migrate_food_data(item) for item in food_data]

    with open(food_file, 'w', encoding='utf-8') as f:
        json.dump(migrated_food, f, ensure_ascii=False, indent=2)

    print(f"   食物数据迁移完成: {len(migrated_food)} 条")

    # 总结
    print("\n" + "="*70)
    print("数据结构迁移完成!")
    print("="*70)
    print(f"\n总计迁移: {len(migrated_furniture) + len(migrated_textile) + len(migrated_food)} 条数据")
    print(f"  - 家具建材: {len(migrated_furniture)} 条")
    print(f"  - 纺织品: {len(migrated_textile)} 条")
    print(f"  - 食物: {len(migrated_food)} 条")
    print("\n新增字段:")
    print("  - advantages (优点)")
    print("  - disadvantages (缺点)")
    print("  - maintenance_tips (保养要点)")
    print("  - health_recommendations (健康建议)")
    print("  - physical_properties (物理特性)")
    print("  - application_scenarios (适用场景)")
    print("\n版本: v13.0")
    print("="*70)

if __name__ == "__main__":
    main()
