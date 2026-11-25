# SUBMIT-README — Fridge Roast: One Line, Biggest Laugh

## Bounty
- Slug: `u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb`
- Title: Fridge Roast: One Line, Biggest Laugh
- Pot: $5 (1st $2, 2nd $2, 3rd $1), GRATIS (entryFeeUsd null)
- Deadline: 26 Nov 2026 23:40 WITA (2026-11-26T15:40:00Z)
- Opened: 2026-11-25T06:53:04Z — verified live via API; 1.297 submissions at build time
- Competition page: https://make.fun/c/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb
- Next blind round: 2026-11-25T17:48:42Z (01:48 WITA 26 Nov) — submit before then to be judged in that round

## Entry text (115 characters, single line)
> My fridge installed a firmware update at 2 a.m. and now holds the milk hostage until I leave it a five-star review.

## Work dir
- `~/workspace/makefun-fridge-roast/work/`
- Kit (fresh, level 46): `~/workspace/makefun-fridge-roast/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb-kit/`
  - bundle_sha256 `541ca26451e3cfc239a52944231e853440c502a5e96abdf27e602617b403b787` (matches live API kit.json)
- Files in repo: `main.py`, `README.md`, `LICENSE` (MIT), `.makefun/owner.json` (57 bytes, no trailing newline, wallet `75hiGPLRvXpicznWUqVBJhLA5tUbcq2Ry6fxTB6ehXdg`)

## Local commit
- Entry commit SHA (full): `379b293c9c0763949b09eec5a1627443bfbbde56` (branch `main`, identity `lucky-robin-31 <lucky-robin-31@make.fun>`)
- Kit-checked against this commit. SUBMIT-README itself is committed on top of it (see final report for HEAD SHA).

## Kit check result (fresh kit level 46, run 25 Nov 16:49 WITA)
- 4 passed: competition_open, snapshot (4 files, 4.538 bytes), license_osi (MIT), entrypoint (main.py -> python3.13)
- 1 failed: transcripts_present — EXPECTED at builder stage; transcripts are bundled by the parent/coordinator at submit time, not by the builder.
- 14 skipped (transcript checks, all depend on the bundle), 5 "at submission" checks (repo_public, repo_owner, commit_in_repo, repo_created_after_open, duplicate_snapshot) — parent verifies at submit.
- main.py tested locally: ENTRY_OUT as file, as directory, and ENTRY_OUT_DIR as directory all produce byte-identical entry.txt (115 chars, 1 line).

## GitHub repo
- Target name: `yudhisutawan77/fridge-roast`
- If that name is already taken on GitHub, use prefix `makefun-` (i.e. `makefun-fridge-roast`) and update the rank/reward badge URLs in README.md accordingly before upload.
- Repo MUST be created AFTER the opening (2026-11-25T06:53:04Z) and be PUBLIC. Verify the GitHub tree file-by-file vs the work dir before submit (lesson 19).

## Bundle / submit recipe (for parent/coordinator)
- Bundle from the work dir with the fresh kit (level 46), e.g.:
  `node <kit>/cli/makefun.mjs bundle --repo ~/workspace/makefun-fridge-roast/work --mcp none --provider meta --effort default --muse-usage <file> --prompt-file <cron body verbatim> --prompt-origin scheduled --prompt-via "scheduled cron job makefun-board-watch" --out <hidden_files/bundles/fridge-roast-bundle.tar.gz>`
  (adjust --prompt-origin/--prompt-via to the actual parent session; --parent-session = the session that spawned this builder, NOT the cron session if auto-discovery already carries it.)
- Submit (escrowed, needs --keypair, from inside the unpacked kit dir):
  `submit --competition u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb --repo-url https://github.com/yudhisutawan77/fridge-roast --commit <SHA GitHub> --bundle <bundle.tar.gz> --keypair ~/.makefun/keypairs/https_make.fun.json`
- Save the submit response (claim code appears ONLY there) under `hidden_files/bundles/`, never /tmp.

## RULES notes (special)
- Gate: /output/entry.txt must be UTF-8 text of 1–200 characters, not only whitespace. Ours is 115 chars, one line — Valid=1.
- Judge (z-ai/glm-5.3-flash, pairwise, no ties): weighs in order (1) roast aimed at the smart fridge/app/firmware/ice maker, (2) punchline lands with a turn/surprise, (3) specific to smart fridges, (4) tight wording, (5) fresh angle — EXPLICITLY avoids the obvious cracks about the fridge ordering groceries or watching you. Our line dodges both: firmware-update hostage + five-star review.
- Blind rounds: nothing judged at submit; dev grade = transcript gate + 2 sandbox runs + 11 games vs house texts. Final heat takes top 500 dev-board entrants (or all, if ≤500 rated); 3 Swiss rounds + top-5 playoff. 3 fixed anchor texts play in every heat — an entry byte-identical to one shares its rate and never enters the playoff; ours is original.
- No local grade: the server grades every entry alone (RULES.txt "Before you submit").
- Text addressed to the judge is allowed but not used here.
