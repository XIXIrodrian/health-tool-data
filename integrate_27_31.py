import json, os

bd = 'processed'
batches = [27, 28, 29, 30, 31]

furn_file = os.path.join(bd, 'furniture.json')
text_file = os.path.join(bd, 'textile.json')

ef = json.load(open(furn_file, 'r', encoding='utf-8'))
et = json.load(open(text_file, 'r', encoding='utf-8'))

print(f'初始: 建材{len(ef)} 纺织{len(et)}')

for b in batches:
    d = json.load(open(f'fetched_real_data_batch{b}.json', 'r', encoding='utf-8'))
    f = [i for i in d if i['category'] != '衣料纺织品']
    t = [i for i in d if i['category'] == '衣料纺织品']
    ef.extend(f)
    et.extend(t)
    print(f'批次{b}: +{len(d)} (建材+{len(f)} 纺织+{len(t)})')

json.dump(ef, open(furn_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(et, open(text_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

food = len(json.load(open(os.path.join(bd, 'food.json'), 'r', encoding='utf-8')))
print(f'\n最终: {food + len(ef) + len(et)} (食物{food} 建材{len(ef)} 纺织{len(et)})')
