import pandas as pd
import numpy as np
import yfinance as yf
import warnings
import os
import time
import subprocess
from datetime import datetime

warnings.filterwarnings('ignore')

# ==========================================
# 1. YOUR TICKER UNIVERSE
# ==========================================
def get_all_ordinaries_tickers():
    return [
        "4DX.AX", "29M.AX", "ABG.AX", "ASK.AX", "AX1.AX", "AIH.AX", "AIS.AX", "A1G.AX", "AFP.AX", "AGL.AX", 
        "A1M.AX", "AGI.AX", "AIZ.AX", "AAI.AX", "ALK.AX", "A4N.AX", "ALQ.AX", "AMA.AX", "AMH.AX", "AMC.AX", 
        "AOV.AX", "AEL.AX", "AMP.AX", "ALD.AX", "ASL.AX", "ANN.AX", "AZY.AX", "ANZ.AX", "APA.AX", "APX.AX", 
        "ARU.AX", "ARB.AX", "ARF.AX", "ALI.AX", "ARG.AX", "ALL.AX", "AYA.AX", "APZ.AX", "AAR.AX", "ATR.AX", 
        "ASX.AX", "ALX.AX", "AUB.AX", "AIA.AX", "AMI.AX", "AZJ.AX", "AUC.AX", "ABB.AX", "ASB.AX", "AAC.AX", 
        "ACL.AX", "AEF.AX", "AFG.AX", "AFI.AX", "ASM.AX", "AUI.AX", "ASG.AX", "BOQ.AX", "BMN.AX", "BAP.AX", 
        "BCI.AX", "BPT.AX", "BLX.AX", "BCN.AX", "BTL.AX", "BGA.AX", "BGL.AX", "BFG.AX", "BEN.AX", "BNZ.AX", 
        "BHP.AX", "BKI.AX", "BC8.AX", "SQ2.AX", "BSL.AX", "BMC.AX", "BML.AX", "BOE.AX", "BOC.AX", "BRN.AX", 
        "BXB.AX", "BVS.AX", "BRE.AX", "BRG.AX", "BTR.AX", "BGP.AX", "BFL.AX", "BWP.AX", "CAY.AX", "CMM.AX", 
        "CSC.AX", "CAR.AX", "CDP.AX", "CIN.AX", "CYL.AX", "CAT.AX", "CWP.AX", "CTM.AX", "CNI.AX", "CIP.AX", 
        "COF.AX", "CHN.AX", "CEL.AX", "CGF.AX", "CIA.AX", "CHI.AX", "CHC.AX", "CLW.AX", "CQR.AX", "CQE.AX", 
        "CNU.AX", "C79.AX", "CVL.AX", "CU6.AX", "CWY.AX", "CVW.AX", "CUV.AX", "CBO.AX", "COH.AX", "CDA.AX", 
        "CGS.AX", "COL.AX", "CKF.AX", "CBA.AX", "CPU.AX", "CEN.AX", "CXO.AX", "CRN.AX", "CTD.AX", "CCP.AX", 
        "CMW.AX", "CSL.AX", "CCL.AX", "DBI.AX", "DTL.AX", "DTR.AX", "DYL.AX", "DRR.AX", "DVP.AX", "DXS.AX", 
        "DXC.AX", "DXI.AX", "DDR.AX", "DGT.AX", "DUI.AX", "DJW.AX", "DN1.AX", "DMP.AX", "DOW.AX", "DPM.AX", 
        "DRO.AX", "DUR.AX", "DNL.AX", "APE.AX", "EBO.AX", "EBR.AX", "EIQ.AX", "ELD.AX", "EOS.AX", "ELV.AX", 
        "ELS.AX", "EHL.AX", "EMR.AX", "EDV.AX", "EOL.AX", "ERA.AX", "EQR.AX", "EQT.AX", "EUR.AX", "EVN.AX", 
        "EVT.AX", "FID.AX", "FDR.AX", "FCL.AX", "FFM.AX", "FPH.AX", "FPR.AX", "FBU.AX", "FLT.AX", "FML.AX", 
        "FRS.AX", "FMG.AX", "FRW.AX", "FGX.AX", "FGG.AX", "GLN.AX", "GDI.AX", "GLF.AX", "GDG.AX", "GNE.AX", 
        "GMD.AX", "GTK.AX", "GNP.AX", "GMG.AX", "GPT.AX", "GQG.AX", "GNC.AX", "GGP.AX", "GNG.AX", "GOZ.AX", 
        "GCI.AX", "GYG.AX", "GWA.AX", "HSN.AX", "HVN.AX", "HLS.AX", "HCW.AX", "HGH.AX", "HM1.AX", "HLI.AX", 
        "HMC.AX", "HDN.AX", "HZN.AX", "HCH.AX", "HUB.AX", "HUM.AX", "IEL.AX", "IGO.AX", "ILU.AX", "IMD.AX", 
        "IMR.AX", "IFT.AX", "INA.AX", "ING.AX", "IFL.AX", "IAG.AX", "IDX.AX", "INR.AX", "IPG.AX", "IPX.AX", 
        "IPH.AX", "IRE.AX", "IGL.AX", "JHX.AX", "JBH.AX", "JDO.AX", "JIN.AX", "JMS.AX", "KSC.AX", "KAR.AX", 
        "KLS.AX", "KSL.AX", "KCN.AX", "KKC.AX", "KGN.AX", "GLS.AX", "L1G.AX", "LSF.AX", "LRV.AX", "LFS.AX", 
        "LLC.AX", "LGI.AX", "LFG.AX", "360.AX", "LIC.AX", "LNW.AX", "LIN.AX", "LTR.AX", "LOT.AX", "LOV.AX", 
        "LYL.AX", "LYC.AX", "MGH.AX", "MAH.AX", "MQG.AX", "MAQ.AX", "MA1.AX", "MAD.AX", "MAF.AX", "MFG.AX", 
        "MAU.AX", "MC2.AX", "MMS.AX", "MM8.AX", "MPL.AX", "MEK.AX", "MP1.AX", "MCY.AX", "MEZ.AX", "MSB.AX", 
        "MTM.AX", "MLX.AX", "MTS.AX", "MEI.AX", "MOT.AX", "MXT.AX", "MMI.AX", "MFF.AX", "MGX.AX", "MIN.AX", 
        "MI6.AX", "MIR.AX", "MGR.AX", "MND.AX", "MYR.AX", "MYS.AX", "NAN.AX", "NAB.AX", "NSR.AX", "NGI.AX", 
        "NWL.AX", "NEU.AX", "NHC.AX", "NEM.AX", "NMG.AX", "NWS.AX", "NXG.AX", "NXT.AX", "NHF.AX", "NIC.AX", 
        "NCK.AX", "NEC.AX", "NST.AX", "NVA.AX", "NWH.AX", "NUF.AX", "NXL.AX", "OCL.AX", "OCA.AX", "OMA.AX", 
        "OBL.AX", "OML.AX", "OPH.AX", "OPT.AX", "OBM.AX", "ORI.AX", "ORG.AX", "ORA.AX", "PAC.AX", "PDN.AX", 
        "PNR.AX", "PGC.AX", "PPC.AX", "PIA.AX", "PE1.AX", "PPM.AX", "PRN.AX", "PCI.AX", "PIC.AX", "PPT.AX", 
        "PRU.AX", "PXA.AX", "PNI.AX", "PL8.AX", "PLS.AX", "PGF.AX", "PMT.AX", "PBH.AX", "PNV.AX", "PPS.AX", 
        "PDI.AX", "PMV.AX", "PME.AX", "PFP.AX", "PSC.AX", "PWH.AX", "PYC.AX", "QAN.AX", "QBE.AX", "QOR.AX", 
        "QAL.AX", "QRI.AX", "QUB.AX", "RAC.AX", "RMS.AX", "RHC.AX", "REA.AX", "RHI.AX", "RDX.AX", "REH.AX", 
        "RG8.AX", "RF1.AX", "RG1.AX", "RPL.AX", "RGN.AX", "REG.AX", "RRL.AX", "RWC.AX", "RMC.AX", "RMD.AX", 
        "RSG.AX", "REV.AX", "SGLLV.AX", "RIC.AX", "RIO.AX", "RXR.AX", "RXL.AX", "RFF.AX", "RYM.AX", "SFR.AX", 
        "SMI.AX", "STO.AX", "SCG.AX", "SEK.AX", "SHV.AX", "SRV.AX", "SSM.AX", "SGH.AX", "SHA.AX", "SIG.AX", 
        "SLX.AX", "SVL.AX", "SGM.AX", "SDR.AX", "SKS.AX", "SKC.AX", "SKT.AX", "SIQ.AX", "SPZ.AX", "SVR.AX", 
        "SHL.AX", "S32.AX", "SXE.AX", "SX2.AX", "SVM.AX", "SPK.AX", "SRG.AX", "SMR.AX", "SBM.AX", "SDF.AX", 
        "SST.AX", "SGQ.AX", "SGP.AX", "STK.AX", "STX.AX", "SNZ.AX", "SUN.AX", "SRL.AX", "SLC.AX", "SUL.AX", 
        "SNL.AX", "SYL.AX", "TAH.AX", "TBN.AX", "TEA.AX", "TNE.AX", "TLX.AX", "TLS.AX", "TPW.AX", "A2M.AX", 
        "TLC.AX", "SGR.AX", "TTT.AX", "TVN.AX", "TOK.AX", "TOR.AX", "TRE.AX", "THL.AX", "TWR.AX", "TPG.AX", 
        "TCL.AX", "TWE.AX", "TBR.AX", "TUA.AX", "TGN.AX", "TCG.AX", "TRA.AX", "TYR.AX", "USL.AX", "UNI.AX", 
        "VAU.AX", "VNT.AX", "VCX.AX", "VGN.AX", "VGL.AX", "VEA.AX", "VUL.AX", "VSL.AX", "VYS.AX", "WA1.AX", 
        "WGN.AX", "WAM.AX", "WGB.AX", "WMX.AX", "WLE.AX", "WMI.AX", "SOL.AX", "WPR.AX", "WQG.AX", "WEB.AX", 
        "WBT.AX", "WES.AX", "WAF.AX", "WGX.AX", "WBC.AX", "WWI.AX", "WHI.AX", "WHF.AX", "WHC.AX", "WIA.AX", 
        "WC8.AX", "WTN.AX", "WTC.AX", "WDS.AX", "WOW.AX", "WOR.AX", "XRO.AX", "YAL.AX", "ZIM.AX", "ZIP.AX", 
        "VAS.AX", "VGS.AX", "IVV.AX", "A200.AX", "IOZ.AX", "QUAL.AX", "NDQ.AX", "VHY.AX", "DACE.AX", "STW.AX", 
        "VGAD.AX", "VTS.AX", "MGOC.AX", "VEU.AX", "IOO.AX", "AAA.AX", "DGCE.AX", "VBND.AX", "DFGH.AX", "IAF.AX", 
        "VDHG.AX", "ETHI.AX", "SUBD.AX", "VAF.AX", "BGBL.AX", "IHVV.AX", "HYGG.AX", "MVW.AX", "VAP.AX", "HBRD.AX", 
        "QHAL.AX", "HGBL.AX", "QPON.AX", "ETPMAG.AX", "IFRA.AX", "CRED.AX", "GDX.AX", "VGE.AX", "QAU.AX", "GLIN.AX", 
        "QSML.AX", "IEM.AX", "IWLD.AX", "VDGR.AX", "IAA.AX", "IXJ.AX", "FANG.AX", "VGB.AX", "CIIH.AX", "PMGOLD.AX"
    ]

# ==========================================
# 2. DATA UTILITIES
# ==========================================
def download_data_robust(tickers, period='5y'):
    print(f"FETCH: Individual Download of {len(tickers)} Symbols...")
    historical_data = {}
    for i, ticker in enumerate(tickers):
        if (i + 1) % 50 == 0:
            print(f"STAMP: Fetched {i+1}...")
            time.sleep(2)
        try:
            df = yf.download(ticker, period=period, interval='1d', progress=False, threads=False)
            if not df.empty and 'Close' in df.columns:
                if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
                df = df[['Open', 'High', 'Low', 'Close', 'Volume']].dropna()
                if len(df) >= 200: historical_data[ticker] = df
        except: pass
    return historical_data

# ==========================================
# 3. BACKTEST ENGINE
# ==========================================
def execute_stepped_simulation(data_dict, market_data, params):
    cash = 100000.0
    positions = {}
    trade_history = []
    peak_equity = 100000.0
    max_drawdown = 0.0
    equity_curve = []

    inds = {}
    for t, df in data_dict.items():
        df = df.copy()
        df['SMA50'] = df['Close'].rolling(50).mean()
        df['SMA150'] = df['Close'].rolling(150).mean()
        df['SMA200'] = df['Close'].rolling(200).mean()
        df['SMA200_20'] = df['SMA200'].shift(20)
        df['52W_H'] = df['High'].rolling(252).max()
        df['52W_L'] = df['Low'].rolling(252).min()
        df['Vol_50'] = df['Volume'].rolling(50).mean()
        tr = pd.concat([(df['High']-df['Low']), (df['High']-df['Close'].shift()).abs(), (df['Low']-df['Close'].shift()).abs()], axis=1).max(axis=1)
        df['ATR_10'] = tr.ewm(alpha=1/10, adjust=False).mean()
        df['ATR_40'] = tr.ewm(alpha=1/40, adjust=False).mean()
        df['VCP'] = df['ATR_10'] / df['ATR_40']
        inds[t] = df.dropna()

    market_df = pd.DataFrame({'Close': market_data['Close'].squeeze()}).dropna()
    market_df['EMA20'] = market_df['Close'].ewm(span=20, adjust=False).mean()
    market_df['SMA50'] = market_df['Close'].rolling(50).mean()
    
    all_dates = market_df.dropna().index

    for date in all_dates:
        m_c, m_e, m_s = float(market_df.loc[date, 'Close']), float(market_df.loc[date, 'EMA20']), float(market_df.loc[date, 'SMA50'])
        market_up = (m_c > m_e) and (m_e > m_s)
        
        current_equity = cash
        open_profit = 0
        for t, pos in positions.items():
            if date in inds[t].index:
                cv = pos['shares'] * float(inds[t].loc[date, 'Close'])
                current_equity += cv
                open_profit += (cv - (pos['shares'] * pos['entry_p']))
        
        equity_curve.append(current_equity)
        peak_equity = max(peak_equity, current_equity)
        max_drawdown = max(max_drawdown, (peak_equity - current_equity) / peak_equity)

        to_sell = []
        for t, pos in positions.items():
            if date not in inds[t].index: continue
            r = inds[t].loc[date]
            if not pos['be']:
                if float(r['High']) >= pos['entry_p'] + (1.5 * pos['risk_ps']):
                    pos['stop'] = pos['entry_p'] * 1.002
                    pos['be'] = True
            if float(r['High']) >= pos['target']: to_sell.append((t, pos['target'], "Target"))
            elif float(r['Low']) <= pos['stop']: to_sell.append((t, pos['stop'], "Stop"))
            elif (date - pos['entry_d']).days >= 28 and float(r['Close']) < pos['entry_p']: to_sell.append((t, float(r['Close']), "TimeStop"))

        for t, pr, rs in to_sell:
            rev = (positions[t]['shares'] * pr) * 0.999
            cash += rev
            trade_history.append({'Ticker': t, 'Profit $': rev - (positions[t]['shares'] * positions[t]['entry_p'])})
            del positions[t]

        if market_up and (len(positions) == 0 or (len(positions) < 4 and open_profit > 0)):
            for t, df in inds.items():
                if t in positions or date not in df.index: continue
                r = df.loc[date]
                c, vol, vol_a = float(r['Close']), float(r['Volume']), float(r['Vol_50'])
                if (c * vol_a) < 1000000 or float(r['VCP']) > params['vcp']: continue
                if (c > float(r['SMA50']) > float(r['SMA150']) > float(r['SMA200']) and c <= (float(r['SMA50']) * 1.10) and c >= (float(r['52W_L']) * 1.3) and c >= (float(r['52W_H']) * 0.75)):
                    if vol >= (vol_a * params['vol']):
                        stop = max(c - (params['atr'] * float(r['ATR_10'])), c * 0.92)
                        risk = c - stop
                        sh = min(int((current_equity * 0.01) / risk), int((current_equity * 0.25) / c))
                        if sh > 0 and cash >= (sh * c * 1.001):
                            cash -= (sh * c * 1.001)
                            positions[t] = {'shares': sh, 'entry_p': c, 'entry_d': date, 'stop': stop, 'target': c + (risk * 3), 'risk_ps': risk, 'be': False}
                            break

    return equity_curve, max_drawdown, trade_history

# ==========================================
# 4. AUTONOMOUS DEPLOYER
# ==========================================
def deploy_winning_params(best_params, pf):
    content = f"""# AUTO-GENERATED CONFIG: {datetime.now().strftime('%Y-%m-%d')}
# Best Profit Factor Found: {pf}
VCP_LIMIT = {best_params['vcp']}
ATR_STOP = {best_params['atr']}
VOL_SURGE = {best_params['vol']}
"""
    with open("strategy_config.py", "w") as f:
        f.write(content)
    
    print("GIT: Committing and Pushing Strategy Improvement...")
    try:
        subprocess.run(["git", "add", "strategy_config.py"], check=True)
        subprocess.run(["git", "commit", "-m", f"Strategy Improvement: PF {pf}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("SUCCESS: Code pushed to VS Code project.")
    except Exception as e:
        print(f"GIT ERROR: Check credentials and repo status. {e}")

# ==========================================
# 5. MAIN OPTIMIZATION LOOP
# ==========================================
def run_autonomous_improvement():
    tickers = get_all_ordinaries_tickers()
    data = download_data_robust(tickers)
    m_data = yf.download('^AXJO', period='5y', interval='1d', progress=False)

    best_pf = 0
    best_p = {}

    print("SEARCH: Testing parameter permutations...")
    for vcp in [0.85, 0.90, 0.95]:
        for atr in [1.5, 2.0, 2.5]:
            for vol in [1.3, 1.4, 1.5]:
                p = {'vcp': vcp, 'atr': atr, 'vol': vol}
                curve, dd, hist = execute_stepped_simulation(data, m_data, p)
                
                gp = sum([t['Profit $'] for t in hist if t['Profit $'] > 0])
                gl = abs(sum([t['Profit $'] for t in hist if t['Profit $'] <= 0]))
                pf = gp / gl if gl != 0 else 0
                
                if pf > best_pf:
                    best_pf = pf
                    best_p = p
                    print(f"LEADER: PF {round(pf, 2)} (VCP:{vcp} ATR:{atr} VOL:{vol})")

    if best_p:
        deploy_winning_params(best_p, round(best_pf, 2))

if __name__ == "__main__":
    run_autonomous_improvement()