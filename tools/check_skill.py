"""AAA-prompt-felix 自检：python tools/check_skill.py"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
REFS = ROOT / "references"

BAD_TERMS = {
    "三视图资产": "应改为「四格设定图资产」",
    "出角色三视图": "应改为「出角色四格设定图」",
    "基础质量卡 3 张": "look-library 实际是 6 张",
    "AAAskill测试": "具体项目名不该写进 skill",
    "AAA_35秒": "具体项目名不该写进 skill",
    "按六步": "应为「第一步的六项」",
    "按以下 8 步": "应为「5.0–5.9 十个环节」",
    "定稿进 `确认`": "应为「定稿直接放分类根下」",
}

REQUIRED = [
    "## 执行纪律",
    "### 第1站",
    "### 第2站",
    "### 第3站",
    "### 第4站",
    "### 第5站",
    "### 第5.5站",
    "### 第6站",
    "## 硬性约束",
]


def main() -> int:
    problems: list[str] = []
    text = SKILL.read_text(encoding="utf-8")
    ref_files = sorted(p.name for p in REFS.iterdir() if p.is_file())

    # 1. 死链：SKILL 里引用的文件必须存在
    cited = set(re.findall(r"references/([\w\-.]+\.(?:md|html))", text))
    for name in sorted(cited):
        if name not in ref_files:
            problems.append(f"死链：references/{name} 不存在")

    # 2. 漏登记：references 下的文件必须出现在总表
    listed = set(
        re.findall(r"^\| `(?:references/)?([\w\-.]+\.(?:md|html))`", text, re.M)
    )
    for name in ref_files:
        if name not in listed:
            problems.append(f"漏登记：references/{name} 未进总表")

    # 3. 失效术语
    for path in [SKILL, *sorted(REFS.glob("*.md"))]:
        body = path.read_text(encoding="utf-8")
        for term, why in BAD_TERMS.items():
            if term in body:
                problems.append(f"{path.name}：出现「{term}」——{why}")

    # 4. 三类资产模板不得跨类用词
    at = (REFS / "asset-templates.md").read_text(encoding="utf-8")

    def section(start: str, end: str) -> str:
        i = at.index(start)
        j = at.index(end, i)
        return at[i:j]

    prop = section("## 2. 道具模板", "## 3. 场景模板")
    scene = section("## 3. 场景模板", "## 3b.")
    char = section("## 1. 角色设定图模板", "## 2. 道具模板")
    for word in ("面部特写", "无头版"):
        if word in prop:
            problems.append(f"asset-templates 道具节出现角色用词「{word}」")
    if "面部特写" in scene:
        problems.append("asset-templates 场景节出现角色用词「面部特写」")
    if "五联" in char:
        problems.append("asset-templates 角色节出现道具用词「五联」")

    # 5. 结构完整性
    for marker in REQUIRED:
        if marker not in text:
            problems.append(f"缺少结构：{marker}")

    # 6. 总表行数与文件数一致
    if len(listed) != len(ref_files):
        problems.append(f"总表 {len(listed)} 行，references 实际 {len(ref_files)} 个文件")

    log = ROOT / "tools" / "_check.log"
    if problems:
        log.write_text(
            f"未通过，共 {len(problems)} 条：\n"
            + "\n".join(f"  - {p}" for p in problems)
            + "\n",
            encoding="utf-8",
        )
        print(f"FAIL {len(problems)}  (see tools/_check.log)")
        return 1

    log.write_text(
        f"全部通过：{len(ref_files)} 个参考文件，结构 {len(REQUIRED)} 项齐全。\n",
        encoding="utf-8",
    )
    print(f"PASS  files={len(ref_files)}  sections={len(REQUIRED)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
