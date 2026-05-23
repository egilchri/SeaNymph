"""
SeaNymph DC Wiring Diagram Generator
Produces wiki/assets/dc-wiring-diagram.png
Run from the SeaNymph/ directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

W, H = 26, 18
fig, ax = plt.subplots(figsize=(W, H))
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis('off')
BG = '#f4f4ee'
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

# Wire colors matching SeaNymph as-installed
YELLOW = '#b08800'
PINK   = '#cc2222'
BLACK  = '#111111'
GRAY   = '#999999'
CTRL   = '#4455aa'

BOX_EDGE  = '#223355'


def draw_box(cx, cy, w, h, line1, line2='', color='#ffffff', fs=11):
    rect = mpatches.FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle="round,pad=0.15",
        linewidth=2, edgecolor=BOX_EDGE, facecolor=color, zorder=3
    )
    ax.add_patch(rect)
    if line2:
        ax.text(cx, cy + 0.28, line1, ha='center', va='center',
                fontsize=fs, fontweight='bold', zorder=4)
        ax.text(cx, cy - 0.28, line2, ha='center', va='center',
                fontsize=fs - 1.5, color='#444', zorder=4)
    else:
        ax.text(cx, cy, line1, ha='center', va='center',
                fontsize=fs, fontweight='bold', zorder=4)


def wire(x1, y1, x2, y2, color, lw=4, dashed=False, label='', loff=(0, 0.28)):
    ls = (0, (5, 3)) if dashed else 'solid'
    ax.plot([x1, x2], [y1, y2], color=color, lw=lw, linestyle=ls,
            zorder=2, solid_capstyle='round')
    if label:
        mx = (x1 + x2) / 2 + loff[0]
        my = (y1 + y2) / 2 + loff[1]
        ax.text(mx, my, label, ha='center', va='bottom', fontsize=9,
                color=color, fontweight='bold')


def hv(x1, y1, x2, y2, color, lw=4, dashed=False):
    """Horizontal then vertical L-wire."""
    ls = (0, (5, 3)) if dashed else 'solid'
    ax.plot([x1, x2], [y1, y1], color=color, lw=lw, linestyle=ls, zorder=2)
    ax.plot([x2, x2], [y1, y2], color=color, lw=lw, linestyle=ls, zorder=2)


def vh(x1, y1, x2, y2, color, lw=4, dashed=False):
    """Vertical then horizontal L-wire."""
    ls = (0, (5, 3)) if dashed else 'solid'
    ax.plot([x1, x1], [y1, y2], color=color, lw=lw, linestyle=ls, zorder=2)
    ax.plot([x1, x2], [y2, y2], color=color, lw=lw, linestyle=ls, zorder=2)


def fuse_sym(cx, cy, color, label=''):
    rect = mpatches.FancyBboxPatch(
        (cx - 0.35, cy - 0.22), 0.7, 0.44,
        boxstyle="round,pad=0.05",
        linewidth=1.5, edgecolor=color, facecolor='white', zorder=5
    )
    ax.add_patch(rect)
    ax.text(cx, cy, 'F', ha='center', va='center', fontsize=9,
            color=color, fontweight='bold', zorder=6)
    if label:
        ax.text(cx + 0.45, cy, label, ha='left', va='center',
                fontsize=9, color=color, fontweight='bold')


def ground_sym(cx, cy):
    ax.plot([cx, cx], [cy, cy + 0.35], color=BLACK, lw=2, zorder=4)
    for i, hw in enumerate([0.45, 0.3, 0.15]):
        ax.plot([cx - hw, cx + hw], [cy - i*0.18, cy - i*0.18],
                color=BLACK, lw=2, zorder=4)


# ── Component positions ───────────────────────────────────────────
SOLAR_X,  SOLAR_Y  =  3.5, 16.8
MPPT_X,   MPPT_Y   =  3.5, 14.0
SW_X,     SW_Y     =  3.5, 11.5
HBAT_X,   HBAT_Y  =  7.5, 10.5
ACR_X,    ACR_Y   = 13.0, 10.5
SBAT_X,   SBAT_Y  = 18.5, 10.5
ALT_X,    ALT_Y   = 22.5, 10.5
POSBUS_X, POSBUS_Y = 13.0, 15.0
PANEL_X,  PANEL_Y  = 22.5, 15.0
SHUNT_X,  SHUNT_Y  =  7.5,  7.0
NEGBUS_X, NEGBUS_Y = 13.0,  3.8

# ── Boxes ─────────────────────────────────────────────────────────
draw_box(SOLAR_X,  SOLAR_Y,  4.0, 1.1, 'Solar Panels', '(Renogy)', '#fafaf0')
draw_box(MPPT_X,   MPPT_Y,   4.2, 1.1, 'Victron MPPT 75/15', 'SmartSolar', '#eef4ff')
draw_box(SW_X,     SW_Y,     3.8, 1.0, 'Solar Disconnect', 'Red ON/OFF switch', '#fff8f0')
draw_box(HBAT_X,   HBAT_Y,   3.8, 1.6, 'House Battery', 'Group 24 AGM', '#e4f4e4')
draw_box(ACR_X,    ACR_Y,    3.6, 1.4, 'Blue Sea SI-ACR', '7610', '#dce8f8')
draw_box(SBAT_X,   SBAT_Y,   3.8, 1.6, 'Start Battery', 'Group 24 AGM', '#e4f4e4')
draw_box(ALT_X,    ALT_Y,    3.4, 1.2, 'Yanmar 1GM', 'Alternator', '#f8ede0')
draw_box(POSBUS_X, POSBUS_Y, 4.4, 1.0, 'Positive Bus Bar', color='#fffbe0')
draw_box(PANEL_X,  PANEL_Y,  3.4, 1.2, 'DC Panel', '(Loads)', '#f0eaff')
draw_box(SHUNT_X,  SHUNT_Y,  3.8, 1.0, 'Victron SmartShunt', 'inline · negative', '#dce8f8')
draw_box(NEGBUS_X, NEGBUS_Y, 4.8, 1.0, 'Negative Bus Bar', color='#e0e0e0')

# Ground
ax.plot([NEGBUS_X, NEGBUS_X], [NEGBUS_Y - 0.5, NEGBUS_Y - 0.9],
        color=BLACK, lw=2.5, zorder=3)
ground_sym(NEGBUS_X, NEGBUS_Y - 0.9)

# ── POSITIVE WIRES ────────────────────────────────────────────────

# Solar → MPPT
wire(SOLAR_X, SOLAR_Y - 0.55, MPPT_X, MPPT_Y + 0.55, YELLOW, lw=3)

# MPPT → switch
wire(MPPT_X, MPPT_Y - 0.55, SW_X, SW_Y + 0.5, YELLOW, lw=3)

# Switch → house battery + (elbow right then down)
hv(SW_X + 1.9, SW_Y, HBAT_X - 1.9, HBAT_Y + 0.45, YELLOW, lw=4)
ax.text((SW_X + 1.9 + HBAT_X - 1.9)/2, SW_Y + 0.3,
        'MPPT out (+)', ha='center', fontsize=9, color=YELLOW, fontweight='bold')

# House battery + → ACR Stud A
wire(HBAT_X + 1.9, HBAT_Y, ACR_X - 1.8, ACR_Y, YELLOW, lw=5,
     label='Stud A', loff=(0, 0.3))

# Start battery + → ACR Stud B
wire(SBAT_X - 1.9, SBAT_Y, ACR_X + 1.8, ACR_Y, PINK, lw=5,
     label='Stud B', loff=(0, 0.3))

# Alternator + → pos bus bar (ASSUMED — elbow up then left)
hv(ALT_X - 0.3, ALT_Y + 0.6, POSBUS_X + 2.2, POSBUS_Y, YELLOW, lw=3, dashed=True)
ax.text(19.5, ALT_Y + 1.4, '(assumed)', ha='center', fontsize=9,
        color=GRAY, style='italic')

# Pos bus bar → ACR top (ASSUMED)
wire(POSBUS_X, POSBUS_Y - 0.5, ACR_X, ACR_Y + 0.7, YELLOW, lw=3, dashed=True)

# DC Panel → pos bus bar (ASSUMED)
wire(PANEL_X - 1.7, PANEL_Y, POSBUS_X + 2.2, POSBUS_Y, YELLOW, lw=3, dashed=True)
ax.text((PANEL_X - 1.7 + POSBUS_X + 2.2)/2, PANEL_Y + 0.3,
        '(assumed)', ha='center', fontsize=9, color=GRAY, style='italic')

# ── NEGATIVE WIRES ────────────────────────────────────────────────

# House battery − → SmartShunt
wire(HBAT_X, HBAT_Y - 0.8, SHUNT_X, SHUNT_Y + 0.5, BLACK, lw=5)

# SmartShunt → neg bus bar
vh(SHUNT_X, SHUNT_Y - 0.5, NEGBUS_X - 1.5, NEGBUS_Y + 0.5, BLACK, lw=5)

# Start battery − → neg bus bar
vh(SBAT_X, SBAT_Y - 0.8, NEGBUS_X + 1.5, NEGBUS_Y + 0.5, BLACK, lw=4)

# Alternator − → neg bus bar (ASSUMED)
vh(ALT_X, ALT_Y - 0.6, NEGBUS_X + 2.3, NEGBUS_Y + 0.2, BLACK, lw=3, dashed=True)

# ── ACR CONTROL WIRES ─────────────────────────────────────────────

# GND spade → neg bus bar (1A fuse, thin control wire)
gnd_wx = ACR_X - 1.0
ax.plot([gnd_wx, gnd_wx], [ACR_Y - 0.7, NEGBUS_Y + 0.5],
        color=CTRL, lw=1.8, zorder=2)
ax.plot([gnd_wx, NEGBUS_X - 0.5], [NEGBUS_Y + 0.5, NEGBUS_Y + 0.5],
        color=CTRL, lw=1.8, zorder=2)
fuse_sym(gnd_wx, (ACR_Y - 0.7 + NEGBUS_Y + 0.5) / 2, CTRL, '1A')

# SI wire — optional, dashed arc to alternator area
ax.annotate(
    '', xy=(ACR_X + 0.8, ACR_Y - 0.7), xytext=(ALT_X - 0.3, ALT_Y - 0.6),
    arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.5,
                    linestyle='dashed', connectionstyle='arc3,rad=-0.3')
)
ax.text(18.5, 7.8, 'SI wire → starter\n(unknown if wired)', ha='center',
        fontsize=9.5, color=GRAY, style='italic')

# ── TERMINAL LABELS on ACR ────────────────────────────────────────
for x, label, color in [(ACR_X - 1.1, 'A', YELLOW), (ACR_X + 1.1, 'B', PINK)]:
    ax.text(x, ACR_Y + 0.25, label, fontsize=12, color=color, fontweight='bold',
            ha='center', va='center',
            bbox=dict(fc='white', ec=color, pad=3, lw=1.5, boxstyle='round'))

# ── LEGEND ────────────────────────────────────────────────────────
lx, ly = 0.4, 7.5
ax.text(lx, ly, 'Legend', fontsize=12, fontweight='bold', color='#222')
legend_items = [
    (YELLOW, 4,   False, 'DC Positive — yellow cable (main positive runs)'),
    (PINK,   4,   False, 'DC Positive — pink/red cable (start battery side)'),
    (BLACK,  4,   False, 'DC Negative — black cable'),
    (CTRL,   1.8, False, 'Control wire — GND/SI (small gauge)'),
    (GRAY,   2.5, True,  'Assumed / not confirmed from photos'),
]
for i, (color, lw, dashed, label) in enumerate(legend_items):
    y = ly - 0.7 * (i + 1)
    ls = (0, (5, 3)) if dashed else 'solid'
    ax.plot([lx, lx + 0.8], [y, y], color=color, lw=lw, linestyle=ls)
    ax.text(lx + 1.05, y, label, fontsize=10, va='center', color='#222')

# ── NOTES ─────────────────────────────────────────────────────────
notes = (
    "Notes\n"
    "  • ACR Studs A & B are interchangeable (dual sensing)\n"
    "  • SmartShunt is inline on house battery negative — measures all house loads\n"
    "  • Alternator → bus bar → ACR routing is a best guess — trace wire to confirm\n"
    "  • DC panel feed point: assumed off bus bar — not confirmed\n"
    "  • SI terminal: check for wire on ACR SI spade — must be crank-only, not ignition-run\n"
    "  • GND wire fuse must be 1A (Blue Sea spec) — intentionally small\n"
    "  • Yanmar 1GM alternator ≈30–40A; #6 AWG / 75–90A fuse on stud A & B cables"
)
ax.text(0.4, 3.8, notes, fontsize=10, va='top', color='#222', linespacing=1.6,
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#fffbe8',
                  edgecolor='#bbaa55', alpha=0.97))

# ── TITLE ─────────────────────────────────────────────────────────
ax.set_title(
    "SeaNymph (Cape Dory 25D)  —  DC Electrical Wiring Diagram\n"
    "Blue Sea SI-ACR 7610 System  ·  As of Sep 2025  ·  Dashed lines = assumed, not confirmed",
    fontsize=14, fontweight='bold', pad=14
)

out = 'wiki/assets/dc-wiring-diagram.png'
plt.tight_layout(pad=0.8)
plt.savefig(out, dpi=180, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Saved → {out}")
