# Trở thành Gold CFD Quant Trader

## 1. Kiến thức nền tảng (Foundation)
- Hiểu rõ **thị trường CFD**: cơ chế khớp lệnh, spread, swap, margin, đòn bẩy, rủi ro counterparty.  
- Cấu trúc thị trường **vàng (XAU/USD)**:  
  - Vai trò vàng trong hệ thống tiền tệ, correlation với USD, lợi suất trái phiếu, inflation.  
  - Ảnh hưởng tin tức (FOMC, NFP, CPI, địa chính trị).  
  - Các phiên giao dịch (London, New York, Asian session).  
- Cơ bản về **tài chính định lượng**: xác suất, thống kê, time series, mô hình stochastic.  
- **Derivatives & hedging**: nguyên tắc phòng ngừa rủi ro (hedge vàng bằng DXY, trái phiếu, ETF).  


## 2. Công cụ & hạ tầng (Tools & Infrastructure)
- **Nền tảng giao dịch**: MT5, cTrader, NinjaTrader, hoặc API (FIX/REST/Websocket).  
- **Ngôn ngữ lập trình**: Python, MQL5, R (Python là cốt lõi).  
- **Backtesting framework**:  
  - Python: Backtrader, Zipline, QuantConnect.  
  - MT5 Strategy Tester.  
- **Data pipeline**:  
  - Tick data (Dukascopy, TrueFX, CQG, Tickmill).  
  - API dữ liệu real-time (Binance Futures Gold CFD, MetaQuotes, FXCM).  
- **Hệ thống phân tích**: Jupyter Notebook, Pandas, NumPy, scikit-learn, TensorFlow/PyTorch.  
- **Quản trị rủi ro**: Position sizing, Kelly criterion, Monte Carlo simulation.  
- **Execution**: smart order routing, slippage control, latency monitoring.  


## 3. Phương pháp giao dịch định lượng (Quant Strategies)
- **Statistical arbitrage**: cointegration với DXY, silver, oil.  
- **Mean reversion**: Bollinger, Kalman filter, Ornstein–Uhlenbeck process.  
- **Trend following**: breakout systems, moving average cross, momentum factors.  
- **Volatility trading**: GARCH, implied volatility từ options vàng.  
- **Machine Learning**:  
  - Classification (predict up/down moves).  
  - Regression (forecast returns).  
  - Reinforcement Learning (position sizing adaptively).  
- **Macro quant overlay**: filter tín hiệu theo Fed policy, bond yields.  


## 4. Quản lý vốn & rủi ro (Risk & Money Management)
- Xác định risk per trade (0.25–0.5% vốn).  
- Max daily drawdown (2–3%).  
- Equity curve control (lock profit khi đạt target).  
- Diversification: phân bổ giữa timeframe (scalping, swing) và giữa chiến lược.  
- Stress testing: kiểm tra chiến lược khi spread giãn, latency tăng, tin tức bất thường.  


## 5. Tâm lý & kỷ luật (Trader’s Mindset)
- Tách biệt **hệ thống** với **cảm xúc** (systematic trading mindset).  
- Kiên nhẫn để theo sát hệ thống định lượng, không phá luật khi drawdown.  
- Hiểu rằng **edge** đến từ thống kê dài hạn, không phải vài lệnh thắng/thua.  


## 6. Lộ trình thực chiến (Step-by-Step Roadmap)
1. **Nắm thị trường vàng**: đọc báo cáo World Gold Council, hiểu dòng tiền ETF vàng.  
2. **Lập trình & dữ liệu**: thu thập 10 năm dữ liệu tick gold, xây backtest.  
3. **Xây chiến lược cơ bản**: MA cross + risk management → backtest.  
4. **Phát triển chiến lược định lượng**: stat arb, machine learning, volatility models.  
5. **Tạo portfolio chiến lược**: kết hợp nhiều hệ thống để giảm drawdown.  
6. **Triển khai live trading**: ban đầu với demo, sau đó micro lot real account.  
7. **Quản trị vốn chuyên nghiệp**: học theo phong cách quỹ (VaR, CVaR, stress test).  
8. **Tự động hóa & scaling**: tạo bot quản lý execution, risk, log, analytics.  


👉 Tóm lại: để thành **gold CFD quant trader**, bạn cần song song 3 yếu tố:  
- **Kiến thức thị trường vàng**  
- **Công nghệ định lượng**  
- **Kỷ luật giao dịch chuyên nghiệp**


---


# Roadmap


## Tổng quan 6 pha

1. **Foundation (Kiến thức thị trường & xác suất–thống kê)**  
   - Cấu trúc vàng (XAUUSD): vai trò trú ẩn, mối liên hệ USD–real yields–CPI–Fed.  
   - Cơ chế CFD: đòn bẩy, margin, swap, spread, slippage, rủi ro broker/counterparty.  
   - Xác suất–thống kê–time series căn bản: phân phối lợi nhuận, stationarity, ACF/PACF, heteroskedasticity.  
   - Kỷ luật và kỳ vọng thống kê: edge đến từ mẫu lớn, quản trị chuỗi thua.

2. **Tooling & Data (Hạ tầng, dữ liệu, backtest)**  
   - MT5 + MQL5, Python, Jupyter.  
   - Pipeline dữ liệu: tick → bar, làm sạch outlier, timezone, phiên.  
   - Backtest đúng thực tế: spread biến thiên, slippage, phí swap, gap, news blackout.

3. **Research & Strategy (R&D chiến lược)**  
   - Trend, mean-reversion, stat-arb (DXY, XAGUSD), volatility, event-aware.  
   - Feature giải thích được, tránh overfit.  
   - Walk-forward, kiểm định giả thuyết.

4. **Risk & Portfolio (Quản trị rủi ro & ghép chiến lược)**  
   - Risk per trade 0.25–0.5% tài khoản, DD ngày 2–3%, tuần 5–6%.  
   - Stop theo ATR, ghép hệ thống, Monte Carlo stress test.

5. **Execution & Ops (Triển khai, giám sát, vận hành)**  
   - EA MQL5: slippage control, partial TP, trailing, lock profit, news filter.  
   - VPS, latency, log, alert, dashboard.  
   - Quy trình phiên: pre → during → post.

6. **Governance (Quy tắc, tài liệu, ra/vào vốn)**  
   - Risk Policy, Runbook sự cố.  
   - Tiêu chí Go/No-Go demo → real.  
   - Lộ trình scaling vốn.

---

## Lộ trình 12 tuần (Core)

### Tuần 1 — Setup & dữ liệu
- Cài MT5, Python, Jupyter.  
- Lấy 5–10 năm dữ liệu XAUUSD tick/1m/5m.  
- Chuẩn hóa dữ liệu, thêm spread, session, news tag.  
**Deliverables:** Repo Git + notebook EDA + module dữ liệu.  
**KPI:** Dữ liệu sạch, EDA cơ bản.

### Tuần 2 — EDA & microstructure
- Phân tích volatility theo phiên.  
- Kiểm tra event windows (CPI/NFP/FOMC).  
- Corr với DXY, XAGUSD, yields.  
**Deliverables:** Báo cáo EDA.  
**KPI:** Xác định giờ trade tốt + giờ black-out.

### Tuần 3 — Backtest framework
- Spread động, slippage, phí swap.  
- News blackout.  
**Deliverables:** Backtest engine Python + MT5 config.  
**KPI:** Sai khác < 5% giữa Python & MT5.

### Tuần 4 — Baseline strategies
- Trend: breakout London/NY, MA/Donchian.  
- Mean-reversion: band, OU, Kalman.  
- Chỉ số đo: CAGR, Sharpe, MAR, MaxDD.  
**Deliverables:** 2 notebooks + báo cáo OOS.  
**KPI:** ≥1 chiến lược Sharpe ≥ 1.0 OOS.

### Tuần 5 — Risk framework
- Sizing theo ATR.  
- Equity guardrails.  
- Monte Carlo lệnh.  
**Deliverables:** Risk policy v1.  
**KPI:** MAR > 0.5.

### Tuần 6 — Volatility models
- ATR regime, GARCH.  
- Vol filters.  
**Deliverables:** Notebook vol-model.  
**KPI:** Sharpe/DD cải thiện.

### Tuần 7 — Stat-arb
- Cointegration XAU–DXY–XAG.  
- Spread trading.  
**Deliverables:** Module stat-arb.  
**KPI:** Corr thấp với Trend/MR.

### Tuần 8 — Event & regime switching
- Blackout tin.  
- Regime detection (HMM, vol regime).  
**Deliverables:** Event filter + regime switcher.  
**KPI:** Giảm tail risk quanh tin.

### Tuần 9 — Portfolio
- Risk parity / diversification.  
- Rolling correlation.  
- Stress test spread/slippage.  
**Deliverables:** Portfolio allocator.  
**KPI:** MaxDD ≤ 12%, Sharpe ≥ 1.2 OOS.

### Tuần 10 — Execution & EA
- EA: signal, risk, order router.  
- Partial TP, trailing, BE, lock profit.  
- Python↔MT5 bridge.  
**Deliverables:** EA v1.  
**KPI:** Deviation demo < 10%.

### Tuần 11 — Walk-Forward
- Walk-Forward Optimization.  
- Reality check.  
**Deliverables:** Báo cáo WFO.  
**KPI:** OOS Sharpe ≥ 1.1.

### Tuần 12 — Demo live
- VPS setup, alert, dashboard.  
- Go/No-Go rules:  
  - Tracking error < 15%,  
  - DD demo ≤ 70% DD kỳ vọng,  
  - Sharpe demo ≥ 80% OOS.  
**Deliverables:** Runbook + báo cáo demo.  
**KPI:** Đủ điều kiện vào real nhỏ.


## Lộ trình nâng cao 12 tuần (13–24)

- **Tuần 13–14:** Order flow, VWAP/TWAP executor.  
- **Tuần 15–16:** ML cơ bản (GBM, linear).  
- **Tuần 17:** RL cho position sizing.  
- **Tuần 18:** Cross-broker testing.  
- **Tuần 19:** VaR/CVaR, stress test tail.  
- **Tuần 20:** Automation (watchdog, logging).  
- **Tuần 21:** Scaling vốn adaptive.  
- **Tuần 22:** Compliance, separation dev/prod.  
- **Tuần 23:** Model audit, MLflow tracking.  
- **Tuần 24:** Tổng kết, tài liệu hóa (Risk Policy v2, Runbook v2).


## Checklist “chuẩn quỹ”

**Hạ tầng & dữ liệu**  
- [ ] Repo Git, env.yaml.  
- [ ] Module dữ liệu, news calendar.  
- [ ] Backtest engine thực tế.

**Chiến lược**  
- [ ] ≥3 hệ thống độc lập.  
- [ ] Walk-forward + OOS ≥ 12–24 tháng.  
- [ ] Báo cáo ổn định tham số.

**Rủi ro & danh mục**  
- [ ] Risk Policy (0.25–0.5%/lệnh, DD day/week).  
- [ ] Portfolio allocator (corr, vol targeting).  
- [ ] Stress test.

**Thực thi**  
- [ ] EA MQL5 đầy đủ chức năng.  
- [ ] VPS + giám sát latency/slippage.  
- [ ] Runbook sự cố.

**KPI**  
- [ ] Sharpe ≥ 1.2, MaxDD ≤ 12%.  
- [ ] Tracking error demo < 15%.  
- [ ] 4 tuần demo ổn định.


## Công thức cốt lõi

- **Position sizing:**  
  `Lot ≈ (Risk_per_trade * Equity) / (SL_pips * PipValue)`  
  SL theo ATR (1.5–2.5×ATR).

- **Equity guardrails:**  
  - Stop nếu DD ngày ≥ 2–3% hoặc DD tuần ≥ 5–6%.  
  - Khi vượt, giảm 50–75% size.

- **News policy:**  
  - Blackout X phút quanh CPI/NFP/FOMC.  
  - Thoát lệnh trước tin lớn.


## Quy trình hàng ngày

1. **Pre-market:** Check hệ thống, news, vol regime, risk.  
2. **During market:** Monitor slippage, spread, news. Không can thiệp.  
3. **Post-market:** Chốt sổ PnL, log, snapshot dữ liệu.


## Cấu trúc dự án

```
gold-quant/
    data/
    research/
    engine/
    strategies/
    portfolio/
    deployment/
    mt5_ea/
    bridge/
    reports/
    config.yaml
    requirements.txt
```

## Lời khuyên

- Ưu tiên đơn giản + kiểm định kỹ.  
- Tất cả thay đổi cần bằng chứng OOS.  
- Ghi nhật ký đầy đủ.  
- Edge = thống kê dài hạn, không phải vài lệnh.


--- 


# Checklist 24 tuần (100+ tasks)


## Tuần 1 — Setup & dữ liệu
1. Cài đặt MT5, Python 3.11+, Jupyter Notebook.  
2. Cài các package Python: pandas, numpy, scipy, statsmodels, scikit-learn, matplotlib, plotly.  
3. Tạo repo Git version control.  
4. Thu thập 5–10 năm dữ liệu XAUUSD tick và bar (1m, 5m).  
5. Chuẩn hóa dữ liệu: timezone, phiên, outlier.  
6. Thêm cột spread, session, news tag.  
7. Lưu dữ liệu raw & clean theo thư mục chuẩn.  

## Tuần 2 — EDA & microstructure
8. Phân tích volatility theo phiên (Á, Âu, Mỹ).  
9. Phân tích phân phối returns, skewness, kurtosis.  
10. Kiểm tra event windows: CPI, NFP, FOMC.  
11. Tạo heatmap correlation: XAUUSD vs DXY, XAGUSD, yields.  
12. Xác định khung giờ “high activity” vs “low activity”.  
13. Vẽ chart OHLC + spread overlay theo phiên.  
14. Viết báo cáo EDA chi tiết với các biểu đồ.  

## Tuần 3 — Backtest framework
15. Xây engine backtest Python cơ bản.  
16. Mô phỏng spread động.  
17. Mô phỏng slippage theo volatility.  
18. Thêm phí swap và overnight cost.  
19. Cài news blackout rules (cấm giao dịch quanh tin nóng).  
20. Test engine với 1 chiến lược demo (ví dụ MA cross).  
21. So sánh kết quả Python vs MT5 Strategy Tester (<5% sai lệch).  

## Tuần 4 — Baseline strategies
22. Xây chiến lược Trend: breakout London/NY, MA/Donchian + ATR stop.  
23. Xây chiến lược Mean-Reversion: Bollinger/OU/Kalman.  
24. Backtest Trend OOS 70/30.  
25. Backtest MR OOS 70/30.  
26. Tính các chỉ số: CAGR, Sharpe, MaxDD, MAR, Hit rate, Avg win/loss.  
27. Vẽ equity curve và distribution lệnh.  
28. So sánh performance Trend vs MR, chọn thông số ban đầu.  

## Tuần 5 — Risk framework
29. Xây module position sizing theo ATR.  
30. Thiết lập risk per trade 0.25–0.5% vốn.  
31. Equity guardrails: DD ngày 2–3%, tuần 5–6%.  
32. Monte Carlo simulation trên chuỗi lệnh Trend.  
33. Monte Carlo simulation trên chuỗi lệnh MR.  
34. Viết báo cáo Risk Policy v1.  
35. Kiểm tra MAR và tần suất vi phạm guardrails.  

## Tuần 6 — Volatility models
36. Tính ATR regime trên các khung thời gian M5, M15, H1.  
37. Xây model GARCH cơ bản để dự đoán volatility.  
38. Điều chỉnh TP/SL theo volatility.  
39. Test chiến lược Trend với vol targeting.  
40. Test chiến lược MR với vol targeting.  
41. So sánh Sharpe & MaxDD trước và sau khi áp dụng volatility models.  
42. Lưu notebook vol-model và báo cáo.  

## Tuần 7 — Stat-arb
43. Kiểm tra cointegration XAU–DXY–XAG.  
44. Tính z-score của spread pairs.  
45. Xây chiến lược Stat-arb hedged beta DXY.  
46. Backtest Stat-arb OOS 70/30.  
47. So sánh PnL vs Trend/MR để đánh giá diversification.  
48. Lưu module stat-arb Python.  
49. Viết báo cáo OOS Stat-arb.  

## Tuần 8 — Event & regime switching
50. Cài news blackout rules nâng cao.  
51. Thiết lập regime detection: HMM, volatility regime, MA slope.  
52. Tạo signal bật/tắt chiến lược theo regime.  
53. Backtest Trend + MR với regime switching.  
54. Backtest Stat-arb với regime switching.  
55. Đánh giá tail risk quanh tin nóng.  
56. Viết báo cáo event & regime switching.  

## Tuần 9 — Portfolio
57. Tính correlation rolling giữa Trend, MR, Stat-arb.  
58. Xây risk parity allocation.  
59. Tối ưu diversification subject to MaxDD.  
60. Monte Carlo simulation danh mục tổng hợp.  
61. Stress test danh mục: spread/slippage tăng 2–3x.  
62. Kiểm tra MAR, Sharpe & MaxDD danh mục.  
63. Viết báo cáo Portfolio.  

## Tuần 10 — Execution & EA
64. Viết EA MQL5: signal module, risk module, order router.  
65. Thêm partial TP, trailing, BE, lock profit.  
66. Cài retry logic & slippage control.  
67. Tích hợp Python↔MT5 bridge nếu tính toán nặng.  
68. Test EA với Strategy Tester (variable spread).  
69. Kiểm tra deviation backtest vs EA < 10%.  
70. Lưu EA version v1 + tài liệu config.  

## Tuần 11 — Walk-Forward
71. Thiết lập Walk-Forward Optimization (cuộn thời gian).  
72. Chia train/test theo nhiều cửa sổ.  
73. Chỉ giữ parameter ổn định qua nhiều cửa sổ.  
74. Tính Sharpe, MaxDD, MAR cho từng cửa sổ.  
75. Vẽ heatmap hiệu năng tham số.  
76. So sánh performance vs baseline.  
77. Viết báo cáo WFO.  

## Tuần 12 — Demo live
78. Setup VPS gần server London/NY.  
79. Cài alert Telegram/Email cho EA.  
80. Thiết lập dashboard PnL, DD, slippage, latency.  
81. Chạy demo 2–4 tuần, theo dõi hiệu năng.  
82. Kiểm tra Go/No-Go rules: tracking error < 15%, DD demo ≤ 70%, Sharpe demo ≥ 80% OOS.  
83. Lưu báo cáo demo + screenshot equity curve.  
84. Chuẩn hóa Runbook vận hành.  

---

## Tuần 13–24 — Nâng cao

### Tuần 13–14 — Microstructure nâng cao
85. Phân tích order flow & imbalance.  
86. Test VWAP/TWAP executor.  
87. Kiểm soát market impact.  
88. Backtest microstructure strategy.  
89. Lưu báo cáo hiệu năng.  
90. Điều chỉnh EA cho execution nâng cao.  

### Tuần 15–16 — Machine Learning
91. Chọn feature cho ML: trend, vol, microstructure.  
92. Train model GBM/linear regularized.  
93. Test model classification/regression OOS.  
94. Tích hợp model với EA (signal filter).  
95. Viết báo cáo ML performance.  
96. Kiểm tra feature importance, tránh black-box.

### Tuần 17 — Reinforcement Learning
97. Thiết lập RL cho position sizing hoặc regime switching.  
98. Test RL trên demo account.  
99. Backtest RL strategy OOS.  
100. Viết báo cáo RL + lesson learned.  
101. Đánh giá rủi ro RL vs baseline.  
102. Chuẩn hóa module RL để tái sử dụng.  

### Tuần 18 — Cross-broker testing
103. Test EA trên 2–3 broker khác nhau.  
104. So sánh spread, slippage, lot size.  
105. Lưu báo cáo cross-broker.  
106. Điều chỉnh EA nếu có chênh lệch.  
107. Test lại portfolio với broker mới.  
108. Viết note về setup tối ưu cho production.

### Tuần 19 — Advanced Risk
109. Tính VaR, CVaR, Expected Shortfall danh mục.  
110. Stress test tail events: flash crash, news shock.  
111. Viết báo cáo tail risk.  
112. Update Risk Policy v2 theo findings.  
113. Test guardrails với tail scenarios.  
114. Xác nhận chiến lược vẫn robust.  

### Tuần 20 — Automation & monitoring
115. Tạo watchdog script kiểm tra EA, VPS.  
116. Tự động log & snapshot trade, equity, latency.  
117. Thiết lập alert tự động cho bất thường.  
118. Test hệ thống automation.  
119. Viết documentation automation.  
120. Demo 1 tuần tự động giám sát.  

### Tuần 21 — Scaling vốn
121. Thiết lập scaling rule theo vol targeting.  
122. Giảm size khi DD cao.  
123. Tăng size khi equity recovery.  
124. Backtest scaling rule trên demo.  
125. Lưu báo cáo scaling effect.  
126. Tích hợp scaling vào EA.  

### Tuần 22 — Compliance & separation
127. Kiểm tra KYC broker.  
128. Tách tài khoản dev/prod.  
129. Kiểm soát quyền truy cập dữ liệu & EA.  
130. Viết policy separation.  
131. Test truy cập & logging.  
132. Lưu báo cáo compliance.

### Tuần 23 — Model audit
133. Rerun backtest với log seed cố định.  
134. Audit các ML module bằng MLflow/CSV.  
135. Kiểm tra parameter drift.  
136. Ghi nhận issues & fix.  
137. Viết báo cáo audit cuối cùng.  
138. Chuẩn hóa mô hình production.  

### Tuần 24 — Tổng kết & tài liệu
139. Chuẩn hóa Risk Policy v2.  
140. Chuẩn hóa Runbook v2.  
141. Tổng hợp báo cáo chiến lược Trend, MR, Stat-arb, RL.  
142. Tổng hợp Dashboard & equity curves demo & OOS.  
143. Chuẩn hóa repo project.  
144. Lập kế hoạch R&D quý tiếp theo.  
145. Lưu file Markdown checklist hoàn chỉnh cho theo dõi.  


✅ Tổng cộng: 145 tasks, 24 tuần, mỗi tuần ≥6 tasks, siêu chi tiết, giống chương trình huấn luyện quỹ chuyên nghiệp.


---


#  Checklist 145 Tasks

| Task ID | Task Description |
|---------|-----------------|
| 1  | Cài đặt MT5, Python 3.11+, Jupyter Notebook. |
| 2  | Cài các package Python: pandas, numpy, scipy, statsmodels, scikit-learn, matplotlib, plotly. |
| 3  | Tạo repo Git version control. |
| 4  | Thu thập 5–10 năm dữ liệu XAUUSD tick và bar (1m, 5m). |
| 5  | Chuẩn hóa dữ liệu: timezone, phiên, outlier. |
| 6  | Thêm cột spread, session, news tag. |
| 7  | Lưu dữ liệu raw & clean theo thư mục chuẩn. |
| 8  | Phân tích volatility theo phiên (Á, Âu, Mỹ). |
| 9  | Phân tích phân phối returns, skewness, kurtosis. |
| 10 | Kiểm tra event windows: CPI, NFP, FOMC. |
| 11 | Tạo heatmap correlation: XAUUSD vs DXY, XAGUSD, yields. |
| 12 | Xác định khung giờ “high activity” vs “low activity”. |
| 13 | Vẽ chart OHLC + spread overlay theo phiên. |
| 14 | Viết báo cáo EDA chi tiết với các biểu đồ. |
| 15 | Xây engine backtest Python cơ bản. |
| 16 | Mô phỏng spread động. |
| 17 | Mô phỏng slippage theo volatility. |
| 18 | Thêm phí swap và overnight cost. |
| 19 | Cài news blackout rules (cấm giao dịch quanh tin nóng). |
| 20 | Test engine với 1 chiến lược demo (ví dụ MA cross). |
| 21 | So sánh kết quả Python vs MT5 Strategy Tester (<5% sai lệch). |
| 22 | Xây chiến lược Trend: breakout London/NY, MA/Donchian + ATR stop. |
| 23 | Xây chiến lược Mean-Reversion: Bollinger/OU/Kalman. |
| 24 | Backtest Trend OOS 70/30. |
| 25 | Backtest MR OOS 70/30. |
| 26 | Tính các chỉ số: CAGR, Sharpe, MaxDD, MAR, Hit rate, Avg win/loss. |
| 27 | Vẽ equity curve và distribution lệnh. |
| 28 | So sánh performance Trend vs MR, chọn thông số ban đầu. |
| 29 | Xây module position sizing theo ATR. |
| 30 | Thiết lập risk per trade 0.25–0.5% vốn. |
| 31 | Equity guardrails: DD ngày 2–3%, tuần 5–6%. |
| 32 | Monte Carlo simulation trên chuỗi lệnh Trend. |
| 33 | Monte Carlo simulation trên chuỗi lệnh MR. |
| 34 | Viết báo cáo Risk Policy v1. |
| 35 | Kiểm tra MAR và tần suất vi phạm guardrails. |
| 36 | Tính ATR regime trên các khung thời gian M5, M15, H1. |
| 37 | Xây model GARCH cơ bản để dự đoán volatility. |
| 38 | Điều chỉnh TP/SL theo volatility. |
| 39 | Test chiến lược Trend với vol targeting. |
| 40 | Test chiến lược MR với vol targeting. |
| 41 | So sánh Sharpe & MaxDD trước và sau khi áp dụng volatility models. |
| 42 | Lưu notebook vol-model và báo cáo. |
| 43 | Kiểm tra cointegration XAU–DXY–XAG. |
| 44 | Tính z-score của spread pairs. |
| 45 | Xây chiến lược Stat-arb hedged beta DXY. |
| 46 | Backtest Stat-arb OOS 70/30. |
| 47 | So sánh PnL vs Trend/MR để đánh giá diversification. |
| 48 | Lưu module stat-arb Python. |
| 49 | Viết báo cáo OOS Stat-arb. |
| 50 | Cài news blackout rules nâng cao. |
| 51 | Thiết lập regime detection: HMM, volatility regime, MA slope. |
| 52 | Tạo signal bật/tắt chiến lược theo regime. |
| 53 | Backtest Trend + MR với regime switching. |
| 54 | Backtest Stat-arb với regime switching. |
| 55 | Đánh giá tail risk quanh tin nóng. |
| 56 | Viết báo cáo event & regime switching. |
| 57 | Tính correlation rolling giữa Trend, MR, Stat-arb. |
| 58 | Xây risk parity allocation. |
| 59 | Tối ưu diversification subject to MaxDD. |
| 60 | Monte Carlo simulation danh mục tổng hợp. |
| 61 | Stress test danh mục: spread/slippage tăng 2–3x. |
| 62 | Kiểm tra MAR, Sharpe & MaxDD danh mục. |
| 63 | Viết báo cáo Portfolio. |
| 64 | Viết EA MQL5: signal module, risk module, order router. |
| 65 | Thêm partial TP, trailing, BE, lock profit. |
| 66 | Cài retry logic & slippage control. |
| 67 | Tích hợp Python↔MT5 bridge nếu tính toán nặng. |
| 68 | Test EA với Strategy Tester (variable spread). |
| 69 | Kiểm tra deviation backtest vs EA < 10%. |
| 70 | Lưu EA version v1 + tài liệu config. |
| 71 | Thiết lập Walk-Forward Optimization (cuộn thời gian). |
| 72 | Chia train/test theo nhiều cửa sổ. |
| 73 | Chỉ giữ parameter ổn định qua nhiều cửa sổ. |
| 74 | Tính Sharpe, MaxDD, MAR cho từng cửa sổ. |
| 75 | Vẽ heatmap hiệu năng tham số. |
| 76 | So sánh performance vs baseline. |
| 77 | Viết báo cáo WFO. |
| 78 | Setup VPS gần server London/NY. |
| 79 | Cài alert Telegram/Email cho EA. |
| 80 | Thiết lập dashboard PnL, DD, slippage, latency. |
| 81 | Chạy demo 2–4 tuần, theo dõi hiệu năng. |
| 82 | Kiểm tra Go/No-Go rules: tracking error < 15%, DD demo ≤ 70%, Sharpe demo ≥ 80% OOS. |
| 83 | Lưu báo cáo demo + screenshot equity curve. |
| 84 | Chuẩn hóa Runbook vận hành. |
| 85 | Phân tích order flow & imbalance. |
| 86 | Test VWAP/TWAP executor. |
| 87 | Kiểm soát market impact. |
| 88 | Backtest microstructure strategy. |
| 89 | Lưu báo cáo hiệu năng. |
| 90 | Điều chỉnh EA cho execution nâng cao. |
| 91 | Chọn feature cho ML: trend, vol, microstructure. |
| 92 | Train model GBM/linear regularized. |
| 93 | Test model classification/regression OOS. |
| 94 | Tích hợp model với EA (signal filter). |
| 95 | Viết báo cáo ML performance. |
| 96 | Kiểm tra feature importance, tránh black-box. |
| 97 | Thiết lập RL cho position sizing hoặc regime switching. |
| 98 | Test RL trên demo account. |
| 99 | Backtest RL strategy OOS. |
| 100 | Viết báo cáo RL + lesson learned. |
| 101 | Đánh giá rủi ro RL vs baseline. |
| 102 | Chuẩn hóa module RL để tái sử dụng. |
| 103 | Test EA trên 2–3 broker khác nhau. |
| 104 | So sánh spread, slippage, lot size. |
| 105 | Lưu báo cáo cross-broker. |
| 106 | Điều chỉnh EA nếu có chênh lệch. |
| 107 | Test lại portfolio với broker mới. |
| 108 | Viết note về setup tối ưu cho production. |
| 109 | Tính VaR, CVaR, Expected Shortfall danh mục. |
| 110 | Stress test tail events: flash crash, news shock. |
| 111 | Viết báo cáo tail risk. |
| 112 | Update Risk Policy v2 theo findings. |
| 113 | Test guardrails với tail scenarios. |
| 114 | Xác nhận chiến lược vẫn robust. |
| 115 | Tạo watchdog script kiểm tra EA, VPS. |
| 116 | Tự động log & snapshot trade, equity, latency. |
| 117 | Thiết lập alert tự động cho bất thường. |
| 118 | Test hệ thống automation. |
| 119 | Viết documentation automation. |
| 120 | Demo 1 tuần tự động giám sát. |
| 121 | Thiết lập scaling rule theo vol targeting. |
| 122 | Giảm size khi DD cao. |
| 123 | Tăng size khi equity recovery. |
| 124 | Backtest scaling rule trên demo. |
| 125 | Lưu báo cáo scaling effect. |
| 126 | Tích hợp scaling vào EA. |
| 127 | Kiểm tra KYC broker. |
| 128 | Tách tài khoản dev/prod. |
| 129 | Kiểm soát quyền truy cập dữ liệu & EA. |
| 130 | Viết policy separation. |
| 131 | Test truy cập & logging. |
| 132 | Lưu báo cáo compliance. |
| 133 | Rerun backtest với log seed cố định. |
| 134 | Audit các ML module bằng MLflow/CSV. |
| 135 | Kiểm tra parameter drift. |
| 136 | Ghi nhận issues & fix. |
| 137 | Viết báo cáo audit cuối cùng. |
| 138 | Chuẩn hóa mô hình production. |
| 139 | Chuẩn hóa Risk Policy v2. |
| 140 | Chuẩn hóa Runbook v2. |
| 141 | Tổng hợp báo cáo chiến lược Trend, MR, Stat-arb, RL. |
| 142 | Tổng hợp Dashboard & equity curves demo & OOS. |
| 143 | Chuẩn hóa repo project. |
| 144 | Lập kế hoạch R&D quý tiếp theo. |
| 145 | Lưu file Markdown checklist hoàn chỉnh cho theo dõi. |
