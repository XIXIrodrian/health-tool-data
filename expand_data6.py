"""第六轮数据扩充脚本 - 添加厨卫、照明、开关、暖通等材料"""
import json
import sys
import os
from datetime import datetime
import hashlib

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def generate_id(name, category):
    unique_string = f"{category}_{name}_{datetime.now().isoformat()}"
    return hashlib.md5(unique_string.encode()).hexdigest()[:16]

def expand_kitchen_bath_lighting():
    """第六轮厨卫照明暖通材料扩充"""
    new_materials = [
        # 厨卫材料类
        {
            "category": "厨卫材料",
            "material_type": "不锈钢水槽",
            "chemical_components": [
                {"name": "304不锈钢", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "重金属析出", "severity": "低", "description": "304不锈钢安全性高"}
            ],
            "visual_cues": ["银白色", "耐腐蚀", "食品级"],
            "certifications": ["GB/T 13520"]
        },
        {
            "category": "厨卫材料",
            "material_type": "石英石台面",
            "chemical_components": [
                {"name": "石英砂", "cas": "14808-60-7", "hazard": "低"},
                {"name": "树脂", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "树脂气味", "severity": "中", "description": "新品可能有树脂味"}
            ],
            "visual_cues": ["坚硬", "花纹丰富", "耐高温"],
            "certifications": ["NSF认证"]
        },
        {
            "category": "厨卫材料",
            "material_type": "亚克力台面",
            "chemical_components": [
                {"name": "PMMA", "cas": "9011-14-7", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "不耐高温", "severity": "中", "description": "怕烫,需用隔热垫"}
            ],
            "visual_cues": ["透明或半透明", "易加工"],
            "certifications": ["GB/T 17219"]
        },
        {
            "category": "厨卫材料",
            "material_type": "陶瓷马桶",
            "chemical_components": [
                {"name": "高温瓷", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "釉面铅镉", "severity": "中", "description": "劣质产品可能超标"}
            ],
            "visual_cues": ["白色光滑", "釉面"],
            "certifications": ["GB 6952"]
        },
        {
            "category": "厨卫材料",
            "material_type": "亚克力浴缸",
            "chemical_components": [
                {"name": "PMMA", "cas": "9011-14-7", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "易划伤", "severity": "低", "description": "表面硬度不如铸铁"}
            ],
            "visual_cues": ["轻质", "保温好", "多种造型"],
            "certifications": ["GB/T 23448"]
        },
        {
            "category": "厨卫材料",
            "material_type": "钢化玻璃淋浴房",
            "chemical_components": [
                {"name": "钢化玻璃", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "自爆风险", "severity": "中", "description": "千分之三自爆率,贴防爆膜"}
            ],
            "visual_cues": ["透明", "3C标识", "边角钝化"],
            "certifications": ["3C认证"]
        },
        # 照明材料类
        {
            "category": "照明材料",
            "material_type": "LED灯珠",
            "chemical_components": [
                {"name": "半导体芯片", "cas": "N/A", "hazard": "低"},
                {"name": "荧光粉", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "蓝光危害", "severity": "中", "description": "选择低蓝光产品"}
            ],
            "visual_cues": ["节能", "长寿命", "光效高"],
            "certifications": ["CQC认证"]
        },
        {
            "category": "照明材料",
            "material_type": "节能灯",
            "chemical_components": [
                {"name": "稀土荧光粉", "cas": "N/A", "hazard": "低"},
                {"name": "汞蒸气", "cas": "7439-97-6", "hazard": "高"}
            ],
            "risk_points": [
                {"type": "汞污染", "severity": "高", "description": "破碎会释放汞蒸气,需回收"},
                {"type": "频闪", "severity": "中", "description": "劣质产品频闪严重"}
            ],
            "visual_cues": ["螺旋形", "比白炽灯节能"],
            "certifications": ["CCC认证"]
        },
        {
            "category": "照明材料",
            "material_type": "灯具塑料外壳",
            "chemical_components": [
                {"name": "PC塑料", "cas": "N/A", "hazard": "中"},
                {"name": "阻燃剂", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "阻燃剂", "severity": "中", "description": "含溴系阻燃剂"}
            ],
            "visual_cues": ["透明或半透明", "阻燃"],
            "certifications": ["CCC认证"]
        },
        {
            "category": "照明材料",
            "material_type": "吸顶灯灯罩",
            "chemical_components": [
                {"name": "亚克力", "cas": "9011-14-7", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "透光率", "severity": "低", "description": "选择高透光率产品"}
            ],
            "visual_cues": ["乳白色", "半透明"],
            "certifications": ["CCC认证"]
        },
        # 开关插座类
        {
            "category": "开关插座",
            "material_type": "PC阻燃面板",
            "chemical_components": [
                {"name": "聚碳酸酯", "cas": "N/A", "hazard": "中"},
                {"name": "阻燃剂", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "阻燃性能", "severity": "中", "description": "必须通过750℃灼热丝测试"}
            ],
            "visual_cues": ["光滑面板", "阻燃标识"],
            "certifications": ["CCC认证"]
        },
        {
            "category": "开关插座",
            "material_type": "铜合金插套",
            "chemical_components": [
                {"name": "黄铜", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "接触电阻", "severity": "中", "description": "铜片厚度需≥0.6mm"}
            ],
            "visual_cues": ["黄铜色", "镀镍处理"],
            "certifications": ["CCC认证"]
        },
        {
            "category": "开关插座",
            "material_type": "USB充电插座",
            "chemical_components": [
                {"name": "电路板", "cas": "N/A", "hazard": "低"},
                {"name": "阻燃塑料", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "过载保护", "severity": "中", "description": "需有过流过压保护"}
            ],
            "visual_cues": ["USB接口", "智能芯片"],
            "certifications": ["CCC认证", "CE认证"]
        },
        # 暖通材料类
        {
            "category": "暖通材料",
            "material_type": "铜铝复合暖气片",
            "chemical_components": [
                {"name": "铜管+铝翅片", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "氧化腐蚀", "severity": "低", "description": "铜管耐腐蚀"}
            ],
            "visual_cues": ["轻质", "散热快"],
            "certifications": ["GB/T 29039"]
        },
        {
            "category": "暖通材料",
            "material_type": "钢制暖气片",
            "chemical_components": [
                {"name": "低碳钢", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "锈蚀", "severity": "中", "description": "需做内防腐处理"}
            ],
            "visual_cues": ["重量大", "价格适中"],
            "certifications": ["GB/T 29039"]
        },
        {
            "category": "暖通材料",
            "material_type": "PERT地暖管",
            "chemical_components": [
                {"name": "耐热聚乙烯", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "环保型", "severity": "低", "description": "食品级材质无毒"}
            ],
            "visual_cues": ["柔韧", "耐高温", "白色或红色"],
            "certifications": ["GB/T 18992"]
        },
        {
            "category": "暖通材料",
            "material_type": "PEXb地暖管",
            "chemical_components": [
                {"name": "交联聚乙烯", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "不可热熔", "severity": "低", "description": "破损需用卡套连接"}
            ],
            "visual_cues": ["记忆性好", "耐高温"],
            "certifications": ["GB/T 18992"]
        },
        {
            "category": "暖通材料",
            "material_type": "空调铜管",
            "chemical_components": [
                {"name": "无氧铜", "cas": "7440-50-8", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "假冒产品", "severity": "中", "description": "警惕回收铜"}
            ],
            "visual_cues": ["红铜色", "导热快"],
            "certifications": ["GB/T 17791"]
        },
        # 屋面材料类
        {
            "category": "屋面材料",
            "material_type": "彩钢瓦",
            "chemical_components": [
                {"name": "镀锌钢板", "cas": "N/A", "hazard": "低"},
                {"name": "彩涂层", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "褪色", "severity": "低", "description": "选择高质量彩涂层"}
            ],
            "visual_cues": ["波浪形", "轻质", "多种颜色"],
            "certifications": ["GB/T 12755"]
        },
        {
            "category": "屋面材料",
            "material_type": "沥青瓦",
            "chemical_components": [
                {"name": "沥青", "cas": "8052-42-4", "hazard": "中"},
                {"name": "玻璃纤维", "cas": "65997-17-3", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "沥青气味", "severity": "中", "description": "高温下有气味"},
                {"type": "多环芳烃", "severity": "中", "description": "沥青含PAHs"}
            ],
            "visual_cues": ["鱼鳞状", "柔韧", "防水"],
            "certifications": ["GB/T 20474"]
        },
        {
            "category": "屋面材料",
            "material_type": "树脂瓦",
            "chemical_components": [
                {"name": "ASA树脂", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "耐候性", "severity": "低", "description": "选择优质ASA材质"}
            ],
            "visual_cues": ["仿古瓦造型", "轻质", "多彩"],
            "certifications": ["GB/T 29755"]
        },
        {
            "category": "屋面材料",
            "material_type": "陶土瓦",
            "chemical_components": [
                {"name": "陶土烧结", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "重量大", "severity": "中", "description": "需加强屋顶结构"}
            ],
            "visual_cues": ["红褐色", "厚重", "耐久"],
            "certifications": ["GB/T 21149"]
        },
        # 外墙材料类
        {
            "category": "外墙材料",
            "material_type": "真石漆",
            "chemical_components": [
                {"name": "天然彩砂", "cas": "N/A", "hazard": "低"},
                {"name": "乳液", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "环保型", "severity": "低", "description": "水性涂料环保"}
            ],
            "visual_cues": ["仿石材效果", "立体感强"],
            "certifications": ["JG/T 24"]
        },
        {
            "category": "外墙材料",
            "material_type": "外墙保温一体板",
            "chemical_components": [
                {"name": "保温层+装饰面", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "粘结强度", "severity": "中", "description": "安装需牢固"}
            ],
            "visual_cues": ["一体化", "保温装饰"],
            "certifications": ["GB/T 29906"]
        },
        {
            "category": "外墙材料",
            "material_type": "铝塑复合板",
            "chemical_components": [
                {"name": "铝板+PE芯材", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "防火等级", "severity": "高", "description": "PE芯材易燃,选择阻燃型"}
            ],
            "visual_cues": ["金属光泽", "平整"],
            "certifications": ["GB/T 17748"]
        },
        {
            "category": "外墙材料",
            "material_type": "文化石",
            "chemical_components": [
                {"name": "水泥+天然石粉", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "放射性", "severity": "低", "description": "天然石材微量放射性"}
            ],
            "visual_cues": ["粗糙质感", "仿天然石"],
            "certifications": ["GB 6566"]
        },
        # 新风净化类
        {
            "category": "新风净化",
            "material_type": "HEPA滤网",
            "chemical_components": [
                {"name": "玻璃纤维", "cas": "65997-17-3", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "需定期更换", "severity": "低", "description": "6-12个月更换"}
            ],
            "visual_cues": ["褶皱结构", "高效过滤"],
            "certifications": ["GB/T 14295"]
        },
        {
            "category": "新风净化",
            "material_type": "活性炭滤网",
            "chemical_components": [
                {"name": "活性炭", "cas": "7440-44-0", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "吸附饱和", "severity": "低", "description": "需定期更换或暴晒"}
            ],
            "visual_cues": ["黑色", "多孔", "吸附异味"],
            "certifications": ["GB/T 7702"]
        },
        {
            "category": "新风净化",
            "material_type": "新风管道",
            "chemical_components": [
                {"name": "PVC或镀锌钢", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "清洁维护", "severity": "低", "description": "需定期清洁"}
            ],
            "visual_cues": ["白色或银色", "圆形管道"],
            "certifications": ["GB 50243"]
        }
    ]

    results = []
    for material in new_materials:
        entry = {
            "material_id": generate_id(material["material_type"], material["category"]),
            "category": material["category"],
            "data": material,
            "source": "第六轮数据扩充-厨卫照明暖通",
            "last_updated": datetime.now().isoformat(),
            "version": "6.0"
        }
        results.append(entry)
    return results

def main():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"

    print("\n" + "="*60)
    print("第六轮数据扩充开始 - 厨卫照明暖通材料")
    print("="*60)

    # 添加厨卫照明暖通材料
    print("\n添加厨卫、照明、开关、暖通、屋面、外墙材料...")
    furniture_file = os.path.join(base_dir, "furniture.json")
    with open(furniture_file, 'r', encoding='utf-8') as f:
        existing_furniture = json.load(f)

    new_materials = expand_kitchen_bath_lighting()
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
    print("第六轮数据扩充完成!")
    print("="*60)
    print(f"家具及建材总数: {len(all_furniture)} 条 (+{len(new_materials)})")
    print("\n新增材料类别:")
    print("  - 厨卫材料 (6种): 不锈钢水槽、石英石台面、亚克力台面、陶瓷马桶、亚克力浴缸、钢化玻璃淋浴房")
    print("  - 照明材料 (4种): LED灯珠、节能灯、灯具塑料外壳、吸顶灯灯罩")
    print("  - 开关插座 (3种): PC阻燃面板、铜合金插套、USB充电插座")
    print("  - 暖通材料 (5种): 铜铝复合暖气片、钢制暖气片、PERT地暖管、PEXb地暖管、空调铜管")
    print("  - 屋面材料 (4种): 彩钢瓦、沥青瓦、树脂瓦、陶土瓦")
    print("  - 外墙材料 (4种): 真石漆、外墙保温一体板、铝塑复合板、文化石")
    print("  - 新风净化 (3种): HEPA滤网、活性炭滤网、新风管道")
    print("="*60)

if __name__ == "__main__":
    main()
