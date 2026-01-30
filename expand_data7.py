"""第七轮数据扩充脚本 - 扩充衣料和食物数据"""
import json
import sys
import os
from datetime import datetime
import hashlib

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def generate_id(name, category):
    unique_string = f"{category}_{name}_{datetime.now().isoformat()}"
    return hashlib.md5(unique_string.encode()).hexdigest()[:16]

def expand_textile_data():
    """扩充衣料纺织品数据"""
    new_textiles = [
        # 婴儿面料类
        {
            "fabric_type": "有机棉",
            "composition": "100%有机棉",
            "chemical_treatments": [{"name": "无化学处理", "hazard": "低"}],
            "health_risks": [{"type": "无特殊风险", "severity": "低", "description": "最安全的婴儿面料"}],
            "health_benefits": ["无农药残留", "无化学染色", "亲肤柔软"],
            "care_instructions": {"washing": "可机洗", "drying": "自然晾干", "ironing": "中温"},
            "certifications": ["GOTS", "OCS"]
        },
        {
            "fabric_type": "纱布棉",
            "composition": "纯棉纱布",
            "chemical_treatments": [{"name": "柔软整���", "hazard": "低"}],
            "health_risks": [{"type": "易变形", "severity": "低", "description": "柔软易变形"}],
            "health_benefits": ["透气性极佳", "吸湿快干", "柔软亲肤"],
            "care_instructions": {"washing": "手洗为佳", "drying": "平铺晾干", "ironing": "低温"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "婴儿竹纤维",
            "composition": "竹纤维",
            "chemical_treatments": [{"name": "抗菌整理", "hazard": "低"}],
            "health_risks": [{"type": "化学加工", "severity": "低", "description": "竹浆粘胶有化学加工"}],
            "health_benefits": ["天然抗菌", "吸湿透气", "柔软舒适"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "中温"},
            "certifications": ["OEKO-TEX"]
        },
        # 运动面料类
        {
            "fabric_type": "压缩面料",
            "composition": "尼龙+氨纶",
            "chemical_treatments": [{"name": "弹力整理", "hazard": "中"}],
            "health_risks": [{"type": "过紧影响循环", "severity": "中", "description": "压力过大影响血液循环"}],
            "health_benefits": ["肌肉支撑", "减少疲劳", "提升表现"],
            "care_instructions": {"washing": "冷水机洗", "drying": "阴干", "ironing": "不熨烫"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "Coolmax",
            "composition": "特殊聚酯纤维",
            "chemical_treatments": [{"name": "吸湿排汗整理", "hazard": "低"}],
            "health_risks": [{"type": "静电", "severity": "低", "description": "易产生静电"}],
            "health_benefits": ["四通道排汗", "快干透气", "温度调节"],
            "care_instructions": {"washing": "可机洗", "drying": "快干", "ironing": "低温"},
            "certifications": ["bluesign"]
        },
        {
            "fabric_type": "瑜伽裤面料",
            "composition": "尼龙+氨纶",
            "chemical_treatments": [{"name": "四向弹力", "hazard": "低"}],
            "health_risks": [{"type": "过敏", "severity": "低", "description": "敏感肌可能过敏"}],
            "health_benefits": ["高弹力", "裸感舒适", "塑形提臀"],
            "care_instructions": {"washing": "冷水洗", "drying": "平铺晾干", "ironing": "不熨烫"},
            "certifications": ["OEKO-TEX"]
        },
        # 皮革类
        {
            "fabric_type": "牛皮革",
            "composition": "天然牛皮",
            "chemical_treatments": [
                {"name": "铬鞣", "hazard": "中"},
                {"name": "染色", "hazard": "中"}
            ],
            "health_risks": [
                {"type": "六价铬", "severity": "高", "description": "劣质皮革铬超标"},
                {"type": "甲醛", "severity": "中", "description": "固色剂含甲醛"}
            ],
            "health_benefits": ["透气性好", "耐用", "高级质感"],
            "care_instructions": {"washing": "专业护理", "drying": "自然晾干", "ironing": "不熨烫"},
            "certifications": ["LWG"]
        },
        {
            "fabric_type": "超纤皮",
            "composition": "超细纤维+聚氨酯",
            "chemical_treatments": [{"name": "PU涂层", "hazard": "中"}],
            "health_risks": [{"type": "聚氨酯气味", "severity": "中", "description": "新品可能有气味"}],
            "health_benefits": ["透气性好", "环保无动物成分", "易打理"],
            "care_instructions": {"washing": "擦拭清洁", "drying": "通风晾干", "ironing": "不熨烫"},
            "certifications": ["REACH"]
        },
        {
            "fabric_type": "Nappa皮",
            "composition": "羊皮/小牛皮",
            "chemical_treatments": [{"name": "植鞣", "hazard": "低"}],
            "health_risks": [{"type": "价格昂贵", "severity": "低", "description": "高端皮革"}],
            "health_benefits": ["柔软细腻", "透气性佳", "环保鞣制"],
            "care_instructions": {"washing": "专业护理", "drying": "阴干", "ironing": "不熨烫"},
            "certifications": ["LWG"]
        },
        # 特殊工艺面料
        {
            "fabric_type": "磨毛面料",
            "composition": "棉或涤棉",
            "chemical_treatments": [{"name": "磨毛处理", "hazard": "低"}],
            "health_risks": [{"type": "掉毛", "severity": "低", "description": "初期可能掉毛"}],
            "health_benefits": ["保暖", "柔软蓬松", "舒适触感"],
            "care_instructions": {"washing": "轻柔洗", "drying": "晾干", "ironing": "低温"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "羊羔绒",
            "composition": "涤纶仿羊毛",
            "chemical_treatments": [{"name": "拉毛处理", "hazard": "低"}],
            "health_risks": [{"type": "静电", "severity": "低", "description": "易产生静电"}],
            "health_benefits": ["极其保暖", "柔软舒适", "价格实惠"],
            "care_instructions": {"washing": "手洗", "drying": "平铺晾干", "ironing": "不熨烫"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "华夫格面料",
            "composition": "纯棉编织",
            "chemical_treatments": [{"name": "柔软整理", "hazard": "低"}],
            "health_risks": [{"type": "缩水", "severity": "低", "description": "纯棉易缩水"}],
            "health_benefits": ["立体质感", "吸水性强", "透气舒适"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "中高温"},
            "certifications": ["OEKO-TEX"]
        },
        # 智能面料
        {
            "fabric_type": "石墨烯面料",
            "composition": "纤维+石墨烯",
            "chemical_treatments": [{"name": "石墨烯涂层", "hazard": "低"}],
            "health_risks": [{"type": "长期安全性", "severity": "低", "description": "新材料长期影响待研究"}],
            "health_benefits": ["远红外保暖", "抗菌抑菌", "防静电"],
            "care_instructions": {"washing": "可机洗", "drying": "晾干", "ironing": "低温"},
            "certifications": ["OEKO-TEX"]
        },
        {
            "fabric_type": "发热纤维",
            "composition": "吸湿发热纤维",
            "chemical_treatments": [{"name": "特殊纤维改性", "hazard": "低"}],
            "health_risks": [{"type": "过热", "severity": "低", "description": "运动时可能过热"}],
            "health_benefits": ["吸湿发热", "保暖舒适", "轻薄"],
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
            "source": "第七轮数据扩充-衣料",
            "last_updated": datetime.now().isoformat(),
            "version": "7.0"
        }
        results.append(entry)
    return results

def expand_food_data():
    """扩充食物数据"""
    new_foods = [
        # 更多谷物
        {
            "name": "小米",
            "category": "谷物类",
            "nutrients": {
                "energy": {"value": 358, "unit": "kcal/100g"},
                "protein": {"value": 9, "unit": "g/100g"},
                "iron": {"value": 5.1, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "50-100g/天"},
            "health_benefits": ["养胃", "补铁", "���神"],
            "contraindications": ["虚寒体质少食"],
            "incompatible_foods": []
        },
        {
            "name": "高粱",
            "category": "谷物类",
            "nutrients": {
                "energy": {"value": 351, "unit": "kcal/100g"},
                "fiber": {"value": 4.3, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "50-100g/天"},
            "health_benefits": ["健脾", "消食", "止泻"],
            "contraindications": ["大便燥结者慎食"],
            "incompatible_foods": []
        },
        {
            "name": "荞麦",
            "category": "谷物类",
            "nutrients": {
                "energy": {"value": 337, "unit": "kcal/100g"},
                "rutin": {"value": "高", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "50-100g/天"},
            "health_benefits": ["降血糖", "降血脂", "软化血管"],
            "contraindications": ["脾胃虚寒少食"],
            "incompatible_foods": []
        },
        # 更多蔬菜
        {
            "name": "莲藕",
            "category": "蔬菜类",
            "nutrients": {
                "energy": {"value": 73, "unit": "kcal/100g"},
                "vitamin_c": {"value": 44, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "100-150g/天"},
            "health_benefits": ["清热凉血", "健脾开胃", "止血"],
            "contraindications": ["脾胃虚寒少食生藕"],
            "incompatible_foods": []
        },
        {
            "name": "芋头",
            "category": "蔬菜类",
            "nutrients": {
                "energy": {"value": 79, "unit": "kcal/100g"},
                "starch": {"value": 17.5, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "100-150g/天"},
            "health_benefits": ["健脾", "补中", "解毒"],
            "contraindications": ["糖尿病患者控制量", "生食有毒"],
            "incompatible_foods": []
        },
        {
            "name": "冬瓜",
            "category": "蔬菜类",
            "nutrients": {
                "energy": {"value": 11, "unit": "kcal/100g"},
                "water": {"value": 96, "unit": "%"}
            },
            "recommended_intake": {"adult": "100-200g/天"},
            "health_benefits": ["利尿消肿", "清热解暑", "减肥"],
            "contraindications": ["脾胃虚寒少食"],
            "incompatible_foods": []
        },
        {
            "name": "苦瓜",
            "category": "蔬菜类",
            "nutrients": {
                "energy": {"value": 19, "unit": "kcal/100g"},
                "苦瓜素": {"value": "高", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "50-100g/天"},
            "health_benefits": ["清热解毒", "降血糖", "明目"],
            "contraindications": ["脾胃虚寒慎食", "孕妇少食"],
            "incompatible_foods": []
        },
        {
            "name": "韭菜",
            "category": "蔬菜类",
            "nutrients": {
                "energy": {"value": 26, "unit": "kcal/100g"},
                "fiber": {"value": 1.4, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "50-100g/天"},
            "health_benefits": ["补肾壮阳", "温中开胃", "散瘀"],
            "contraindications": ["阴虚火旺者慎食", "胃溃疡少食"],
            "incompatible_foods": [{"food": "蜂蜜", "reason": "同食易腹泻", "severity": "轻微"}]
        },
        # 更多水果
        {
            "name": "榴莲",
            "category": "水果类",
            "nutrients": {
                "energy": {"value": 147, "unit": "kcal/100g"},
                "sugar": {"value": 27, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "100g/天"},
            "health_benefits": ["滋补", "增强免疫", "活血散寒"],
            "contraindications": ["糖尿病患者禁食", "热性体质少食", "肥胖者控制量"],
            "incompatible_foods": [{"food": "白酒", "reason": "同食易上火", "severity": "中等"}]
        },
        {
            "name": "芒果",
            "category": "水果类",
            "nutrients": {
                "energy": {"value": 35, "unit": "kcal/100g"},
                "carotene": {"value": 897, "unit": "μg/100g"}
            },
            "recommended_intake": {"adult": "1-2个/天"},
            "health_benefits": ["明目", "美容", "防癌"],
            "contraindications": ["芒果过敏者禁食", "皮炎湿疹少食"],
            "incompatible_foods": []
        },
        {
            "name": "荔枝",
            "category": "水果类",
            "nutrients": {
                "energy": {"value": 70, "unit": "kcal/100g"},
                "vitamin_c": {"value": 41, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "5-10颗/天"},
            "health_benefits": ["补脾益肝", "生津止渴", "补血"],
            "contraindications": ["上火体质少食", "空腹大量食用易低血糖", "糖尿病患者慎食"],
            "incompatible_foods": []
        },
        {
            "name": "桃子",
            "category": "水果类",
            "nutrients": {
                "energy": {"value": 48, "unit": "kcal/100g"},
                "iron": {"value": 0.8, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "1-2个/天"},
            "health_benefits": ["生津润肠", "活血", "补铁"],
            "contraindications": ["多食易腹胀", "糖尿病患者控制量"],
            "incompatible_foods": []
        },
        {
            "name": "樱桃",
            "category": "水果类",
            "nutrients": {
                "energy": {"value": 46, "unit": "kcal/100g"},
                "iron": {"value": 5.9, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "10-15颗/天"},
            "health_benefits": ["补血", "美容", "抗炎"],
            "contraindications": ["上火体质少食", "溃疡患者慎食"],
            "incompatible_foods": []
        },
        # 海鲜类
        {
            "name": "螃蟹",
            "category": "水产类",
            "nutrients": {
                "energy": {"value": 95, "unit": "kcal/100g"},
                "protein": {"value": 17.5, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "100-150g/天"},
            "health_benefits": ["清热解毒", "补骨添髓", "养筋活血"],
            "contraindications": ["痛风患者禁食", "孕妇慎食", "脾胃虚寒少食"],
            "incompatible_foods": [{"food": "柿子", "reason": "引起腹泻", "severity": "高"}]
        },
        {
            "name": "鱿鱼",
            "category": "水产类",
            "nutrients": {
                "energy": {"value": 75, "unit": "kcal/100g"},
                "protein": {"value": 15.2, "unit": "g/100g"},
                "cholesterol": {"value": 268, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "50-100g/天"},
            "health_benefits": ["补钙", "护肝", "补脑"],
            "contraindications": ["高胆固醇者少食", "海鲜过敏者禁食"],
            "incompatible_foods": []
        },
        {
            "name": "扇贝",
            "category": "水产类",
            "nutrients": {
                "energy": {"value": 60, "unit": "kcal/100g"},
                "protein": {"value": 11.1, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "50-100g/天"},
            "health_benefits": ["滋阴补肾", "健脾调中"],
            "contraindications": ["海鲜过敏者禁食", "痛风患者少食"],
            "incompatible_foods": []
        },
        {
            "name": "生蚝",
            "category": "水产类",
            "nutrients": {
                "energy": {"value": 57, "unit": "kcal/100g"},
                "zinc": {"value": 71, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "50-100g/天"},
            "health_benefits": ["补锌", "提高免疫", "补肾"],
            "contraindications": ["海鲜过敏者禁食", "生食需新鲜卫生"],
            "incompatible_foods": []
        },
        # 蛋类
        {
            "name": "鸡蛋",
            "category": "蛋类",
            "nutrients": {
                "energy": {"value": 144, "unit": "kcal/100g"},
                "protein": {"value": 13.3, "unit": "g/100g"},
                "cholesterol": {"value": 585, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "1-2个/天"},
            "health_benefits": ["优质蛋白", "护眼", "健脑"],
            "contraindications": ["高胆固醇者控制量"],
            "incompatible_foods": [{"food": "豆浆", "reason": "影响吸收", "severity": "轻微"}]
        },
        {
            "name": "鸭蛋",
            "category": "蛋类",
            "nutrients": {
                "energy": {"value": 180, "unit": "kcal/100g"},
                "protein": {"value": 12.6, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "1个/天"},
            "health_benefits": ["滋阴清肺", "补血"],
            "contraindications": ["脾胃虚寒少食"],
            "incompatible_foods": []
        },
        {
            "name": "鹌鹑蛋",
            "category": "蛋类",
            "nutrients": {
                "energy": {"value": 160, "unit": "kcal/100g"},
                "protein": {"value": 12.8, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "3-5个/天"},
            "health_benefits": ["补脑", "养血", "强身"],
            "contraindications": ["高胆固醇者控制量"],
            "incompatible_foods": []
        },
        # 更多调味品
        {
            "name": "辣椒",
            "category": "调味品",
            "nutrients": {
                "vitamin_c": {"value": 144, "unit": "mg/100g"},
                "capsaicin": {"value": "高", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "适量"},
            "health_benefits": ["开胃", "促进消化", "驱寒"],
            "contraindications": ["胃溃疡禁食", "痔疮患者少食", "上火体质慎食"],
            "incompatible_foods": []
        },
        {
            "name": "孜然",
            "category": "调味品",
            "nutrients": {},
            "recommended_intake": {"adult": "1-3g/天"},
            "health_benefits": ["温中暖胃", "散寒止痛", "杀菌"],
            "contraindications": ["阴虚火旺者慎用"],
            "incompatible_foods": []
        },
        {
            "name": "香叶",
            "category": "调味品",
            "nutrients": {},
            "recommended_intake": {"adult": "2-3片/次"},
            "health_benefits": ["增香", "祛腥", "助消化"],
            "contraindications": [],
            "incompatible_foods": []
        },
        # 饮品
        {
            "name": "黑咖啡",
            "category": "饮品类",
            "nutrients": {
                "energy": {"value": 1, "unit": "kcal/100ml"},
                "caffeine": {"value": 40, "unit": "mg/100ml"}
            },
            "recommended_intake": {"adult": "1-3杯/天"},
            "health_benefits": ["提神", "抗氧化", "促进代谢"],
            "contraindications": ["孕妇少饮", "失眠者避免", "胃溃疡患者慎饮"],
            "incompatible_foods": []
        },
        {
            "name": "豆浆",
            "category": "饮品类",
            "nutrients": {
                "energy": {"value": 14, "unit": "kcal/100ml"},
                "protein": {"value": 1.8, "unit": "g/100ml"}
            },
            "recommended_intake": {"adult": "200-300ml/天"},
            "health_benefits": ["补充植��蛋白", "降胆固醇", "美容"],
            "contraindications": ["痛风患者少饮", "必须煮熟"],
            "incompatible_foods": [{"food": "鸡蛋", "reason": "影响吸收", "severity": "轻微"}]
        },
        # 烹饪油
        {
            "name": "大豆油",
            "category": "油脂类",
            "nutrients": {
                "energy": {"value": 899, "unit": "kcal/100g"},
                "vitamin_e": {"value": 93, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "25-30g/天"},
            "health_benefits": ["补充维E", "降胆固醇"],
            "contraindications": ["高温易产生有害物"],
            "incompatible_foods": []
        },
        {
            "name": "菜籽油",
            "category": "油脂类",
            "nutrients": {
                "energy": {"value": 899, "unit": "kcal/100g"},
                "油酸": {"value": 61, "unit": "%"}
            },
            "recommended_intake": {"adult": "25-30g/天"},
            "health_benefits": ["软化血管", "延缓衰老"],
            "contraindications": [],
            "incompatible_foods": []
        },
        {
            "name": "亚麻籽油",
            "category": "油脂类",
            "nutrients": {
                "energy": {"value": 899, "unit": "kcal/100g"},
                "α-亚麻酸": {"value": "55%", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "5-10ml/天"},
            "health_benefits": ["补充Omega-3", "降血脂", "健脑"],
            "contraindications": ["不耐高温,凉拌为主"],
            "incompatible_foods": []
        }
    ]

    results = []
    for food in new_foods:
        entry = {
            "material_id": generate_id(food["name"], food["category"]),
            "category": food["category"],
            "data": food,
            "source": "第七轮数据扩充-食物",
            "last_updated": datetime.now().isoformat(),
            "version": "7.0"
        }
        results.append(entry)
    return results

def main():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"

    print("\n" + "="*60)
    print("第七轮数据扩充开始 - 衣料和食物")
    print("="*60)

    # 扩充衣料数据
    print("\n扩充衣料纺织品数据...")
    textile_file = os.path.join(base_dir, "textile.json")
    with open(textile_file, 'r', encoding='utf-8') as f:
        existing_textile = json.load(f)

    new_textile = expand_textile_data()
    all_textile = existing_textile + new_textile

    with open(textile_file, 'w', encoding='utf-8') as f:
        json.dump(all_textile, f, ensure_ascii=False, indent=2)

    print(f"   原有: {len(existing_textile)} 条")
    print(f"   新增: {len(new_textile)} 条")
    print(f"   总计: {len(all_textile)} 条")

    # 扩充食物数据
    print("\n扩充食物数据...")
    food_file = os.path.join(base_dir, "food.json")
    with open(food_file, 'r', encoding='utf-8') as f:
        existing_food = json.load(f)

    new_food = expand_food_data()
    all_food = existing_food + new_food

    with open(food_file, 'w', encoding='utf-8') as f:
        json.dump(all_food, f, ensure_ascii=False, indent=2)

    print(f"   原有: {len(existing_food)} 条")
    print(f"   新增: {len(new_food)} 条")
    print(f"   总计: {len(all_food)} 条")

    # 总结
    print("\n" + "="*60)
    print("第七轮数据扩充完成!")
    print("="*60)
    print(f"衣料纺织品: {len(all_textile)} 条 (+{len(new_textile)})")
    print(f"食物数据: {len(all_food)} 条 (+{len(new_food)})")
    print("\n新增衣料类别:")
    print("  - 婴儿面料 (3种): 有机棉、纱布棉、婴儿竹纤维")
    print("  - 运动面料 (3种): 压缩面料、Coolmax、瑜伽裤面料")
    print("  - 皮革类 (3种): 牛皮革、超纤皮、Nappa皮")
    print("  - 特殊工艺 (3种): 磨毛面料、羊羔绒、华夫格面料")
    print("  - 智能面料 (2种): 石墨烯面料、发热纤维")
    print("\n新增食物类别:")
    print("  - 谷物 (3种): 小米、高粱、荞麦")
    print("  - 蔬菜 (5种): 莲藕、芋头、冬瓜、苦瓜、韭菜")
    print("  - 水果 (5种): 榴莲、芒果、荔枝、桃子、樱桃")
    print("  - 海鲜 (4种): 螃蟹、鱿鱼、扇贝、生蚝")
    print("  - 蛋类 (3种): 鸡蛋、鸭蛋、鹌鹑蛋")
    print("  - 调味品 (3种): 辣椒、孜然、香叶")
    print("  - 饮品 (2种): 黑咖啡、豆浆")
    print("  - 油脂 (3种): 大豆油、菜籽油、亚麻籽油")
    print("="*60)

if __name__ == "__main__":
    main()
