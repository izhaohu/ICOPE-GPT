import os
import json


def merge_json_files(dir_path, output_file):
    data = []
    for filename in os.listdir(dir_path):
        if filename.endswith(".json"):
            full_path = os.path.join(dir_path, filename)
            with open(full_path, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
                data.extend(file_data)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

    print(f'Total data count in the merged JSON file: {len(data)}')


if __name__ == "__main__":
    dir_path = "/opt/caregpt/text_tool/output_json/AD相关知识库"
    output_file = "/opt/caregpt/text_tool/merged_output_ad.json"
    merge_json_files(dir_path, output_file)
