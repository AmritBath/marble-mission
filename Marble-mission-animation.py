import numpy as np
import random
# ------------------------------------------------
# Fun summary
# ------------------------------------------------
def generate_fun_summary(days_alone, n_marbles):

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
    print(f"🕰 Days spent alone throwing marbles: {days_alone}")
    print(f"💤 Fatigue condition: {random.choice(fatigue_opts)}")
    print(f"🍽 Hunger status: {random.choice(hunger_opts)}")
    print(f"🪐 Current best friend: {random.choice(friend_opts)}")
    for line in random.sample(extra_lines, 2):
        print(line)

# ------------------------------------------------
# Main
# ------------------------------------------------
if __name__ == "__main__":
    try:
        n_marbles = int(user_marble_count)
    except:
        n_marbles = 10
        print("No valid user_marble_count passed in. Using default of 10 marbles.\n")

    generate_fun_summary("Countless!", n_marbles)
