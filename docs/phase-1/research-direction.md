
# NTUFC Quant Research Project
## Supply-Chain Information Diffusion and Cross-Sectional Return Predictability in Taiwan

**Status:** Research exploration / data feasibility validation  
**Target market:** Taiwan equities, initially semiconductor-related companies  
**Team:** 6 members  
**Methodological foundation:** Gu, Kelly & Xiu (2020)  
**Final presentation:** January 9, 2027  
**Report, slides, and GitHub deadline:** January 2, 2027  
**Initial topic proposal deadline:** November 29, 2026  

---

# 1. Executive Summary

## 1.1 Research Direction

We aim to investigate whether information about one firm's operating performance can predict subsequent stock returns of economically connected companies in Taiwan.

Our primary information source is the monthly revenue disclosure system in Taiwan, where listed companies regularly disclose their previous month's revenue.

We hypothesize that investors may not immediately incorporate information about one firm into the valuations of its suppliers, customers, or other economically connected firms.

The research combines:

- Financial economics and information diffusion
- Supply-chain relationships and economic networks
- Taiwan's monthly revenue disclosures
- Cross-sectional machine learning
- Event studies and statistical hypothesis testing
- Portfolio construction and realistic backtesting

The objective is not simply to improve predictive accuracy using additional features.

**We want to identify, explain, and empirically evaluate a specific mechanism of delayed information incorporation across economically connected companies.**

## 1.2 Working Research Question

> Does information from monthly revenue announcements propagate gradually and asymmetrically along Taiwan's semiconductor supply chain, and can these information delays generate out-of-sample stock-return predictability?

This remains a working question, subject to the literature review and data feasibility study.

## 1.3 Potential Paper Title

**Asymmetric Information Diffusion Along Taiwan's Semiconductor Supply Chain: Evidence from Monthly Revenue Announcements**

Alternative:

**Supply-Chain Information Networks and Cross-Sectional Return Predictability in Taiwan**

---

# 2. Academic Motivation

## 2.1 Economic Background

Financial markets may not immediately incorporate all available information into security prices.

When a company releases information about its operating performance, the announcement may contain information relevant to other companies.

For example:

1. Company A announces unexpectedly strong revenue.
2. Company B is a supplier of Company A.
3. Stronger revenue at A may indicate stronger demand for B's products.
4. Investors may not immediately incorporate this implication into B's valuation.
5. B's stock return may subsequently adjust.

This creates a potential cross-firm information transmission mechanism.

However, the economic interpretation is not necessarily positive.

Revenue growth at a customer could reflect increased purchasing, inventory accumulation, market-share changes, or other developments.

Therefore, the sign and magnitude of information transmission must be established empirically.

## 2.2 Why Taiwan?

Taiwan provides an interesting research environment because:

- Listed companies regularly disclose monthly revenue.
- Company-specific disclosure dates can differ.
- Taiwan has economically interconnected semiconductor-related industries.
- Public annual reports contain information about corporate relationships.
- TEJ and Bloomberg provide potentially useful historical financial data.
- Historical stock prices and some fundamental data are also available through public sources.

These features may enable more precise investigation of information transmission than quarterly-only disclosure environments.

## 2.3 Why This Is Not Just Generic Alpha Mining

Gu, Kelly & Xiu (2020) provide a general framework for forecasting stock returns using machine learning.

We intend to use a similar empirical workflow but investigate a specific economic mechanism.

| Generic ML Alpha Research | Our Proposed Research |
|---|---|
| Predict future returns | Study cross-firm information transmission |
| Use conventional stock characteristics | Construct economically motivated network features |
| Compare ML algorithms | Test a particular financial hypothesis |
| Maximize predictive performance | Explain when and why predictability exists |
| Evaluate IC and Sharpe | Evaluate statistical, economic, and trading implications |

**ML is our empirical tool, not the primary source of novelty.**

---

# 3. Literature Review

## 3.1 Core Methodological Foundation

### Gu, Kelly & Xiu (2020)
**Empirical Asset Pricing via Machine Learning**

Journal: The Review of Financial Studies

https://doi.org/10.1093/rfs/hhaa009

Main contribution:

- Systematic evaluation of ML methods for asset pricing.
- Nonlinear models can capture predictive interactions missed by simpler regressions.
- Momentum, liquidity, and volatility characteristics are important predictors.
- Evaluates both forecasting performance and economic portfolio performance.

Relevance:

Provides the methodological foundation for our cross-sectional forecasting, model comparison, and evaluation pipeline.

It is not our proposed novel contribution.

## 3.2 Economic Links and Delayed Information

### Cohen & Frazzini (2008)
**Economic Links and Predictable Returns**

Journal: The Journal of Finance

https://doi.org/10.1111/j.1540-6261.2008.01379.x

Main contribution:

- Documents return predictability across economically linked firms.
- Uses customer-supplier relationships.
- Connects delayed price adjustments with limited investor attention.

Relevance:

Foundational evidence that economic relationships can generate cross-asset predictability.

**Implication for novelty:** Simply demonstrating that supplier and customer returns predict one another would not be original.

### Menzly & Ozbas (2010)
**Market Segmentation and Cross-Predictability of Returns**

Journal: The Journal of Finance

https://doi.org/10.1111/j.1540-6261.2010.01578.x

Main contribution:

- Studies gradual information diffusion across economically related industries.
- Connects cross-predictability with investor specialization and market segmentation.
- Examines the influence of analyst coverage and institutional ownership.

Relevance:

Provides a theoretical basis for investigating whether information transmission depends on investor attention and market participation.

## 3.3 Taiwan Monthly Revenue Research

### Chen, Liu & Chiao (2022)
**Unexpected Monthly Revenue in the Taiwan Stock Market: A Comprehensive Analysis**

Journal: Journal of Management and Business Research

https://doi.org/10.6504/JMBR.202212_39(4).0003

Main contribution:

- Studies unexpected monthly revenue in Taiwan.
- Finds predictive information about future earnings growth and stock returns.
- Examines monthly versus quarterly information.
- Investigates institutional investor behavior before disclosures.

Relevance:

Provides a foundation for constructing revenue-surprise variables and understanding their relationship with stock returns.

**Implication for novelty:** A simple monthly revenue surprise strategy is insufficient.

## 3.4 Important Recent Overlapping Research

### Cai (2026)
**The Role of ETFs in Information Transmission: Evidence from Taiwan**

NTU Master's Thesis

https://tdr.lib.ntu.edu.tw/handle/123456789/102197

Main contribution:

- Investigates information transmission around monthly revenue announcements.
- Examines how earlier announcements from industry peers relate to other firms' returns.
- Studies the moderating role of ETF involvement.

Relevance:

This is particularly important because it studies cross-firm information transmission using Taiwan's monthly revenue disclosures.

**Our research must establish how an explicitly directed supply-chain network differs from an industry-peer information transmission approach.**

## 3.5 Portfolio Construction Literature (Secondary)

### Grinold & Kahn
**Active Portfolio Management**

Relevant concepts:

- Information Coefficient (IC)
- Information Ratio (IR)
- Breadth
- Transfer Coefficient
- Translation of predictive signals into portfolio performance

The Fundamental Law of Active Management provides an approximate relationship:

    IR ≈ IC × sqrt(BR)

Its extended form includes implementation efficiency:

    IR ≈ TC × IC × sqrt(BR)

These frameworks may help explain why statistically useful predictions do not necessarily generate strong portfolio performance.

Portfolio optimization is optional for our initial research and should not distract from the main hypothesis.

---

# 4. Proposed Research Contribution

We do not claim that supply-chain return predictability itself is new.

Our potential contribution is the combination of:

1. Company-level monthly revenue announcements.
2. Historically disclosed, directional supplier-customer relationships.
3. Event sequencing between connected firms.
4. Cross-sectional ML and interpretable econometric testing.
5. Economic mechanisms explaining heterogeneous information diffusion.

The main questions are:

- Does direction matter?
- Does announcement sequencing matter?
- Does investor attention moderate information transmission?
- Does the information add predictive value beyond industry-level signals?
- Can the relationship support a realistic trading strategy?

A successful paper should contribute new empirical evidence about at least one of these mechanisms.

The exact research gap remains **unverified** until the financial team completes a focused literature review.

---

# 5. Research Hypotheses

## H1 — Supply-Chain Information Transmission

**Null hypothesis (H0):**

Revenue surprises from economically connected companies have no incremental predictive content for a target firm's future returns after controlling for conventional firm characteristics and industry information.

**Alternative hypothesis (H1):**

Revenue surprises from connected firms provide incremental predictive information.

Proposed tests:

- Network revenue surprise versus own-company revenue surprise.
- Network information versus industry-average information.
- Actual company links versus placebo links.

## H2 — Asymmetric Information Diffusion

Information may propagate differently between:

- Customer → Supplier
- Supplier → Customer

Possible reasons include:

- Demand versus supply information
- Differences in bargaining power
- Differences in information visibility
- Different economic exposures
- Different levels of investor attention

We will test whether the direction of a disclosed commercial relationship changes return predictability.

We will not assume that the predictive effect has the same sign in both directions.

## H3 — Announcement Sequencing and Information Delay

Suppose Company A releases its monthly revenue before Company B.

If A and B are economically connected, A's announcement may contain information relevant to B before B releases its own revenue.

Hypothesis:

> Earlier revenue disclosures from economically connected companies predict subsequent returns of firms that have not yet announced.

This is the preferred event-study design.

It requires reliable company-specific disclosure dates.

## H4 — Conditional Information Diffusion

The magnitude and speed of information transmission may depend on:

- Firm size
- Stock liquidity
- Institutional investor activity
- Market volatility
- Supply-chain relationship direction
- Economic relationship importance

Potential mechanism:

Information diffusion may be slower when investors have less incentive or ability to analyze indirect corporate information.

This hypothesis is a secondary extension, not necessarily required for the minimum viable paper.

## H5 — Economic Value (Applied Extension)

A strategy incorporating network-based information may outperform a conventional forecasting strategy after accounting for:

- Transaction costs
- Portfolio constraints
- Liquidity
- Risk exposures
- Realistic trading delays

Strong forecasting results alone will not be considered evidence of profitable implementation.

---

# 6. Data Sources and Current Status

## 6.1 Available Data Infrastructure

| Data | Source | Status |
|---|---|---|
| Monthly corporate revenue | TEJ / FinMind / MOPS | Source identified |
| Revenue publication dates | TEJ | Documented; entitlement and export need testing |
| Historical stock prices | Bloomberg / TEJ / FinMind / yfinance | Available in principle |
| Supplier-customer relationships | MOPS annual reports | Extraction demonstrated |
| Historical relationship coverage | MOPS / Bloomberg | Not yet established |
| Institutional trading | TEJ / TWSE / FinMind | Optional |
| Annual product composition | TEJ Pro | Sample inspected |
| Risk and valuation characteristics | TEJ / Bloomberg / public data | To be selected |
| TEJ API | TEJ | Subscription access unconfirmed |

## 6.2 Monthly Revenue

Preferred source: TEJ, particularly point-in-time monthly revenue data.

Useful variables:

- Company ID
- Revenue reporting month
- Monthly revenue
- Original announcement date
- Initial versus corrected disclosure
- Previous-year comparable revenue
- Data availability timestamp

TEJ publicly documents PIT monthly revenue records and historical revisions.

However, our specific university subscription and extraction permissions still require confirmation.

### Alternative: FinMind

Dataset:

    TaiwanStockMonthRevenue

https://finmind.github.io/tutor/TaiwanMarket/Fundamental/

Advantages:

- Python access
- Historical Taiwan monthly revenue
- Convenient public-data integration

Limitations:

- Its `date` is not necessarily the true company announcement date.
- `create_time` is not the official MOPS release timestamp.
- Historical original disclosure dates are not reliably available.

Therefore:

**FinMind is useful for baseline revenue features, but TEJ is preferable for the event-driven information timing design.**

## 6.3 Historical Market Data

Potential sources:

- TEJ Pro
- Bloomberg Terminal
- FinMind
- yfinance
- TWSE / TPEx official historical records

Required variables:

- OHLCV
- Adjusted returns
- Dividends and corporate actions
- Market capitalization
- Industry classification
- Listing and delisting information
- Liquidity and trading restrictions

For final results, data must be checked for:

- Survivorship bias
- Delisting bias
- Corporate-action errors
- Adjusted-price consistency
- Stock suspensions
- Limit-up / limit-down conditions

yfinance is acceptable for early pipeline development but should not be the sole authoritative source for the final historical universe.

---

# 7. Company Relationship Dataset

## 7.1 What We Need

We aim to construct a directed graph:

    Supplier A → Customer B

For each relationship, record:

- Supplier ID
- Customer ID
- Relationship direction
- Relationship type
- Reporting company
- Source document
- Source page
- Disclosure date
- Relationship strength, if available
- Evidence quality
- Validity or expiration date, if established

The graph must be historically valid at every trading date.

## 7.2 Confirmed Extraction from TSMC's Annual Report

Source:

**TSMC Annual Report 2023 (I)**

Relevant sections:

- Pages 106–107: Raw Materials and Supply Chain Management
- Pages 108–109: Customer Trust
- Page 110: Major Customer Revenue Disclosures

This report contains:

- 33 distinct named supplier companies in material-category tables.
- 10 named customer companies.
- Anonymous major suppliers and customers with disclosed procurement/revenue shares.

### Examples of named suppliers

| Company | Material category |
|---|---|
| GlobalWafers | Raw wafers |
| SUMCO | Raw wafers |
| FST | Raw wafers |
| Siltronic | Raw wafers |
| Air Liquide | Chemicals and gases |
| Entegris | Chemicals, gases, and CMP materials |
| DuPont | Chemicals, lithography, and CMP materials |
| Wah Lee | Chemicals |
| Fujifilm Electronic Materials | Chemicals and other materials |

### Examples of named customers

| Company | Relationship |
|---|---|
| AMD | TSMC customer |
| Amazon Web Services | TSMC customer |
| Broadcom | TSMC customer |
| Infineon | TSMC customer |
| Intel | TSMC customer |
| MediaTek | TSMC customer |
| NVIDIA | TSMC customer |
| NXP | TSMC customer |
| Qualcomm | TSMC customer |
| Sony Semiconductor Solutions | TSMC customer |

These names are reported by TSMC.

However:

- Named companies are not necessarily Taiwan-listed.
- The report does not disclose transaction shares for all named firms.
- Some major customers and suppliers are anonymized.
- A named relationship does not establish its exact economic weight.
- The relationship must not be assumed to exist historically before the relevant disclosure.

### Anonymous counterparties

The report identifies:

- Two major suppliers as Company A and Company B.
- Two major customers as Customer A and Customer B.

Their procurement/revenue shares are disclosed.

**We must not guess their identities or assign their percentages to named companies.**

## 7.3 Historical Availability

The uploaded report is for fiscal year 2023.

The MOPS document listing shown during our data investigation identifies an upload timestamp of May 16, 2024.

For a conservative historical backtest, relationships extracted exclusively from this report should not be treated as available before its verified public disclosure date.

The fiscal year and the public availability date are different.

Older annual reports must be used to reconstruct relationships at earlier dates.

## 7.4 Relationship Sources

Priority:

1. MOPS historical annual reports
2. Bloomberg SPLC historical supply-chain data
3. TEJ relationship modules, if licensed
4. Company investor relations and historical disclosures
5. Public supply-chain maps, for discovering candidate relationships

Supporting information:

- TEJ annual product composition
- TPEx industry value-chain classifications

**Important distinction:**

Product composition is not a verified supplier-customer network.

TSMC selling 3nm or 5nm wafers does not tell us which companies directly buy those wafers.

Product composition may be used as an additional economic exposure feature.

## 7.5 Remaining Relationship Data Problems

### Problem A: Sparse Taiwan-listed network

Many of TSMC's explicitly named partners are foreign firms.

A network built around TSMC alone may contain too few Taiwan-listed tradable companies.

Solution:

Extract disclosures from multiple Taiwanese firms, especially:

- Semiconductor manufacturers
- IC designers
- Packaging and testing firms
- Materials suppliers
- Equipment suppliers
- Electronics manufacturers

Measure how many unique Taiwan-listed targets, directed edges, and historical announcement events remain.

### Problem B: Incomplete historical disclosure

Some firms do not name their customers or suppliers.

Solution:

- Extract the relationships that can be verified.
- Supplement with other contemporaneous disclosures.
- Preserve missing or unknown relationships as unknown.
- Avoid assuming that an undisclosed edge does not exist.

### Problem C: Relationship strength

Named relationships may lack transaction amounts.

Solution:

Start with binary link weights.

Possible later extensions:

- Disclosed revenue dependence
- Disclosed procurement dependence
- Source-based confidence
- Category-specific exposure

Do not infer exact transaction shares without evidence.

### Problem D: Relationship staleness

A relationship disclosed in 2021 may have ended by 2024.

Solution:

Evaluate several approaches:

- Annual network snapshots
- Conservative relationship expiration rules
- Sensitivity tests with different staleness windows

A reporting-date window is a research assumption, not proof that the relationship remained economically active.

---

# 8. Research Design

## 8.1 Preferred Design: Event-Driven Information Diffusion

Example:

1. Company A announces unexpectedly high monthly revenue.
2. Company B is a previously disclosed supplier or customer.
3. Company B has not yet announced its own monthly revenue.
4. We construct a signal for B using A's announcement.
5. We measure B's subsequent abnormal returns.

This directly investigates whether information moves between companies before all relevant earnings information is published.

### Event Timeline

    A's revenue announced
             |
             v
    Information enters public market
             |
             v
    Construct signal for connected firm B
             |
             v
    Trade only after information is available
             |
             v
    Measure B's subsequent returns
             |
             v
    End event window or censor at B's own announcement

The final event-window definition must account for announcement clustering and overlapping events.

## 8.2 Conservative Alternative Design

If exact revenue announcement dates are unavailable:

- Wait until the required monthly revenue information is publicly available.
- Construct supply-chain signals using a common information cutoff.
- Predict subsequent 5-day or 20-day stock returns.

Alternative research question:

> Does supply-chain revenue information contain incremental predictive value after controlling for own-firm and industry information?

This is less directly about early announcement sequencing, but it remains a defensible empirical study.

---

# 9. Feature Engineering

## 9.1 Conventional Cross-Sectional Features

Baseline features:

- Short-term reversal
- 1-month momentum
- 3-month momentum
- Volatility
- Trading volume
- Turnover
- Market capitalization
- Liquidity
- Industry indicators

Optional:

- Valuation ratios
- Institutional flows
- Fundamental growth indicators

All features must be computed using historical information available at the decision time.

## 9.2 Monthly Revenue Surprise

Let:

    R(i,m) = firm i's revenue for month m
    E[R(i,m)] = forecast based on previously available data

Define:

    Surprise(i,m) = (R(i,m) - E[R(i,m)]) / E[R(i,m)]

Possible expectation models:

1. Same-month-last-year benchmark
2. Trailing seasonally adjusted growth
3. Historical time-series forecast
4. Cross-sectional expected revenue model

The denominator and treatment of nonpositive forecasts require care.

The basic model should use a transparent and reproducible definition.

## 9.3 Network Revenue Surprise

For firm i at decision time t:

    NS(i,t) = Σ_j w(i,j,t) × Surprise(j,t)

where:

- j is an economically connected company.
- w(i,j,t) is an edge weight known at t.
- Surprise(j,t) is included only after j's disclosure is public.

The implemented signal must define the aggregation window precisely.

Separate features should be constructed for:

- Customer-originated information
- Supplier-originated information
- Same-industry information
- Firm's own revenue information

## 9.4 Potential Advanced Features

Only if data support them:

- Number of connected firms announcing recently
- Weighted average revenue surprise
- Fraction of connected firms with positive surprises
- Upstream versus downstream information imbalance
- Network degree
- Concentration of connected-firm information
- Interaction with institutional flow
- Interaction with liquidity and volatility

Graph neural networks are not required.

A small, sparse historical network may be better analyzed using transparent engineered network features.

---

# 10. Modeling Plan

## 10.1 Model Selection Principles

The objective is to test financial hypotheses.

Model complexity should increase only when justified by the data and research question.

## 10.2 Initial Models

| Model | Purpose |
|---|---|
| Historical mean / simple ranking | Naive baseline |
| OLS | Interpretable empirical benchmark |
| Ridge | Regularized linear baseline |
| Lasso | Feature selection and sparsity |
| LightGBM | Nonlinearities and interactions |
| Ensemble | Optional robustness extension |

Deep learning is optional.

We should not use a neural network merely to claim higher project difficulty.

## 10.3 Core Comparisons

| Model | Feature set |
|---|---|
| M0 | Conventional price-volume characteristics |
| M1 | M0 + own monthly revenue surprise |
| M2 | M1 + industry-average revenue surprise |
| M3 | M2 + network-based surprise |
| M4 | M3 + directional network information |
| M5 | M4 + attention / institutional-flow interactions |

This design aims to isolate the marginal contribution of each information source.

## 10.4 Placebo and Ablation Tests

Important tests:

- Remove network features.
- Replace actual links with shuffled links.
- Preserve industry structure when creating network placebos.
- Compare network signals with ordinary peer momentum.
- Compare actual relationships with industry-only connections.
- Compare forward and reverse information directions.

A successful model is not sufficient.

**We need evidence that actual economic relationships matter.**

---

# 11. Statistical Evaluation

## 11.1 Predictive Performance

Metrics:

- Pearson IC
- Rank IC
- Out-of-sample R²
- IC by market regime
- IC by sector and liquidity group
- Prediction stability across time

Rank IC and Pearson IC are different statistics.

For a conditional event study, we should also evaluate directly whether network information predicts future abnormal returns.

## 11.2 Econometric Tests

Possible methods:

- Cross-sectional regressions
- Fama-MacBeth regressions
- Panel regressions
- Event studies
- Interaction-effect tests

Potential controls:

- Market return
- Industry return
- Firm size
- Liquidity
- Momentum
- Volatility
- Firm's own revenue surprise

Inference should account for:

- Cross-firm dependence
- Calendar-time effects
- Repeated firm observations
- Overlapping event windows
- Multiple hypothesis testing

Use appropriate clustered or time-series-robust inference rather than treating every event as independent.

## 11.3 Economic Interpretation

We want to answer:

- Is information transmitted?
- In which direction?
- How rapidly?
- Is the effect economically substantial?
- Which firm characteristics explain the effect?
- Does it survive conventional industry and momentum controls?

A statistically significant relationship is not automatically a tradable strategy.

---

# 12. Backtesting and Portfolio Evaluation

## 12.1 Initial Portfolio

Start with simple portfolios:

- Rank securities by predicted returns.
- Buy the strongest candidates.
- Compare against an appropriate benchmark.
- Optionally evaluate a theoretical long-short strategy.

For Taiwan, a long-only or benchmark-relative strategy may be more realistic than unconstrained short selling.

## 12.2 Portfolio Construction Extensions

Possible methods:

1. Equal-weight ranking
2. Value-weighted ranking
3. Inverse-volatility weighting
4. Constrained mean-variance optimization

The standard MVO objective is:

    maximize:
        alpha_hat' * w - (lambda / 2) * w' * Sigma_hat * w

Possible extensions:

- Transaction-cost penalty
- Sector neutrality
- Position limits
- Liquidity constraints
- Turnover constraints

MVO is a possible extension, not the core research contribution.

## 12.3 Backtest Metrics

Report:

- Annualized returns
- Sharpe ratio
- Information Ratio
- Maximum drawdown
- Turnover
- Transaction costs
- Exposure concentration
- Performance by market regime
- Performance against simple benchmarks

## 12.4 Taiwan-Specific Trading Limitations

Consider:

- Brokerage fees
- Securities transaction tax
- Bid-ask spread
- Market impact
- Price limits
- Trading suspensions
- Short-sale availability
- Borrowing costs
- Low-liquidity stocks

Avoid claiming that a theoretical long-short portfolio is fully implementable without verifying shorting conditions.

---

# 13. Major Research Risks and Solutions

| Risk | Why it matters | Proposed solution |
|---|---|---|
| Look-ahead bias | Future information leaks into historical signals | Explicit information-availability timestamps |
| Revenue revisions | Corrected observations replace original data | TEJ PIT records or audited original disclosures |
| Historical network leakage | Current relationships used in past periods | Dated annual-report snapshots |
| Sparse network | Too few Taiwan-listed connected firms | Expand reporting-company universe |
| Missing relationships | Disclosures are incomplete | Document sample selection and coverage |
| Anonymous customers | Counterparty identity unknown | Do not infer identities |
| Weak relationship weights | Transaction sizes not disclosed | Binary links initially |
| Industry confounding | Network signals proxy for sector trends | Industry baselines and network placebos |
| Common macroeconomic news | Multiple firms react to the same shock | Market/industry controls and event timing |
| Survivorship bias | Only current listed firms retained | Include delisted companies where possible |
| Event-window contamination | Target firm releases its own information | Censor or explicitly model overlapping announcements |
| Data-snooping | Many specifications tested repeatedly | Predefine primary hypotheses and preserve final test data |
| Small sample | Complex models overfit | Prefer simple models; validate statistical power |
| Trading frictions | Paper alpha may not be monetizable | Cost-aware backtests |
| Proprietary data redistribution | Bloomberg / TEJ license restrictions | Keep licensed raw data out of public GitHub |

---

# 14. Technical Pipeline Architecture

## 14.1 Overall Workflow

    Data Sources
        |
        v
    Data Ingestion
        |
        v
    Data Cleaning & Validation
        |
        v
    Point-in-Time Data Alignment
        |
        v
    Historical Relationship Network
        |
        v
    Feature Engineering
        |
        v
    Target / Label Construction
        |
        v
    Train / Validation / Test
        |
        v
    Model Training
        |
        v
    Prediction & Signal Generation
        |
        v
    Portfolio Construction
        |
        v
    Backtesting
        |
        v
    Statistical & Economic Evaluation

## 14.2 Suggested Repository Structure

    quant-research/
    ├── README.md
    ├── RESEARCH_PLAN.md
    ├── pyproject.toml
    ├── configs/
    ├── data/
    │   └── public_samples/
    ├── src/
    │   ├── ingestion/
    │   ├── cleaning/
    │   ├── point_in_time/
    │   ├── networks/
    │   ├── features/
    │   ├── models/
    │   ├── portfolios/
    │   ├── backtesting/
    │   └── evaluation/
    ├── tests/
    ├── notebooks/
    ├── experiments/
    ├── literature/
    └── reports/

Exclude licensed raw Bloomberg and TEJ data from the public repository.

## 14.3 Validation Requirements

Tests should include:

- No feature timestamps after decision timestamps.
- No target return leakage into training features.
- Proper train/validation/test separation.
- Correct handling of overlapping labels.
- Correct portfolio weight normalization.
- Correct accounting for transaction costs.
- Reproducible results with fixed seeds.
- Accurate corporate-action handling.

Vibe-coding is acceptable for development efficiency, but generated code must be inspected and tested.

---

# 15. First Two Weeks: Project Organization

## 15.1 Team Structure

Two parallel teams of three members.

### Technical Team

Primary responsibilities:

- Establish the repository and development environment.
- Build the research pipeline.
- Retrieve public stock-market data.
- Implement simple features and labels.
- Test OLS/Ridge/LightGBM baselines.
- Create a minimal portfolio backtest.
- Verify statistical and accounting correctness.

The initial objective is a **reproducible research pipeline**, not positive alpha.

### Financial Research Team

Primary responsibilities:

- Read the relevant academic literature.
- Identify the precise research gap.
- Formulate falsifiable hypotheses.
- Construct and verify company relationships.
- Evaluate data coverage.
- Develop the proposed economic mechanism.
- Determine whether the original event-driven design is feasible.

The initial objective is a **defensible research proposal**, not a collection of speculative trading ideas.

Subgroup leadership can rotate at agreed milestones while task ownership remains stable.

## 15.2 Week 1

### Technical Team

- Set up GitHub.
- Download a small Taiwan stock universe.
- Create baseline momentum and volatility features.
- Build forward-return labels.
- Implement an end-to-end baseline.
- Establish time-alignment and data-quality tests.

### Financial Team

- Read Cohen & Frazzini (2008).
- Read Menzly & Ozbas (2010).
- Read Chen et al. (2022).
- Review Cai (2026).
- Extract a small relationship network from historical annual reports.
- Verify monthly revenue publication-date accessibility.

### Joint Checkpoint

Discuss:

- What the literature already establishes.
- Whether the proposed contribution remains distinct.
- Which data are available.
- Whether the pipeline supports event-time features.

## 15.3 Week 2

### Technical Team

- Refine the pipeline.
- Add baseline model comparisons.
- Build a modular feature interface.
- Run reproducibility tests.
- Prototype a toy network feature using verified historical disclosures.

### Financial Team

- Expand relationship extraction to multiple reporting firms.
- Measure Taiwan-listed network coverage.
- Construct a small event dataset.
- Compare the potential contribution against existing literature.
- Prepare a research proposal and hypotheses.

### Joint Checkpoint

Demonstrate:

- A working baseline ML/backtesting pipeline.
- A historically dated company-relationship sample.
- Revenue availability and announcement-date checks.
- A feasible statistical research design.
- A decision on the primary research direction.

---

# 16. Feasibility Decision Gates

## Gate A — Revenue Data

Proceed if:

- Historical revenue values are available.
- Announcement dates can be retrieved or conservatively approximated.
- Original versus revised values can be handled appropriately.

## Gate B — Company Relationships

Proceed if:

- Named company links can be extracted.
- Relationship direction is identifiable.
- Public disclosure dates are recorded.
- Enough historically connected Taiwan-listed companies remain for analysis.

## Gate C — Statistical Power

Proceed if:

- There are enough independent events or company-month observations.
- There is enough variation in announcement sequencing.
- The sample is large enough for at least simple statistical models.

We should calculate sample coverage before committing to sophisticated ML.

## Gate D — Research Novelty

Proceed if:

- The question differs meaningfully from existing papers.
- The hypotheses are falsifiable.
- The research offers a plausible economic contribution.
- The main empirical tests are feasible by January 2.

If these gates fail, narrow the scope or use a related research question.

---

# 17. Backup Research Directions

## Backup A — Post-Disclosure Supply-Chain Information Value

If exact announcement sequencing cannot be reconstructed:

> Does supply-chain revenue information improve future return prediction after all relevant monthly disclosures become public?

This retains network-based features while reducing event-timing requirements.

## Backup B — Product-Level Economic Exposure

If directed company relationships are too sparse:

> Do shared product exposures or complementary production-stage exposures explain cross-sectional information diffusion in Taiwan's semiconductor industry?

Use historical TEJ product composition and public industry classifications.

This is not equivalent to direct supplier-customer information transmission and must be presented as a different mechanism.

## Backup C — Institutional Disagreement and Momentum Failure

If the network dataset is infeasible:

> Can disagreements between foreign and domestic institutional investors predict the continuation or reversal of cross-sectional momentum in Taiwan?

Potential public data:

- TWSE institutional activity
- TEJ historical institutional trading
- FinMind

This is a lower-data-risk research direction that fits the same ML pipeline.

---

# 18. Timeline and Deadlines

| Period | Objective | Deliverable |
|---|---|---|
| Early November | Literature and data feasibility | Research candidates and proof-of-concept data |
| First 2 weeks | Pipeline and hypothesis exploration | Working baseline and proposed hypotheses |
| November 17–29 | Select and prototype primary hypothesis | Initial topic proposal |
| November 29 | Topic proposal deadline | Topic, references, 300+ word explanation |
| Late November–Mid December | Main implementation | Empirical results and initial strategy |
| Mid–Late December | Robustness, debugging and improvement | Validated results and report draft |
| January 2 | Submission | Written report, slides and GitHub |
| January 3–8 | Presentation preparation | Rehearsal and Q&A preparation |
| January 9 | Final presentation | 15-minute presentation and Q&A |

All final experiments should be completed before the January 2 submission deadline.

---

# 19. What Counts as a Successful Research Project?

The project does not need to discover a profitable strategy to make an academic contribution.

Successful outcomes could include:

### Positive finding

We identify a statistically reliable information-diffusion effect and demonstrate incremental predictive or economic value.

### Conditional finding

We discover that information transmission depends on relationship direction, disclosure sequence, or investor attention.

### Negative finding

We find that apparent supply-chain alpha disappears after controlling for industry movements, information timing, or trading costs.

A carefully designed negative result can still be informative.

However, claims must be proportional to the sample size, identification strategy, and robustness of the evidence.

---

# 20. Immediate Next Actions

## Data

- [ ] Confirm TEJ API entitlement.
- [ ] Verify monthly revenue publication-date exports.
- [ ] Verify original versus revised monthly revenue access.
- [ ] Build a historical stock-price sample.
- [ ] Download annual reports for multiple Taiwan semiconductor companies.
- [ ] Extract named supplier/customer links.
- [ ] Record each relationship's source and publication date.
- [ ] Count unique Taiwan-listed nodes and usable directed edges.

## Research

- [ ] Read four core papers.
- [ ] Identify the closest competing research.
- [ ] Decide whether the contribution focuses on direction, sequencing, or attention.
- [ ] Specify primary and secondary hypotheses.
- [ ] Define baseline signals.
- [ ] Define a primary event window.
- [ ] Design the industry and shuffled-network placebo tests.

## Technical

- [ ] Create repository.
- [ ] Establish data schemas.
- [ ] Build baseline feature engineering.
- [ ] Implement Ridge and LightGBM.
- [ ] Implement chronological validation.
- [ ] Implement simple portfolio backtesting.
- [ ] Create leakage and accounting unit tests.
- [ ] Document reproducibility.

---

# 21. References and Data Resources

## Academic Papers

1. Gu, S., Kelly, B., & Xiu, D. (2020).
   Empirical Asset Pricing via Machine Learning.
   *The Review of Financial Studies*, 33(5), 2223–2273.
   https://doi.org/10.1093/rfs/hhaa009

2. Cohen, L., & Frazzini, A. (2008).
   Economic Links and Predictable Returns.
   *The Journal of Finance*, 63(4), 1977–2011.
   https://doi.org/10.1111/j.1540-6261.2008.01379.x

3. Menzly, L., & Ozbas, O. (2010).
   Market Segmentation and Cross-Predictability of Returns.
   *The Journal of Finance*, 65(4), 1555–1580.
   https://doi.org/10.1111/j.1540-6261.2010.01578.x

4. Chen, J.-C., Liu, Y.-R., & Chiao, C. (2022).
   Unexpected Monthly Revenue in the Taiwan Stock Market:
   A Comprehensive Analysis.
   *Journal of Management and Business Research*, 39(4), 503–545.
   https://doi.org/10.6504/JMBR.202212_39(4).0003

5. Cai, Y.-M. (2026).
   The Role of ETFs in Information Transmission:
   Evidence from Taiwan.
   National Taiwan University Master's Thesis.
   https://tdr.lib.ntu.edu.tw/handle/123456789/102197

## Primary Company Evidence

6. Taiwan Semiconductor Manufacturing Company (2023).
   *TSMC Annual Report 2023 (I)*.
   Relevant sections: 5.3.5 and 5.4.1.
   Original annual report obtained from TWSE electronic filings.

## Data Resources

7. TEJ Monthly Sales
   https://www.tejwin.com/en/product-services/financial-data/monthly-sales/

8. TEJ Point-in-Time Monthly Revenue Research Note
   https://www.tejwin.com/en/insight/monthly-revenue-info-part1/

9. FinMind Taiwan Market Fundamental Data
   https://finmind.github.io/tutor/TaiwanMarket/Fundamental/

10. Market Observation Post System (MOPS)
    https://mops.twse.com.tw/

11. Taiwan Stock Exchange
    https://www.twse.com.tw/

12. Bloomberg Supply Chain Analysis (SPLC)
    Historical network availability and export permissions
    must be verified under our Bloomberg access.

---

# 22. Final Research Philosophy

Our objective is not simply to train a complex ML model that achieves a high Sharpe ratio.

We want to conduct a coherent, reproducible empirical investigation of an economically motivated research question.

The central research process is:

**Financial theory → Research hypothesis → Data construction → Statistical tests → ML forecasting → Backtesting → Economic interpretation**

The proposed novel contribution is not the use of machine learning itself.

It is the empirical investigation of whether, how, and under what conditions operating information propagates across economically connected Taiwanese companies.

The first two weeks should determine whether this contribution can be established credibly using our available data and time.

**Current status: promising research direction; historical network coverage, event-timing access, statistical power, and precise novelty remain to be validated.**
