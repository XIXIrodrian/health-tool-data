"""第十轮数据扩充脚本 - 智能家居、园林景观、卫浴洁具、五金配件"""
import json
import sys
import os
from datetime import datetime
import hashlib

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def generate_id(name, category):
    unique_string = f"{category}_{name}_{datetime.now().isoformat()}"
    return hashlib.md5(unique_string.encode()).hexdigest()[:16]

def expand_building_materials():
    """第十轮家具建材数据扩充"""
    new_materials = [
        # 智能家居类
        {
            "category": "智能家居",
            "material_type": "智能门锁",
            "chemical_components": [
                {"name": "锌合金外壳", "cas": "N/A", "hazard": "低"},
                {"name": "电路板", "cas": "N/A", "hazard": "低"},
                {"name": "锂电池", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "电磁辐射", "severity": "低", "description": "符合国标辐射标准"},
                {"type": "信息安全", "severity": "中", "description": "选择知名品牌避免数据泄露"}
            ],
            "visual_cues": ["金属质感", "指纹识别", "电子显示屏"],
            "certifications": ["GA 374", "3C认证"]
        },
        {
            "category": "智能家居",
            "material_type": "智能窗帘电机",
            "chemical_components": [
                {"name": "直流电机", "cas": "N/A", "hazard": "低"},
                {"name": "塑料外壳", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "电气安全", "severity": "中", "description": "需专业安装"},
                {"type": "噪音", "severity": "低", "description": "选择静音电机"}
            ],
            "visual_cues": ["管状电机", "遥控器", "WiFi连接"],
            "certifications": ["CCC认证", "CE认证"]
        },
        {
            "category": "智能家居",
            "material_type": "智能开关面板",
            "chemical_components": [
                {"name": "PC阻燃材料", "cas": "N/A", "hazard": "中"},
                {"name": "触摸芯片", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "触摸失灵", "severity": "低", "description": "潮湿环境可能失灵"},
                {"type": "阻燃性", "severity": "中", "description": "必须通过阻燃测试"}
            ],
            "visual_cues": ["玻璃面板", "触摸式", "LED指示灯"],
            "certifications": ["CCC认证"]
        },
        {
            "category": "智能家居",
            "material_type": "智能插座",
            "chemical_components": [
                {"name": "阻燃PC", "cas": "N/A", "hazard": "中"},
                {"name": "WiFi模块", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "过载保护", "severity": "中", "description": "需有过流保护功能"},
                {"type": "电磁辐射", "severity": "低", "description": "符合国标"}
            ],
            "visual_cues": ["远程控制", "功率监测", "定时功能"],
            "certifications": ["CCC认证", "SRRC认证"]
        },
        {
            "category": "智能家居",
            "material_type": "智能灯泡",
            "chemical_components": [
                {"name": "LED芯片", "cas": "N/A", "hazard": "低"},
                {"name": "散热铝材", "cas": "N/A", "hazard": "低"},
                {"name": "WiFi模块", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "蓝光危害", "severity": "中", "description": "选择低蓝光产品"},
                {"type": "频闪", "severity": "低", "description": "优质产品无频闪"}
            ],
            "visual_cues": ["可调色温", "可调亮度", "语音控制"],
            "certifications": ["CQC认证", "CCC认证"]
        },
        # 园林景观类
        {
            "category": "园林景观",
            "material_type": "防腐木",
            "chemical_components": [
                {"name": "松木/樟子松", "cas": "N/A", "hazard": "低"},
                {"name": "ACQ防腐剂", "cas": "N/A", "hazard": "中"},
                {"name": "铜基防腐剂", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "防腐剂毒性", "severity": "中", "description": "传统CCA含砷,选ACQ/ACB环保型"},
                {"type": "皮肤接触", "severity": "低", "description": "儿童游乐设施需特别注意"}
            ],
            "visual_cues": ["绿褐色", "户外耐用", "防水防腐"],
            "certifications": ["GB/T 22102"]
        },
        {
            "category": "园林景观",
            "material_type": "塑木复合材料",
            "chemical_components": [
                {"name": "PE/PP塑料", "cas": "N/A", "hazard": "低"},
                {"name": "木粉", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "高温变形", "severity": "中", "description": "夏季高温可能软化"},
                {"type": "环保型", "severity": "低", "description": "可回收材料"}
            ],
            "visual_cues": ["仿木纹理", "防水防腐", "免维护"],
            "certifications": ["GB/T 24508"]
        },
        {
            "category": "园林景观",
            "material_type": "景观石",
            "chemical_components": [
                {"name": "天然石材", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "放射性", "severity": "低", "description": "天然石材A类合格"},
                {"type": "重量大", "severity": "中", "description": "基础需承重"}
            ],
            "visual_cues": ["自然纹理", "多种颜色", "不规则形状"],
            "certifications": ["GB 6566"]
        },
        {
            "category": "园林景观",
            "material_type": "人造草坪",
            "chemical_components": [
                {"name": "PE/PP草丝", "cas": "N/A", "hazard": "低"},
                {"name": "橡胶颗粒填充", "cas": "N/A", "hazard": "中"},
                {"name": "背胶", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "橡胶颗粒", "severity": "中", "description": "回收轮胎颗粒可能含重金属"},
                {"type": "高温", "severity": "中", "description": "夏季表面温度高"}
            ],
            "visual_cues": ["绿色草丝", "柔软舒适", "排水孔"],
            "certifications": ["GB/T 20394", "SGS检测"]
        },
        {
            "category": "园林景观",
            "material_type": "透水砖",
            "chemical_components": [
                {"name": "陶瓷/混凝土", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "环保型", "severity": "低", "description": "雨水渗透减少积水"}
            ],
            "visual_cues": ["多孔结构", "透水性强", "防滑"],
            "certifications": ["CJ/T 188"]
        },
        # 卫浴洁具类
        {
            "category": "卫浴洁具",
            "material_type": "智能马桶",
            "chemical_components": [
                {"name": "陶瓷坯体", "cas": "N/A", "hazard": "低"},
                {"name": "电子元件", "cas": "N/A", "hazard": "低"},
                {"name": "PP盖板", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "漏电风险", "severity": "中", "description": "需接地保护"},
                {"type": "水路安全", "severity": "中", "description": "需专业安装"}
            ],
            "visual_cues": ["即热式加热", "自动冲洗", "烘干功能"],
            "certifications": ["GB 6952", "CCC认证"]
        },
        {
            "category": "卫浴洁具",
            "material_type": "浴室柜",
            "chemical_components": [
                {"name": "防水板材", "cas": "N/A", "hazard": "中"},
                {"name": "陶瓷盆", "cas": "N/A", "hazard": "低"},
                {"name": "油漆/烤漆", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "甲醛释放", "severity": "中", "description": "板材需E1级以上"},
                {"type": "防水性能", "severity": "中", "description": "潮湿环境需防水好"}
            ],
            "visual_cues": ["防水处理", "多层收纳", "镜柜组合"],
            "certifications": ["GB 18584"]
        },
        {
            "category": "卫浴洁具",
            "material_type": "淋浴花洒",
            "chemical_components": [
                {"name": "铜合金本体", "cas": "N/A", "hazard": "低"},
                {"name": "电镀层", "cas": "N/A", "hazard": "中"},
                {"name": "硅胶出水孔", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "铅析出", "severity": "中", "description": "劣质产品铅超标"},
                {"type": "电镀层脱落", "severity": "低", "description": "选择优质电镀"}
            ],
            "visual_cues": ["金属光泽", "可调节角度", "多种出水模式"],
            "certifications": ["GB 18145"]
        },
        {
            "category": "卫浴洁具",
            "material_type": "防臭地漏",
            "chemical_components": [
                {"name": "不锈钢", "cas": "N/A", "hazard": "低"},
                {"name": "硅胶密封圈", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "密封失效", "severity": "中", "description": "需定期清理"},
                {"type": "排水不畅", "severity": "低", "description": "选择大排量"}
            ],
            "visual_cues": ["T型/U型/翻板式", "不��钢面板", "防虫网"],
            "certifications": ["GB 50015"]
        },
        {
            "category": "卫浴洁具",
            "material_type": "角阀三角阀",
            "chemical_components": [
                {"name": "铜合金阀体", "cas": "N/A", "hazard": "低"},
                {"name": "陶瓷阀芯", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "铅析出", "severity": "中", "description": "选择无铅角阀"},
                {"type": "漏水", "severity": "中", "description": "安装需密封"}
            ],
            "visual_cues": ["三角形", "开关手柄", "连接软管"],
            "certifications": ["GB 18145"]
        },
        # 门窗五金类
        {
            "category": "门窗五金",
            "material_type": "门把手",
            "chemical_components": [
                {"name": "锌合金/不锈钢", "cas": "N/A", "hazard": "低"},
                {"name": "电镀层", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "重金属", "severity": "低", "description": "优质产品符合标准"},
                {"type": "表面氧化", "severity": "低", "description": "劣质电镀易脱落"}
            ],
            "visual_cues": ["金属质感", "人体工学设计", "多种款式"],
            "certifications": ["GB/T 22807"]
        },
        {
            "category": "门窗五金",
            "material_type": "合页铰链",
            "chemical_components": [
                {"name": "不锈钢/铁", "cas": "N/A", "hazard": "低"},
                {"name": "润滑油", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "承重不足", "severity": "中", "description": "选择合适尺寸和数量"},
                {"type": "生锈", "severity": "低", "description": "304不锈钢更耐用"}
            ],
            "visual_cues": ["多片连接", "轴承结构", "阻尼/液压"],
            "certifications": ["GB/T 16454"]
        },
        {
            "category": "门窗五金",
            "material_type": "门窗密封条",
            "chemical_components": [
                {"name": "EPDM橡胶", "cas": "N/A", "hazard": "低"},
                {"name": "PVC", "cas": "9002-86-2", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "气味", "severity": "低", "description": "新品需通风"},
                {"type": "老化", "severity": "低", "description": "EPDM更耐久"}
            ],
            "visual_cues": ["柔软有弹性", "黑色/白色", "多种截面形状"],
            "certifications": ["GB/T 12002"]
        },
        {
            "category": "门窗五金",
            "material_type": "执手锁",
            "chemical_components": [
                {"name": "锌合金/铝合金", "cas": "N/A", "hazard": "低"},
                {"name": "锁芯", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "防盗等级", "severity": "中", "description": "选择B级或C级锁芯"},
                {"type": "表面处理", "severity": "低", "description": "优质电镀不易脱落"}
            ],
            "visual_cues": ["把手+锁", "钥匙孔", "金属光泽"],
            "certifications": ["GA 374"]
        },
        # 其他建材辅料类
        {
            "category": "建材辅料",
            "material_type": "玻璃胶",
            "chemical_components": [
                {"name": "硅酮胶", "cas": "N/A", "hazard": "中"},
                {"name": "醇类溶剂", "cas": "N/A", "hazard": "中"}
            ],
            "risk_points": [
                {"type": "酸性气味", "severity": "中", "description": "酸性胶刺激性强,选中性胶"},
                {"type": "固化期VOCs", "severity": "中", "description": "固化时需通风"}
            ],
            "visual_cues": ["透明/白色/黑色", "软管包装", "胶枪施工"],
            "certifications": ["GB/T 14683"]
        },
        {
            "category": "建材辅料",
            "material_type": "聚氨酯发泡胶",
            "chemical_components": [
                {"name": "聚氨酯", "cas": "9009-54-5", "hazard": "高"},
                {"name": "异氰酸酯", "cas": "N/A", "hazard": "高"}
            ],
            "risk_points": [
                {"type": "异氰酸酯毒性", "severity": "高", "description": "施工需戴口罩"},
                {"type": "易燃", "severity": "高", "description": "远离明火"}
            ],
            "visual_cues": ["泡沫状", "膨胀性强", "固化后硬化"],
            "certifications": ["GB/T 30652"]
        },
        {
            "category": "建材辅料",
            "material_type": "玻璃贴膜",
            "chemical_components": [
                {"name": "PET基材", "cas": "N/A", "hazard": "低"},
                {"name": "金属涂层", "cas": "N/A", "hazard": "低"},
                {"name": "压敏胶", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "气泡瑕疵", "severity": "低", "description": "需专业施工"},
                {"type": "环保型", "severity": "低", "description": "优质产品无异味"}
            ],
            "visual_cues": ["透明/磨砂/反光", "隔热防UV", "防爆功能"],
            "certifications": ["GB/T 38264"]
        },
        {
            "category": "建材辅料",
            "material_type": "地板保护膜",
            "chemical_components": [
                {"name": "PE塑料膜", "cas": "N/A", "hazard": "低"},
                {"name": "无纺布", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "环保型", "severity": "低", "description": "装修期临时保护"},
                {"type": "胶痕", "severity": "低", "description": "低粘胶不留痕"}
            ],
            "visual_cues": ["蓝色/白色", "卷材", "可定制厚度"],
            "certifications": ["环保无毒"]
        },
        {
            "category": "建材辅料",
            "material_type": "吊顶龙骨配件",
            "chemical_components": [
                {"name": "镀锌钢", "cas": "N/A", "hazard": "低"}
            ],
            "risk_points": [
                {"type": "承重", "severity": "中", "description": "需符合承载要求"},
                {"type": "锈蚀", "severity": "低", "description": "镀锌防锈"}
            ],
            "visual_cues": ["吊杆、主龙骨、副龙骨、吊件", "银白色"],
            "certifications": ["GB/T 11981"]
        }
    ]

    results = []
    for material in new_materials:
        entry = {
            "material_id": generate_id(material["material_type"], material["category"]),
            "category": material["category"],
            "data": material,
            "source": "第十轮数据扩充-智能家居园林卫浴五金",
            "last_updated": datetime.now().isoformat(),
            "version": "10.0"
        }
        results.append(entry)
    return results

def main():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"

    print("\n" + "="*60)
    print("第十轮数据扩充开始 - 智能家居、园林景观、卫浴洁具、五金配件")
    print("="*60)

    # 添加建材数据
    print("\n添加新建材数据...")
    furniture_file = os.path.join(base_dir, "furniture.json")
    with open(furniture_file, 'r', encoding='utf-8') as f:
        existing_furniture = json.load(f)

    new_materials = expand_building_materials()
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
    print("第十轮数据扩充完成!")
    print("="*60)
    print(f"家具及建材总数: {len(all_furniture)} 条 (+{len(new_materials)})")
    print("\n新增材料类别:")
    print("  - 智能家居 (5种): 智能门锁、智能窗帘电机、智能开关面板、智能插座、智能灯泡")
    print("  - 园林景观 (5种): 防腐木、塑木复合材料、景观石、人造草坪、透水砖")
    print("  - 卫浴洁具 (5种): 智能马桶、浴室柜、淋浴花洒、防臭地漏、角阀三角阀")
    print("  - 门窗五金 (4种): 门把手、合页铰链、门窗密封条、执手锁")
    print("  - 建材辅料 (5种): 玻璃胶、聚氨酯发泡胶、玻璃贴膜、地板保护膜、吊顶龙骨配件")
    print("="*60)

if __name__ == "__main__":
    main()
