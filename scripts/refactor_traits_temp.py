src = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\traits\10_정신.md"
dst = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\traits\17_관계.md"

print(f"Reading from {src}")
with open(src, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Header update for 10_정신.md
# Line 1 (Index 0)
lines[0] = "# 10. 정신 (Mind & Spirit)\n"
# Line 3 (Index 2)
lines[2] = (
    "> **설명:** 존재의 자아, 의지력, 감정 상태, 신념, 트라우마 등 **내면의 정신세계(OS)**를 포괄하는 트레잇입니다.\n"
)

# Extract Relationship traits
# Line 204 (Index 203) to Line 299 (Index 298)
start_idx = 203
end_idx = 299

# Verify boundaries
print(f"Check Line 204 (Index 203): {lines[start_idx].strip()}")
print(f"Check Line 299 (Index 298): {lines[end_idx - 1].strip()}")
print(f"Check Line 300 (Index 299): {lines[end_idx].strip()}")

relation_traits = lines[start_idx:end_idx]
remaining_traits = lines[:start_idx] + lines[end_idx:]

# Write 17_관계.md
header_rela = [
    "# 17. 관계 (Relationships)\n",
    "\n",
    "> **설명:** 타인, 집단, 사회와의 상호작용(Interactions), 애정, 증오, 정치, 계급 등 **관계성(Relational/Social)**에 기반한 트레잇입니다.\n",
    "\n",
    "## 트레잇 목록\n",
    "\n",
    "| 키워드 | 하위 분류 | 설명 |\n",
    "| :--- | :---: | :--- |\n",
]

print(f"Writing to {dst}")
with open(dst, "w", encoding="utf-8") as f:
    f.writelines(header_rela + relation_traits)

print(f"Writing back to {src}")
with open(src, "w", encoding="utf-8") as f:
    f.writelines(remaining_traits)

print("Refactoring Done")
