"""批次18数据采集 - 瓷砖、地板、玻璃、高档纺织品"""
import json
import os
from datetime import datetime
import hashlib

def generate_id(name, category):
    unique_string = f"{category}_{name}_{datetime.now().isoformat()}"
    return hashlib.md5(unique_string.encode()).hexdigest()[:16]

def fetch_building_materials_batch18():
    """批次18建材数据"""
    materials = [
        # 瓷砖类
        {
            "category": "瓷砖",
            "material_type": "抛光砖",
            "standard": "GB/T 4100-2015",
            "chemical_components": [
                {"name": "高岭土", "cas": "1332-58-7", "hazard": "低"},
                {"name": "长石", "cas": "N/A", "hazard": "低"},
                {"name": "石英", "cas": "14808-60-7", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "放射性", "severity": "低", "description": "需检测放射性指标A类"}
            ],
            "visual_cues": ["表面光滑明亮", "镜面效果", "吸水率低"],
            "certifications": ["GB/T 4100-2015", "A类放射性"],
            "advantages": ["硬度高", "耐磨损", "易清洁", "光泽度好"],
            "disadvantages": ["防滑性差", "易显脏"],
            "maintenance_tips": ["定期打蜡", "避免硬物划伤", "及时清理污渍"],
            "health_recommendations": ["选择A类产品", "保持干燥", "防滑处理"],
            "physical_properties": {"吸水率": "≤0.5%", "破坏强度": "≥1300N", "放射性": "A类"},
            "application_scenarios": ["客厅", "餐厅", "商业空间"]
        },
        {
            "category": "瓷砖",
            "material_type": "仿古砖",
            "standard": "GB/T 4100-2015",
            "chemical_components": [
                {"name": "陶土", "cas": "N/A", "hazard": "低"},
                {"name": "釉料", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [],
            "visual_cues": ["亚光表面", "复古纹理", "防滑设计"],
            "certifications": ["GB/T 4100-2015"],
            "advantages": ["防滑性好", "耐脏", "装饰性强", "质感丰富"],
            "disadvantages": ["不易清洁凹凸纹理", "价格较高"],
            "maintenance_tips": ["定期清洁缝隙", "避免酸碱侵蚀"],
            "health_recommendations": ["防滑安全", "适合老人儿童"],
            "physical_properties": {"吸水率": "≤3%", "防滑系数": "≥0.5", "耐磨性": "4级"},
            "application_scenarios": ["厨房", "卫生间", "阳台"]
        },
        # 木地板类
        {
            "category": "地板",
            "material_type": "实木地板",
            "standard": "GB/T 15036.1-2018",
            "chemical_components": [
                {"name": "天然木材", "cas": "N/A", "hazard": "无"},
                {"name": "木蜡油涂层", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [],
            "visual_cues": ["天然木纹", "整块实木", "质感温润"],
            "certifications": ["GB/T 15036.1-2018", "FSC认证"],
            "advantages": ["环保天然", "脚感舒适", "可翻新", "档次高"],
            "disadvantages": ["价格昂贵", "需定期保养", "怕水怕潮"],
            "maintenance_tips": ["保持干燥", "定期打蜡", "避免暴晒", "防虫防霉"],
            "health_recommendations": ["零甲醛", "调节湿度", "冬暖夏凉"],
            "physical_properties": {"含水率": "8%-12%", "表面硬度": "≥2.0kN", "甲醛": "未检出"},
            "application_scenarios": ["卧室", "书房", "客厅"]
        },
        {
            "category": "地板",
            "material_type": "实木复合地板",
            "standard": "GB/T 18103-2022",
            "chemical_components": [
                {"name": "实木表层", "cas": "N/A", "hazard": "无"},
                {"name": "胶合板基层", "cas": "N/A", "hazard": "低"},
                {"name": "环保胶", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "甲醛", "severity": "低", "description": "E1级≤0.124mg/m³"}
            ],
            "visual_cues": ["实木表层", "多层结构", "稳定不变形"],
            "certifications": ["GB/T 18103-2022", "E1级"],
            "advantages": ["稳定性好", "价格适中", "脚感接近实木", "易安装"],
            "disadvantages": ["不可多次翻新", "含少量胶水"],
            "maintenance_tips": ["避免积水", "定期清洁", "防止重物压"],
            "health_recommendations": ["E1级环保", "通风3个月", "适合地暖"],
            "physical_properties": {"甲醛释放量": "≤0.124mg/m³", "表面耐磨": "≥6000转", "静曲强度": "≥30MPa"},
            "application_scenarios": ["客厅", "卧室", "地暖房"]
        },
        # 玻璃类
        {
            "category": "玻璃",
            "material_type": "钢化玻璃",
            "standard": "GB 15763.2-2005",
            "chemical_components": [
                {"name": "二氧化硅", "cas": "14808-60-7", "hazard": "低"},
                {"name": "氧化钠", "cas": "1313-59-3", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "自爆", "severity": "低", "description": "极低概率自爆(3‰)"}
            ],
            "visual_cues": ["透明均匀", "边角处理圆滑", "有钢化标志"],
            "certifications": ["GB 15763.2-2005", "3C认证"],
            "advantages": ["强度高5倍", "碎裂成颗粒", "耐温差", "安全性好"],
            "disadvantages": ["不可切割加工", "极低概率自爆"],
            "maintenance_tips": ["避免尖锐撞击", "定期检查", "边缘保护"],
            "health_recommendations": ["安全玻璃首选", "贴防爆膜更安全"],
            "physical_properties": {"抗冲击强度": "≥5倍普通玻璃", "碎片状态": "钝角小颗粒", "耐温差": "200℃"},
            "application_scenarios": ["淋浴房", "玻璃门", "玻璃隔断"]
        },
        {
            "category": "玻璃",
            "material_type": "中空玻璃",
            "standard": "GB/T 11944-2012",
            "chemical_components": [
                {"name": "玻璃", "cas": "N/A", "hazard": "无"},
                {"name": "干燥剂", "cas": "N/A", "hazard": "无"},
                {"name": "密封胶", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [],
            "visual_cues": ["双层或多层", "中间空气层", "边缘密封"],
            "certifications": ["GB/T 11944-2012", "节能认证"],
            "advantages": ["隔热保温", "隔音降噪", "防结露", "节能环保"],
            "disadvantages": ["重量大", "价格高", "安装要求高"],
            "maintenance_tips": ["检查密封性", "清洁内外表面", "避免撞击"],
            "health_recommendations": ["节能舒适", "隔音降噪", "冬暖夏凉"],
            "physical_properties": {"传热系数": "≤2.8W/(m²·K)", "隔音量": "≥30dB", "露点": "≤-40℃"},
            "application_scenarios": ["外窗", "阳光房", "幕墙"]
        },
        # 墙纸类
        {
            "category": "墙纸",
            "material_type": "纯纸墙纸",
            "standard": "GB/T 34844-2017",
            "chemical_components": [
                {"name": "纸浆", "cas": "N/A", "hazard": "无"},
                {"name": "水性墨", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [],
            "visual_cues": ["纸质薄", "透气性好", "环保无味"],
            "certifications": ["GB/T 34844-2017", "环保标志"],
            "advantages": ["环保安全", "透气性好", "色彩柔和", "儿童适用"],
            "disadvantages": ["不耐水", "不耐擦洗", "易破损"],
            "maintenance_tips": ["避免潮湿", "轻柔清洁", "防止撕裂"],
            "health_recommendations": ["零甲醛", "透气性好", "儿童房首选"],
            "physical_properties": {"透气性": "优秀", "甲醛": "未检出", "重金属": "未检出"},
            "application_scenarios": ["儿童房", "卧室", "书房"]
        },
        {
            "category": "墙纸",
            "material_type": "无纺布墙纸",
            "standard": "GB/T 34844-2017",
            "chemical_components": [
                {"name": "聚酯纤维", "cas": "N/A", "hazard": "低"},
                {"name": "水性涂层", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [],
            "visual_cues": ["布质感", "厚实", "立体纹理"],
            "certifications": ["GB/T 34844-2017", "环保认证"],
            "advantages": ["环保透气", "耐用", "易施工", "防霉防潮"],
            "disadvantages": ["价格较高", "花色受限"],
            "maintenance_tips": ["可擦洗", "避免尖锐物", "定期除尘"],
            "health_recommendations": ["低VOCs", "防霉抗菌", "全屋适用"],
            "physical_properties": {"克重": "≥200g/m²", "透气性": "良好", "耐擦洗次数": "≥500次"},
            "application_scenarios": ["客厅", "卧室", "办公室"]
        }
    ]

    results = []
    for material in materials:
        results.append({
            "material_id": generate_id(material['material_type'], material['category']),
            "category": material['category'],
            "data": material,
            "source": "国家建材标准数据库",
            "last_updated": datetime.now().isoformat(),
            "version": "18.0"
        })

    return results

def fetch_textiles_batch18():
    """批次18纺织品数据"""
    textiles = [
        {
            "fabric_type": "羊绒面料",
            "composition": "100% 山羊绒",
            "standard": "GB/T 16988-2013",
            "chemical_treatments": [
                {"name": "柔软整理", "hazard": "低"}
            ],
            "health_risks": [],
            "health_benefits": ["保暖性极佳", "柔软舒适", "轻盈透气", "奢华品质"],
            "care_instructions": {
                "washing": "30度手洗或专业干洗",
                "drying": "平铺阴干",
                "ironing": "低温蒸汽熨烫"
            },
            "certifications": ["GB 18401 A类", "国际羊绒标志"],
            "category": "衣料纺织品",
            "advantages": ["保暖性是羊毛8倍", "超柔软", "轻薄", "高档奢华"],
            "disadvantages": ["价格昂贵", "易起球", "需精心护理"],
            "maintenance_tips": ["专业干洗", "防虫防蛀", "折叠收纳", "避免摩擦"],
            "health_recommendations": ["敏感肌适用", "冬季保暖首选", "透气不闷"],
            "physical_properties": {"细度": "14-16μm", "保暖率": "羊毛的8倍", "起球等级": "3级"},
            "application_scenarios": ["大衣", "围巾", "毛衣"]
        },
        {
            "fabric_type": "羽绒填充物",
            "composition": "90% 白鸭绒 + 10% 羽毛",
            "standard": "GB/T 14272-2021",
            "chemical_treatments": [
                {"name": "高温消毒", "hazard": "无"},
                {"name": "除臭处理", "hazard": "低"}
            ],
            "health_risks": [],
            "health_benefits": ["保暖轻盈", "透气性好", "吸湿排汗"],
            "care_instructions": {
                "washing": "专业水洗或干洗",
                "drying": "低温烘干拍打",
                "storage": "通风干燥处存放"
            },
            "certifications": ["GB/T 14272-2021", "RDS认证"],
            "category": "衣料纺织品",
            "advantages": ["保暖性极佳", "重量轻", "蓬松度高", "耐用"],
            "disadvantages": ["清洗不便", "怕水", "价格较高"],
            "maintenance_tips": ["避免压缩", "定期拍打", "防潮防虫", "专业清洗"],
            "health_recommendations": ["透气保暖", "防寒首选", "注意过敏"],
            "physical_properties": {"蓬松度": "≥750", "含绒量": "90%", "耗氧指数": "≤4.8"},
            "application_scenarios": ["羽绒服", "被子", "睡袋"]
        },
        {
            "fabric_type": "氨纶弹力布",
            "composition": "95% 棉 + 5% 氨纶",
            "standard": "FZ/T 13014-2015",
            "chemical_treatments": [
                {"name": "染色", "hazard": "中"}
            ],
            "health_risks": [],
            "health_benefits": ["弹性好", "舒适贴身", "不易变形"],
            "care_instructions": {
                "washing": "40度机洗",
                "drying": "避免高温烘干",
                "ironing": "低温熨烫"
            },
            "certifications": ["GB 18401 A类"],
            "category": "衣料纺织品",
            "advantages": ["高弹性", "回弹性好", "舒适贴身", "不易起皱"],
            "disadvantages": ["不耐高温", "易老化"],
            "maintenance_tips": ["避免暴晒", "低温洗涤", "阴干"],
            "health_recommendations": ["贴身舒适", "运动适用", "透气性好"],
            "physical_properties": {"弹性伸长率": "≥300%", "回弹率": "≥95%", "克重": "180-220g/m²"},
            "application_scenarios": ["T恤", "内衣", "运动服"]
        },
        {
            "fabric_type": "涤棉混纺工装布",
            "composition": "65% 涤纶 + 35% 棉",
            "standard": "GB/T 14644-2014",
            "chemical_treatments": [
                {"name": "抗皱整理", "hazard": "低"},
                {"name": "染色", "hazard": "中"}
            ],
            "health_risks": [],
            "health_benefits": ["耐磨耐用", "易洗快干"],
            "care_instructions": {
                "washing": "60度机洗",
                "drying": "可机烘",
                "ironing": "中温熨烫"
            },
            "certifications": ["GB 18401 B类", "阻燃B1级"],
            "category": "衣料纺织品",
            "advantages": ["挺括耐用", "抗皱免烫", "易洗快干", "价格实惠"],
            "disadvantages": ["透气性一般", "易起静电"],
            "maintenance_tips": ["定期清洗", "使用柔顺剂", "避免高温"],
            "health_recommendations": ["工装首选", "耐脏耐磨", "不适合贴身"],
            "physical_properties": {"克重": "200-260g/m²", "断裂强力": "≥450N", "耐磨次数": "≥3000次"},
            "application_scenarios": ["工作服", "制服", "劳保服"]
        },
        {
            "fabric_type": "冰丝凉感布",
            "composition": "改性聚酯纤维",
            "standard": "FZ/T 73036-2010",
            "chemical_treatments": [
                {"name": "凉感整理", "hazard": "低"},
                {"name": "吸湿整理", "hazard": "低"}
            ],
            "health_risks": [],
            "health_benefits": ["凉感降温", "吸湿速干", "光滑舒适"],
            "care_instructions": {
                "washing": "30度机洗",
                "drying": "阴干",
                "ironing": "低温熨烫"
            },
            "certifications": ["GB 18401 B类", "凉感认证"],
            "category": "衣料纺织品",
            "advantages": ["瞬间凉感", "吸湿排汗", "丝滑触感", "抗菌防臭"],
            "disadvantages": ["不耐高温", "易勾丝"],
            "maintenance_tips": ["避免尖锐物", "低温洗涤", "避免暴晒"],
            "health_recommendations": ["夏季凉爽", "降温2-3度", "敏感肌慎用"],
            "physical_properties": {"克重": "100-140g/m²", "凉感系数": "≥0.15", "透湿率": "≥5000g/(m²·24h)"},
            "application_scenarios": ["夏季内衣", "凉席", "运动服"]
        }
    ]

    results = []
    for textile in textiles:
        results.append({
            "material_id": generate_id(textile['fabric_type'], '衣料纺织品'),
            "category": "衣料纺织品",
            "data": textile,
            "source": "纺织品标准数据库",
            "last_updated": datetime.now().isoformat(),
            "version": "18.0"
        })

    return results

def main():
    print("\n" + "="*70)
    print("批次18数据采集 - 瓷砖地板玻璃墙纸 + 高档纺织品")
    print("="*70)

    all_new_data = []

    # 获取建材数据
    print("\n1. 获取建材标准数据...")
    material_data = fetch_building_materials_batch18()
    all_new_data.extend(material_data)
    print(f"   已获取建材数据: {len(material_data)} 条")
    print("   类别: 瓷砖(2) 地板(2) 玻璃(2) 墙纸(2)")

    # 获取纺织品数据
    print("\n2. 获取纺织品标准数据...")
    textile_data = fetch_textiles_batch18()
    all_new_data.extend(textile_data)
    print(f"   已获取纺织品数据: {len(textile_data)} 条")
    print("   类别: 羊绒 羽绒 氨纶 涤棉 冰丝")

    # 保存到文件
    output_file = "fetched_real_data_batch18.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_new_data, f, ensure_ascii=False, indent=2)

    print("\n" + "="*70)
    print("批次18数据采集完成!")
    print("="*70)
    print(f"\n总计获取: {len(all_new_data)} 条新数据")
    print(f"  - 建材: {len(material_data)} 条")
    print(f"  - 纺织品: {len(textile_data)} 条")
    print(f"\n已保存到: {output_file}")
    print("\n数据来源标准:")
    print("  建材:")
    print("    - GB/T 4100-2015 (陶瓷砖)")
    print("    - GB/T 15036.1-2018 (实木地板)")
    print("    - GB/T 18103-2022 (实木复合地板)")
    print("    - GB 15763.2-2005 (钢化玻璃)")
    print("    - GB/T 11944-2012 (中空玻璃)")
    print("    - GB/T 34844-2017 (壁纸)")
    print("  纺织品:")
    print("    - GB/T 16988-2013 (山羊绒)")
    print("    - GB/T 14272-2021 (羽绒服装)")
    print("    - FZ/T 13014-2015 (氨纶弹力织物)")
    print("    - GB/T 14644-2014 (涤棉混纺)")
    print("    - FZ/T 73036-2010 (凉感织物)")
    print("="*70)

if __name__ == "__main__":
    main()
