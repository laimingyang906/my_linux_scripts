file_path = "/var/log/nginx/access.log"
with open (file_path, 'r', encoding='utf-8') as f:
	lines = f.readlines()

keyword = "Mozilla"
print(f"包含{keyword}的行有：")
for line in lines:
	if keyword in line:
		print(line.strip())
