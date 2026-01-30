"""第九轮数据扩充脚本 - 羊毛、再生、功能运动、特殊场景、时尚面料"""
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
    """第九轮衣料数据库扩充"""
    new_textiles = [
        # 羊毛制品类
        {
            "fabric_type": "美利奴羊毛",
            "composition": "100%美利奴羊毛",
            "chemical_treatments": [{"name": "防缩处理", "hazard": "低"}],
            "health_risks": [{"type": "羊毛过敏", "severity": "低", "description": "少数人对羊毛蛋白过敏"}],
            "health_benefits": ["天然透气", "温度调节", "防臭抑菌", "吸湿排汗"],
            "care_instructions": {"washing": "冷水手洗或羊毛程序", "drying": "平铺晾干", "ironing": "低温隔布"},
            "certifications": ["ZQ Merino认证", "OEKO-TEX"]
        },
        {
            "fabric_type": "山羊绒",
            "composition": "100%山羊绒",
            "chemical_treatments": [{"name": "柔软处理", "hazard": "低"}],
            "health_risks": [{"type": "价格昂贵", "severity": "低", "description": "高端奢侈面料"}],
            "health_benefits": ["极致柔软", "轻盈保暖", "亲肤舒适"],
            "care_instructions": {"washing": "专业干洗", "drying": "平铺阴干", "ironing": "不熨烫或低温隔布"},
            "certifications": ["OEKO-TEX", "羊绒标识"]
        },
        {
            "fabric_type": "羊驼毛",
            "composition": "羊驼毛纤维",
            "chemical_treatments": [{"name": "去杂质处理", "hazard": "低"}],
            "health_risks": [{"type": "纤维较粗", "severity": "低", "description": "初次穿着可能有轻微扎感"}],
            "health_benefits": ["保暖性强", "天然防水", "低过敏性", "耐久耐磨"],
            "care_instructions": {"washing": "手洗或干洗", "drying": "平铺晾干", "ironing": "低温"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "马海毛",
            "composition": "安哥拉山羊毛",
            "chemical_treatments": [{"name": "柔软整理", "hazard": "低"}],
            "health_risks": [{"type": "掉毛", "severity": "低", "description": "初期可能掉毛"}],
            "health_benefits": ["光泽华丽", "弹性好", "保暖透气"],
            "care_instructions": {"washing": "干洗为佳", "drying": "阴干", "ironing": "低温隔布"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "羊毛混纺",
            "composition": "羊毛+涤纶/腈纶",
            "chemical_treatments": [{"name": "防缩防蛀", "hazard": "低"}],
            "health_risks": [{"type": "合成纤维", "severity": "低", "description": "含化纤透气性略降"}],
            "health_benefits": ["易打理", "抗皱", "价格适中", "保暖"],
            "care_instructions": {"washing": "可机洗", "drying": "低温烘干或晾干", "ironing": "中温"},
            "certifications": ["OEKO-TEX"]
        },
        # 再生/环保面料类
        {
            "fabric_type": "再生涤纶rPET",
            "composition": "回收塑料瓶再生纤维",
            "chemical_treatments": [{"name": "再生处理", "hazard": "低"}],
            "health_risks": [{"type": "环保型", "severity": "低", "description": "减少塑料污染"}],
            "health_benefits": ["环保可持续", "性能同涤纶", "减少碳排放"],
            "care_instructions": {"washing": "可机洗", "drying": "低温烘干", "ironing": "低温"},
            "certifications": ["GRS全球回收标准", "bluesign"]
        },
        {
            "fabric_type": "再生尼龙Econyl",
            "composition": "废弃渔网再生尼龙",
            "chemical_treatments": [{"name": "解聚再聚合", "hazard": "低"}],
            "health_risks": [{"type": "环保型", "severity": "低", "description": "海洋清洁材料"}],
            "health_benefits": ["清理海洋垃圾", "性能同尼龙", "可持续循环"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "低温"},
            "certifications": ["Econyl认证", "GRS"]
        },
        {
            "fabric_type": "天丝莱赛尔",
            "composition": "桉树浆粕纤维",
            "chemical_treatments": [{"name": "闭环溶剂法", "hazard": "低"}],
            "health_risks": [{"type": "环保型", "severity": "低", "description": "99%溶剂回收"}],
            "health_benefits": ["天然来源", "丝滑亲肤", "透气吸湿", "抑菌防臭"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "中温"},
            "certifications": ["Tencel认证", "FSC森林认证"]
        },
        {
            "fabric_type": "莫代尔Modal",
            "composition": "榉木浆粕纤维",
            "chemical_treatments": [{"name": "湿法纺丝", "hazard": "低"}],
            "health_risks": [{"type": "易皱", "severity": "低", "description": "纯莫代尔易起皱"}],
            "health_benefits": ["柔软亲肤", "吸湿性好", "不易起球", "色牢度高"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "中温"},
            "certifications": ["OEKO-TEX", "FSC"]
        },
        {
            "fabric_type": "有机亚麻",
            "composition": "有机种植亚麻纤维",
            "chemical_treatments": [{"name": "无化学处理", "hazard": "低"}],
            "health_risks": [{"type": "易皱", "severity": "低", "description": "亚麻易起皱"}],
            "health_benefits": ["天然抗菌", "吸湿透气", "凉爽舒适", "环保无污染"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "高温蒸汽"},
            "certifications": ["GOTS", "OCS", "欧盟有机认证"]
        },
        # 功能性运动面料
        {
            "fabric_type": "氯丁橡胶泳衣布",
            "composition": "氯丁橡胶+尼龙面料",
            "chemical_treatments": [{"name": "橡胶发泡", "hazard": "中"}],
            "health_risks": [
                {"type": "橡胶过敏", "severity": "中", "description": "少数人对氯丁橡胶过敏"},
                {"type": "气味", "severity": "低", "description": "新品可能有橡胶味"}
            ],
            "health_benefits": ["保温防寒", "浮力辅助", "防水性强", "保护皮肤"],
            "care_instructions": {"washing": "淡水冲洗", "drying": "阴干", "ironing": "不熨烫"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "瑜伽速干布",
            "composition": "涤纶+氨纶",
            "chemical_treatments": [{"name": "吸湿排汗整理", "hazard": "低"}],
            "health_risks": [{"type": "静电", "severity": "低", "description": "易产生静电"}],
            "health_benefits": ["四向弹力", "速干透气", "紧密包裹", "排汗快"],
            "care_instructions": {"washing": "冷水机洗", "drying": "阴干", "ironing": "不熨烫"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "登山防撕裂尼龙",
            "composition": "高强度尼龙",
            "chemical_treatments": [
                {"name": "防撕裂编织", "hazard": "低"},
                {"name": "DWR拒水剂", "hazard": "中"}
            ],
            "health_risks": [{"type": "PFAS", "severity": "中", "description": "传统DWR含全氟化合物"}],
            "health_benefits": ["高强度", "耐磨防撕", "轻量化", "防泼水"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "低温"},
            "certifications": ["bluesign"]
        },
        {
            "fabric_type": "滑雪防风面料",
            "composition": "尼龙+防风膜",
            "chemical_treatments": [{"name": "防风透气膜", "hazard": "低"}],
            "health_risks": [{"type": "透气性", "severity": "低", "description": "高强度运动透气性有限"}],
            "health_benefits": ["防风保暖", "轻量", "防泼水", "耐寒性强"],
            "care_instructions": {"washing": "可机洗", "drying": "低温烘干", "ironing": "不熨烫"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "跑步反光面料",
            "composition": "涤纶+反光条",
            "chemical_treatments": [{"name": "反光材料贴合", "hazard": "低"}],
            "health_risks": [{"type": "反光条脱落", "severity": "低", "description": "需定期检查"}],
            "health_benefits": ["夜间可见", "安全保护", "透气排汗"],
            "care_instructions": {"washing": "轻柔洗", "drying": "阴干", "ironing": "不熨烫"},
            "certifications": ["EN ISO 20471"]
        },
        {
            "fabric_type": "骑行压缩面料",
            "composition": "尼龙+氨纶+硅胶垫",
            "chemical_treatments": [{"name": "梯度压缩", "hazard": "低"}],
            "health_risks": [{"type": "过度压缩", "severity": "中", "description": "尺码不当影响血液循环"}],
            "health_benefits": ["肌肉支撑", "减震护垫", "排汗速干", "减少疲劳"],
            "care_instructions": {"washing": "手洗", "drying": "阴干", "ironing": "不熨烫"},
            "certifications": ["OEKO-TEX"]
        },
        # 特殊场景面料
        {
            "fabric_type": "医用级抗菌面料",
            "composition": "棉+银离子/铜离子",
            "chemical_treatments": [{"name": "抗菌整理", "hazard": "低"}],
            "health_risks": [{"type": "金属过敏", "severity": "低", "description": "极少数人过敏"}],
            "health_benefits": ["99.9%抗菌", "防螨除臭", "持久抑菌", "伤口护理"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "中温"},
            "certifications": ["GB/T 20944", "ISO 20743"]
        },
        {
            "fabric_type": "阻燃窗帘布",
            "composition": "涤纶+阻燃剂",
            "chemical_treatments": [{"name": "永久阻燃整理", "hazard": "中"}],
            "health_risks": [
                {"type": "阻燃剂", "severity": "中", "description": "含磷系或氮系阻燃剂"},
                {"type": "气味", "severity": "低", "description": "新品需通风"}
            ],
            "health_benefits": ["防火安全", "遇火不易燃烧", "公共场所必备"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "低温"},
            "certifications": ["GB 20286", "B1级阻燃"]
        },
        {
            "fabric_type": "防螨寝具面料",
            "composition": "高支高密纯棉",
            "chemical_treatments": [{"name": "物理防螨", "hazard": "低"}],
            "health_risks": [{"type": "环保型", "severity": "低", "description": "物理防螨无化学添加"}],
            "health_benefits": ["阻隔螨虫", "缓解过敏", "透气舒适", "可水洗"],
            "care_instructions": {"washing": "60℃以上热水洗", "drying": "高温烘干杀螨", "ironing": "高温"},
            "certifications": ["OEKO-TEX", "防螨检测报告"]
        },
        {
            "fabric_type": "防静电洁净服",
            "composition": "涤纶+导电纤维",
            "chemical_treatments": [{"name": "导电丝植入", "hazard": "低"}],
            "health_risks": [{"type": "环保型", "severity": "低", "description": "电子厂必备"}],
            "health_benefits": ["防静电", "防尘", "洁净无脱落", "舒适透气"],
            "care_instructions": {"washing": "专用洗涤", "drying": "低温烘干", "ironing": "不熨烫"},
            "certifications": ["GB 12014", "GB/T 23316"]
        },
        {
            "fabric_type": "防紫外线遮阳布",
            "composition": "涤纶+UV吸收剂",
            "chemical_treatments": [{"name": "UV整理", "hazard": "低"}],
            "health_risks": [{"type": "环保型", "severity": "低", "description": "户外必备"}],
            "health_benefits": ["UPF50+", "阻挡98%紫外线", "防晒护肤", "降温隔热"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "低温"},
            "certifications": ["AS/NZS 4399", "UPF认证"]
        },
        # 时尚/高端面料
        {
            "fabric_type": "真丝缎面",
            "composition": "100%桑蚕丝",
            "chemical_treatments": [{"name": "缎纹织造", "hazard": "低"}],
            "health_risks": [{"type": "娇贵易损", "severity": "低", "description": "需精心护理"}],
            "health_benefits": ["奢华光泽", "丝滑亲肤", "透气抑菌", "护肤美容"],
            "care_instructions": {"washing": "干洗或手洗", "drying": "阴干", "ironing": "低温反面熨"},
            "certifications": ["真丝标识", "OEKO-TEX"]
        },
        {
            "fabric_type": "丝绒天鹅绒",
            "composition": "粘胶或涤纶绒毛",
            "chemical_treatments": [{"name": "起绒处理", "hazard": "低"}],
            "health_risks": [{"type": "掉毛", "severity": "低", "description": "初期可能掉毛"}],
            "health_benefits": ["奢华质感", "柔软舒适", "保暖性好", "高级感"],
            "care_instructions": {"washing": "干洗", "drying": "阴干", "ironing": "蒸汽熨烫"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "欧根纱",
            "composition": "真丝或涤纶",
            "chemical_treatments": [{"name": "硬挺整理", "hazard": "低"}],
            "health_risks": [{"type": "易钩丝", "severity": "低", "description": "轻薄易损"}],
            "health_benefits": ["轻盈飘逸", "透明质感", "时尚高雅"],
            "care_instructions": {"washing": "手洗或干洗", "drying": "悬挂阴干", "ironing": "低温隔布"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "雪纺",
            "composition": "真丝或涤纶",
            "chemical_treatments": [{"name": "强捻处理", "hazard": "低"}],
            "health_risks": [{"type": "易皱", "severity": "低", "description": "轻薄易皱"}],
            "health_benefits": ["轻薄透气", "飘逸柔美", "舒适凉爽"],
            "care_instructions": {"washing": "手洗", "drying": "悬挂阴干", "ironing": "低温隔布"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "针织羊毛",
            "composition": "羊毛针织物",
            "chemical_treatments": [{"name": "防缩柔软", "hazard": "低"}],
            "health_risks": [{"type": "易变形", "severity": "低", "description": "针织物易拉伸"}],
            "health_benefits": ["弹性好", "保暖舒适", "透气性佳", "贴身合体"],
            "care_instructions": {"washing": "手洗或羊毛程序", "drying": "平铺晾干", "ironing": "低温蒸汽"},
            "certifications": ["OEKO-TEX", "羊毛标识"]
        }
    ]

    results = []
    for textile in new_textiles:
        entry = {
            "material_id": generate_id(textile["fabric_type"], "衣料纺织品"),
            "category": "衣料纺织品",
            "data": textile,
            "source": "第九轮数据扩充-羊毛环保运动时尚",
            "last_updated": datetime.now().isoformat(),
            "version": "9.0"
        }
        results.append(entry)
    return results

def main():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"

    print("\n" + "="*60)
    print("第九轮数据扩充开始 - 羊毛、环保、运动、时尚面料")
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
    print("第九轮数据扩充完成!")
    print("="*60)
    print(f"衣料纺织品总数: {len(all_textile)} 条 (+{len(new_textile)})")
    print("\n新增面料类别:")
    print("  - 羊毛制品类 (5种): 美利奴羊毛、山羊绒、羊驼毛、马海毛、羊毛混纺")
    print("  - 再生环保类 (5种): 再生涤纶rPET、再生尼龙Econyl、天丝莱赛尔、莫代尔、有机亚麻")
    print("  - 功能运动类 (6种): 氯丁橡胶泳衣、瑜伽速干布、登山防撕裂尼龙、")
    print("                      滑雪防风面料、跑步反光面料、骑行压缩面料")
    print("  - 特殊场景类 (5种): 医用级抗菌面料、阻燃窗帘布、防螨寝具面料、")
    print("                      防静电洁净服、防紫外线遮阳布")
    print("  - 时尚高端类 (5种): 真丝缎面、丝绒天鹅绒、欧根纱、雪纺、针织羊毛")
    print("="*60)

if __name__ == "__main__":
    main()
