import gradio as gr
from time_of_concentration_calculator import (
    kirpich_tc,
    scs_lag_tc,
    KIRPICH_NOTE,
    SCS_NOTE,
)

def calculate_tc(L, S, L_units, S_units, cover, method):
    try:
        L = float(L)
        S = float(S)
    except (TypeError, ValueError):
        return "Please enter valid numeric values for length and slope."

    if L <= 0 or S <= 0:
        return "Length and slope must be positive numbers."

    # Convert length to feet if needed
    if L_units == "meters":
        L = L * 3.28084

    # Slope is dimensionless; no conversion needed

    if method == "Kirpich":
        tc_min, warning = kirpich_tc(L, S)
        note = KIRPICH_NOTE if warning else ""
        sentence = f"For Kirpich, time of concentration is {tc_min:.2f} minutes ({tc_min/60:.2f} hours)."
        if warning:
            sentence += " **Warning:** Inputs are outside the recommended range (L < 10,000 ft, 0.003 < S < 0.07)."
    else:  # SCS Lag
        cn_map = {
            "Smooth bare soil": 85,
            "Pasture/grassland": 75,
            "Cultivated with residue": 70,
            "Forest/woodland": 65,
        }
        Y = cn_map.get(cover, 70)  # default if cover not found
        tc_min = scs_lag_tc(L, S, Y)
        sentence = f"For SCS Lag, time of concentration is {tc_min:.2f} minutes ({tc_min/60:.4f} hours)."
        note = SCS_NOTE

    return f"{sentence}\n\n{note}"

with gr.Blocks(title="Time of Concentration Calculator") as demo:
    gr.Markdown("# Time of Concentration Calculator")
    gr.Markdown("Estimate the time of concentration for a watershed using Kirpich or SCS Lag methods.")

    with gr.Row():
        L_input = gr.Number(label="Watershed Length", value=1000)
        L_units = gr.Radio(choices=["feet", "meters"], label="Length units", value="feet")
    with gr.Row():
        S_input = gr.Number(label="Average Slope (decimal)", value=0.02)
        S_units = gr.Radio(choices=["ft/ft", "m/m"], label="Slope units", value="ft/ft")
    with gr.Row():
        cover = gr.Dropdown(
            choices=["Smooth bare soil", "Pasture/grassland", "Cultivated with residue", "Forest/woodland"],
            label="Surface Cover",
            value="Pasture/grassland",
        )
    with gr.Row():
        method = gr.Radio(choices=["Kirpich", "SCS Lag"], label="Method", value="Kirpich")

    calculate_btn = gr.Button("Calculate")
    output = gr.Markdown(label="Results")

    calculate_btn.click(
        fn=calculate_tc,
        inputs=[L_input, S_input, L_units, S_units, cover, method],
        outputs=output,
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
