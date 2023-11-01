# -*- coding: utf-8 -*-


import badx12

def parse_edi_file(file_path):
    try:
        # 使用 badX12 解析 EDI 文件
        edi_object = badx12.parse_file(file_path)
        
        # 返回解析后的数据
        return edi_object
    
    except Exception as e:
        # 如果解析出现错误，捕获异常并打印错误信息
        print("An error occurred while parsing the EDI file:", str(e))
        return None

# 示例用法
if __name__ == "__main__":
    edi_file_path = "C:\\Davidlocal\\PMD_EDI_TOOL\\data\\input\\sample_edi.edi"
    parsed_edi = parse_edi_file(edi_file_path)
    if parsed_edi:
        print("Successfully parsed EDI file:")
        print(parsed_edi)
