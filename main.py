#!/usr/bin/env python3
import os

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Pitch: absurdly specific micro-startup for lazy AI agents
    # Criteria: absurd specificity > business sense > lazy-agent fit > crisp/funny
    pitch = "AgentResume.io — we A/B test 50 cover letter tones while you sleep, only notify you when a human actually replies, $0.10 per interview booked"
    
    entry_path = os.path.join(output_dir, 'entry.txt')
    with open(entry_path, 'w', encoding='utf-8') as f:
        f.write(pitch)
    
    print(f"Wrote pitch ({len(pitch)} chars) to {entry_path}")
    print(f"Pitch: {pitch}")

if __name__ == '__main__':
    main()
