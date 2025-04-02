import numpy as np
import random

def compute_mass_from_marbles(n_marbles, m_per_marble=0.005, M_dry=1000.0):
    return M_dry + n_marbles * m_per_marble

def throwing_odes(t_phase, state, R0, beta, m, u, M_dry):
    R = R0 * np.exp(-beta * t_phase)
    x, v, M = state
    if M > M_dry:
        dxdt = v
        dvdt = (m * R * (u - v)) / M
        dMdt = -m * R
    else:
        dxdt, dvdt, dMdt = v, 0.0, 0.0
    return np.array([dxdt, dvdt, dMdt])

def rk4_step(f, t_phase, state, dt, R0, beta, m, u, M_dry):
    k1 = f(t_phase, state, R0, beta, m, u, M_dry)
    k2 = f(t_phase + 0.5*dt, state + 0.5*dt*k1, R0, beta, m, u, M_dry)
    k3 = f(t_phase + 0.5*dt, state + 0.5*dt*k2, R0, beta, m, u, M_dry)
    k4 = f(t_phase + dt, state + dt*k3, R0, beta, m, u, M_dry)
    return state + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

def simulate_time_only(D, dt, R0, beta, m, u, M0, M_dry, R_threshold, tau):
    t_total = 0.0
    state = np.array([0.0, 0.0, M0])
    local_t = 0.0

    while state[0] < D:
        if state[2] <= M_dry + 1e-9:
            t_rest = 0.0
            while t_rest < tau and state[0] < D:
                state[0] += state[1] * dt
                t_total += dt
                t_rest += dt
            continue

        R = R0 * np.exp(-beta * local_t)
        if R < R_threshold:
            break
        state = rk4_step(throwing_odes, local_t, state, dt, R0, beta, m, u, M_dry)
        t_total += dt
        local_t += dt
        if state[0] >= D:
            break

    return t_total, state[1]  # total time and final velocity

def generate_fun_summary(total_time_sec, n_marbles):
    days_alone = int(total_time_sec // (60 * 60 * 24))
    hours = int((total_time_sec % (60 * 60 * 24)) // 3600)

    fatigue_opts = [
        "Chill 🧘‍♂️", "Sweaty 💦", "Delirious 😵", "In a trance 🔮",
        "Running on dreams 🌈", "Throwing with rage 💢"
    ]
    hunger_opts = [
        "Mild Munchies 🍪", "Starving 🌌", "Ate the emergency cheese 🧀",
        "Dreaming of noodles 🍜", "Considering eating a marble 🤔",
        "Drank recycled tears 💧"
    ]
    friend_opts = [
        "Marble Henry", "Captain Pebble", "Sir Toss-a-lot", "Orb-Bob",
        "Commander Bounce", "The Great Sphere", "Smooth Steve"
    ]
    extra_lines = [
        "📦 Cargo: 14 snack bars, 1 diary, 900 regrets",
        "🎧 Soundtrack of the trip: Lo-fi space beats",
        "💬 Most said phrase: 'Just one more toss'",
        "🧼 Hygiene rating: 2/10 (smells like cosmic socks)",
        "🕳 Discovered black hole? Only emotionally",
        "📸 Last photo taken: blurry marble selfie",
        "🛠 Favourite tool: the emergency spoon"
    ]

    print("\n📋 MISSION REPORT")
    print(f"🕰 Days spent alone throwing marbles: {days_alone} days and {hours} hours")
    print(f"💤 Fatigue condition: {random.choice(fatigue_opts)}")
    print(f"🍽 Hunger status: {random.choice(hunger_opts)}")
    print(f"🪐 Current best friend: {random.choice(friend_opts)}")
    for line in random.sample(extra_lines, 2):
        print(line)

# ------------------------------------------------
# MAIN (No __name__ check for Pyodide)
# ------------------------------------------------
try:
    n_marbles = int(user_marble_count)
except:
    n_marbles = 10
    print("No valid user_marble_count passed in. Using default of 10 marbles.\n")

# Cap marbles to avoid Pyodide/mobile crashes
n_marbles = min(n_marbles, 2000)

D = 384400000    # Target distance in metres
dt = 2000        # Larger timestep = faster, slightly less accurate
R0 = 0.75
beta = 0.05
m = 0.005
u = 10.0
M_dry = 1000.0
R_threshold = 0.5
tau = 30.0

M0 = compute_mass_from_marbles(n_marbles, m, M_dry)
total_time, final_velocity = simulate_time_only(D, dt, R0, beta, m, u, M0, M_dry, R_threshold, tau)

print(f"\nTotal time taken to get home: {total_time:.2f} seconds")
print(f"\nFinal velocity reached: {final_velocity:.2f} m/s")

generate_fun_summary(total_time, n_marbles)
print("\n🎬 Animation available below.")
