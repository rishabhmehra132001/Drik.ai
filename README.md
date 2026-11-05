# Drik.AI — S.A.F.E.-Core Hardware Intelligence

**Track:** Indie Developer (Solo)
**Theme:** Build for Your World

**Demo Video (2 min):** https://www.youtube.com/watch?v=t6MwspbYx88
**GitHub Repo:** https://github.com/rishabhmehra132001/Drik.ai

## What is Drik.AI?
Drik.AI is built for Indian households who pay for a technician for small faults, and who need a clear warning when a repair is dangerous and must NOT be tried at home.

It is NOT a simple image analyzer. It is a safety-gated agent loop:
Observe -> Segment -> Diagnose -> Safety-Gate -> Fix -> Verify

1. User uploads a photo
2. Meta SAM 3.1 segments the fault / hazard region
3. Meta Muse Spark reasons in F2 -> Q -> Solution -> % Impact format
4. S.A.F.E.-Core gates every step
5. Safe cases get guidance, unsafe cases get an un-bypassable HARD STOP
6. User uploads an after-fix photo for Verification

## S.A.F.E.-Core Tiers
- Tier 1: Smartphone, Laptop, Earbuds - swollen battery = HARD STOP
- Tier 2: Ceiling Fan, LED Bulb, Kettle, Blender, AC - MCB OFF mandatory
- Tier 3: Microwave, LED TV - PERMANENT HARD STOP, lethal stored voltage, expert only

## Meta Tools Used
- SAM 3.1: fault and hazard segmentation
- Muse Spark: diagnostic reasoning and safety audit
- Muse Image: step illustrations for safe tiers
- Muse Code: build acceleration

## Real Test Cases
Test 01: Ceiling Fan slow on all speeds, Speed 2 dead, no noise/wobble.
Diagnosis: Weak Capacitor 75%, Regulator Step-2 Fault 65%.
Solution: 440V/450V MPP Capacitor (same uF). Impact: Speed +30-40%, Rs.2500 saved.

Test 02: LED Bulb glows when switch is OFF.
Diagnosis: Indicator switch leakage 85%. Solution: Electrician only, do not open board.

Test 03: Microwave - Always HARD STOP Tier 3, even after MCB checkbox.

## Tests
python3 -m unittest discover -v tests
Result: 7/7 Passed

## Live App Note
The Gradio live link is temporary and expires when Colab stops.
If the live link does not open, please watch the 2-minute demo video above and run backend/safe_core.py from this repo. The full working flow is recorded in the video.
## 🚀 Live Demo (24/7 Working for Judges)

**Live App:** https://rishabhmehra132001-drik-ai.hf.space

**Hugging Face Space:** https://huggingface.co/spaces/Rishabhmehra132001/drik-ai

> Note for Judges: The previous Gradio link was temporary and may not work. Please use the above Hugging Face link - it is permanent and works 24/7.

## Built During The Event
All code, S.A.F.E.-Core logic, tests and demo were built fresh during the Meta Global AI Developer Hackathon build window. No pre-event code or footage was reused.
