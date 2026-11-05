"""Shared business story for lessons 22-25: daily orders of an online candle shop ("Hearthside").

Orders = trend + annual season + weekday effect + noise (+ optional extras).  Every lesson calls ``orders_series`` with its
own window, seed and extras, so each data.csv is self-contained while the story (and the weekday pattern) is the same.
Not a lesson module (the name does not match ``lNN_*.py``), so build.py ignores it.
"""
import numpy as np
import pandas as pd

# additive weekday effects in orders/day, Monday..Sunday (they sum to zero)
WEEKDAY = np.array([9.0, 5.0, 1.0, -1.0, 6.0, -10.0, -10.0])
DAYNAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def orders_series(start, n, seed, base=150.0, lin=0.30, quad=0.0, annual=0.0, annual_peak_doy=355, ar=0.3, sd=7.5,
                  rw_sd=0.0, weekday_scale=1.0, shift_at=None, shift_size=0.0, spikes=(), sd_mult_from=None, sd_mult=1.0):
    """Return a DataFrame(date, orders) with integer orders.

    lin/quad     : trend = base + lin*t + quad*t^2
    annual       : amplitude of a cosine annual cycle peaking at ``annual_peak_doy``
    ar, sd       : AR(1) noise with stationary-ish innovation sd ``sd``
    rw_sd        : sd of a random-walk level component (adds horizon-dependent uncertainty)
    shift_at/size: permanent level shift
    spikes       : iterable of (index, size) one-day spikes
    sd_mult_from : from this index on the noise sd is multiplied by ``sd_mult`` (volatility regime change)
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start, periods=n, freq="D")
    t = np.arange(n)
    level = base + lin * t + quad * t ** 2
    if annual:
        level = level + annual * np.cos(2 * np.pi * (dates.dayofyear.to_numpy() - annual_peak_doy) / 365.0)
    if rw_sd:
        level = level + np.cumsum(rng.normal(0, rw_sd, n))
    if shift_at is not None:
        level = level + np.where(t >= shift_at, shift_size, 0.0)
    wd = weekday_scale * WEEKDAY[dates.dayofweek.to_numpy()]
    mult = np.ones(n)
    if sd_mult_from is not None:
        mult[sd_mult_from:] = sd_mult
    noise = np.zeros(n)
    e = rng.normal(0, sd, n) * mult
    for i in range(n):
        noise[i] = e[i] + (ar * noise[i - 1] if i else 0.0)
    y = level + wd + noise
    for i, s in spikes:
        y[i] += s
    return pd.DataFrame({"date": dates, "orders": np.round(y).astype(int)})
