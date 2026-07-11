import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# WEATHER DATA USING PANDAS
# ==========================================

weather = {
    "Date":[
        "01-Jul","02-Jul","03-Jul","04-Jul","05-Jul",
        "06-Jul","07-Jul","08-Jul","09-Jul","10-Jul",
        "11-Jul","12-Jul","13-Jul","14-Jul","15-Jul"
    ],

    "Temperature":[
        32,34,36,35,33,
        31,30,29,30,31,
        33,34,35,36,37
    ],

    "Humidity":[
        62,60,58,55,64,
        70,74,78,75,72,
        68,66,63,61,59
    ],

    "WindSpeed":[
        12,10,8,15,18,
        17,16,15,13,12,
        11,9,8,10,12
    ],

    "Rainfall":[
        0,2,0,5,12,
        18,20,15,8,4,
        1,0,0,2,0
    ]
}

df = pd.DataFrame(weather)

# ==========================================
# WEATHER CONDITION
# ==========================================

def weather_condition(rain):

    if rain == 0:
        return "Sunny"

    elif rain <= 10:
        return "Cloudy"

    else:
        return "Rainy"

df["Condition"] = df["Rainfall"].apply(weather_condition)

# ==========================================
# KPI VALUES
# ==========================================

current_temp = df["Temperature"].iloc[-1]

avg_temp = df["Temperature"].mean()

highest_temp = df["Temperature"].max()

lowest_temp = df["Temperature"].min()

avg_humidity = df["Humidity"].mean()

total_rain = df["Rainfall"].sum()

avg_wind = df["WindSpeed"].mean()

sunny_days = (df["Condition"] == "Sunny").sum()

rainy_days = (df["Condition"] == "Rainy").sum()

cloudy_days = (df["Condition"] == "Cloudy").sum()

# ==========================================
# DARK THEME
# ==========================================

plt.style.use("dark_background")

fig = plt.figure(figsize=(20,12))

fig.patch.set_facecolor("#101820")

fig.suptitle(
    "WEATHER ANALYTICS DASHBOARD",
    fontsize=24,
    color="white",
    fontweight="bold"
)

# ==========================================
# KPI CARDS
# ==========================================

plt.figtext(
    0.03,
    0.93,
    f"Current Temp\n{current_temp} °C",
    fontsize=14,
    color="white",
    bbox=dict(
        facecolor="#ff5733",
        boxstyle="round,pad=0.7"
    )
)

plt.figtext(
    0.18,
    0.93,
    f"Average Temp\n{avg_temp:.1f} °C",
    fontsize=14,
    color="white",
    bbox=dict(
        facecolor="#3498db",
        boxstyle="round,pad=0.7"
    )
)

plt.figtext(
    0.34,
    0.93,
    f"Highest Temp\n{highest_temp} °C",
    fontsize=14,
    color="white",
    bbox=dict(
        facecolor="#2ecc71",
        boxstyle="round,pad=0.7"
    )
)

plt.figtext(
    0.50,
    0.93,
    f"Lowest Temp\n{lowest_temp} °C",
    fontsize=14,
    color="white",
    bbox=dict(
        facecolor="#9b59b6",
        boxstyle="round,pad=0.7"
    )
)

plt.figtext(
    0.66,
    0.93,
    f"Humidity\n{avg_humidity:.1f} %",
    fontsize=14,
    color="white",
    bbox=dict(
        facecolor="#1abc9c",
        boxstyle="round,pad=0.7"
    )
)

plt.figtext(
    0.82,
    0.93,
    f"Total Rain\n{total_rain} mm",
    fontsize=14,
    color="white",
    bbox=dict(
        facecolor="#f39c12",
        boxstyle="round,pad=0.7"
    )
)

# ==========================================
# NEXT PART STARTS HERE
# ==========================================

# Chart 1
ax1 = plt.subplot(3,2,1)

ax1.plot(
    df["Date"],
    df["Temperature"],
    marker="o",
    linewidth=3
)

ax1.set_title("Temperature Trend")

ax1.set_ylabel("Temperature (°C)")

ax1.tick_params(axis="x", rotation=45)

# ==========================================
# CHART 2 - HUMIDITY BAR CHART
# ==========================================

ax2 = plt.subplot(3,2,2)

ax2.bar(
    df["Date"],
    df["Humidity"],
    color="deepskyblue"
)

ax2.set_title("Humidity (%)", fontsize=12)

ax2.set_ylabel("%")

ax2.tick_params(axis="x", rotation=45)

ax2.grid(alpha=0.3)


# ==========================================
# CHART 3 - WIND SPEED AREA CHART
# ==========================================

ax3 = plt.subplot(3,2,3)

ax3.fill_between(
    df["Date"],
    df["WindSpeed"],
    color="lime",
    alpha=0.6
)

ax3.plot(
    df["Date"],
    df["WindSpeed"],
    color="white",
    linewidth=2
)

ax3.set_title("Wind Speed (km/h)", fontsize=12)

ax3.set_ylabel("km/h")

ax3.tick_params(axis="x", rotation=45)

ax3.grid(alpha=0.3)


# ==========================================
# CHART 4 - RAINFALL
# ==========================================

ax4 = plt.subplot(3,2,4)

ax4.bar(
    df["Date"],
    df["Rainfall"],
    color="orange"
)

ax4.set_title("Rainfall (mm)", fontsize=12)

ax4.set_ylabel("mm")

ax4.tick_params(axis="x", rotation=45)

ax4.grid(alpha=0.3)


# ==========================================
# CHART 5 - WEATHER DISTRIBUTION
# ==========================================

ax5 = plt.subplot(3,2,5)

weather_count = df["Condition"].value_counts()

ax5.pie(
    weather_count,
    labels=weather_count.index,
    autopct="%1.1f%%",
    startangle=90
)

ax5.set_title("Weather Distribution")


# ==========================================
# CHART 6 - TEMP VS HUMIDITY
# ==========================================

ax6 = plt.subplot(3,2,6)

ax6.scatter(
    df["Temperature"],
    df["Humidity"],
    s=120
)

ax6.set_title("Temperature vs Humidity")

ax6.set_xlabel("Temperature (°C)")

ax6.set_ylabel("Humidity (%)")

ax6.grid(alpha=0.3)


# ==========================================
# FOOTER
# ==========================================

plt.figtext(
    0.35,
    0.02,
    "Developed using Python | Pandas | Matplotlib",
    fontsize=11,
    color="white"
)


plt.tight_layout(rect=[0,0.04,1,0.87])

plt.show()
