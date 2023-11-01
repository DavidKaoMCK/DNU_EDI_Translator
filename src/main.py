from PMD_EDI_TOOL.src.edi_parsed import parse_edi_file

# 调用解析器来解析 EDI 文件
edi_file_path = 'C:\Davidlocal\PMD_EDI_TOOL\sample_edi.edi'  # 替换成你的 EDI 文件路径
parsed_edi = parse_edi_file(edi_file_path)

if parsed_edi:
    # 打印解析后的 EDI 数据
    print(parsed_edi)
else:
    print("Failed to parse the EDI file.")
