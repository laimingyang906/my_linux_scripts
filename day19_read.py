file_path = "/root/my_scripts/check_disk.sh"

with open(file_path, 'r', encoding='utf-8') as f:
	lines = f.readlines()

print(f"这个文件一共有{len(lines)}行")
keyword = "echo"
print(f"包含'{keyword}'的行有：")
for line in lines:
	if keyword in line:
		print(line.strip())
