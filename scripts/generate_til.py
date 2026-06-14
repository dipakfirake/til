import json
import random
import os
import hashlib
import re
from datetime import datetime, timezone, timedelta
from topics_data import TOPICS

COMMIT_PREFIXES = [
    "til: ", "learn: ", "notes: ", "study: ", "docs: ",
    "ref: ", "concept: ", "explore: ", "deep-dive: ",
]

USED_FILE = os.path.join(os.path.dirname(__file__), "..", "used_topics.json")

def get_used():
    if os.path.exists(USED_FILE):
        with open(USED_FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_used(used):
    with open(USED_FILE, "w") as f:
        json.dump(sorted(list(used)), f)

def pick_topic():
    used = get_used()
    total = len(TOPICS)
    available = [i for i in range(total) if i not in used]

    # All topics exhausted — streak is complete!
    if not available:
        return None, used

    # Deterministic random pick based on date
    ist = timezone(timedelta(hours=5, minutes=30))
    today = datetime.now(ist).strftime("%Y-%m-%d")
    seed = int(hashlib.md5(today.encode()).hexdigest(), 16)
    random.seed(seed)
    
    idx = random.choice(available)
    used.add(idx)
    save_used(used)
    return TOPICS[idx], used

def safe_filename(title):
    name = title.lower()
    for ch in " /()&,:;'\"?!@#$%^*+=[]{}|\\<>`~":
        name = name.replace(ch, "-")
    while "--" in name:
        name = name.replace("--", "-")
    return name.strip("-")[:80]

def create_entry(topic):
    ist = timezone(timedelta(hours=5, minutes=30))
    date_str = datetime.now(ist).strftime("%Y-%m-%d")
    cat, title, content = topic
    
    cat_dir = os.path.join(os.getcwd(), cat)
    os.makedirs(cat_dir, exist_ok=True)
    
    fname = f"{date_str}-{safe_filename(title)}.md"
    fpath = os.path.join(cat_dir, fname)
    
    md = f"# {title}\n\n> _{date_str}_ | Category: **{cat}**\n\n{content.strip()}\n"
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(md)
    
    prefix = random.choice(COMMIT_PREFIXES)
    return f"{prefix}{title}"

def update_readme(used_count, total):
    ist = timezone(timedelta(hours=5, minutes=30))
    date_str = datetime.now(ist).strftime("%Y-%m-%d")
    path = os.path.join(os.getcwd(), "README.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    marker = "<!-- til-stats -->"
    stats = f"{marker}\n> 📊 **{used_count}/{total}** topics completed | Last updated: {date_str}\n"
    if marker in content:
        content = re.sub(f"{marker}.*?\n", stats, content, count=1)
    else:
        content = content.rstrip() + f"\n\n---\n\n{stats}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    topic, used = pick_topic()
    total = len(TOPICS)
    used_count = len(used)
    
    if topic is None:
        print(f"All {total} topics exhausted. Streak complete!")
        gh = os.environ.get("GITHUB_OUTPUT", "")
        if gh:
            with open(gh, "a") as f:
                f.write("has_new=false\n")
        return
    
    commit_msg = create_entry(topic)
    update_readme(used_count, total)
    
    print(f"[{used_count}/{total}] {commit_msg}")
    gh = os.environ.get("GITHUB_OUTPUT", "")
    if gh:
        with open(gh, "a") as f:
            f.write(f"commit_msg={commit_msg}\n")
            f.write("has_new=true\n")

if __name__ == "__main__":
    main()
