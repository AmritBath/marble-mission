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
        dxdt = v
        dvdt = 0.0
        dMdt = 0.0
    return np.array([dxdt, dvdt, dMdt])

def rk4_step(f, t_phase, state, dt, R0, beta, m, u, M_dry):
    k1 = f(t_phase, state, R0, beta, m, u, M_dry)
    k2 = f(t_phase + 0.5*dt, state + 0.5*dt*k1, R0, beta, m, u, M_dry)
    k3 = f(t_phase + 0.5*dt, state + 0.5*dt*k2, R0, beta, m, u, M_dry)
    k4 = f(t_phase + dt, state + dt*k3, R0, beta, m, u, M_dry)
    return state + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

def throwing_phase(state, t_total, dt, R0, beta, m, u, M_dry, R_threshold, D):
    local_t = 0.0
    t_vals, x_vals, v_vals, a_vals, M_vals = [], [], [], [], []
    while True:
        R = R0 * np.exp(-beta * local_t)
        if R < R_threshold or state[2] <= M_dry + 1e-9:
            break
        t_vals.append(t_total)
        x_vals.append(state[0])
        v_vals.append(state[1])
        a_vals.append((m * R * (u - state[1])) / state[2] if state[2] > M_dry else 0.0)
        M_vals.append(state[2])
        state = rk4_step(throwing_odes, local_t, state, dt, R0, beta, m, u, M_dry)
        local_t += dt
        t_total += dt
        if state[0] >= D:
            break
    return state, t_total, t_vals, x_vals, v_vals, a_vals, M_vals

def resting_phase(state, t_total, dt, tau, D):
    t_vals, x_vals, v_vals, a_vals, M_vals = [], [], [], [], []
    t_rest = 0.0
    while t_rest < tau:
        t_vals.append(t_total)
        x_vals.append(state[0])
        v_vals.append(state[1])
        a_vals.append(0.0)
        M_vals.append(state[2])
        state[0] += state[1] * dt
        t_total += dt
        t_rest += dt
        if state[0] >= D:
            break
    return state, t_total, t_vals, x_vals, v_vals, a_vals, M_vals

def simulate_full(D, dt, R0, beta, m, u, M0, M_dry, R_threshold, tau):
    t_total = 0.0
    state = np.array([0.0, 0.0, M0])
    all_t, all_x, all_v, all_a, all_M = [], [], [], [], []
    while state[0] < D:
        if state[2] <= M_dry + 1e-9:
            while state[0] < D:
                all_t.append(t_total)
                all_x.append(state[0])
                all_v.append(state[1])
                all_a.append(0.0)
                all_M.append(state[2])
                state[0] += state[1] * dt
                t_total += dt
            break
        state, t_total, t_vals, x_vals, v_vals, a_vals, M_vals = \
            throwing_phase(state, t_total, dt, R0, beta, m, u, M_dry, R_threshold, D)
        all_t.extend(t_vals)
        all_x.extend(x_vals)
        all_v.extend(v_vals)
        all_a.extend(a_vals)
        all_M.extend(M_vals)
        if state[0] >= D:
            break
        state, t_total, t_vals, x_vals, v_vals, a_vals, M_vals = \
            resting_phase(state, t_total, dt, tau, D)
        all_t.extend(t_vals)
        all_x.extend(x_vals)
        all_v.extend(v_vals)
        all_a.extend(a_vals)
        all_M.extend(M_vals)
    return np.array(all_t), np.array(all_x), np.array(all_v), np.array(all_a), np.array(all_M)

def generate_fun_summary(days_alone, n_marbles):
    fatigue_opts = ["Chill 🧘‍♂️", "Sweaty 💦", "Delirious 😵", "In a trance 🔮", "Running on dreams 🌈", "Throwing with rage 💢"]
    hunger_opts = ["Mild Munchies 🍪", "Starving 🌌", "Ate the emergency cheese 🧀", "Dreaming of noodles 🍜", "Considering eating a marble 🤔", "Drank recycled tears 💧"]
    friend_opts = ["Marble Henry", "Captain Pebble", "Sir Toss-a-lot", "Orb-Bob", "Commander Bounce", "The Great Sphere", "Smooth Steve"]
    extra_lines = ["📦 Cargo: 14 snack bars, 1 diary, 900 regrets", "🎧 Soundtrack of the trip: Lo-fi space beats", "💬 Most said phrase: 'Just one more toss'", "🧼 Hygiene rating: 2/10 (smells like cosmic socks)", "🕳 Discovered black hole? Only emotionally", "📸 Last photo taken: blurry marble selfie", "🛠 Favourite tool: the emergency spoon"]
    
    print("\n📋 MISSION REPORT")
    print(f"🕰 Days spent alone throwing marbles: {days_alone} days")
    print(f"💤 Fatigue condition: {random.choice(fatigue_opts)}")
    print(f"🍽 Hunger status: {random.choice(hunger_opts)}")
    print(f"🪐 Current best friend: {random.choice(friend_opts)}")
    for line in random.sample(extra_lines, 2):
        print(line)

# ---- USER INPUT SIMULATION ----
try:
    n_marbles = int(user_marble_count)  # this must be defined externally (e.g. in the browser environment)
except:
    n_marbles = 10
    print("No valid user_marble_count passed in. Using default of 10 marbles.\n")

# ---- SIMULATION CONFIG ----
D = 384400000    # metres
dt = 1000
R0 = 0.75
beta = 0.05
m = 0.005
u = 10.0
M_dry = 1000.0
R_threshold = 0.5
tau = 30.0

# ---- RUN SIMULATION ----
M0 = compute_mass_from_marbles(n_marbles, m, M_dry)
t_vals, x_vals, v_vals, a_vals, M_vals = simulate_full(D, dt, R0, beta, m, u, M0, M_dry, R_threshold, tau)
final_time = t_vals[-1]

if n_marbles < 1000:
    years = final_time // (365.25 * 24 * 60 * 60)
    remaining_seconds = final_time % (365.25 * 24 * 60 * 60)
    days = remaining_seconds // (24 * 60 * 60)
    remaining_seconds %= (24 * 60 * 60)
    hours = remaining_seconds // (60 * 60)
    remaining_seconds %= (60 * 60)
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    print(f"\nTotal time taken to get home: {years:.0f} years, {days:.0f} days, {hours:.0f} hours, {minutes:.0f} minutes, {seconds:.0f} seconds")
    generate_fun_summary(days, n_marbles)
else:
    print(f"\nTotal time taken to get home: too many years to count! Now I am but an old bear.")
    generate_fun_summary("Countless", n_marbles)

print("\n🎬 Animation available below.")
