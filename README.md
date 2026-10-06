# StoryBrand Messaging Kit

A small, independent messaging skill for business owners and teams using Codex or Claude Code. Turn a business brief into a customer-first BrandScript, one-liner, PEACE soundbites, and usable copy. No app, dependency install, account integration, or private knowledge base required.

## Use it

```sh
git clone https://github.com/bettergraininfo-rgb/storybrand-messaging-kit.git
cd storybrand-messaging-kit
```

Fill out [the business brief](business-brief.md), then paste it into your agent conversation. Do not commit confidential briefs to a public repository.

### Codex

Start Codex in this directory. The project skill lives at `.agents/skills/storybrand-messaging/SKILL.md`.

```text
Use $storybrand-messaging to draft a full messaging kit from this brief: ...
```

For another project, copy the entire `.agents/skills/storybrand-messaging` directory to that project's `.agents/skills/`. Restart the agent session after installation. The `references` folder must travel with the skill.

### Claude Code

Start Claude Code in this directory and explicitly load the same canonical file:

```text
Read .agents/skills/storybrand-messaging/SKILL.md and its linked lessons.
Follow it to draft a homepage from this brief: ...
```

For another project, copy the skill directory as above and use the same prompt. No Claude configuration changes are required. This explicit-read workflow is not a separately registered slash command.

## What is included

- [One canonical skill](.agents/skills/storybrand-messaging/SKILL.md): intake, seven-element BrandScript, copy, evidence checks.
- [Ten supporting lessons](.agents/skills/storybrand-messaging/references/lessons.md): concise practical guidance with source links.
- [Sources and limits](SOURCES.md): attribution and editorial boundaries.
- `check.py`: a standard-library check for paths, lesson count, and basic publication hygiene.

## Check it

```sh
python3 check.py
```

For a live agent smoke test, ask for a full kit for a fictional SMS reminder service for independent tutors. Supply no results data or trial terms. Check that it returns Brief and assumptions, BrandScript, One-liner, PEACE soundbites, Requested copy, and Claims and checks, without inventing proof or promising a free trial. Structural checks are not proof that marketing claims are true or that copy will convert.

## Limits

These are original summaries and adaptations of messaging ideas associated with Donald Miller and StoryBrand, not official course material or a substitute for the books. No affiliation, endorsement, or certification is claimed. There are no PDFs, transcripts, client records, or scientific efficacy claims in the kit. Human review is required before publication, especially for regulated products and testimonials.
