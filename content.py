import random

SUGGESTIONS = [
    "Reorganize your desktop icons first. It's basically prep work.",
    "Make coffee. Great work starts with hydration.",
    "Watch one productivity video. Knowledge is progress.",
    "Clean your keyboard. You can't work in these conditions.",
    "Check your emails. Someone might need you urgently.",
    "Create a to-do list for your to-do list.",
    "Adjust your chair. Ergonomics are important.",
    "Find the perfect playlist. Music fuels productivity.",
    "Take a quick break. Mental preparation is essential.",
    "Research the best way to get started. Preparation is everything.",
    "Open 15 browser tabs. You're building momentum.",
    "Check the weather. You need the right atmosphere."
]

EXCUSE_STARTS = [
    "I would have started, but",
    "Honestly, I was about to, but",
    "I had everything planned, except",
    "My productivity was interrupted because",
    "I was mentally prepared, but",
    "I swear I was going to, but",
    "It's not procrastination if",
    "I can't possibly work until"
]

EXCUSE_REASONS = [
    "my ex texted me.",
    "my chair was at a bad angle.",
    "my coffee wasn't emotionally ready.",
    "the Wi-Fi looked suspicious.",
    "I haven't found the perfect playlist.",
    "my keyboard needs emotional support.",
    "the universe clearly needs me to rest.",
    "I accidentally opened YouTube.",
    "my brain is still loading.",
    "it's an odd-numbered minute.",
    "I need to mentally prepare for mentally preparing.",
    "my desk has the wrong energy.",
    "I forgot what I was supposed to do.",
    "I work better under pressure, and there's no pressure yet."
]

DELAY_REASONS = [
    "Research shows your brain peaks later today.",
    "Starting now would be rushing. Quality takes patience.",
    "You're not procrastinating; you're building anticipation.",
    "The deadline isn't close enough to activate your full potential.",
    "Great ideas need time to marinate.",
    "Your future self is better equipped to handle this.",
    "It's important to respect your current lack of motivation.",
    "You should wait for the perfect moment. It builds character.",
    "Your productivity window is probably tomorrow morning.",
    "A little more planning will definitely make starting easier.",
    "You're giving your brain time to develop a strategy.",
    "The task isn't going anywhere. Unfortunately."
]

def get_suggestion():
    return random.choice(SUGGESTIONS)

def get_excuse():
    return f"{random.choice(EXCUSE_STARTS)} {random.choice(EXCUSE_REASONS)}"

def get_delay_reason():
    return f"{random.choice(DELAY_REASONS)}"
