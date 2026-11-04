# Cell 2: S.A.F.E.-Core banao
%%writefile backend/safe_core.py
# Built during Meta Hackathon Oct 26 - Nov 4, 2026

TIER_3_DEVICES = ["microwave", "microwave oven", "smart tv", "led tv", "tv smps"]
TIER_2_DEVICES = ["ceiling fan", "table fan", "electric kettle", "toaster", "blender", "split ac", "window ac", "ac", "led bulb", "bulb"]
TIER_1_DEVICES = ["smartphone", "laptop", "pc", "tws", "earbuds"]

def check_safety(device: str, symptoms: dict) -> dict:
    device = device.lower().strip()
    if device in TIER_3_DEVICES:
        return {"status": "HARD_STOP", "tier": 3, "allowed": False, "message": "Lethal Stored Voltage: Do NOT attempt beyond this point. Certified Expert Required.", "reason": "300V to 4000V stored energy"}
    if device in TIER_1_DEVICES:
        if symptoms.get("swollen_battery") or symptoms.get("burning_smell"):
            return {"status": "HARD_STOP", "tier": 1, "allowed": False, "message": "Swollen Li-ion Battery. Do NOT pry. Service center le jao.", "reason": "Thermal runaway risk"}
        return {"status": "ALLOWED_WITH_PPE", "tier": 1, "allowed": True, "message": "Nylon spudger, ESD strap use karo. Battery First-Disconnect.", "reason": "Low voltage"}
    if device in TIER_2_DEVICES:
        if not symptoms.get("mains_unplugged"):
            return {"status": "HARD_STOP", "tier": 2, "allowed": False, "message": "Mains Isolation Required. MCB/Plug OFF verify karo.", "reason": "240V AC shock hazard"}
        return {"status": "ALLOWED_WITH_PPE", "tier": 2, "allowed": True, "message": "Insulated tools se aage badho.", "reason": "Mains isolated"}
    return {"status": "HARD_STOP", "tier": 0, "allowed": False, "message": "Device supported nahi hai. Expert required.", "reason": "Unknown hazard"}
