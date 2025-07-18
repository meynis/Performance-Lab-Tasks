import sys
import json

def fill_test_values(tests_structure, values_dict):
    """
    Рекурсивно заполняет структуру тестов значениями из values_dict
    """
    if isinstance(tests_structure, dict):
        if 'id' in tests_structure:
            test_id = tests_structure['id']
            if test_id in values_dict:
                tests_structure['value'] = values_dict[test_id]
        
        for key, value in tests_structure.items():
            if key == 'values' and isinstance(value, list):
                for item in value:
                    fill_test_values(item, values_dict)
            elif isinstance(value, (dict, list)):
                fill_test_values(value, values_dict)
    
    elif isinstance(tests_structure, list):
        for item in tests_structure:
            fill_test_values(item, values_dict)

def main():
    if len(sys.argv) != 4:
        print("Использование: python task3.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    
    with open(values_file, 'r', encoding='utf-8') as f:
        values_data = json.load(f)
    
    values_dict = {}
    for item in values_data['values']:
        values_dict[item['id']] = item['value']
    
    with open(tests_file, 'r', encoding='utf-8') as f:
        tests_data = json.load(f)
    
    fill_test_values(tests_data, values_dict)
    
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(tests_data, f, indent=2, ensure_ascii=False)
    
    print(f"Отчет сохранен в {report_file}")

if __name__ == "__main__":
    main()