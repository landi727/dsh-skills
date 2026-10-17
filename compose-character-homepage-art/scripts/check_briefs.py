#!/usr/bin/env python3
"""Check plan metadata only; generated pixels still require visual QA."""
import json
import sys
from itertools import combinations
from pathlib import Path

def check(data):
    problems = []
    items = data.get('concepts', [])
    if len(items) != data.get('expected_count'):
        problems.append('方案数与 expected_count 不符')
    ids = [str(c.get('id', '')) for c in items]
    if any(not i for i in ids) or len(set(ids)) != len(ids):
        problems.append('ID 缺失或重复')
    fields = ('silhouette', 'whitespace', 'cast_layout', 'spatial_relation', 'primary_object')
    for c in items:
        label = str(c.get('id', '?'))
        for field in fields:
            if not c.get(field):
                problems.append(f'{label}: 缺少 {field}')
        rect = c.get('blank_rect', [])
        if len(rect) != 4 or not all(isinstance(v, (int, float)) for v in rect):
            problems.append(f'{label}: blank_rect 需为四个数值')
        else:
            x, y, w, h = rect
            if min(x, y) < 0 or min(w, h) <= 0 or x+w > 1 or y+h > 1 or w*h < .20:
                problems.append(f'{label}: 留白太小或超出画幅')
        if not 3 <= len(c.get('objects', [])) <= 5:
            problems.append(f'{label}: 环境物件/组应为 3–5 个')
        if data.get('profile') == 'neutral-flat':
            try:
                color = c['background'].lstrip('#')
                if len(color) != 6:
                    raise ValueError()
                rgb = [int(color[i:i+2], 16) for i in (0, 2, 4)]
                if max(rgb)-min(rgb) > 12:
                    problems.append(f'{label}: 大面积基底偏离中性')
            except (KeyError, TypeError, ValueError, AttributeError):
                problems.append(f'{label}: background 需为 #RRGGBB')
            if not .38 <= c.get('body_height', 0) <= .48:
                problems.append(f'{label}: 主身高超出约定')
            ratios = c.get('ratios', [])
            if len(ratios) != 3 or any(not isinstance(a, (int, float)) or abs(a-b) > .04 for a, b in zip(ratios, (1, .88, .98))):
                problems.append(f'{label}: 三宠比例超出约定')
    for a, b in combinations(items, 2):
        if sum(a.get(f) != b.get(f) for f in fields) < 3:
            problems.append(f'{a.get("id")}/{b.get("id")}: 不足三项构图差异')
    return problems

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('用法: check_briefs.py briefs.json')
    try:
        problems = check(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8')))
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
        sys.exit(f'读取失败: {exc}')
    for problem in problems:
        print('FAIL:', problem)
    if problems:
        sys.exit(1)
    print('PASS: 规格关口通过；仍需逐张查看实际生成图。')
