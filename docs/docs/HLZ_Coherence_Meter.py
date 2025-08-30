# HLZ_Coherence_Meter.py

from datetime import datetime

def compute_hlz_score(c_em, c_eeg, c_lunar):
    """Calculate HLZ (Harmonic Lock-in Zone) score from weighted coherence values."""
    weight_em = 0.4
    weight_eeg = 0.4
    weight_lunar = 0.2
    hlz_score = (weight_em * c_em) + (weight_eeg * c_eeg) + (weight_lunar * c_lunar)
    return round(hlz_score, 3)

def generate_report(c_em, c_eeg, c_lunar):
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    hlz_score = compute_hlz_score(c_em, c_eeg, c_lunar)
    report = f"""
    HLZ Coherence Report
    ---------------------
    🕒 Timestamp: {timestamp}
    📉 C_EM (Kp Index Correlation): {c_em}
    🧠 C_EEG (Theta Coherence): {c_eeg}
    🌕 C_Lunar (Lunar Phase Weight): {c_lunar}
    🎯 Final HLZ Score: {hlz_score}
    """
    return report

# Example usage — update with real or simulated values
if __name__ == "__main__":
    c_em = 0.65      # Correlation to Kp Index (geomagnetic)
    c_eeg = 0.82     # Theta EEG coherence
    c_lunar = 0.73   # Normalized lunar influence
    print(generate_report(c_em, c_eeg, c_lunar))
