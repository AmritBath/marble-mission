import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
from IPython.display import HTML, display
from scipy.ndimage import rotate
import random

# ------------------------------------------------
# Constants
# ------------------------------------------------
EARTH_MOON_DISTANCE = 384400  # in km

# ------------------------------------------------
# Mass calculation from marble count
# ------------------------------------------------
def compute_mass_from_marbles(n_marbles, m_per_marble=0.005, M_dry=1000.0):
    return M_dry + n_marbles * m_per_marble

# ------------------------------------------------
# ODE function for the throwing phase
# ------------------------------------------------
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

# ------------------------------------------------
# RK4 integration step
# ------------------------------------------------
def rk4_step(f, t_phase, state, dt, R0, beta, m, u, M_dry):
    k1 = f(t_phase, state, R0, beta, m, u, M_dry)
    k2 = f(t_phase + 0.5*dt, state + 0.5*dt*k1, R0, beta, m, u, M_dry)
    k3 = f(t_phase + 0.5*dt, state + 0.5*dt*k2, R0, beta, m, u, M_dry)
    k4 = f(t_phase + dt, state + dt*k3, R0, beta, m, u, M_dry)
    return state + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

# ------------------------------------------------
# Throwing phase
# ------------------------------------------------
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

# ------------------------------------------------
# Resting phase
# ------------------------------------------------
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

# ------------------------------------------------
# Full simulation
# ------------------------------------------------
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
        state, t_total, t_vals, x_vals, v_vals, a_vals, M_vals = throwing_phase(state, t_total, dt, R0, beta, m, u, M_dry, R_threshold, D)
        all_t.extend(t_vals)
        all_x.extend(x_vals)
        all_v.extend(v_vals)
        all_a.extend(a_vals)
        all_M.extend(M_vals)
        if state[0] >= D:
            break
        state, t_total, t_vals, x_vals, v_vals, a_vals, M_vals = resting_phase(state, t_total, dt, tau, D)
        all_t.extend(t_vals)
        all_x.extend(x_vals)
        all_v.extend(v_vals)
        all_a.extend(a_vals)
        all_M.extend(M_vals)
    return np.array(all_t), np.array(all_x), np.array(all_v), np.array(all_a), np.array(all_M)

# ------------------------------------------------
# Rocket animation (restored with rocket image)
# ------------------------------------------------
def animate_rocket(distance):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, distance)
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    ax.set_xlabel("Distance Travelled (m)")
    ax.set_title("🚀 Rocket Progress")
    try:
        space_bg = mpimg.imread("space.jpg")
    except:
        space_bg = np.ones((10, 10, 3)) * 0.05
    ax.imshow(space_bg, extent=[0, distance, -2, 2], aspect='auto', zorder=0)
    try:
        rocket_img = mpimg.imread("rocket.png")
        #rotated_rocket = rotate(rocket_img, -90, reshape=False)
        imagebox = OffsetImage(rocket_img, zoom=0.1)
        ab = AnnotationBbox(imagebox, (0, 0), frameon=False)
        ax.add_artist(ab)
    except:
        ab = None

    def update(frame):
        new_x = frame * (distance / 100)
        if ab:
            ab.xybox = (new_x, 0)
        return ab,

    ani = animation.FuncAnimation(fig, update, frames=100, blit=True, interval=30)
    plt.close(fig)
    return HTML(ani.to_jshtml())

# ------------------------------------------------
# Fun summary generator
# ------------------------------------------------
def generate_fun_summary(total_time_sec, n_marbles):
    days_alone = int(total_time_sec // (60 * 60 * 24))
    hours = int((total_time_sec % (60 * 60 * 24)) // 3600)
    fatigue_opts = ["Chill 🧘‍♂️", "Sweaty 💦", "Delirious 😵", "In a trance 🔮", "Running on dreams 🌈", "Throwing with rage 💢"]
    hunger_opts = ["Mild Munchies 🍪", "Starving 🌌", "Ate the emergency cheese 🧀", "Dreaming of noodles 🍜", "Considering eating a marble 🤔", "Drank recycled tears 💧"]
    friend_opts = ["Marble Henry", "Captain Pebble", "Sir Toss-a-lot", "Orb-Bob", "Commander Bounce", "The Great Sphere", "Smooth Steve"]
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
# Main entry point
# ------------------------------------------------

if __name__ == "__main__":
    while True:
        try:
            n_marbles = user_marble_count
            break  # Valid input received, break out of loop
        except ValueError:
            print("That's not a valid number. Try again.")

    # --- All this only runs once you have a valid integer ---
    D = 384400000
    dt = 1000
    R0 = 0.75
    beta = 0.05
    m = 0.005
    u = 10.0
    M_dry = 1000.0
    R_threshold = 0.5
    tau = 30.0

    M0 = compute_mass_from_marbles(n_marbles, m, M_dry)
    t_vals, x_vals, v_vals, a_vals, M_vals = simulate_full(D, dt, R0, beta, m, u, M0, M_dry, R_threshold, tau)

    total_time = t_vals[-1]
    final_distance_km = x_vals[-1] / 1000
    final_velocity = v_vals[-1]

    print(f"\nTotal time taken to get home: {total_time:.2f} seconds")
    print(f"\nFinal velocity reached: {final_velocity:.2f} m/s")

    generate_fun_summary(total_time, n_marbles)

    _ = animate_rocket(final_distance_km)
    display(_)
