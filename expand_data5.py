"""第五轮数据扩充脚本 - 继续添加更多房屋建材"""
import json
import sys
import os
from datetime import datetime
import hashlib

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def generate_id(name, category):
    unique_string = f"{category}_{name}_{datetime.now().isoformat()}"
    return hashlib.md5(unique_string.encode()).hexdigest()[:16]

def expand_more_building_materials():
    """第五轮房屋建材数据扩充"""
    new_materials = [
        # 地面材料类
        {
            "category": "地面材料",
            "material_type": "水磨石地面",
            "chemical_components": [
                {"name": "水泥", "cas": "N/A", "hazard": "低"},
                {"name": "石子", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "放射性", "severity": "低", "description": "天然石材微量放射性"}
            ],
            "visual_cues": ["石子镶嵌", "打磨光滑", "耐用"],
            "certifications": ["GB 50209"]
        },
        {
            "category": "地面材料",
            "material_type": "环氧地坪",
            "chemical_components": [
                {"name": "环氧树脂", "cas": "25068-38-6", "hazard": "中"},
                {"name": "固化剂", "cas": "N/A", "hazard": "高"}
            ],
            "risk_points": [
                {"type": "VOCs释放", "severity": "高", "description": "施工期VOCs高"},
                {"type": "固化剂刺激", "severity": "高", "description": "固化剂有强刺激性"}
            ],
            "visual_cues": ["光滑无缝", "颜色可选", "工业风"],
            "certifications": ["GB 50212"]
        },
        {
            "category": "地面材料",
            "material_type": "水泥自流平",
            "chemical_components": [
                {"name": "特种水泥", "cas": "N/A", "hazard": "低"},
                {"name": "流平剂", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "碱性", "severity": "中", "description": "施工时注意防护"}
            ],
            "visual_cues": ["灰色", "平整光滑", "工业感"],
            "certifications": ["JC/T 985"]
        },
        # 墙体材料类
        {
            "category": "墙体材料",
            "material_type": "GRC轻质隔墙板",
            "chemical_components": [
                {"name": "玻璃纤维", "cas": "65997-17-3", "hazard": "低"},
                {"name": "水泥", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "纤维刺激", "severity": "低", "description": "切割时产生粉尘"}
            ],
            "visual_cues": ["轻质", "高强度", "隔音好"],
            "certifications": ["GB/T 23451"]
        },
        {
            "category": "墙体材料",
            "material_type": "石膏砌块",
            "chemical_components": [
                {"name": "石膏", "cas": "13397-24-5", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "防水性差", "severity": "中", "description": "不适合潮湿环境"}
            ],
            "visual_cues": ["白色", "轻质", "易加工"],
            "certifications": ["GB/T 28627"]
        },
        {
            "category": "墙体材料",
            "material_type": "ALC蒸压加气混凝土板",
            "chemical_components": [
                {"name": "硅酸盐", "cas": "N/A", "hazard": "低"},
                {"name": "铝粉", "cas": "7429-90-5", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "环保型", "severity": "低", "description": "保温隔热性能好"}
            ],
            "visual_cues": ["灰白色", "多孔轻质", "可钉可锯"],
            "certifications": ["GB 15762"]
        },
        # 钢材类
        {
            "category": "钢材类",
            "material_type": "螺纹钢",
            "chemical_components": [
                {"name": "低合金钢", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "锈蚀", "severity": "中", "description": "需做防锈处理"}
            ],
            "visual_cues": ["表面肋纹", "高强度"],
            "certifications": ["GB 1499"]
        },
        {
            "category": "钢材类",
            "material_type": "角钢",
            "chemical_components": [
                {"name": "碳素钢", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "锐边", "severity": "低", "description": "施工注意防护"}
            ],
            "visual_cues": ["L形截面", "常用于支架"],
            "certifications": ["GB/T 706"]
        },
        {
            "category": "钢材类",
            "material_type": "方管",
            "chemical_components": [
                {"name": "碳素钢", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "镀锌层", "severity": "低", "description": "热镀锌更耐用"}
            ],
            "visual_cues": ["方形空心", "结构稳定"],
            "certifications": ["GB/T 6728"]
        },
        # 木材类
        {
            "category": "木材类",
            "material_type": "落叶松木方",
            "chemical_components": [
                {"name": "天然木材", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "防腐处理", "severity": "中", "description": "需防腐防虫处理"}
            ],
            "visual_cues": ["黄褐色", "结构用材"],
            "certifications": ["GB/T 14019"]
        },
        {
            "category": "木材类",
            "material_type": "杉木板",
            "chemical_components": [
                {"name": "天然木材", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "易变形", "severity": "中", "description": "需自然干燥"}
            ],
            "visual_cues": ["浅黄色", "清香", "质地软"],
            "certifications": ["GB/T 14019"]
        },
        {
            "category": "木材类",
            "material_type": "樟子松",
            "chemical_components": [
                {"name": "天然木材", "cas": "N/A", "hazard": "低"},
                {"name": "松脂", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "松脂气味", "severity": "低", "description": "天然松香味"}
            ],
            "visual_cues": ["浅黄色", "木节多", "性价比高"],
            "certifications": ["GB/T 14019"]
        },
        # 电线电缆类
        {
            "category": "电线电缆",
            "material_type": "BV单股铜芯线",
            "chemical_components": [
                {"name": "无氧铜", "cas": "7440-50-8", "hazard": "低"},
                {"name": "PVC绝缘", "cas": "9002-86-2", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "燃烧有毒", "severity": "高", "description": "PVC燃烧释放氯化氢"},
                {"type": "铜芯纯度", "severity": "中", "description": "警惕铜包铝"}
            ],
            "visual_cues": ["硬线", "红黄蓝绿色"],
            "certifications": ["GB/T 5023"]
        },
        {
            "category": "电线电缆",
            "material_type": "BVR多股铜芯线",
            "chemical_components": [
                {"name": "无氧铜", "cas": "7440-50-8", "hazard": "低"},
                {"name": "PVC绝缘", "cas": "9002-86-2", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "燃烧有毒", "severity": "高", "description": "同BV线风险"}
            ],
            "visual_cues": ["软线", "多股绞合", "易穿管"],
            "certifications": ["GB/T 5023"]
        },
        {
            "category": "电线电缆",
            "material_type": "ZR阻燃电线",
            "chemical_components": [
                {"name": "铜芯", "cas": "7440-50-8", "hazard": "低"},
                {"name": "阻燃PVC", "cas": "N/A", "hazard": "中"},
                {"name": "阻燃剂", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "阻燃剂", "severity": "中", "description": "含溴系或磷系阻燃剂"}
            ],
            "visual_cues": ["ZR标识", "阻燃性能"],
            "certifications": ["GB/T 19666"]
        },
        {
            "category": "电线电缆",
            "material_type": "WDZN低烟无卤电线",
            "chemical_components": [
                {"name": "铜芯", "cas": "7440-50-8", "hazard": "低"},
                {"name": "聚烯烃", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "环保型", "severity": "低", "description": "燃烧无卤素气体,最安全"}
            ],
            "visual_cues": ["WDZN标识", "绿色环保"],
            "certifications": ["GB/T 19666"]
        },
        # 装修辅材类
        {
            "category": "装修辅材",
            "material_type": "耐水腻子粉",
            "chemical_components": [
                {"name": "灰钙粉", "cas": "N/A", "hazard": "低"},
                {"name": "白水泥", "cas": "N/A", "hazard": "低"},
                {"name": "胶粉", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "甲醛", "severity": "低", "description": "成品腻子甲醛低"}
            ],
            "visual_cues": ["白色粉末", "加水搅拌"],
            "certifications": ["JG/T 298"]
        },
        {
            "category": "装修辅材",
            "material_type": "石膏粉",
            "chemical_components": [
                {"name": "熟石膏", "cas": "10101-41-4", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "粉尘", "severity": "低", "description": "施工时注意防尘"}
            ],
            "visual_cues": ["白色细粉", "凝固快"],
            "certifications": ["GB/T 9776"]
        },
        {
            "category": "装修辅材",
            "material_type": "界面剂",
            "chemical_components": [
                {"name": "丙烯酸乳液", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "环保型", "severity": "低", "description": "水性环保无毒"}
            ],
            "visual_cues": ["乳液状", "增强附着力"],
            "certifications": ["JG/T 363"]
        },
        {
            "category": "装修辅材",
            "material_type": "瓷砖填缝剂",
            "chemical_components": [
                {"name": "水泥基", "cas": "N/A", "hazard": "低"},
                {"name": "颜料", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "易脱落", "severity": "低", "description": "不如美缝剂耐用"}
            ],
            "visual_cues": ["干粉", "颜色可选"],
            "certifications": ["JC/T 1004"]
        },
        # 隔音材料类
        {
            "category": "隔音材料",
            "material_type": "隔音棉",
            "chemical_components": [
                {"name": "聚酯纤维", "cas": "25038-59-9", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "环保型", "severity": "低", "description": "无甲醛无刺激"}
            ],
            "visual_cues": ["蓬松纤维", "吸音好"],
            "certifications": ["GB/T 16731"]
        },
        {
            "category": "隔音材料",
            "material_type": "隔音板",
            "chemical_components": [
                {"name": "高密度板", "cas": "N/A", "hazard": "中"},
                {"name": "隔音层", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "甲醛", "severity": "中", "description": "密度板基材可能释放甲醛"}
            ],
            "visual_cues": ["复合结构", "重量大"],
            "certifications": ["GB/T 19889"]
        },
        {
            "category": "隔音材料",
            "material_type": "隔音减震垫",
            "chemical_components": [
                {"name": "橡胶", "cas": "N/A", "hazard": "低"},
                {"name": "发泡材料", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "气味", "severity": "低", "description": "新品可能有橡胶味"}
            ],
            "visual_cues": ["黑色垫层", "弹性好"],
            "certifications": ["GB/T 19889"]
        },
        # 龙骨类
        {
            "category": "龙骨类",
            "material_type": "轻钢龙骨",
            "chemical_components": [
                {"name": "镀锌钢板", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "锐边", "severity": "低", "description": "施工时注意防护"}
            ],
            "visual_cues": ["银白色", "轻质", "C型或U型"],
            "certifications": ["GB/T 11981"]
        },
        {
            "category": "龙骨类",
            "material_type": "木龙骨",
            "chemical_components": [
                {"name": "木材", "cas": "N/A", "hazard": "低"},
                {"name": "防腐剂", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "防腐剂", "severity": "中", "description": "需选环保防腐处理"},
                {"type": "防火性差", "severity": "中", "description": "不如轻钢龙骨"}
            ],
            "visual_cues": ["方形木条", "常见规格30*50mm"],
            "certifications": ["GB 50210"]
        },
        {
            "category": "龙骨类",
            "material_type": "铝合金龙骨",
            "chemical_components": [
                {"name": "铝合金", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "价格高", "severity": "低", "description": "成本高于轻钢"}
            ],
            "visual_cues": ["银色", "轻质", "防锈"],
            "certifications": ["GB/T 11981"]
        },
        # 五金配件类
        {
            "category": "五金配件",
            "material_type": "膨胀螺栓",
            "chemical_components": [
                {"name": "碳钢", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "承重", "severity": "中", "description": "选择合适规格和材质"}
            ],
            "visual_cues": ["锥形膨胀", "承重固定"],
            "certifications": ["GB/T 1228"]
        },
        {
            "category": "五金配件",
            "material_type": "不锈钢铰链",
            "chemical_components": [
                {"name": "304不锈钢", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "假冒304", "severity": "中", "description": "警惕铁镀铬冒充"}
            ],
            "visual_cues": ["银白色", "阻尼可调"],
            "certifications": ["GB/T 16454"]
        },
        {
            "category": "五金配件",
            "material_type": "铜合金水龙头",
            "chemical_components": [
                {"name": "黄铜", "cas": "N/A", "hazard": "低"},
                {"name": "铅", "cas": "7439-92-1", "hazard": "高"}
            ],
            "risk_points": [
                {"type": "铅析出", "severity": "高", "description": "劣质龙头铅超标"},
                {"type": "选无铅龙头", "severity": "低", "description": "铜含量≥59%无铅"}
            ],
            "visual_cues": ["金属质感", "重量足"],
            "certifications": ["GB 18145"]
        }
    ]

    results = []
    for material in new_materials:
        entry = {
            "material_id": generate_id(material["material_type"], material["category"]),
            "category": material["category"],
            "data": material,
            "source": "第五轮数据扩充-更多房屋建材",
            "last_updated": datetime.now().isoformat(),
            "version": "5.0"
        }
        results.append(entry)
    return results

def main():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"

    print("\n" + "="*60)
    print("第五轮数据扩充开始 - 更多房屋建材")
    print("="*60)

    # 继续添加建材数据
    print("\n添加更多房屋建材数据...")
    furniture_file = os.path.join(base_dir, "furniture.json")
    with open(furniture_file, 'r', encoding='utf-8') as f:
        existing_furniture = json.load(f)

    new_materials = expand_more_building_materials()
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
    print("第五轮数据扩充完成!")
    print("="*60)
    print(f"家具及建材总数: {len(all_furniture)} 条 (+{len(new_materials)})")
    print("\n新增建材类别:")
    print("  - 地面材料 (3种): 水磨石、环氧地坪、水泥自流平")
    print("  - 墙体材料 (3种): GRC轻质隔墙板、石膏砌块、ALC板")
    print("  - 钢材类 (3种): 螺纹钢、角钢、方管")
    print("  - 木材类 (3种): 落叶松木方、杉木板、樟子松")
    print("  - 电线电缆 (4种): BV线、BVR线、ZR阻燃线、WDZN低烟无卤线")
    print("  - 装修辅材 (4种): 耐水腻子粉、石膏粉、界面剂、填缝剂")
    print("  - 隔音材料 (3种): 隔音棉、隔音板、隔音减震垫")
    print("  - 龙骨类 (3种): 轻钢龙骨、木龙骨、铝合金龙骨")
    print("  - 五金配件 (3种): 膨胀螺栓、不锈钢铰链、铜合金水龙头")
    print("="*60)

if __name__ == "__main__":
    main()
