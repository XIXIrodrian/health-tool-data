import json, os
base_dir = 'processed'
fetched = json.load(open('fetched_real_data_batch18.json', 'r', encoding='utf-8'))
furn = [i for i in fetched if i['category'] != '衣料纺织品']
text = [i for i in fetched if i['category'] == '衣料纺织品']
furn_file = os.path.join(base_dir, 'furniture.json')
text_file = os.path.join(base_dir, 'textile.json')
exist_f = json.load(open(furn_file, 'r', encoding='utf-8'))
exist_t = json.load(open(text_file, 'r', encoding='utf-8'))
all_f = exist_f + furn
all_t = exist_t + text
json.dump(all_f, open(furn_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(all_t, open(text_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'建材: {len(exist_f)}->{len(all_f)} (+{len(furn)})')
print(f'纺织: {len(exist_t)}->{len(all_t)} (+{len(text)})')
print(f'总计: {len(exist_f)+len(exist_t)}->{len(all_f)+len(all_t)} (+{len(fetched)})')
