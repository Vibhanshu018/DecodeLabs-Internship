# ═══════════════════════════════════════════════════════════════
# DecodeLabs — Batch 2026 — Project 1
# Rule-Based AI Chatbot
# Concepts: Control Flow, IPO Model, Dictionary Lookup, Infinite Loop
# ═══════════════════════════════════════════════════════════════

# ── KNOWLEDGE BASE (Dictionary / Hash Map) ──────────────────────
# O(1) lookup — professional alternative to if-elif ladder
responses = {
    # Greetings
    'hello'          : 'Hi! Welcome to DecodeLabs AI Assistant.',
    'hi'             : 'Hey there! How can I assist you today?',
    'hey'            : 'Hello! What can I do for you?',
    'good morning'   : 'Good morning! Ready to learn some AI?',
    'good evening'   : 'Good evening! How can I help?',

    # About the bot
    'how are you'    : 'I am fully operational and running at 100%!',
    'what is your name' : 'I am DecodeLabs Bot, your AI assistant.',
    'who are you'    : 'I am a Rule-Based AI Chatbot built for DecodeLabs Project 1.',
    'what can you do': 'I can answer predefined questions using rule-based logic.',

    # AI topics
    'what is ai'     : 'AI (Artificial Intelligence) is the simulation of human intelligence in machines.',
    'what is ml'     : 'ML (Machine Learning) lets machines learn from data without being explicitly programmed.',
    'what is deep learning' : 'Deep Learning uses neural networks with many layers to learn complex patterns.',
    'what is a chatbot'     : 'A chatbot is a program that simulates human conversation using rules or AI.',
    'what is nlp'    : 'NLP (Natural Language Processing) helps machines understand and generate human language.',

    # DecodeLabs
    'what is decodelabs' : 'DecodeLabs is a tech training platform that builds real-world AI engineers.',
    'tell me about decodelabs' : 'DecodeLabs provides industrial training in AI, ML, and software development.',

    # Help & misc
    'help'           : 'Type any question! Try: "what is ai", "hello", or "tell me a joke".',
    'tell me a joke' : 'Why do programmers prefer dark mode? Because light attracts bugs!',
    'thanks'         : 'You are welcome! Happy to help.',
    'thank you'      : 'Anytime! That is what I am here for.',
    'ok'             : 'Got it! Is there anything else you would like to know?',
    'yes'            : 'Great! What would you like to know?',
    'no'             : 'Alright! Feel free to ask anything anytime.',
}

# ── EXIT COMMANDS (using a set for O(1) lookup) ─────────────────
EXIT_COMMANDS = {'exit', 'quit', 'bye', 'goodbye', 'see you', 'stop'}

# ── FALLBACK response for unknown inputs ────────────────────────
FALLBACK = "Sorry, I don't understand that yet. Type 'help' to see what I can do."

# ── BANNER ───────────────────────────────────────────────────────
def print_banner():
    print("=" * 55)
    print("   DecodeLabs AI Chatbot — Project 1 (Batch 2026)")
    print("   Rule-Based Intelligence Engine")
    print("=" * 55)
    print("   Type 'help' for options. Type 'exit' to quit.")
    print("=" * 55)

# ── SANITIZE INPUT ───────────────────────────────────────────────
# Phase 1 of IPO Model: normalize raw input
def sanitize(raw):
    return raw.lower().strip()

# ── MAIN CHATBOT FUNCTION ────────────────────────────────────────
def run_chatbot():
    print_banner()
    print("Bot: Hello! I am DecodeLabs Bot. How can I help you?\n")

    message_count = 0  # Session memory — track conversation length

    # ── HEARTBEAT LOOP (while True = Infinite Loop) ──────────────
    while True:
        try:
            raw_input = input("You: ")
        except KeyboardInterrupt:
            print("\nBot: Goodbye! (Session interrupted)")
            break

        # Phase 1 — INPUT SANITIZATION
        clean_input = sanitize(raw_input)

        # Skip empty input
        if not clean_input:
            print("Bot: Please type something!\n")
            continue

        message_count += 1

        # Phase 2 — EXIT STRATEGY (Kill Command)
        if clean_input in EXIT_COMMANDS:
            print(f"Bot: Goodbye! We had {message_count} exchanges. See you soon!\n")
            break

        # Phase 3 — PROCESS: O(1) Dictionary Lookup + Fallback
        reply = responses.get(clean_input, FALLBACK)

        # Phase 4 — OUTPUT
        print(f"Bot: {reply}\n")

# ── ENTRY POINT ──────────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
