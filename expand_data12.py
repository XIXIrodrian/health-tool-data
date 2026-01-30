"""第十二轮数据扩充脚本 - 铁艺家具材料"""
import json
import sys
import os
from datetime import datetime
import hashlib

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def generate_id(name, category):
    unique_string = f"{category}_{name}_{datetime.now().isoformat()}"
    return hashlib.md5(unique_string.encode()).hexdigest()[:16]

def expand_iron_art_materials():
    """第十二轮家具建材数据扩充 - 铁艺材料"""
    new_materials = [
        {
            "category": "金属家具",
            "material_type": "铁艺家具",
            "chemical_components": [
                {"name": "冷轧钢板", "cas": "N/A", "hazard": "低"},
                {"name": "锌（镀锌层）", "cas": "7440-66-6", "hazard": "低"},
                {"name": "防锈漆", "cas": "N/A", "hazard": "中"},
                {"name": "涂料（表面处理）", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "潮湿腐蚀", "severity": "中", "description": "长时间不通风会导致空气潮湿，对铁艺配件产生侵蚀"},
                {"type": "紫外线损伤", "severity": "中", "description": "阳光长时间照射会导致漆色发生变化，出现干裂剥落"},
                {"type": "金属氧化", "severity": "中", "description": "金属受到氧化会发生变质"},
                {"type": "磕碰损伤", "severity": "低", "description": "磕碰容易造成漆面损伤，露出金属基材"},
                {"type": "涂料VOCs", "severity": "中", "description": "表面涂漆可能含挥发性有机物，新品需通风"}
            ],
            "visual_cues": [
                "金属光泽",
                "各种造型和花纹",
                "表面涂漆处理",
                "常见金属+布艺或金属+玻璃组合",
                "质地坚硬",
                "重量较重"
            ],
            "physical_properties": {
                "硬度": "高",
                "重量": "重",
                "强度": "好",
                "防锈性能": "良好（内部含锌）",
                "耐火性": "优秀",
                "使用寿命": "长"
            },
            "application_scenarios": ["阳台", "卧室", "客厅", "户外"],
            "advantages": [
                "防火能力很好，经过烈火考验",
                "绿色环保，可重复利用",
                "节省空间，功能多样",
                "经久耐用，使用寿命长",
                "不易生锈（内部含锌）",
                "具有抗衰老特点（外层上漆防氧化）"
            ],
            "disadvantages": [
                "手感比较坚硬冰冷",
                "颜色比较单一",
                "使用时会有声响",
                "需要定期保养维护"
            ],
            "maintenance_tips": [
                "房间要通风，避免潮湿环境",
                "经常清洁除尘，用纯棉针织抹布擦拭",
                "避免阳光照晒，可用窗帘遮挡",
                "使用时注意避免磕碰，轻拿轻放",
                "不要使用加湿器，维护正常湿度",
                "定期刷防腐漆（夏季为佳）"
            ],
            "health_recommendations": [
                "环保性好，材料可回收利用",
                "适合追求耐用性的家庭",
                "注意防潮和防晒",
                "定期维护可延长使用寿命",
                "新品需通风散味（涂料VOCs）"
            ],
            "certifications": ["GB/T 3325（金属家具通用技术条件）", "环保涂料认证"]
        }
    ]

    results = []
    for material in new_materials:
        entry = {
            "material_id": generate_id(material["material_type"], material["category"]),
            "category": material["category"],
            "data": material,
            "source": "第十二轮数据扩充-铁艺家具材料",
            "last_updated": datetime.now().isoformat(),
            "version": "12.0"
        }
        results.append(entry)
    return results

def main():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"

    print("\n" + "="*60)
    print("第十二轮数据扩充开始 - 铁艺家具材料")
    print("="*60)

    # 添加建材数据
    print("\n添加铁艺家具材料数据...")
    furniture_file = os.path.join(base_dir, "furniture.json")
    with open(furniture_file, 'r', encoding='utf-8') as f:
        existing_furniture = json.load(f)

    new_materials = expand_iron_art_materials()
    all_furniture = existing_furniture + new_materials

    with open(furniture_file, 'w', encoding='utf-8') as f:
        json.dump(all_furniture, f, ensure_ascii=False, indent=2)

    print(f"   原有: {len(existing_furniture)} 条")
    print(f"   新增: {len(new_materials)} 条")
    print(f"   总计: {len(all_furniture)} 条")

    # 统计各类别
    categories = {}
    for item in all_furniture:
        cat = item['category']
        categories[cat] = categories.get(cat, 0) + 1

    print("\n各类别统计:")
    for cat, count in sorted(categories.items()):
        print(f"   {cat}: {count}条")

    # 总结
    print("\n" + "="*60)
    print("第十二轮数据扩充完成!")
    print("="*60)
    print(f"家具及建材总数: {len(all_furniture)} 条 (+{len(new_materials)})")
    print("\n新增材料类别:")
    print("  - 金属家具: 铁艺家具（含详细物理特性、优缺点、保养方法）")
    print("\n铁艺家具特点:")
    print("  优点: 防火、环保可回收、耐用、不易生锈")
    print("  注意: 需防潮防晒、定期保养、新品需通风")
    print("="*60)

if __name__ == "__main__":
    main()
