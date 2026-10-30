"""Vẽ Use Case Diagram (chuẩn UML) cho ReLoop dưới dạng SVG.

Chạy: python docs/usecase/build_usecase_diagrams.py
Kết quả: docs/usecase/ucd-*.svg — nhúng vào README và docs/03-use-cases.md.

Mỗi sơ đồ: tác nhân chính đứng ngoài khung, phía trên; các nhóm use case (theo phân hệ) chia
hai cột, đường nối đi trong hành lang giữa nên không cắt qua elip. Quan hệ <<include>> / <<extend>> vẽ bằng mũi tên nét đứt.
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent

# ---------------------------------------------------------------- dữ liệu
G_AUTH = ("M1 Xác thực", ["UC01 Đăng nhập", "UC02 Đăng xuất", "UC03 Quên mật khẩu",
                          "UC04 Kích hoạt tài khoản", "UC05 Hồ sơ cá nhân"])
G_DASH = ("M8 Dashboard", ["UC06 Xem dashboard"])


def diagrams():
    return {
        "ucd-owner": {
            "title": "Use Case — Chủ shop (OWNER)",
            "actor": "Chủ shop",
            "left": [
                ("M1 Xác thực", ["UC01 Đăng nhập", "UC02 Đăng xuất", "UC03 Quên mật khẩu",
                                 "UC05 Hồ sơ cá nhân"]),
                ("M2 Người ký gửi", ["UC07 Quản lý người ký gửi", "UC08 Mời vào cổng"]),
                ("M3 Nhận hàng", ["UC09 Tạo phiếu nhận hàng", "UC10 AI nhận diện ảnh",
                                  "UC11 AI gợi ý giá", "UC12 Xác nhận phiếu tại quầy",
                                  "UC13 In tem QR"]),
            ],
            "right": [
                ("M4–M5 Kho & Bán hàng", ["UC14 Xem kho hàng", "UC15 Điều chỉnh giá",
                                          "UC17 Yêu cầu giảm dưới sàn", "UC19 Xử lý hàng hết hạn",
                                          "UC20 Báo thất lạc / hư hỏng", "UC21 AI viết caption",
                                          "UC22 Bán hàng POS", "UC23 Đổi trả"]),
                ("M6 Đối soát & Chi trả", ["UC24 Xem số dư người gửi", "UC26 Duyệt & chi trả VietQR",
                                           "UC27 Xuất sao kê PDF"]),
                ("M8–M9 Báo cáo & Quản trị", ["UC06 Xem dashboard", "UC30 Báo cáo & Excel",
                                              "UC31 Quản lý nhân viên", "UC32 Cấu hình shop",
                                              "UC33 Nhật ký hoạt động", "UC34 Nhận thông báo"]),
            ],
            "relations": [("UC10", "UC09", "extend"), ("UC11", "UC09", "extend")],
        },
        "ucd-staff": {
            "title": "Use Case — Nhân viên (STAFF)",
            "actor": "Nhân viên",
            "left": [
                G_AUTH,
                ("M2 Người ký gửi", ["UC07 Tạo & xem người ký gửi", "UC08 Mời vào cổng"]),
            ],
            "right": [
                ("M3 Nhận hàng", ["UC09 Tạo phiếu nhận hàng", "UC10 AI nhận diện ảnh",
                                  "UC11 AI đề xuất giá", "UC13 In tem QR"]),
                ("M4–M5 Kho & Bán hàng", ["UC14 Xem kho hàng", "UC19 Xử lý hàng hết hạn",
                                          "UC21 AI viết caption", "UC22 Bán hàng POS",
                                          "UC23 Đổi trả trong hạn"]),
                ("M8–M9", ["UC06 Dashboard ca bán", "UC34 Nhận thông báo"]),
            ],
            "relations": [("UC10", "UC09", "extend"), ("UC11", "UC09", "extend")],
        },
        "ucd-consignor": {
            "title": "Use Case — Người ký gửi (CONSIGNOR)",
            "actor": "Người ký gửi",
            "left": [
                G_AUTH,
                ("M8 Tổng quan", ["UC06 Dashboard cá nhân", "UC34 Nhận thông báo"]),
            ],
            "right": [
                ("M7 Hàng & Phê duyệt", ["UC29 Xem hàng của tôi", "UC12 Xác nhận phiếu nhận hàng",
                                         "UC18 Duyệt / từ chối giảm giá"]),
                ("M6 Ví & Chi trả", ["UC24 Xem số dư & lịch sử", "UC25 Yêu cầu rút tiền",
                                     "UC27 Xuất sao kê PDF"]),
            ],
            "relations": [],
        },
        "ucd-system": {
            "title": "Use Case — Tác nhân hệ thống (SYSTEM, AI)",
            "actor": "Scheduler",
            "actor_kind": "system",
            "left": [
                ("Job hằng ngày", ["UC16 Giảm giá tự động", "UC19 Cảnh báo & đánh dấu hết hạn",
                                   "UC28 Giải phóng tiền tạm giữ"]),
            ],
            "right": [
                ("Claude API", ["UC10 AI nhận diện ảnh", "UC11 AI gợi ý giá", "UC21 AI viết caption"]),
            ],
            "right_actor": "Claude API",
            "relations": [],
        },
    }


# ---------------------------------------------------------------- bố cục
EW, EH = 250, 44          # kích thước elip
ROW = 56                  # khoảng cách dọc giữa các elip
G_HEAD, G_PAD, G_GAP = 30, 14, 22
COL_GAP = 300             # hành lang giữa hai cột, nơi đi các đường nối
ACTOR_H = 140             # khoảng phía trên khung dành cho tác nhân
MARGIN, TITLE_H = 30, 56
FONT = "Segoe UI, Roboto, Helvetica, Arial, sans-serif"

C = {
    "bg": "#ffffff", "text": "#1f2937", "muted": "#6b7280",
    "boundary": "#1168bd", "boundary_bg": "#f5f9ff",
    "group": "#94a3b8", "group_bg": "#ffffff",
    "ell": "#e8f1fb", "ell_stroke": "#1168bd", "ai": "#f3ecfd", "ai_stroke": "#7a4fbf",
    "line": "#475569", "rel": "#7a4fbf",
}


def layout_column(groups, x, y0):
    """Trả về danh sách hộp nhóm và vị trí từng elip trong một cột."""
    boxes, ells, y = [], {}, y0
    for title, ucs in groups:
        h = G_HEAD + len(ucs) * ROW + G_PAD - (ROW - EH)
        boxes.append((x, y, EW + 2 * G_PAD, h, title))
        for i, uc in enumerate(ucs):
            cx = x + G_PAD + EW / 2
            cy = y + G_HEAD + i * ROW + EH / 2
            ells[uc.split()[0]] = (cx, cy, uc)
        y += h + G_GAP
    return boxes, ells, y - G_GAP


def wrap(label, width=30):
    words, lines, cur = label.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    lines.append(cur)
    return lines


def stick_figure(x, y, name):
    """Người que UML; (x, y) là đỉnh đầu."""
    s = C["text"]
    return (f'<g stroke="{s}" stroke-width="2" fill="none">'
            f'<circle cx="{x}" cy="{y + 12}" r="12" fill="#fff"/>'
            f'<line x1="{x}" y1="{y + 24}" x2="{x}" y2="{y + 60}"/>'
            f'<line x1="{x - 22}" y1="{y + 36}" x2="{x + 22}" y2="{y + 36}"/>'
            f'<line x1="{x}" y1="{y + 60}" x2="{x - 18}" y2="{y + 88}"/>'
            f'<line x1="{x}" y1="{y + 60}" x2="{x + 18}" y2="{y + 88}"/></g>'
            f'<text x="{x}" y="{y + 110}" text-anchor="middle" font-weight="600" '
            f'font-size="15" fill="{s}">{escape(name)}</text>')


def system_actor(x, y, name, stereo="system"):
    """Tác nhân hệ thống: hộp có stereotype."""
    w, h = 130, 64
    return (f'<rect x="{x - w / 2}" y="{y}" width="{w}" height="{h}" rx="6" fill="#fff" '
            f'stroke="{C["text"]}" stroke-width="2"/>'
            f'<text x="{x}" y="{y + 24}" text-anchor="middle" font-size="12" fill="{C["muted"]}">'
            f'&#171;{stereo}&#187;</text>'
            f'<text x="{x}" y="{y + 46}" text-anchor="middle" font-size="15" font-weight="600" '
            f'fill="{C["text"]}">{escape(name)}</text>')


def render(key, d):
    gw = EW + 2 * G_PAD
    bx = MARGIN
    lx = bx + 100
    rx = lx + gw + COL_GAP
    bt = TITLE_H + MARGIN + ACTOR_H          # mép trên khung hệ thống
    top = bt + 34
    lboxes, lells, lbottom = layout_column(d["left"], lx, top)
    rboxes, rells, rbottom = layout_column(d["right"], rx, top)
    bottom = max(lbottom, rbottom) + 20
    bw = rx + gw + 100 - bx
    W = bw + 2 * MARGIN
    extra_right = 0
    if d.get("right_actor"):
        extra_right = 180
        W += extra_right
    H = bottom + MARGIN

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}" font-family="{FONT}">',
           f'<rect width="{W}" height="{H}" fill="{C["bg"]}"/>',
           f'<text x="{W / 2}" y="{MARGIN + 18}" text-anchor="middle" font-size="20" '
           f'font-weight="700" fill="{C["text"]}">{escape(d["title"])}</text>']

    # khung hệ thống
    out.append(f'<rect x="{bx}" y="{bt}" width="{bw}" height="{bottom - bt}" '
               f'rx="10" fill="{C["boundary_bg"]}" stroke="{C["boundary"]}" stroke-width="2"/>')
    out.append(f'<text x="{bx + 16}" y="{bt + 24}" font-size="15" font-weight="700" '
               f'fill="{C["boundary"]}">ReLoop — System Boundary</text>')

    # tác nhân chính: ngoài khung, phía trên hành lang giữa hai cột
    ax = lx + gw + COL_GAP / 2
    ay = TITLE_H + MARGIN
    ai_ucs = {"UC10", "UC11", "UC21"}
    lines, shapes = [], []

    if d.get("actor_kind") == "system":
        out_actor = system_actor(ax, ay + 20, d["actor"])
        hand_l = hand_r = (ax, ay + 84)
    else:
        out_actor = stick_figure(ax, ay, d["actor"])
        hand_l = hand_r = (ax, ay + 120)

    for boxes in (lboxes, rboxes):
        for x, y, w, h, title in boxes:
            shapes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{C["group_bg"]}" '
                          f'stroke="{C["group"]}" stroke-dasharray="5 4"/>'
                          f'<text x="{x + 10}" y="{y + 19}" font-size="12" font-weight="600" '
                          f'fill="{C["muted"]}">{escape(title)}</text>')

    def ellipse(cx, cy, label, ai):
        fill, stroke = (C["ai"], C["ai_stroke"]) if ai else (C["ell"], C["ell_stroke"])
        parts = wrap(label)
        t = "".join(f'<tspan x="{cx}" dy="{0 if i == 0 else 15}">{escape(p)}</tspan>'
                    for i, p in enumerate(parts))
        ty = cy + 5 - (len(parts) - 1) * 7.5
        return (f'<ellipse cx="{cx}" cy="{cy}" rx="{EW / 2}" ry="{EH / 2}" fill="{fill}" '
                f'stroke="{stroke}" stroke-width="1.5"/>'
                f'<text x="{cx}" y="{ty}" text-anchor="middle" font-size="13" fill="{C["text"]}">{t}</text>')

    is_system = d.get("actor_kind") == "system"
    for ells, side in ((lells, "L"), (rells, "R")):
        for uid, (cx, cy, label) in ells.items():
            ai = uid in ai_ucs
            shapes.append(ellipse(cx, cy, label, ai))
            if is_system and side == "R":
                continue  # nối với tác nhân AI bên phải
            if side == "L":
                lines.append((hand_l, (cx + EW / 2, cy)))
            else:
                lines.append((hand_r, (cx - EW / 2, cy)))

    for (x1, y1), (x2, y2) in lines:
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{C["line"]}" stroke-width="1.2"/>')
    out.extend(shapes)

    # quan hệ include / extend (cùng một cột, vẽ cung ở mép ngoài)
    ells_all = {**lells, **rells}
    out.append(f'<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" '
               f'markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10" fill="none" '
               f'stroke="{C["rel"]}" stroke-width="1.5"/></marker></defs>')
    for i, (src, dst, kind) in enumerate(d["relations"]):
        sx, sy, _ = ells_all[src]
        dx, dy, _ = ells_all[dst]
        outer = 1 if src in rells else -1
        ex = sx + outer * EW / 2
        tx = dx + outer * EW / 2
        bulge = ex + outer * (34 + 26 * i)
        out.append(f'<path d="M{ex},{sy} C{bulge},{sy} {bulge},{dy} {tx},{dy}" fill="none" '
                   f'stroke="{C["rel"]}" stroke-width="1.4" stroke-dasharray="6 4" marker-end="url(#arr)"/>')
        lab_x = bulge + outer * 4
        out.append(f'<text x="{lab_x}" y="{(sy + dy) / 2 + 4}" font-size="11" fill="{C["rel"]}" '
                   f'text-anchor="{"start" if outer > 0 else "end"}">&#171;{kind}&#187;</text>')

    out.append(out_actor)

    # tác nhân AI bên ngoài khung (sơ đồ hệ thống)
    if d.get("right_actor"):
        ox = bx + bw + extra_right / 2 + 10
        oy = (top + bottom) / 2 - 32
        for uid, (cx, cy, _) in rells.items():
            out.insert(4, f'<line x1="{cx + EW / 2}" y1="{cy}" x2="{ox - 65}" y2="{oy + 32}" '
                          f'stroke="{C["line"]}" stroke-width="1.2"/>')
        out.append(system_actor(ox, oy, d["right_actor"], "external"))

    # chú thích
    out.append(f'<g font-size="11" fill="{C["muted"]}">'
               f'<ellipse cx="{bx + 24}" cy="{H - 14}" rx="14" ry="7" fill="{C["ai"]}" stroke="{C["ai_stroke"]}"/>'
               f'<text x="{bx + 44}" y="{H - 10}">Use case có dùng AI (Claude API)</text></g>')
    out.append("</svg>")
    (OUT / f"{key}.svg").write_text("\n".join(out), encoding="utf-8")
    return key


def render_overview():
    """Sơ đồ tổng quát: chỉ các tính năng chính, mỗi tác nhân nối thẳng tới use case của mình."""
    # (mã, nhãn, có AI) — thứ tự từ trên xuống, xếp để đường nối hai bên không chồng nhau
    ucs = [
        ("A", "Đăng nhập & quản lý tài khoản", False),
        ("I", "Xác nhận phiếu & duyệt giảm giá", False),
        ("J", "Theo dõi hàng, ví & rút tiền", False),
        ("B", "Quản lý người ký gửi", False),
        ("C", "Nhận hàng ký gửi", False),
        ("D", "AI nhận diện ảnh & gợi ý giá", True),
        ("E", "Quản lý kho & giá bán", False),
        ("F", "Bán hàng & đổi trả", False),
        ("G", "Đối soát & chi trả", False),
        ("H", "Báo cáo & quản trị shop", False),
    ]
    ow, oh, row = 300, 46, 66
    left_zone, right_zone, pad = 200, 230, 50
    bx = MARGIN + left_zone
    bw = ow + 2 * pad
    bt = TITLE_H + MARGIN
    top = bt + 50
    W = bx + bw + right_zone + MARGIN
    bottom = top + len(ucs) * row
    H = bottom + MARGIN + 30

    pos = {k: (bx + pad + ow / 2, top + i * row + oh / 2) for i, (k, _, _) in enumerate(ucs)}
    lx_edge = bx + pad              # mép trái các elip
    rx_edge = bx + pad + ow         # mép phải các elip

    def row_y(r):
        return top + r * row + oh / 2

    lax = MARGIN + 90
    rax = bx + bw + right_zone / 2
    people = [  # (tên, x, y đầu, cạnh nối, use case)
        ("Chủ shop", lax, row_y(2.4) - 36, "L", "ABCEFGH"),
        ("Nhân viên", lax, row_y(6.2) - 36, "L", "ABCEF"),
        ("Người ký gửi", rax, row_y(1) - 36, "R", "AIJ"),
    ]
    systems = [  # (tên, stereotype, y tâm, use case)
        ("Claude API", "external", row_y(4.6), "D"),
        ("Scheduler", "system", row_y(7.6), "EG"),
    ]

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}" font-family="{FONT}">',
           f'<rect width="{W}" height="{H}" fill="{C["bg"]}"/>',
           f'<text x="{W / 2}" y="{MARGIN + 18}" text-anchor="middle" font-size="20" '
           f'font-weight="700" fill="{C["text"]}">Use Case tổng quát — ReLoop</text>',
           f'<rect x="{bx}" y="{bt}" width="{bw}" height="{bottom - bt + 10}" rx="10" '
           f'fill="{C["boundary_bg"]}" stroke="{C["boundary"]}" stroke-width="2"/>',
           f'<text x="{bx + 16}" y="{bt + 26}" font-size="15" font-weight="700" '
           f'fill="{C["boundary"]}">ReLoop — System Boundary</text>']

    for name, x, y, side, keys in people:
        sx = x + 22 if side == "L" else x - 22
        for k in keys:
            ex = lx_edge if side == "L" else rx_edge
            out.append(f'<line x1="{sx}" y1="{y + 36}" x2="{ex}" y2="{pos[k][1]}" '
                       f'stroke="{C["line"]}" stroke-width="1.2"/>')
    for name, stereo, cy, keys in systems:
        for k in keys:
            out.append(f'<line x1="{rax - 65}" y1="{cy}" x2="{rx_edge}" y2="{pos[k][1]}" '
                       f'stroke="{C["line"]}" stroke-width="1.2"/>')

    for k, label, ai in ucs:
        cx, cy = pos[k]
        fill, stroke = (C["ai"], C["ai_stroke"]) if ai else (C["ell"], C["ell_stroke"])
        out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{ow / 2}" ry="{oh / 2}" fill="{fill}" '
                   f'stroke="{stroke}" stroke-width="1.5"/>'
                   f'<text x="{cx}" y="{cy + 5}" text-anchor="middle" font-size="14" '
                   f'fill="{C["text"]}">{escape(label)}</text>')

    # D «extend» C: mũi tên ngắn từ elip AI lên elip Nhận hàng
    cx, cy_c = pos["C"]
    _, cy_d = pos["D"]
    out.append(f'<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" '
               f'markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10" fill="none" '
               f'stroke="{C["rel"]}" stroke-width="1.5"/></marker></defs>')
    out.append(f'<line x1="{cx}" y1="{cy_d - oh / 2}" x2="{cx}" y2="{cy_c + oh / 2}" stroke="{C["rel"]}" '
               f'stroke-width="1.4" stroke-dasharray="5 3" marker-end="url(#arr)"/>'
               f'<text x="{cx + 8}" y="{(cy_c + cy_d) / 2 + 4}" font-size="11" fill="{C["rel"]}">'
               f'&#171;extend&#187;</text>')

    for name, x, y, side, _ in people:
        out.append(stick_figure(x, y, name))
    for name, stereo, cy, _ in systems:
        out.append(system_actor(rax, cy - 32, name, stereo))

    out.append(f'<g font-size="11" fill="{C["muted"]}">'
               f'<ellipse cx="{bx + 14}" cy="{H - 18}" rx="14" ry="7" fill="{C["ai"]}" stroke="{C["ai_stroke"]}"/>'
               f'<text x="{bx + 34}" y="{H - 14}">Use case có dùng AI (Claude API)</text></g>')
    out.append("</svg>")
    (OUT / "ucd-overview.svg").write_text("\n".join(out), encoding="utf-8")
    return "ucd-overview"


if __name__ == "__main__":
    print("Đã tạo", render_overview() + ".svg")
    for k, v in diagrams().items():
        print("Đã tạo", render(k, v) + ".svg")
