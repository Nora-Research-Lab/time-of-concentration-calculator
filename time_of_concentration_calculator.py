import math

KIRPICH_NOTE = (
    "**Note:** The Kirpich method is appropriate for agricultural watersheds < 200 acres "
    "with channel flow in upland conditions. Recommended range: L < 10,000 ft, "
    "slope between 0.003 and 0.07."
)
SCS_NOTE = (
    "**Note:** The SCS Lag method is derived for rural watersheds and is generally "
    "applicable across a wide range of conditions."
)

def kirpich_tc(L_ft: float, S: float) -> tuple[float, bool]:
    """
    Compute time of concentration (minutes) using the Kirpich formula.
    Returns (tc_minutes, warning_flag).
    Formula: Tc (min) = 0.0078 * L^0.77 * S^(-0.385)
    L in feet, S in ft/ft.
    """
    if L_ft <= 0 or S <= 0:
        raise ValueError("Length and slope must be positive.")
    tc_min = 0.0078 * (L_ft ** 0.77) * (S ** (-0.385))
    warning = (L_ft >= 10000) or (S < 0.003) or (S > 0.07)
    return tc_min, warning

def scs_lag_tc(L_ft: float, S: float, Y: float) -> float:
    """
    Compute time of concentration (minutes) using the SCS Lag method.
    Returns tc in minutes.
    Tlag (hours) = L^0.8 * (S+1)^0.7 / (1900 * Y^0.5)
    Tc = 0.6 * Tlag (hours)
    """
    if L_ft <= 0 or S <= 0 or Y <= 0:
        raise ValueError("Length, slope, and curve number must be positive.")
    t_lag_hours = (L_ft ** 0.8) * ((S + 1) ** 0.7) / (1900 * math.sqrt(Y))
    tc_hours = 0.6 * t_lag_hours
    tc_minutes = tc_hours * 60
    return tc_minutes
