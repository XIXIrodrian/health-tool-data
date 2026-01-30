import json, os, glob

base_dir = 'processed'
for batch_file in sorted(glob.glob('fetched_real_data_batch*.json')):
    print(f'整合 {batch_file}...')
    data = json.load(open(batch_file, 'r', encoding='utf-8'))
    furn = [i for i in data if i['category'] != '衣料纺织品']
    text = [i for i in data if i['category'] == '衣料纺织品']

    if furn:
        furn_file = os.path.join(base_dir, 'furniture.json')
        existing = json.load(open(furn_file, 'r', encoding='utf-8'))
        json.dump(existing + furn, open(furn_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print(f'  建材: {len(existing)} + {len(furn)} = {len(existing)+len(furn)}')

    if text:
        text_file = os.path.join(base_dir, 'textile.json')
        existing = json.load(open(text_file, 'r', encoding='utf-8'))
        json.dump(existing + text, open(text_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print(f'  纺织: {len(existing)} + {len(text)} = {len(existing)+len(text)}')

food_count = len(json.load(open(os.path.join(base_dir, 'food.json'), 'r', encoding='utf-8')))
furn_count = len(json.load(open(os.path.join(base_dir, 'furniture.json'), 'r', encoding='utf-8')))
text_count = len(json.load(open(os.path.join(base_dir, 'textile.json'), 'r', encoding='utf-8')))
print(f'\n总计: {food_count + furn_count + text_count} (食物{food_count} 建材{furn_count} 纺织{text_count})')
