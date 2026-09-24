import cv2, json, os, numpy as np
BUF = '/home/user/bfyp-social-media/public/social/buffer'
F10 = '/tmp/claude-0/-home-user-bfyp-social-media/1f926514-02a2-525f-ad54-1d666f4fe0d6/scratchpad/study/f10'
F1 = '/tmp/claude-0/-home-user-bfyp-social-media/1f926514-02a2-525f-ad54-1d666f4fe0d6/scratchpad/study/frames'
OUT = '/opt/bfyp/assets/screens'
C = [
 # id, source, box (x0,y0,x1,y1), capture, page, note
 ('whale_card', f'{BUF}/carousels/s3_whales-1ae56a5c01.png', (68,620,1012,1240), '2026-09-23 21:38 UTC', 'Whale Activity', 'LIT large transfer card'),
 ('sm_rows_678', f'{BUF}/carousels/s4_smart-b1474793d1.png', (104,604,976,1219), '2026-09-23 21:38 UTC', 'Smart Money leaderboard', 'rows 6-8'),
 ('sm_rows_12', f'{BUF}/carousels/s1_cover-a18982697c.png', (140,672,940,1232), '2026-09-23 21:38 UTC', 'Smart Money · Scored wallet universe', 'rows 1-2 + header'),
 ('today_lines', f'{BUF}/carousels/s2_today-560a5b13cf.png', (68,606,1012,1240), '2026-09-23 21:28 UTC', 'Today', 'observed lines'),
 ('today_cats', f'{BUF}/fresh/today_story-68bc826c3a.png', (108,716,972,1458), '2026-09-23 22:14 UTC', 'Today', 'category counts card'),
 ('today_footer', f'{BUF}/fresh/today_story-68bc826c3a.png', (70,1470,1010,1548), '2026-09-23 22:14 UTC', 'Today', 'footer: observed activity, nothing is a prediction'),
 ('today_head', f'{BUF}/fresh/today_story-68bc826c3a.png', (70,330,1010,700), '2026-09-23 22:14 UTC', 'Today', 'headline: 354 observations in the last 24h'),
 ('spy_cards', f'{BUF}/carousels/s5_etf-2bb66040d5.png', (144,622,936,1192), '2026-09-23 21:38 UTC', 'ETF · SPY', 'net assets / holdings / filed'),
 ('voo_cards', f'{BUF}/carousels/e3_voo-99fee83f3f.png', (172,576,908,1200), '2026-09-23 22:01 UTC', 'ETF · VOO', 'fund net assets / holdings / filed (incl. capture pill)'),
 ('spy_note', f'{BUF}/carousels/e4_note-5474a28ad0.png', (106,534,974,818), '2026-09-23 22:01 UTC', 'ETF · SPY', 'as-filed note (incl. capture pill)'),
 ('nvda_filings4', f'{BUF}/carousels/s6_stocks-3955eff09a.png', (68,604,1012,1212), '2026-09-23 21:39 UTC', 'Stocks · NVDA', 'recent filings (4 rows)'),
 ('nvda_filings5', f'{BUF}/stories/st_n3_filings-9bd9209208.png', (144,790,936,1504), '2026-09-23 22:01 UTC', 'Stocks · NVDA', 'recent filings (5 rows incl. N-PX)'),
 ('nvda_fund', f'{F1}/nvda_record_reel-3266dcd4d2/f_06.png', (150,885,930,1548), '2026-09-23 22:01 UTC', 'Stocks · NVDA', 'annual fundamentals as filed'),
 ('nvda_insider', f'{F1}/nvda_record_reel-3266dcd4d2/f_13.png', (106,948,976,1538), '2026-09-23 22:01 UTC', 'Stocks · NVDA', 'insider forms 3/4/5'),
 ('ai_prompt', f'{BUF}/carousels/s7_research-2b42816faa.png', (146,592,934,1222), '2026-09-23 21:39 UTC', 'AI Research', 'prompt box'),
 ('ai_ask', f'{BUF}/carousels/g3_context-f554c41ec8.png', (176,604,904,1200), '2026-09-23 22:09 UTC', 'ETF · SPY', 'Ask BFYP about this'),
 ('ai_label', f'{BUF}/carousels/g4_label-48a97523b1.png', (106,620,974,876), '2026-09-23 22:09 UTC', 'AI Research', 'AI label'),
 ('free_card', f'{BUF}/carousels/f1_cover-42de585985.png', (108,562,972,1016), '2026-09-23 22:09 UTC', 'Pricing', 'Free $0 card'),
 ('free_list', f'{BUF}/carousels/f2_plan-2534ffbf44.png', (226,590,854,1220), '2026-09-23 22:09 UTC', 'Pricing', 'free plan list'),
 ('honesty', f'{BUF}/carousels/f3_honesty-4339204bc9.png', (60,640,1020,990), '2026-09-23 22:09 UTC', 'Pricing', "Don't take our word for it"),
 ('sm_page', f'{F10}/BFYP_REEL_13_FINAL-f2d9cf7600/f_002.png', (30,462,1050,1545), '2026-09-23 21:38 UTC', 'Smart Money', 'page top: disclaimer, asset consensus, wallet list'),
 ('sm_scores', f'{F10}/BFYP_REEL_13_FINAL-f2d9cf7600/f_023.png', (30,600,1050,1215), '2026-09-23 21:38 UTC', 'Smart Money leaderboard', 'score + confidence column'),
 ('spy_page', f'{F10}/BFYP_REEL_15_FINAL-9c99d7a370/f_001.png', (30,462,1050,1545), '2026-09-23 22:01 UTC', 'ETF · SPY', 'page top: cards, asset mix, top holdings 1-13'),
 ('spy_bottom', f'{F10}/BFYP_REEL_15_FINAL-9c99d7a370/f_054.png', (30,622,1050,1215), '2026-09-23 22:01 UTC', 'ETF · SPY', 'top holdings 8-15 + as-filed note'),
]
cat = {}
for cid, src, box, cap, page, note in C:
    im = cv2.imread(src)
    assert im is not None, src
    x0,y0,x1,y1 = box
    crop = im[y0:y1, x0:x1]
    if '/frames/' in src or '/f10/' in src:
        crop = cv2.fastNlMeansDenoisingColored(crop, None, 2, 2, 5, 13)
    cv2.imwrite(f'{OUT}/{cid}.png', crop)
    up = cv2.resize(crop, (crop.shape[1]*2, crop.shape[0]*2), interpolation=cv2.INTER_LANCZOS4)
    blur = cv2.GaussianBlur(up, (0,0), 1.2)
    up = cv2.addWeighted(up, 1.35, blur, -0.35, 0)
    cv2.imwrite(f'{OUT}/{cid}@2x.png', up)
    cat[cid] = {'kind': ('data' if cid in ('today_cats','today_footer','today_head') else 'screen'), 'src': os.path.relpath(src, '/') if src.startswith(BUF) else src, 'box': box, 'w': crop.shape[1], 'h': crop.shape[0], 'captured': cap, 'page': page, 'note': note}
json.dump(cat, open(f'{OUT}/catalog.json','w'), indent=1)
# contact sheet
tiles=[]
for cid in cat:
    im = cv2.imread(f'{OUT}/{cid}.png'); h=int(im.shape[0]*300/im.shape[1]); t=cv2.resize(im,(300,h))
    t = cv2.copyMakeBorder(t,24,4,4,4,cv2.BORDER_CONSTANT,value=(40,40,40)); cv2.putText(t,cid,(4,18),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    tiles.append(t)
cols=6; rows=[]
for i in range(0,len(tiles),cols):
    row=tiles[i:i+cols]; hmax=max(t.shape[0] for t in row)
    row=[cv2.copyMakeBorder(t,0,hmax-t.shape[0],0,0,cv2.BORDER_CONSTANT,value=(0,0,0)) for t in row]
    while len(row)<cols: row.append(np.zeros((hmax,308,3),np.uint8))
    rows.append(np.hstack(row))
cv2.imwrite('/opt/bfyp/test/assets_sheet.jpg', np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 85])
print(len(cat), 'assets')
