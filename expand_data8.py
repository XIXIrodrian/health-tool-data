"""第八轮数据扩充脚本 - 专门扩充衣料数据库"""
import json
import sys
import os
from datetime import datetime
import hashlib

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def generate_id(name, category):
    unique_string = f"{category}_{name}_{datetime.now().isoformat()}"
    return hashlib.md5(unique_string.encode()).hexdigest()[:16]

def expand_textile_database():
    """第八轮衣料数据库扩充"""
    new_textiles = [
        # 新型纤维类
        {
            "fabric_type": "大豆纤维",
            "composition": "大豆蛋白纤维",
            "chemical_treatments": [{"name": "蛋白质改性", "hazard": "低"}],
            "health_risks": [{"type": "大豆过敏", "severity": "低", "description": "大豆过敏者慎用"}],
            "health_benefits": ["柔软亲肤", "保湿", "抗菌"],
            "care_instructions": {"washing": "手洗", "drying": "阴干", "ironing": "低温"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "牛奶纤维",
            "composition": "牛奶蛋白纤维",
            "chemical_treatments": [{"name": "蛋白质提取", "hazard": "低"}],
            "health_risks": [{"type": "牛奶过敏", "severity": "低", "description": "牛奶过敏者慎用"}],
            "health_benefits": ["滋养肌肤", "保湿", "柔滑"],
            "care_instructions": {"washing": "手洗", "drying": "平铺晾干", "ironing": "低温"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "玉米纤维",
            "composition": "聚乳酸纤维PLA",
            "chemical_treatments": [{"name": "生物降解", "hazard": "低"}],
            "health_risks": [{"type": "环保型", "severity": "低", "description": "可完全生物降解"}],
            "health_benefits": ["天然抑菌", "透气", "环保"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "低温"},
            "certifications": ["生物降解认证"]
        },
        {
            "fabric_type": "苎麻",
            "composition": "天然麻纤维",
            "chemical_treatments": [{"name": "柔软处理", "hazard": "低"}],
            "health_risks": [{"type": "粗糙感", "severity": "低", "description": "质地较粗"}],
            "health_benefits": ["凉爽透气", "抗菌", "吸湿"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "高温"},
            "certifications": ["OEKO-TEX"]
        },
        # 工作服面料类
        {
            "fabric_type": "工装帆布",
            "composition": "纯棉或棉涤",
            "chemical_treatments": [{"name": "阻燃整理", "hazard": "中"}],
            "health_risks": [{"type": "阻燃剂", "severity": "中", "description": "含阻燃剂残留"}],
            "health_benefits": ["耐磨", "耐用", "防火"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "高温"},
            "certifications": ["GB 8965"]
        },
        {
            "fabric_type": "防静电面料",
            "composition": "涤纶+导电丝",
            "chemical_treatments": [{"name": "导电纤维植入", "hazard": "低"}],
            "health_risks": [{"type": "无特殊风险", "severity": "低", "description": "安全性高"}],
            "health_benefits": ["防静电", "防尘", "净化空气"],
            "care_instructions": {"washing": "可机洗", "drying": "低温烘干", "ironing": "不熨烫"},
            "certifications": ["GB 12014"]
        },
        {
            "fabric_type": "高可见度反光布",
            "composition": "涤纶+反光材料",
            "chemical_treatments": [{"name": "反光涂层", "hazard": "中"}],
            "health_risks": [{"type": "涂层剥落", "severity": "低", "description": "需定期检查"}],
            "health_benefits": ["夜间可见", "安全保护"],
            "care_instructions": {"washing": "轻柔洗", "drying": "晾干", "ironing": "不熨烫"},
            "certifications": ["EN ISO 20471"]
        },
        # 家纺面料类
        {
            "fabric_type": "贡缎",
            "composition": "高支高密纯棉",
            "chemical_treatments": [{"name": "丝光处理", "hazard": "低"}],
            "health_risks": [{"type": "易皱", "severity": "低", "description": "需熨烫整理"}],
            "health_benefits": ["光泽好", "手感滑", "舒适"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "高温"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "提花面料",
            "composition": "纯棉或混纺",
            "chemical_treatments": [{"name": "柔软整理", "hazard": "低"}],
            "health_risks": [{"type": "缩水", "severity": "低", "description": "纯棉易缩水"}],
            "health_benefits": ["立体花纹", "美观", "透气"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "中温"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "天鹅绒",
            "composition": "涤纶或棉",
            "chemical_treatments": [{"name": "起绒处理", "hazard": "低"}],
            "health_risks": [{"type": "掉毛", "severity": "低", "description": "初期可能掉毛"}],
            "health_benefits": ["柔软舒适", "光泽华丽", "保暖"],
            "care_instructions": {"washing": "干洗", "drying": "阴干", "ironing": "不熨烫"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "窗帘遮光布",
            "composition": "涤纶+黑丝遮光层",
            "chemical_treatments": [{"name": "遮光涂层", "hazard": "中"}],
            "health_risks": [{"type": "涂层气味", "severity": "中", "description": "新品需通风"}],
            "health_benefits": ["遮光", "隔热", "隔音"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "低温"},
            "certifications": ["OEKO-TEX"]
        },
        # 内衣面料类
        {
            "fabric_type": "蕾丝",
            "composition": "尼龙或涤纶",
            "chemical_treatments": [{"name": "染色", "hazard": "中"}],
            "health_risks": [
                {"type": "染料过敏", "severity": "中", "description": "深色蕾丝染料多"},
                {"type": "易钩丝", "severity": "低", "description": "需小心穿着"}
            ],
            "health_benefits": ["轻薄", "透气", "美观"],
            "care_instructions": {"washing": "手洗", "drying": "平铺晾干", "ironing": "不熨烫"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "无痕冰丝",
            "composition": "锦纶+氨纶",
            "chemical_treatments": [{"name": "凉感整理", "hazard": "低"}],
            "health_risks": [{"type": "易起球", "severity": "低", "description": "质量差的易起球"}],
            "health_benefits": ["无痕", "凉感", "弹力好"],
            "care_instructions": {"washing": "手洗", "drying": "阴干", "ironing": "不熨烫"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "桑蚕丝",
            "composition": "100%真丝",
            "chemical_treatments": [{"name": "轻度染色", "hazard": "低"}],
            "health_risks": [{"type": "昂贵易损", "severity": "低", "description": "需精心护理"}],
            "health_benefits": ["亲肤", "透气", "抗菌"],
            "care_instructions": {"washing": "手洗或干洗", "drying": "阴干", "ironing": "低温隔布"},
            "certifications": ["真丝标识"]
        },
        # 户外技术面料类
        {
            "fabric_type": "Gore-Tex",
            "composition": "尼龙+ePTFE膜",
            "chemical_treatments": [
                {"name": "防水薄膜", "hazard": "低"},
                {"name": "DWR拒水剂", "hazard": "中"}
            ],
            "health_risks": [{"type": "PFAS", "severity": "中", "description": "传统DWR含全氟化合物"}],
            "health_benefits": ["防水透气", "防风", "耐用"],
            "care_instructions": {"washing": "可机洗", "drying": "低温烘干激活", "ironing": "不熨烫"},
            "certifications": ["Gore-Tex认证"]
        },
        {
            "fabric_type": "Softshell软壳",
            "composition": "尼龙+聚酯+氨纶",
            "chemical_treatments": [{"name": "DWR防泼水", "hazard": "中"}],
            "health_risks": [{"type": "PFAS", "severity": "中", "description": "含全氟化合物"}],
            "health_benefits": ["弹力", "透气", "轻度防水"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "不熨烫"},
            "certifications": ["bluesign"]
        },
        {
            "fabric_type": "Primaloft保暖棉",
            "composition": "合成超细纤维",
            "chemical_treatments": [{"name": "防水处理", "hazard": "低"}],
            "health_risks": [{"type": "环保型", "severity": "低", "description": "部分使用再生材料"}],
            "health_benefits": ["保暖", "轻盈", "防水"],
            "care_instructions": {"washing": "可机洗", "drying": "低温烘干", "ironing": "不熨烫"},
            "certifications": ["Primaloft认证"]
        },
        # 医用防护面料类
        {
            "fabric_type": "医用防护服面料",
            "composition": "聚丙烯无纺布",
            "chemical_treatments": [{"name": "抗菌处理", "hazard": "低"}],
            "health_risks": [{"type": "不透气", "severity": "中", "description": "长时间穿着闷热"}],
            "health_benefits": ["防液体渗透", "防病毒", "一次性使用"],
            "care_instructions": {"washing": "一次性", "drying": "不适用", "ironing": "不适用"},
            "certifications": ["GB 19082"]
        },
        {
            "fabric_type": "银离子抗菌布",
            "composition": "棉+银离子",
            "chemical_treatments": [{"name": "银离子整理", "hazard": "低"}],
            "health_risks": [{"type": "银过敏", "severity": "低", "description": "极少数人过敏"}],
            "health_benefits": ["持久抗菌", "防臭", "安全"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "中温"},
            "certifications": ["抗菌检测报告"]
        },
        {
            "fabric_type": "芳纶阻燃布",
            "composition": "芳纶纤维",
            "chemical_treatments": [{"name": "本征阻燃", "hazard": "低"}],
            "health_risks": [{"type": "价格昂贵", "severity": "低", "description": "高端防护材料"}],
            "health_benefits": ["永久阻燃", "耐高温", "高强度"],
            "care_instructions": {"washing": "专业清洗", "drying": "晾干", "ironing": "不熨烫"},
            "certifications": ["GB 8965"]
        },
        # 传统民族面料类
        {
            "fabric_type": "香云纱",
            "composition": "真丝+薯莨汁染色",
            "chemical_treatments": [{"name": "天然植物染色", "hazard": "低"}],
            "health_risks": [{"type": "价格昂贵", "severity": "低", "description": "非遗传统工艺"}],
            "health_benefits": ["防晒", "凉爽", "独特质感"],
            "care_instructions": {"washing": "干洗", "drying": "阴干", "ironing": "不熨烫"},
            "certifications": ["非遗认证"]
        },
        {
            "fabric_type": "苗族蜡染布",
            "composition": "棉布+蜡染",
            "chemical_treatments": [{"name": "蜂蜡防染", "hazard": "低"}],
            "health_risks": [{"type": "掉色", "severity": "低", "description": "天然染料可能掉色"}],
            "health_benefits": ["天然染色", "民族特色", "透气"],
            "care_instructions": {"washing": "手洗", "drying": "阴干", "ironing": "中温"},
            "certifications": ["非遗认证"]
        },
        {
            "fabric_type": "土布",
            "composition": "纯棉手工织造",
            "chemical_treatments": [{"name": "无化学处理", "hazard": "低"}],
            "health_risks": [{"type": "粗糙", "severity": "低", "description": "质地较粗需软化"}],
            "health_benefits": ["天然环保", "透气", "吸湿"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "高温"},
            "certifications": ["非遗认证"]
        },
        # 高科技面料类
        {
            "fabric_type": "相变调温面料",
            "composition": "纤维+相变材料",
            "chemical_treatments": [{"name": "相变微胶囊", "hazard": "低"}],
            "health_risks": [{"type": "新材料", "severity": "低", "description": "高科技新材料"}],
            "health_benefits": ["智能调温", "恒温舒适"],
            "care_instructions": {"washing": "可机洗", "drying": "低温", "ironing": "低温"},
            "certifications": ["Outlast认证"]
        },
        {
            "fabric_type": "抗紫外线面料",
            "composition": "涤纶+紫外线吸收剂",
            "chemical_treatments": [{"name": "UV吸收剂整理", "hazard": "低"}],
            "health_risks": [{"type": "化学助剂", "severity": "低", "description": "助剂残留极少"}],
            "health_benefits": ["UPF50+", "防晒", "保护皮肤"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "低温"},
            "certifications": ["UPF认证"]
        },
        {
            "fabric_type": "纳米纤维面料",
            "composition": "纳米改性纤维",
            "chemical_treatments": [{"name": "纳米技术", "hazard": "低"}],
            "health_risks": [{"type": "新技术", "severity": "低", "description": "长期安全性研究中"}],
            "health_benefits": ["自清洁", "防污", "透气"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "低温"},
            "certifications": ["OEKO-TEX"]
        },
        # 特殊用途面料
        {
            "fabric_type": "电磁屏蔽布",
            "composition": "金属纤维+普通纤维",
            "chemical_treatments": [{"name": "金属纤维混纺", "hazard": "低"}],
            "health_risks": [{"type": "金属氧化", "severity": "低", "description": "需防潮"}],
            "health_benefits": ["屏蔽辐射", "防电磁波"],
            "care_instructions": {"washing": "轻柔手洗", "drying": "阴干", "ironing": "不熨烫"},
            "certifications": ["屏蔽效能测试"]
        },
        {
            "fabric_type": "负离子面料",
            "composition": "纤维+负离子粉末",
            "chemical_treatments": [{"name": "负离子整理", "hazard": "低"}],
            "health_risks": [{"type": "功效争议", "severity": "低", "description": "保健效果有待验证"}],
            "health_benefits": ["释放负离子", "净化空气", "改善睡眠"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "低温"},
            "certifications": ["OEKO-TEX"]
        }
    ]

    results = []
    for textile in new_textiles:
        entry = {
            "material_id": generate_id(textile["fabric_type"], "衣料纺织品"),
            "category": "衣料纺织品",
            "data": textile,
            "source": "第八轮数据扩充-衣料专项",
            "last_updated": datetime.now().isoformat(),
            "version": "8.0"
        }
        results.append(entry)
    return results

def main():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"

    print("\n" + "="*60)
    print("第八轮数据扩充开始 - 衣料数据库专项扩充")
    print("="*60)

    # 扩充衣料数据
    print("\n扩充衣料纺织品数据库...")
    textile_file = os.path.join(base_dir, "textile.json")
    with open(textile_file, 'r', encoding='utf-8') as f:
        existing_textile = json.load(f)

    new_textile = expand_textile_database()
    all_textile = existing_textile + new_textile

    with open(textile_file, 'w', encoding='utf-8') as f:
        json.dump(all_textile, f, ensure_ascii=False, indent=2)

    print(f"   原有: {len(existing_textile)} 条")
    print(f"   新增: {len(new_textile)} 条")
    print(f"   总计: {len(all_textile)} 条")

    # 统计各类型
    types = {}
    for item in all_textile:
        fabric_type = item['data']['fabric_type']
        types[fabric_type] = types.get(fabric_type, 0) + 1

    print(f"\n衣料面料种类: {len(types)}种")

    # 总结
    print("\n" + "="*60)
    print("第八轮数据扩充完成!")
    print("="*60)
    print(f"衣料纺织品总数: {len(all_textile)} 条 (+{len(new_textile)})")
    print("\n新增面料类别:")
    print("  - 新型纤维 (4种): 大豆纤维、牛奶纤维、玉米纤维、苎麻")
    print("  - 工作服面料 (3种): 工装帆布、防静电面料、高可见度反光布")
    print("  - 家纺面料 (4种): 贡缎、提花面料、天鹅绒、窗帘遮光布")
    print("  - 内衣面料 (3种): 蕾丝、无痕冰丝、桑蚕丝")
    print("  - 户外技术面料 (3种): Gore-Tex、Softshell软壳、Primaloft保暖棉")
    print("  - 医用防护 (3种): 医用防护服面料、银离子抗菌布、芳纶阻燃布")
    print("  - 传统民族 (3种): 香云纱、苗族蜡染布、土布")
    print("  - 高科技面料 (3种): 相变调温、抗紫外线、纳米纤维")
    print("  - 特殊用途 (2种): 电磁屏蔽布、负离子面料")
    print("="*60)

if __name__ == "__main__":
    main()
