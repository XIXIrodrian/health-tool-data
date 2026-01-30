"""第十一轮数据扩充脚本 - 肉类、坚果、豆制品、菌菇、中药食材"""
import json
import sys
import os
from datetime import datetime
import hashlib

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def generate_id(name, category):
    unique_string = f"{category}_{name}_{datetime.now().isoformat()}"
    return hashlib.md5(unique_string.encode()).hexdigest()[:16]

def expand_food_data():
    """第十一轮食物数据扩充"""
    new_foods = [
        # 肉类
        {
            "name": "牛肉",
            "category": "肉类",
            "nutrients": {
                "energy": {"value": 125, "unit": "kcal/100g"},
                "protein": {"value": 20.1, "unit": "g/100g"},
                "iron": {"value": 2.8, "unit": "mg/100g"},
                "zinc": {"value": 4.73, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "50-75g/天"},
            "health_benefits": ["补铁", "增强肌肉", "提高免疫力", "补充优质蛋白"],
            "contraindications": ["高尿酸者少食", "肠胃虚弱者适量"],
            "incompatible_foods": [{"food": "栗子", "reason": "不易消化", "severity": "轻微"}]
        },
        {
            "name": "羊肉",
            "category": "肉类",
            "nutrients": {
                "energy": {"value": 203, "unit": "kcal/100g"},
                "protein": {"value": 19, "unit": "g/100g"},
                "fat": {"value": 14.1, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "50-100g/天"},
            "health_benefits": ["温中暖胃", "补气养血", "御寒", "壮阳"],
            "contraindications": ["热性体质少食", "高血脂者控制量", "夏季少食"],
            "incompatible_foods": [{"food": "西瓜", "reason": "寒热相冲", "severity": "中等"}]
        },
        {
            "name": "猪肉",
            "category": "肉类",
            "nutrients": {
                "energy": {"value": 395, "unit": "kcal/100g"},
                "protein": {"value": 13.2, "unit": "g/100g"},
                "fat": {"value": 37, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "50-75g/天"},
            "health_benefits": ["滋阴润燥", "补肾养血", "提供能量"],
            "contraindications": ["高血脂者少食肥肉", "肥胖者控制量"],
            "incompatible_foods": [{"food": "杏仁", "reason": "影响吸收", "severity": "轻微"}]
        },
        {
            "name": "鸡肉",
            "category": "肉类",
            "nutrients": {
                "energy": {"value": 167, "unit": "kcal/100g"},
                "protein": {"value": 19.3, "unit": "g/100g"},
                "fat": {"value": 9.4, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "50-100g/天"},
            "health_benefits": ["低脂高蛋白", "增强体力", "温中补气", "健脾胃"],
            "contraindications": ["痛风急性期慎食", "去皮更健康"],
            "incompatible_foods": []
        },
        {
            "name": "鸭肉",
            "category": "肉类",
            "nutrients": {
                "energy": {"value": 240, "unit": "kcal/100g"},
                "protein": {"value": 15.5, "unit": "g/100g"},
                "fat": {"value": 19.7, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "50-100g/天"},
            "health_benefits": ["滋阴养胃", "清热利水", "补虚"],
            "contraindications": ["脾胃虚寒少食"],
            "incompatible_foods": []
        },
        # 坚果类
        {
            "name": "核桃",
            "category": "坚果类",
            "nutrients": {
                "energy": {"value": 654, "unit": "kcal/100g"},
                "fat": {"value": 65.2, "unit": "g/100g"},
                "protein": {"value": 15.2, "unit": "g/100g"},
                "omega-3": {"value": "丰富", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "2-3个/天（20-30g）"},
            "health_benefits": ["健脑益智", "补肾", "润肠通便", "抗氧化"],
            "contraindications": ["易上火", "肥胖者控制量", "腹泻者慎食"],
            "incompatible_foods": [{"food": "白酒", "reason": "易上火", "severity": "中等"}]
        },
        {
            "name": "杏仁",
            "category": "坚果类",
            "nutrients": {
                "energy": {"value": 578, "unit": "kcal/100g"},
                "protein": {"value": 21.3, "unit": "g/100g"},
                "vitamin_e": {"value": 25.6, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "8-10颗/天（15-20g）"},
            "health_benefits": ["润肺止咳", "美容养颜", "降血脂", "抗衰老"],
            "contraindications": ["苦杏仁有毒需熟食", "婴幼儿慎食"],
            "incompatible_foods": [{"food": "猪肉", "reason": "影响吸收", "severity": "轻微"}]
        },
        {
            "name": "腰果",
            "category": "坚果类",
            "nutrients": {
                "energy": {"value": 552, "unit": "kcal/100g"},
                "fat": {"value": 36.7, "unit": "g/100g"},
                "protein": {"value": 17.3, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "10-15颗/天（15-20g）"},
            "health_benefits": ["增强免疫", "保护心血管", "补充能量"],
            "contraindications": ["过敏者禁食", "高热量控制量"],
            "incompatible_foods": []
        },
        {
            "name": "开心果",
            "category": "坚果类",
            "nutrients": {
                "energy": {"value": 614, "unit": "kcal/100g"},
                "protein": {"value": 20.6, "unit": "g/100g"},
                "fiber": {"value": 10.6, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "10-15颗/天（15-20g）"},
            "health_benefits": ["护眼明目", "润肠通便", "降血脂", "抗氧化"],
            "contraindications": ["易上火", "肥胖者控制量"],
            "incompatible_foods": []
        },
        {
            "name": "夏威夷果",
            "category": "坚果类",
            "nutrients": {
                "energy": {"value": 718, "unit": "kcal/100g"},
                "fat": {"value": 76, "unit": "g/100g"},
                "单不饱和脂肪酸": {"value": "极高", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "3-5颗/天（10-15g）"},
            "health_benefits": ["降胆固醇", "健脑", "美容护肤", "调节血脂"],
            "contraindications": ["高热量", "肥胖者少食", "消化不良者慎食"],
            "incompatible_foods": []
        },
        # 豆制品类
        {
            "name": "豆腐",
            "category": "豆制品类",
            "nutrients": {
                "energy": {"value": 81, "unit": "kcal/100g"},
                "protein": {"value": 8.1, "unit": "g/100g"},
                "calcium": {"value": 164, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "100-150g/天"},
            "health_benefits": ["补钙", "优质植物蛋白", "降胆固醇", "易消化"],
            "contraindications": ["痛风急性期少食", "肾功能不全者控制量", "胃寒者少食生豆腐"],
            "incompatible_foods": [{"food": "菠菜", "reason": "草酸影响钙吸收", "severity": "轻微"}]
        },
        {
            "name": "豆皮",
            "category": "豆制品类",
            "nutrients": {
                "energy": {"value": 409, "unit": "kcal/100g"},
                "protein": {"value": 44.6, "unit": "g/100g"},
                "calcium": {"value": 116, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "50-80g/天"},
            "health_benefits": ["高蛋白", "补钙", "预防骨质疏松"],
            "contraindications": ["痛风患者少食", "胃肠虚弱者适量"],
            "incompatible_foods": []
        },
        {
            "name": "腐竹",
            "category": "豆制品类",
            "nutrients": {
                "energy": {"value": 459, "unit": "kcal/100g"},
                "protein": {"value": 44.6, "unit": "g/100g"},
                "fat": {"value": 21.7, "unit": "g/100g"}
            },
            "recommended_intake": {"adult": "30-50g/天（干品）"},
            "health_benefits": ["高蛋白", "预防老年痴呆", "降血脂"],
            "contraindications": ["痛风患者少食", "肾病患者控制量"],
            "incompatible_foods": []
        },
        {
            "name": "豆干",
            "category": "豆制品类",
            "nutrients": {
                "energy": {"value": 140, "unit": "kcal/100g"},
                "protein": {"value": 16.2, "unit": "g/100g"},
                "calcium": {"value": 318, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "50-80g/天"},
            "health_benefits": ["高钙", "高蛋白", "低脂肪", "预防骨质疏松"],
            "contraindications": ["痛风患者控制量", "含盐量高需控制"],
            "incompatible_foods": []
        },
        {
            "name": "豆浆粉",
            "category": "豆制品类",
            "nutrients": {
                "energy": {"value": 422, "unit": "kcal/100g"},
                "protein": {"value": 25, "unit": "g/100g"},
                "大豆异黄酮": {"value": "丰富", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "20-30g/天（冲泡用）"},
            "health_benefits": ["补充植物蛋白", "降胆固醇", "调节内分泌", "方便快捷"],
            "contraindications": ["痛风患者少饮", "需冲泡熟透"],
            "incompatible_foods": [{"food": "鸡蛋", "reason": "影响吸收", "severity": "轻微"}]
        },
        # 菌菇类
        {
            "name": "香菇",
            "category": "菌菇类",
            "nutrients": {
                "energy": {"value": 19, "unit": "kcal/100g"},
                "protein": {"value": 2.2, "unit": "g/100g"},
                "香菇多糖": {"value": "丰富", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "50-100g/天（鲜品）"},
            "health_benefits": ["提高免疫力", "抗肿瘤", "降血脂", "补充维生素D"],
            "contraindications": ["痛风急性期慎食", "脾胃虚寒少食"],
            "incompatible_foods": []
        },
        {
            "name": "黑木耳",
            "category": "菌菇类",
            "nutrients": {
                "energy": {"value": 27, "unit": "kcal/100g"},
                "iron": {"value": 97.4, "unit": "mg/100g（干品）"},
                "fiber": {"value": 29.9, "unit": "g/100g（干品）"}
            },
            "recommended_intake": {"adult": "10-15g/天（干品）"},
            "health_benefits": ["补铁补血", "清肺", "润肠通便", "降血脂"],
            "contraindications": ["需充分泡发", "孕妇适量", "出血性疾病慎食"],
            "incompatible_foods": [{"food": "田螺", "reason": "不易消化", "severity": "中等"}]
        },
        {
            "name": "银耳",
            "category": "菌菇类",
            "nutrients": {
                "energy": {"value": 200, "unit": "kcal/100g（干品）"},
                "protein": {"value": 10, "unit": "g/100g"},
                "银耳多糖": {"value": "丰富", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "10-15g/天（干品）"},
            "health_benefits": ["滋阴润肺", "美容养颜", "提高免疫力", "润肠通便"],
            "contraindications": ["需充分煮熟", "隔夜银耳不宜食用", "外感风寒者慎食"],
            "incompatible_foods": []
        },
        {
            "name": "平菇",
            "category": "菌菇类",
            "nutrients": {
                "energy": {"value": 20, "unit": "kcal/100g"},
                "protein": {"value": 2.0, "unit": "g/100g"},
                "氨基酸": {"value": "齐全", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "100-150g/天"},
            "health_benefits": ["增强免疫", "降血压", "抗肿瘤", "舒筋活血"],
            "contraindications": ["痛风患者控制量"],
            "incompatible_foods": []
        },
        {
            "name": "金针菇",
            "category": "菌菇类",
            "nutrients": {
                "energy": {"value": 26, "unit": "kcal/100g"},
                "protein": {"value": 2.4, "unit": "g/100g"},
                "赖氨酸": {"value": "丰富", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "80-120g/天"},
            "health_benefits": ["益智健脑", "促进儿童发育", "抗疲劳", "降血脂"],
            "contraindications": ["脾胃虚寒者少食", "必须煮熟"],
            "incompatible_foods": []
        },
        # 中药食材类
        {
            "name": "枸杞",
            "category": "中药食材",
            "nutrients": {
                "energy": {"value": 258, "unit": "kcal/100g"},
                "胡萝卜素": {"value": 3100, "unit": "μg/100g"},
                "枸杞多糖": {"value": "丰富", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "10-20g/天"},
            "health_benefits": ["明目", "养肝", "补肾", "抗衰老", "提高免疫"],
            "contraindications": ["感冒发烧不宜", "腹泻者慎食", "高血压未控制者慎食"],
            "incompatible_foods": [{"food": "绿茶", "reason": "影响吸收", "severity": "轻微"}]
        },
        {
            "name": "红枣",
            "category": "中药食材",
            "nutrients": {
                "energy": {"value": 264, "unit": "kcal/100g（干品）"},
                "vitamin_c": {"value": 243, "unit": "mg/100g（鲜品）"},
                "铁": {"value": 3.7, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "3-5颗/天"},
            "health_benefits": ["补血", "养颜", "健脾胃", "安神", "提高免疫"],
            "contraindications": ["糖尿病患者控制量", "湿热体质少食", "多食易胀气"],
            "incompatible_foods": [{"food": "葱", "reason": "影响消化", "severity": "轻微"}]
        },
        {
            "name": "山药",
            "category": "中药食材",
            "nutrients": {
                "energy": {"value": 56, "unit": "kcal/100g"},
                "淀粉": {"value": 11.7, "unit": "g/100g"},
                "黏液蛋白": {"value": "丰富", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "100-200g/天"},
            "health_benefits": ["健脾养胃", "补肾益精", "降血糖", "益肺止咳"],
            "contraindications": ["便秘者少食", "前列腺癌、乳腺癌患者慎食"],
            "incompatible_foods": [{"food": "碱性食物/药物", "reason": "破坏营养", "severity": "轻微"}]
        },
        {
            "name": "百合",
            "category": "中药食材",
            "nutrients": {
                "energy": {"value": 162, "unit": "kcal/100g（干品）"},
                "protein": {"value": 3.2, "unit": "g/100g"},
                "秋水仙碱": {"value": "微量", "unit": "N/A"}
            },
            "recommended_intake": {"adult": "20-30g/天（干品）"},
            "health_benefits": ["润肺止咳", "清心安神", "美容养颜", "抗疲劳"],
            "contraindications": ["风寒咳嗽不宜", "脾胃虚寒者慎食", "鲜百合需煮熟"],
            "incompatible_foods": [{"food": "羊肉", "reason": "腹泻", "severity": "中等"}]
        },
        {
            "name": "莲子",
            "category": "中药食材",
            "nutrients": {
                "energy": {"value": 344, "unit": "kcal/100g（干品）"},
                "protein": {"value": 17.2, "unit": "g/100g"},
                "钾": {"value": 846, "unit": "mg/100g"}
            },
            "recommended_intake": {"adult": "20-30g/天（干品）"},
            "health_benefits": ["养心安神", "健脾止泻", "补肾固精", "清热降火（莲心）"],
            "contraindications": ["便秘者少食", "腹胀者慎食"],
            "incompatible_foods": [{"food": "牛奶", "reason": "影响吸收", "severity": "轻微"}]
        }
    ]

    results = []
    for food in new_foods:
        entry = {
            "material_id": generate_id(food["name"], food["category"]),
            "category": food["category"],
            "data": food,
            "source": "第十一轮数据扩充-肉类坚果豆制品菌菇中药",
            "last_updated": datetime.now().isoformat(),
            "version": "11.0"
        }
        results.append(entry)
    return results

def main():
    base_dir = r"D:\Users\86198\WeChatProjects\数据库\processed"

    print("\n" + "="*60)
    print("第十一轮数据扩充开始 - 肉类、坚果、豆制品、菌菇、中药食材")
    print("="*60)

    # 扩充食物数据
    print("\n扩充食物数据库...")
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

    # 统计各类别
    categories = {}
    for item in all_food:
        cat = item.get('category') or item.get('data', {}).get('category', '未分类')
        categories[cat] = categories.get(cat, 0) + 1

    print("\n各类别统计:")
    for cat, count in sorted(categories.items()):
        print(f"   {cat}: {count}条")

    # 总结
    print("\n" + "="*60)
    print("第十一轮数据扩充完成!")
    print("="*60)
    print(f"食物数据总数: {len(all_food)} 条 (+{len(new_food)})")
    print("\n新增食物类别:")
    print("  - 肉类 (5种): 牛肉、羊肉、猪肉、鸡肉、鸭肉")
    print("  - 坚果类 (5种): 核桃、杏仁、腰果、开心果、夏威夷果")
    print("  - 豆制品类 (5种): 豆腐、豆皮、腐竹、豆干、豆浆粉")
    print("  - 菌菇类 (5种): 香菇、黑木耳、银耳、平菇、金针菇")
    print("  - 中药食材 (5种): 枸杞、红枣、山药、百合、莲子")
    print("="*60)

if __name__ == "__main__":
    main()
