# scripts/validate.py
import yaml, sys

nodes = yaml.safe_load(open("graph/nodes.yaml"))["nodes"]
edges = yaml.safe_load(open("graph/edges.yaml"))["edges"]

node_ids = {n["id"] for n in nodes}
stage_index = {n["id"]: {s["name"] for s in n["stages"]} for n in nodes}
errors = []

# 1. ID 唯一
if len(node_ids) != len(nodes):
    errors.append("节点 ID 有重复")

# 2. 前置引用存在
for n in nodes:
    for p in n.get("prerequisites", []):
        if p["node"] not in node_ids:
            errors.append(f"{n['id']} 的前置 {p['node']} 不存在")

# 3. 边引用存在 + 环节名存在
for e in edges:
    if e["from"] not in node_ids or e["to"] not in node_ids:
        errors.append(f"边 {e['id']} 引用了不存在的节点")
        continue
    target_node, target_stage = e["consumed_at"].split(" / ", 1)
    if target_node != e["to"]:
        errors.append(f"边 {e['id']} 的 consumed_at 节点与 to 不一致")
    if target_stage not in stage_index[e["to"]]:
        errors.append(f"边 {e['id']} 的消费环节 '{target_stage}' 不在 {e['to']} 的 stages 中")

# 4. 共享节点恰好 2 个
shared = [n["id"] for n in nodes if n.get("shared")]
if sorted(shared) != ["A2", "S1"]:
    errors.append(f"共享节点应为 A2/S1，实际为 {shared}")

if errors:
    print("FAIL")
    [print(" -", e) for e in errors]
    sys.exit(1)
print(f"OK: {len(nodes)} nodes, {len(edges)} edges, shared={shared}")
